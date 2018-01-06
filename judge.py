import requests
import sys
import os
import numpy as np
from bs4 import BeautifulSoup
import time
accountsF=sys.argv[1]
todoF=sys.argv[2]
loginF='./login'
resultF=sys.argv[3]
with open(accountsF,'r') as file:
    accounts=file.readlines()[0].split(',')
with open(todoF,'r') as file:
    todo=file.readlines()[0].split(',')
with open(loginF,'r') as file:
    login=file.readlines()[0].split(',')
scores=[]

session_requests = requests.session()
head = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
login_url='https://zerojudge.tw/Login'
payload = {
	"account": login[0], 
	"passwd": login[1], 
}

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = head
)

for acc in range(5):
    scores.append([])
    for tod in range(len(todo)):
        payloads ={
            'problemid':todo[tod],
            'account':accounts[acc]
        }
        res = session_requests.get('https://zerojudge.tw/Submissions?problemid='+todo[tod]+'&account='+accounts[acc],headers=head, verify=False)
        c=res.text
        if (c.find('<span class="acstyle">AC</span>')>0):
            print(c.find('<span class="acstyle">AC</span>'))
            scores[acc].append('v')
        else:
            scores[acc].append('')
        time.sleep(0.1)
session_requests.close()
result = session_requests.post(
	'https://zerojudge.tw/Logout', 
	headers = head
)
with open(resultF,'w') as file:
    for i in range(len(todo)):
        file.write(',')
        file.write(todo[i])  
    file.write("\n")
    for i in range(len(accounts)):
        file.write(accounts[i])
        for j in range(len(todo)):
            file.write(',')
            file.write(scores[i][j])
        file.write('\n')
