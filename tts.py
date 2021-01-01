import requests
import sys
import webbrowser
while True:
    a = input("Type your text here: ")
    b = input("Chose your preferred language here e.g. EN for English: ")
    r1 = requests.get(url='https://tts.baidu.com/text2audio?', params={'tex':a, 'cuid':'baike','lan':b,'ctp':'1' ,'pdt':'1', 'vol':'9',
    'rate':'32' , 'per':'8', 'qq-pf-to':'pcqq.c2c'})     
    #print(r1.url)
    webbrowser.open(r1.url, new=0, autoraise=False) 

