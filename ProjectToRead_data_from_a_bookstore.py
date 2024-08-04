import re
from bs4 import BeautifulSoup
import requests
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="farhad_AFA1380A",
    database="new_schema"
)
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS bookstore (name varchar(255), volume varchar(155), number varchar(150), month varchar(255), year varchar(100))")


res = requests.get('https://www.gutenberg.org/ebooks/bookshelf/220')

soup = BeautifulSoup(res.text, 'html.parser')

val = soup.find_all('span',  attrs={'class':'title'})

for i in range(0,15):
    word = val[i].text
    if re.search(r".+\,.+\,.+", word) != None:
        values = word.split(',')
        if len(values) == 3:
            sql = "INSERT INTO bookstore (name, volume, number) VALUES (%s, %s, %s)"
            to_insert = [values[0], values[1], values[2]]
            cursor.execute(sql, to_insert)
            db.commit()
        if len(values) == 4:
            sql = "INSERT INTO bookstore (name, volume, month, year) VALUES (%s, %s, %s, %s)"
            to_insert = [values[0], values[1], values[2], values[3]]
            cursor.execute(sql, to_insert)
            db.commit()
        if len(values) == 5:
            sql = "INSERT INTO bookstore (name, volume, number, month, year) VALUES (%s, %s, %s, %s, %s)"
            to_insert = [values[0], values[1], values[2], values[3], values[4]]
            cursor.execute(sql, to_insert)
            db.commit()
db.close()