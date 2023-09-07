class Account:
    __instance = None
    
    def __init__(self):
        cls = type(self)
        if cls.__instance is None:
            self.__balance = 100000
            self.__sales_volumn = 0  # 매출
            self.__expenses = 0  # 지출
            cls.__instance = self
        
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            return cls()
        return cls.__instance
        
    def regist_expenses(self, budget):
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