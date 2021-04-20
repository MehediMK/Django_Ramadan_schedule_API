from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def home(request):
    # thi url old version
    #url = 'https://www.urdupoint.com/islam/dhaka-ramadan-calendar-sehar-aftar-timing.html'
    #this url in updated
    url = 'https://www.urdupoint.com/islam/ramadan-calendar-sehar-aftar-timings-up.html'
    data  = requests.get(url)
    soup = BeautifulSoup(data.content,'html.parser')
    ramadan = soup.find('table')
    ramadan_head = [i.text for i in ramadan.find_all('th')]
    ramadan_doc = [x.text for x in ramadan.find_all('td')]
    output = {}
    for rh in range(len(ramadan_head)):
        if ramadan_head[2] == ramadan_head[rh]:
            mydata = ramadan_doc[2]
            output[ramadan_head[rh]] = f'{int(mydata[:2])-12}{mydata[2:]} PM'
            print(f'{ramadan_head[rh]} = {int(mydata[:2])-12}{mydata[2:]}')
        else:
            output[ramadan_head[rh]] = f'{ramadan_doc[rh]} AM'
            print(f'{ramadan_head[rh]} = {ramadan_doc[rh]}')
    print('This is output:',output)
    return render(request,'index.html',context={'finaloutput':output})