from AbstractSMTPConnector import *

class GmailConnector(AbstractSMTPConnector):
    def __init__(self, conf):
        self.conf = conf
        
    def connect(self):
        print('Gmail SMTP 서버에 연결되었습니다.')