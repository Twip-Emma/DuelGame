'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 22:10:37
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-22 15:30:53
'''

# 角色实体
class Player():
    def __init__(self, user_id: str) -> None:
        self.user_id = None
        self.max_hp = None
        self.max_mp = None
        self.hp = None
        self.mp = None
        self.atk = None
        self.amo = None

        self.skills: dict = {}
        self.buffs: dict = {}
        self.equips: dict = {}
        


    # 打印用户基础数值
    def __str__(self) -> str:
        text = None
        return (text)

    # 角色攻击
    def attack(self, skill: str, target) -> None:
        pass

    # 角色受击
    def attacked(self, skill) -> None:
        pass

    # 数据库同步基础属性
    def db_sync(self) -> None:
        return self

    # 根据已有BUFF计算临时角色面板
    def buff_temp(self):
        return None

    # 所有BUFF减少一回合
    def delete_buff_round(self):
        pass

    #计算装备带来的临时面板
    def equip_temp(self):
        return None
