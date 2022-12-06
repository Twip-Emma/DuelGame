'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-12-06 15:27:55
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-12-06 16:02:32
'''
import json
from os import system
from pathlib import Path
from typing import Optional

from game_load.db_handler import new_user, select_user
from game_load.entity.Player import Player
from game_load.entity.Skill import ChargeAttack, NormalAttack

BASE_PATH: str = Path(__file__).absolute().parents[0]
DATA_PATH: str = str(Path(BASE_PATH)/r"game_load"/r"game_data"/r"equip_data.json")
EQUIP_DATA:dict = json.load(open(DATA_PATH, 'r', encoding='utf8'))


SKILL_SELECT = {
    "普通攻击": NormalAttack,
    "重击": ChargeAttack
}


# 用户查询个人信息
def get_user_info(user_id: str) -> dict:
    a = Player(user_id=user_id)
    return a.get_data()


# 攻击
def user_attack(user_id: str, target_id: str, skill: str) -> Optional[str]:
    a = Player(user_id=user_id)
    b = Player(user_id=target_id)

    use_skill = None
    try:
        use_skill = SKILL_SELECT[skill]
    except:
        return f"名为{skill}的技能不存在"

    try:
        return a.attack(use_skill, b)
    except:
        return f"你没有学会{skill}这个技能"


# 查询所有武器
def select_all_equip() -> str:
    txt = ""
    for _, item in EQUIP_DATA.items():
        txt += f"""【{item["name"]}】花费金币：{item["base_cost"]} | 升级花费：{item["up_cost"]}  """
        base_atk = 0
        atk_up = 0
        base_amo = 0
        amo_up = 0
        try:
            base_atk = item["base_atk"]
            atk_up = item["atk_up"]
        except:
            pass
        try:
            base_amo = item["base_amo"]
            amo_up = item["amo_up"]
        except:
            pass
        
        txt += f"""\n      基础面板：{base_atk}/{base_amo} | 升级幅度：+{atk_up}/+{amo_up}"""
        txt += f"""\n      {item["txt"]}\n\n"""
    
    return txt




print(select_all_equip())