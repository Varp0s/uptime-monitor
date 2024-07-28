from requests import get, post
import cloudscraper
import time

useragent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

request_headers= {
    'User-Agent': useragent
}

def send_get_request(request_url):
    response= get(request_url, headers=request_headers)
    # response_time= response.elapsed.total_seconds()
    return response.status_code

def cloudscraper_request(request_url):
    cloudscraper_scraper= cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'platform': 'windows',
        'mobile': False })

    response= cloudscraper_scraper.get(request_url)
    return response.status_code