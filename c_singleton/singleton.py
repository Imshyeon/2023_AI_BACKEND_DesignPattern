class DataBaseConfig:
    
    __instance = None
    
    def __init__(self): # 생성자 호출 시 실행
        print('__init__')
        self.__address = 'oracle'
        self.__name = '11g'
        self.__instance = self
        
    @classmethod    
    def get_instance(cls):  # class     // 한번 초기화 한 뒤에는 Init 사용되는게 아니라 그 다음은 init이 아니라 self return
        if cls.__instance is None:
            cls.__instance = cls()  # 생성자(init) 호출
            
        return cls.__instance # None이 아니면 기존의 인스턴스를 반환
        
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
#--------------------------------
    
conf1 = DataBaseConfig.get_instance() # init 생성
print(conf1.get_address(), conf1.get_name())    

conf2 = DataBaseConfig.get_instance()   # init 안함 ==> conf1과 객체주소 같음
print(conf2.get_address(), conf2.get_name())
