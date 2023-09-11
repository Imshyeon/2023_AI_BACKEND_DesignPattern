from User import *


if __name__ == '__main__':
    user = User.UserBuilder().name('ksh')\
        .email('kzoen0040@naver.com')\
        .password('1234abcd')\
        .tell('010-1234-5678')\
        .build()
        
    print(user)