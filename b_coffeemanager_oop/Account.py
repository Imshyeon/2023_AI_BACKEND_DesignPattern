class Account:
    
    def __init__(self):
        self.__balance = 100000
        self.__sales_volumn = 0  # 매출
        self.__expenses = 0  # 지출
        
    def register_expenses(self, budget):    # 지출 등록 로직
        if self.__balance > budget:
            self.__balance -= budget
            self.__expenses += budget
            return True
        return False
    
    def register_sales(self, pay_price):
        self.__balance += pay_price
        self.__sales_volumn += pay_price

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_sales_volumn(self):
        return self.__sales_volumn

    def set_sales_volumn(self, sales_volumn):
        self.__sales_volumn = sales_volumn

    def get_expenses(self):
        return self.__expenses

    def set_expenses(self, expenses):
        self.__expenses = expenses

