from src.webhook.Discord import Discord
from src.logo.logo import logo
import time

class Menu:
    def __init__(self):
        pass
    
    def bots(self):
        dc = Discord()
        dc.execute()

    def logo(self):
        lg = logo()
        return lg
    
    def execute(self):
        print(self.logo())
        self.bots()
        time.sleep(1)
