# extract entire source code and store it in text file
import requests
# selectorlib extracts only that particular code from source code
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    # Scrape the page source from the URL
    response = requests.get(URL)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_mail():
    print("Mail was sent!")


def store(extracted):
    with open("data.txt", "a")as file:
        file.write(extracted + "\n")


def read(extracted):
    with open("data.txt", "r")as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            # Only want to store data when the event is new
            store(extracted)
            send_mail()