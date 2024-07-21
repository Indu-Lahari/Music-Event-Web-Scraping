# extract entire source code and store it in text file
import requests
# selectorlib extracts only that particular code from source code
import selectorlib
import smtplib
import ssl
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect("data.db")


def scrape(url):
    # Scrape the page source from the URL
    response = requests.get(URL)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "indulahari6@gmail.com"
    password = "etzz hnjh nusz mtbs"

    receiver = "indulahari6@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context)as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("mail was sent!")


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)",row)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    Band, City, Date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE Band=? AND City=? AND Date=?", (Band, City, Date))
    rows = cursor.fetchall()
    print(rows)
    return rows


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                # Only want to store data when the event is new
                store(extracted)
                send_email(message="Hey, new event was found!")
        time.sleep(2)