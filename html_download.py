import requests
from lxml import etree
import re

def html_save():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = 'https://www.smzdm.com/jingxuan/'

    response = requests.get(url, headers=headers)
    html_content = response.text
    with open('test.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
        

if __name__ == '__main__':
    html_save()