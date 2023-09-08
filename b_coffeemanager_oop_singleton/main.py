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
    
    # 주문 금액이 10000원 이상인 주문은 10% 할인하는 정책을 추가.1