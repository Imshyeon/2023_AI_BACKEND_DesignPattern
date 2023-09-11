from config.EmailConfig import *
from DaumConnector import *
from NaverConnector import *
from GmailConnector import *

class SMTPConnectorFactory:
    
    @staticmethod
    def create(mail):
        connectors = {
            'Daum' : DaumConnector(EmailConfig.DAUM_CONFIG),
            'Naver' : NaverConnector(EmailConfig.NAVER_CONFIG),
            'Gmail' : GmailConnector(EmailConfig.GMAIL_CONFIG),
        }
        
        return connectors.get(mail)