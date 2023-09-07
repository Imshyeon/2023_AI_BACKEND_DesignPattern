class DataBaseConfig:   # new 생성


    __instance = None   # 최초호출이 아닐 때는 instance는 None이 아니게 됨.
    __init = False  # 덮어써지게 됨을 방지.. 
    
    def __new__(cls, *args, **kwargs): # => 얘가 생성하는 함수 (만약 재정의 하지 않는다면, 얘는 object꺼를 물려받은 거임)
        if cls.__instance is None:  # 없으면 새로운 객체를 생성
            cls.__instance = super().__new__(cls)
        return cls.__instance   # 있으면 cls의 인스턴스를 반환

    def __init__(self, address, name): # init 생성 => 객체를 초기화하는 함수지, 객체 자체는 __new__가 만듦.
        cls = type(self)
        # if cls.__instance is None:  # 최초 호출 시, 아래 수행
        if not cls.__init:  # False라면
            self.__address = address
            self.__name = name
            # cls.__instance = self 
            cls.__init = True


    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            return cls()
        return cls.__instance   # 최초호출이 아닐 시.


    def get_name(self):
        return self.__name


    def get_address(self):
        return self.__address


conf3 = DataBaseConfig('oracle','11g')    # 생성자 호출
conf1 = DataBaseConfig('mysql','33') 
print(conf3.get_address(), conf3.get_name(), conf3)

# conf1 = DataBaseConfig('mysql','33')   # 만약 얘가 DataBaseConfig()로 되어있다면, 얘는 init 안의 if절을 만족하지 못함 그래서, get_address(), get_name() 안됨
                                        # 생성자체를 __new__가 함. 이미 이전에 생성해 놓은 게 있다면 이전 거를 반환하도록 만들어야함
print(conf1.get_address(), conf1.get_name(), conf1)


# conf2 = DataBaseConfig.get_instance()
# print(conf2.get_address(), conf2.get_name(), conf2)

# singleton은 데이터가 덮어써지면 안됨
#하지만 아래와 같이 하면 데이터가 덮어써지게 됨. => __init = False 하고 init안에 if 추가, cls.init = True 하면 conf3의 내용이 나옴. oracle 11g / oracle 11g (이전에는 mysql 33 / mysql 33)
# conf3 = DataBaseConfig('oracle','11g')    # 생성자 호출
# conf1 = DataBaseConfig('mysql','33') 
# print(conf3.get_address(), conf3.get_name(), conf3)
# print(conf1.get_address(), conf1.get_name(), conf1)