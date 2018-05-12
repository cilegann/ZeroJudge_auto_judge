import requests
import sys
import os
import time
import getpass
accountsF='./data/'+sys.argv[1]
todoF='./data/'+sys.argv[2]
resultF=sys.argv[3]
head = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

def getAccount():
    user= input(">>> Valid account to login: ")
    pwd = getpass.getpass()
    return([user,pwd])

def doLogin(session_request):
    login=getAccount()
    login_url='https://zerojudge.tw/Login'
    login_payload = {
        "account": login[0], 
        "passwd": login[1], 
    }
    result = session_requests.post(
        login_url, 
        data = login_payload, 
        headers = head
    )
    if result.text=='{"currentPage":"./"}':
        return session_request,True
    else:
        return session_request,False

def getScores(session_request,accounts,todo):
    scores=[]
    for acc in range(len(accounts)):
        print("Getting score of "+accounts[acc])
        scores.append([])
        for tod in range(len(todo)):
            print("  "+todo[tod],end='\r')
            res = session_requests.get('https://zerojudge.tw/Submissions?problemid='+todo[tod]+'&account='+accounts[acc],headers=head, verify=False)
            c=res.text
            if (c.find('<span class="acstyle">AC</span>')>0):
                scores[acc].append('v')
            else:
                scores[acc].append('')
            time.sleep(0.1)
        print("  Done.")
    return scores

if __name__ == "__main__":
    with open(accountsF,'r') as file:
        accounts=file.readlines()[0].split(',')
    with open(todoF,'r') as file:
        todo=file.readlines()[0].split(',')
    session_requests = requests.session()
    session_resuests,status = doLogin(session_requests)
    if status is False:
        print("Login Failed.")
    else:
        scores = getScores(session_requests,accounts,todo)
        session_requests.post(
            'https://zerojudge.tw/Logout', 
            headers = head
        )
        session_requests.close()

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
        print("Result saved as "+resultF)
        print("Logging out..")
        result=session_requests.get("https://zerojudge.tw/Logout")
        print("Jod done at "+time.asctime( time.localtime(time.time()) ))
