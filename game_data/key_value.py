'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-12 15:14:11
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-22 15:21:45
'''
import sys
sys.path.append("..")
from entity.Buff import BuffAnger, BuffWarpath, BuffResist
from entity.Equip import WoodenSword, WoodenShield
from entity.Skill import NormalAttack, ChargeAttack


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