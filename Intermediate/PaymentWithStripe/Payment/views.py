# payments/views.py

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from .models import Subscription
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def index(request):
    return render(request, 'index.html', {
        'stripe_public_key': settings.STRIPE_TEST_PUBLIC_KEY
    })

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': 'prctbl_1Px1qPRu9ZyK2FIX8wqL2oF8',
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=request.build_absolute_uri(),
                cancel_url=request.build_absolute_uri(),
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=403)

def handle_webhook(request):
    event = None
    try:
        event = stripe.Event.construct_from(
            request.body, stripe.api_key
        )
    except ValueError as e:
        return JsonResponse({'success': False, 'error': str(e)})

    if event.type == 'customer.subscription.created':
        subscription = event.data.object
        save_subscription_to_database(subscription.id, subscription.customer)

    return JsonResponse({'success': True})

def save_subscription_to_database(subscription_id, customer_id):
    subscription = Subscription(
        subscription_id=subscription_id,
        customer_id=customer_id
    )
    subscription.save()
