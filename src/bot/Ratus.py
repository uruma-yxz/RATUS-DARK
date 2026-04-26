import os
import json
import platform
import requests

class Ratus:
    def __init__(self):
        self.username = None
        self.OS = None
        self.distro = None
        self.ip = []
        self.db = "src/database/user.json"

    def getOS(self):
        self.OS = os.name
        self.distro = platform.system()

    def getIP(self):
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            ipinfo = response.json()['ip']
            self.ip.append(ipinfo)
        except:
            return None
        
    def malweres(self):
        pass
    
    def user(self):
        self.username = os.getlogin()

    def multiplasSend(self):
        self.user()
        self.getOS()
        self.getIP()

    def dadosDb(self):
        dados = {
            "SUCESSO":"ON",
            "UserName":f"{self.username}",
            "OS": f"{self.distro} {self.OS}",
            "IP": f"{self.ip}"
                 }
        return dados

    def mostre(self):
        return f"OS: {self.distro} {self.OS} | IP: {self.ip}"
    
    def ler_db(self):
        with open(self.db,"r",encoding="utf-8") as rJs:
            dados = json.load(rJs)
        return dados
        
    def send_db(self,dados:dict):
        with open(self.db,"w",encoding="utf-8") as js:
            json.dump(dados,js,ensure_ascii=False,indent=2)

    def execute(self):
        self.malweres()
        self.multiplasSend()
        self.dados = self.dadosDb()
        self.send_db(self.dados)
