class Account:
    __instance = None
    __init = False
    
    def __new__(cls, *args, **kwargs): # => 얘가 생성하는 함수 (만약 재정의 하지 않는다면, 얘는 object꺼를 물려받은 거임)
        if cls.__instance is None:  # 없으면 새로운 객체를 생성
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        cls = type(self)
        if not cls.__init:
            self.__balance = 100000
            self.__sales_volumn = 0  # 매출
            self.__expenses = 0  # 지출
            cls.__init = True
        
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