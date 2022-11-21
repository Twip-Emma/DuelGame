'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 22:10:37
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-21 15:12:24
'''
from db_handler import select_user, update_user, select_equip, new_user, select_buff, select_skill
from buff import BaseBuffFactory
from equip import BaseEquipFactory

from key_value import EQUIP_TABLE, BUFF_TABLE, SKILL_TABLE


# 角色实体
class Player():
    def __init__(self, user_id: str) -> None:
        user_data = select_user(user_id=user_id)
        if user_data == []:
            new_user(user_id)
            user_data = select_user(user_id=user_id)
        user_data = user_data[0]
        
        self.user_id = user_data[0]
        self.max_hp = user_data[1]
        self.max_mp = user_data[2]
        self.hp = user_data[3]
        self.mp = user_data[4]
        self.atk = user_data[5]
        self.amo = user_data[6]

        self.skills: dict = {}
        self.buffs: dict = {}
        self.equips: dict = {}

        # 初始化角色装备、BUFF、技能
        self.__add_equip()
        self.__add_buff()
        self.__add_skill()
        


    # 打印用户基础数值
    def __str__(self) -> str:
        temp_equip = self.equip_temp()

        text = "==========用户：" + str(self.user_id) + "==========\n"
        text += "生命值：" + str(self.hp) + "/" + str(self.max_hp)
        text += " | 魔法值：" + str(self.mp) + "/" + str(self.max_mp) + "\n"
        text += "攻击：" + str(self.atk) + "+" + str(temp_equip.atk)
        text += " | 防御：" + str(self.amo) + "+" + str(temp_equip.amo)
        
        return (text)

    # 角色攻击
    def attack(self, skill: str, target) -> None:
        target.attacked(self.skills[skill.__name__])

    # 角色受击
    def attacked(self, skill) -> None:
        skill.calc(self)

    # 数据库同步基础属性
    def db_sync(self) -> None:
        update_user(self)
        return self

    # 获得技能
    def __add_skill(self):
        for key,value in SKILL_TABLE.items():
            learn = select_skill(key, self.user_id)[0][0]
            if learn <= 0:
                continue
            self.skills.update({
                key: value(self)
            })

    # 获得BUFF
    def __add_buff(self):
        for key,value in BUFF_TABLE.items():
            round = select_buff(key, self.user_id)[0][0]
            if round <= 0:
                continue
            self.buffs.update({
                key: value()
            })

    # 根据已有BUFF计算临时角色面板
    def buff_temp(self):
        factory = BaseBuffFactory(self)
        for _, buff_entity in self.buffs.items():
            factory = buff_entity.use_buff(factory)
        return factory.temp()

    # 所有BUFF减少一回合
    def delete_buff_round(self):
        pass

    # 获得装备
    def __add_equip(self):
        for key, value in EQUIP_TABLE.items():
            level = select_equip(key, self.user_id)[0][0]
            if level == -1:
                continue
            self.equips.update({
                key: value(level)
            })

    #计算装备带来的临时面板
    def equip_temp(self):
        factory = BaseEquipFactory(self)
        for _, buff_entity in self.equips.items():
            factory = buff_entity.use_equip(factory)
        return factory.temp()
