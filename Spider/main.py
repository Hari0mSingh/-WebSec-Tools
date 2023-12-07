from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Request failed: {url}")
        print(f"Error: {e}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tags = soup.find_all('a')
        urls = []

        for tag in a_tags:
            href = tag.get('href')
            if href is not None and href != "":
                urls.append(href)

        # print('urls are',urls)
        for url2 in urls:
            if url2 not in visited_urls:
                visited_urls.add(url2)
                url_join = urljoin(url,url2)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join,keyword)
            else:
                pass
                


url = input("Enter the URL you want to scrape: ")
keyword = input("Enter the keyword you want to search in the provided URL: ")
spider_urls(url, keyword)
