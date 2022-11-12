'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-12 15:14:11
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-12 21:45:16
'''
from buff import *
from equip import *
from skill import *


BUFF_TABLE = {
    "BuffAnger": BuffAnger,
    "BuffWarpath": BuffWarpath,
    "BuffResist": BuffResist
}

EQUIP_TABLE = {
    "WoodenSword": WoodenSword,
    "WoodenShield": WoodenShield
}

SKILL_TABLE = {
    "NormalAttack": NormalAttack,
    "ChargeAttack": ChargeAttack
}


# for item in SKILL_TABLE.values():
#     print(item)