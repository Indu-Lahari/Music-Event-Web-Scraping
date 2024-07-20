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


if __name__ == "__main__":
    print(scrape(URL))
