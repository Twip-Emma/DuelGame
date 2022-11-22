'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-12 13:41:42
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-22 15:58:28
'''
# 计算装备效果总和
class BaseEquipFactory:
    def __init__(self, owner):
        self.__owner = owner

        self.atk = None
        self.amo = None

    # 计算BUFF加持下的临时面板
    def temp(self):
        return None


class WoodenSword:
    def __init__(self, level) -> None:
        pass

    def use_equip(self, equipFactory):
        return None


class WoodenShield:
    def __init__(self, level) -> None:
        pass

    def use_equip(self, equipFactory):
        return None