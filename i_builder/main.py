from User import *
from Calculator import *

if __name__ == '__main__':
    user = User.UserBuilder().name('ksh')\
        .email('kzoen0040@naver.com')\
        .password('1234abcd')\
        .tell('010-1234-5678')\
        .build()
        
    print(user)
    
    # calculator
    cal = CalculatorAns(10)
    val = cal.add(10).add(10).subtract(5).divide(3).end()
    print('cal.add(10).add(10).subtract(5).divide(3).end() = ',val)