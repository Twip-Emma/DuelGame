'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 23:07:11
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-22 15:31:31
'''
import sys
sys.path.append("..")
from entity_mrr.Player import Player

# from .Player import Player
# from typing import Optional


# 计算工厂
class SkillsComputingFactory:
    def __init__(self) -> None:
        pass


# 普通攻击
class NormalAttack:
    def __init__(self, owner: Player):
        self.__owner = owner
        self.__power = 1.0


    # 计算桑海
    def calc(self, target: Player):
        # 主动发起的
        temp_buff = self.__owner.buff_temp() # 计算BUFF带来的倍率增减
        temp_equip = self.__owner.equip_temp() # 计算装备带来的数值增减

        # 目标的
        t_temp_buff = target.buff_temp() # 计算BUFF带来的倍率增减
        t_temp_equip = target.equip_temp() # 计算装备带来的数值增减

        # 计算敌人实际护甲
        target_amo = (target.amo + t_temp_equip.amo) * t_temp_buff.amo

        # 剩余血量 = 原有血量 - (技能倍率 * (buff加成 * (装备数值 + 基础数值)) - 敌人防御)
        calct = self.__power * (temp_buff.atk * ( temp_equip.atk + self.__owner.atk)) - target_amo
        target.hp -= calct

        # 同步数据:面板、BUFF回合
        target.db_sync().delete_buff_round()  # 被攻击者
        self.__owner.db_sync().delete_buff_round()  # 主动发起者

        print(f"你对 {target.user_id} 造成了 {calct} 伤害！\n\n{target.user_id} 剩余生命值：{target.hp}")


# 重击
class ChargeAttack:
    __power = 2.0

    def get_hurt(self, atk: int) -> int:
        return atk*self.__power
