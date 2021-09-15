from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time

cookies = { 'MoodleSession': 'cv0o8h3len1uncfdbdaqt13o09'
    
}

headers = {
     'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
}

url = 'http://moodle.fink.rs/user/profile.php?id=1020';

def makeI():
    response = requests.get(url, headers=headers, cookies=cookies, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.findAll('li', {'class', 'contentnode'})

    content = content[len(content) - 1]
    t = str(content.findAll('dd')[0])
    global init;
    init = '';
    for c in t[4:]:
        if c == '(': break
        init += c

    init= init.strip()
    print(init)
   

def makeResponse():
    response = requests.get(url, headers=headers, cookies=cookies, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.findAll('li', {'class', 'contentnode'})

    content = content[len(content) - 1]
    target = str(content.findAll('dd')[0])
    global targetString
    targetString = '';
    for c in target[4:]:
        if c == '(': break
        targetString += c
    
    targetString = targetString.strip()


def compare():
    makeResponse()
    if(targetString != init):
        print('Korisnik je ulogovan.')
        print(targetString)
        sound()
    

def sound():
    while True:
        print('\a')
        time.sleep(1)
        
makeI()
while True:
    compare()
    time.sleep(3)
