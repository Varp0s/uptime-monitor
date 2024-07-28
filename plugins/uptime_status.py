import requests
import time
from datetime import datetime
from database.db import log_status
import logging
from helpers.http_request_helper import cloudscraper_request

logging.basicConfig(level=logging.INFO)

def check_domain(domain):
    try:
        cloudscraper_request(domain)
        return 'up'

    except requests.exceptions.ConnectionError:
        return 'down'

def monitor_domains(domains):
    while True:
        for domain in domains:
            status = check_domain(domain)
            log_status(domain, status)
            logging.info(f"{datetime.now()} - {domain} is {status}")
            # print(f"{datetime.now()} - {domain} is {status}")
        time.sleep(60)
