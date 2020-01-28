import urllib.request
import requests
import time

class RuCaptchaConnection:
    token = None
    def __init__(self, token):
        self.token = token

    def send(self, file):
        data = {"key" : self.token}
        files = {"file": file}
        response = requests.post("https://rucaptcha.com/in.php", data=data, files=files)
        if(response.status_code == 200):
            if(response.text.split('|')[0].upper() == 'OK'):
                return RuCaptcha(cid = int(response.text.split('|')[1]), token = self.token)
            else: 
                raise ValueError(response.text)
        else:
            raise ValueError(f'[{response.status_code}] Could not connect to RuCatcha server!')

class RuCaptcha:
    cid = None
    token = None
    decision = None
    def __init__(self, cid, token):
        self.token = token
        self.cid = cid   

    def captcha_ready(self):
        data = {"key" : self.token, 'action': 'get', 'id': self.cid}
        response = requests.post("https://rucaptcha.com/res.php", data=data)
        if(response.text.split('|')[0].upper() == "OK"):
            return True
        elif(response.text == "CAPCHA_NOT_READY"):
            self.decision = response.text.split('|')[0]
            return False
        else:
            raise ValueError(response.text)
    
    def get_decision(self):
        if(self.decision == None):
            data = {"key" : self.token, 'action': 'get', 'id': self.cid}
            response = requests.post("https://rucaptcha.com/res.php", data=data)
            if(response.text.split('|')[0].upper() == "OK"):
                self.decision = response.text.split('|')[1]
                return self.decision
            elif(response.text == "CAPCHA_NOT_READY"):
                raise ValueError(response.text)
            else:
                raise ValueError(response.text)
        else: 
            return self.decision
    
    def wait_decision(self):
        waited = 0
        data = {"key" : self.token, 'action': 'get', 'id': self.cid}
        while True:
            if(waited >= 60):
                raise ValueError('Timeout waiting decision')
            response = requests.post("https://rucaptcha.com/res.php", data=data)
            if(response.text.split('|')[0].upper() == "OK"):
                self.decision = response.text.split('|')[1]
                return self.decision
            else:
                time.sleep(2)
                waited += 5
                continue