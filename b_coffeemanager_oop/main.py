from Coffee import *
from Sales import *
from Menu import *

def main():
    drinks = [
        Coffee("아메리카노", 10, 0, 3, 2000, 3000),
        Coffee("모카", 10, 0, 3, 3000, 4000),
        Coffee("라떼", 10, 0, 3, 4000, 5000)
    ]

    Menu(Sales(), drinks).main_menu()

if __name__ == "__main__":
    main()
    
# 처음에 잔액, 매출, 지출 변경값이 제대로 반영이 안된 이유 : Account는 한번만 생성해야한다. 왜냐하면 Account는 계속 살려서 사용을 해야하니까..
# 이런 것들을 component라고 함.
# Payment에서 한번 더 Account를 생성해버림.
# ===> 이 객체 하나 때문에 너무 많은 것을 수정해야한다...! 조금 이상한디?!

# 이럴 때 Singleton Design Pattern 쓴다.. -> c_singleton