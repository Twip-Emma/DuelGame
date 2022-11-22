'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-11 18:08:38
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-22 15:58:20
'''
import copy


# BUFF工厂 - 计算BUFF全效果
class BaseBuffFactory:
    def __init__(self, owner):
        self.__owner = owner

        self.atk = None
        self.amo = None

    # 计算BUFF加持下的临时面板
    def temp(self):
        return None


# 怒气 - 增伤50%
class BuffAnger:
    def use_buff(self, buffFactory):
        return None


# 战意 - 增伤100%
class BuffWarpath:
    def use_buff(self, buffFactory):
        return None


# 抵抗 - 受到伤害时，护甲增加50%
class BuffResist:
    def use_buff(self, buffFactory):
        return None
