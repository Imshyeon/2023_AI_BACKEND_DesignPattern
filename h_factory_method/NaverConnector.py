from AbstractSMTPConnector import *

class NaverConnector(AbstractSMTPConnector):
    def __init__(self, conf):
        self.conf = conf
        
    def connect(self):
        print('Naver SMTP 서버에 연결되었습니다.')