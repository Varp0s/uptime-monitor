import os
import logging

def read_domains(file_path):
    if not os.path.exists(file_path):
        print(f"{file_path} not found!")
        return []
    
    with open(file_path, 'r') as file:
        domains = [line.strip() for line in file.readlines()]
        if 'https' and 'http' not in domains:
            domain_with_paremeter = [f'https://{domain}' for domain in domains]

    return domain_with_paremeter
    

