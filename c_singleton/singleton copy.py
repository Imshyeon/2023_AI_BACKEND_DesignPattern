class DataBaseConfig:


    __instance = None


    def __init__(self):
        cls = type(self)
        if cls.__instance is None:
            self.__address = 'oracle'
            self.__name = '11g'
            cls.__instance = self


    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            return cls()
        return cls.__instance


    def get_name(self):
        return self.__name


    def get_address(self):
        return self.__address


conf3 = DataBaseConfig()
print(conf3.get_address(), conf3.get_name(), conf3)


conf1 = DataBaseConfig.get_instance()
print(conf1.get_address(), conf1.get_name(), conf1)


conf2 = DataBaseConfig.get_instance()
print(conf2.get_address(), conf2.get_name(), conf2)

