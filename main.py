'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 22:10:30
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-12 23:00:58
'''
from entity import Player
from skill import *
from buff import *
from equip import *

a = Player("12580")
print(a)
b = Player("12581")
print(b)

# print("======攻击后======")
# a添加BUFF
# a.add_buff(BuffAnger) 
# a.add_buff(BuffWarpath)

# b添加BUFF和装备
# b.add_buff(BuffResist)

# a.add_skill(NormalAttack) # 使用普攻
try:
    a.attack(NormalAttack, b)
except:
    print("你没有学会这个技能")
print(b)


# a = {"1":"一", "2":"二"}

# for key, value in a.items():
#     print(key, value)