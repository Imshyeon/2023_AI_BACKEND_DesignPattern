class Player:
    def __init__(self, instrument):
        self.instrument = instrument

    # 외부에서 실행을 위해 호출하기 위한 것이 facade 
    # => 객체의 자율성 : 객체의 역할 및 책임을 수행하는 과정을 객체가 자율적으로 결정하도록 코드를 작성
    # 이런식으로 해야 유연한 프로그램이 된다!
    def play(self):
        self.__prepare()
        self.__ing()
        self.__end()
        self.__curtain_call()
        
    def __prepare(self):    # 외부에서 호출할 수 없도록 막아둠! private 설정 (은닉화) => 객체의 세부 구현을 숨김
        print(self.instrument + '를 연주할 준비 중...')
        
    def __ing(self):
        print(self.instrument + '를 연주 중...')
        
    def __end(self):
        print(self.instrument + '를 연주 완료...')
        
    def __curtain_call(self):
        print('커튼콜 진행...')