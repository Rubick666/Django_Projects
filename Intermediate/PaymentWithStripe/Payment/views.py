from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from .models import Subscription
import stripe
from django.views.decorators.csrf import csrf_protect, csrf_exempt

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

@csrf_protect
def index(request):
    return render(request, 'index.html', {
        'stripe_public_key': settings.STRIPE_TEST_PUBLIC_KEY
    })

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{'price': 'price_1PxA93Ru9ZyK2FIXlcD4whoF', 'quantity': 1}],
                mode='payment',
                success_url=request.build_absolute_uri(),
                cancel_url=request.build_absolute_uri(),
                client_reference_id=str(request.user.id) if request.user.is_authenticated else None,
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=403)

@csrf_exempt
def handle_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']



            save_subscription_to_database(
                session['id'],
                session.get('customer', 'unknown'),
                session.get('customer_details', {}).get('email'),
                session['amount_total'] / 100.0,
                session['currency'],
                session['payment_status']
            )

        return JsonResponse({'success': True})
    except ValueError:
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'error': 'Invalid signature'}, status=400)

def save_subscription_to_database(subscription_id, customer_id, customer_email, amount_total, currency, payment_status):
    try:
        Subscription.objects.create(
            subscription_id=subscription_id,
            customer_id=customer_id,
            customer_email=customer_email,
            amount_total=amount_total,
            currency=currency,
            payment_status=payment_status
        )
    except Exception as e:
        pass
