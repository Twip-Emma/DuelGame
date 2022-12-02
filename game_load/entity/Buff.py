'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-11 18:08:38
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-12-02 22:27:46
'''
import copy


# BUFF工厂 - 计算BUFF全效果
class BaseBuffFactory:
    def __init__(self, owner):
        self.__owner = owner

        self.atk_up = 1  # 攻击加成
        self.amo_up = 1  # 防御加成

    # 计算BUFF加持下的临时面板
    def temp(self):
        temp_entity = copy.deepcopy(self.__owner)
        temp_entity.atk = self.atk_up
        temp_entity.amo = self.amo_up
        return temp_entity


# 怒气 - 增伤50%
class BuffAnger:
    def use_buff(self, buffFactory):
        buffFactory.atk_up = buffFactory.atk_up + 0.5
        return buffFactory


# 战意 - 增伤100%
class BuffWarpath:
    def use_buff(self, buffFactory):
        buffFactory.atk_up = buffFactory.atk_up + 1
        return buffFactory


# 抵抗 - 受到伤害时，护甲增加50%
class BuffResist:
    def use_buff(self, buffFactory):
        buffFactory.amo_up = buffFactory.amo_up + 0.5
        return buffFactory


BUFF_TABLE = {
    "BuffAnger": BuffAnger,
    "BuffWarpath": BuffWarpath,
    "BuffResist": BuffResist
}