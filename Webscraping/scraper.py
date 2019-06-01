from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import requests

def getURL():
    url = input("Enter URL to scrape: ")
    return(url)

def getRequest(url):
    req = requests.get(url)
    return(req)

def scrapeByClass(req, tag, target, findBool):
    soup = BeautifulSoup(req.text, 'html.parser')
    rawData = []
    start = time.time()
    if findBool is True:
        for data in tqdm(soup.findAll(tag, attrs={'class' : target})):
            #strip any whitespace at the beginning and end and convert to str
            rawData.append(data.get_text().strip())
    else:
        rawData.append((soup.find(tag, attrs={'class' : target})).strip())
    end = time.time()
    final = end - start
    totalTime = str(round(final, 4))
    print("Successfully scraped data in " + totalTime + "s.")
    return rawData

def printData(data):
    for i in range(len(data)):
        print(data[i])

