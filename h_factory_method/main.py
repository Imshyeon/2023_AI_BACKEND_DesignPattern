from SMTPConnectorFactory import *


if __name__ == '__main__':
    daum = SMTPConnectorFactory.create('Daum')
    daum.connect()