'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 23:07:11
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-12-04 19:53:33
'''
from .Player import Player
from typing import Union


# 计算工厂
def computing_factory(you: Player, target: Player, power: float, power_cost: int = None) -> Union[tuple, str]:
    # 攻击合法性判断
    if you.hp <= 0:
        return "您已死亡，无法发动攻击！"

    if target.hp <= 0:
        return "目标已死亡，攻击失败！"

    if power_cost:
        if you.mp <= power_cost:
            return f"魔法值不足！您需要{power_cost}点魔法值发动此技能！\n你的魔法值：{you.mp}"

    # 主动发起的
    temp_buff: Player = you.buff_temp()  # 计算BUFF带来的倍率增减
    temp_equip: Player = you.equip_temp()  # 计算装备带来的数值增减

    # 目标的
    t_temp_buff: Player = target.buff_temp()  # 计算BUFF带来的倍率增减
    t_temp_equip: Player = target.equip_temp()  # 计算装备带来的数值增减

    # 计算敌人实际护甲
    target_amo = (target.amo + t_temp_equip.amo) * t_temp_buff.amo

    # 剩余血量 = 原有血量 - (技能倍率 * (buff加成 * (装备数值 + 基础数值)) - 敌人防御)
    calct = power * (temp_buff.atk * (temp_equip.atk + you.atk)) - target_amo
    target.hp -= calct

    return (target, f"你对 {target.user_id} 造成了 {calct} 伤害！\n\n{target.user_id} 剩余生命值：{target.hp}")


# 普通攻击
class NormalAttack:
    def __init__(self, owner: Player):
        self.__owner = owner
        self.__power = 1.0

    # 计算伤害

    def calc(self, target: Player) -> str:
        # # 主动发起的
        # temp_buff: Player = self.__owner.buff_temp() # 计算BUFF带来的倍率增减
        # temp_equip: Player = self.__owner.equip_temp() # 计算装备带来的数值增减

        # # 目标的
        # t_temp_buff: Player = target.buff_temp() # 计算BUFF带来的倍率增减
        # t_temp_equip: Player = target.equip_temp() # 计算装备带来的数值增减

        # # 计算敌人实际护甲
        # target_amo = (target.amo + t_temp_equip.amo) * t_temp_buff.amo

        # # 剩余血量 = 原有血量 - (技能倍率 * (buff加成 * (装备数值 + 基础数值)) - 敌人防御)
        # calct = self.__power * (temp_buff.atk * ( temp_equip.atk + self.__owner.atk)) - target_amo
        # target.hp -= calct

        data = computing_factory(
            you=self.__owner, target=target, power=self.__power)
        if type(data) == str:
            return data

        target = data[0]
        message = data[1]

        # 同步数据:面板、BUFF回合
        target.db_sync().delete_buff_round()  # 被攻击者
        self.__owner.db_sync().delete_buff_round()  # 主动发起者
        return message


# 重击
class ChargeAttack:
    __power = 2.0

    def get_hurt(self, atk: int) -> int:
        return atk*self.__power


SKILL_TABLE = {
    "NormalAttack": NormalAttack,
    "ChargeAttack": ChargeAttack
}
