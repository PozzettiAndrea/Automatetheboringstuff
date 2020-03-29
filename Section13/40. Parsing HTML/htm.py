import bs4
import requests
import os

def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#oneTimeBuyBox > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h5:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
    return elems[0].text.strip()


price = getAmazonPrice("https://www.amazon.co.uk/Hermesetas-2879104-Liquid-200ml/dp/B001E977VQ")
print('The price is ' + price)

os.system("pause")