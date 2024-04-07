from smtplib import _fix_eols

import requests
from send_email import *
api_key= "d8d27d18a997455aa6569b6f5f4c2134"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d8d27d18a997455aa6569b6f5f4c2134"

request = requests.get(url)
content = request.json()

for index,article in enumerate(content["articles"]):
    title=article["title"]
    descr=article["description"]
    message = f"""\
Subject: DAILY NEWS- Topic {index + 1}  {title} 
{descr}
    """
    msg = _fix_eols(message).encode('utf-8')
    send_email(msg)
