'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-12 13:41:42
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-12-04 16:54:13
'''
import json
import copy
from pathlib import Path

BASE_PATH: str = Path(__file__).absolute().parents[1]
print(BASE_PATH)
DATA_PATH: str = str(Path(BASE_PATH)/r"game_data"/r"equip_data.json")
EQUIP_DATA:dict = json.load(open(DATA_PATH, 'r', encoding='utf8'))


# 计算装备效果总和
class BaseEquipFactory:
    def __init__(self, owner):
        self.__owner = owner

        self.atk_up = 0  # 攻击加成
        self.amo_up = 0  # 防御加成

    # 计算BUFF加持下的临时面板
    def temp(self):
        temp_entity = copy.deepcopy(self.__owner)
        temp_entity.atk = self.atk_up
        temp_entity.amo = self.amo_up
        return temp_entity


class WoodenSword:
    def __init__(self, level) -> None:
        self.level = level
        self.atk_up = EQUIP_DATA["WoodenSword"]["base_atk"] + \
            level * EQUIP_DATA["WoodenSword"]["atk_up"]

    def use_equip(self, equipFactory):
        equipFactory.atk_up += self.atk_up
        return equipFactory


class WoodenShield:
    def __init__(self, level) -> None:
        self.level = level
        self.amo_up = EQUIP_DATA["WoodenShield"]["base_amo"] + \
            level * EQUIP_DATA["WoodenShield"]["amo_up"]

    def use_equip(self, equipFactory):
        equipFactory.amo_up += self.amo_up
        return equipFactory


EQUIP_TABLE = {
    "WoodenSword": WoodenSword,
    "WoodenShield": WoodenShield
}