from SpringConcert import *
from SummerConcert import *
from AutumnConcert import *
from WinterConcert import *

# 만약에 기능 추가하면 수정할 데가 너무 많다.. => 변경 사항을 받아들이기에 적합하지 않은 구조

if __name__=='__main__':
    spring = SpringConcert()
    spring.start_concert()
    print()
    summer = SummerConcert()
    summer.start_concert()
    print()
    autumn = AutumnConcert()
    autumn.start_concert()
    print()
    winter = WinterConcert()
    winter.start_concert()