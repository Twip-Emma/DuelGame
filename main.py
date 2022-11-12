'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 22:10:30
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-12 14:53:33
'''
from entity import Player
from skill import *
from buff import *
from equip import *

a = Player("12580")
print(a)
b = Player("12581")
print(b)

print("======攻击后======")
# a添加BUFF
a.add_buff(BuffAnger) 
a.add_buff(BuffWarpath)

# a穿装备
a.add_equip(WoodenSword, 5)

# b添加BUFF和装备
b.add_buff(BuffResist)
b.add_equip(WoodenShield, 10)

a.add_skill(NormalAttack) # 使用普攻
a.attack(NormalAttack, b)
print(b)


# a = {"1":"一", "2":"二"}

# for key, value in a.items():
#     print(key, value)