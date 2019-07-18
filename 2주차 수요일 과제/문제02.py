import random

name = input('캐릭터의 이름을 입력하세요: ')
ap = random.randint(6,8)
ad = random.randint(6,8)

if ad > ap:
    job = '전사'
elif ad == ap:
    job = '궁수'
else:
    job = '법사'

class Game():
    def __init__(self,name,ad,ap,job):
        self.name = name
        self.ad = ad
        self.ap = ap
        self.job = job

x = Game(name,ad,ap,job)

print('캐릭터의 이름:',x.name)
print('캐릭터 정보: 힘({0}), 지력({1})'.format(ad,ap))
print('캐릭터 직업:',x.job)
