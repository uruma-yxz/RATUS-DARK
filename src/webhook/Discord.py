import requests
from src.bot.Ratus import Ratus

class Discord:
    def __init__(self):
        self.web = "src/token/token_webhook.txt"
        self.db = "src/database/user.json"

    def readToken(self):
        with open(self.web,"r",encoding="utf-8") as token:
            return token.read()
        
    def bot(self):
        bot = Ratus()
        dados = bot.execute()
        return dados
    
    def sedWebhook(self,urlDc:str):
        with open(self.db,"rb") as web:
            files = {
                'file': (self.db, web, 'application/json')
            }
            response = requests.post(urlDc,files=files)
            return response

    def execute(self):
        dc = Discord()
        ratus = self.bot()
        url = dc.readToken()
        self.sedWebhook(url)