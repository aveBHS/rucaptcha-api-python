import urllib.request
import requests

class RuCaptchaConnection:
    token = ''
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
    cid = ''
    token = ''
    def __init__(self, cid, token):
        self.token = token
        self.cid = cid   

