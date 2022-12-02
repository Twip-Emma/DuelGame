'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 22:12:50
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-12-02 22:29:32
'''
from pathlib import Path
import sqlite3
from .entity.Buff import BUFF_TABLE


BASE_PATH: str = Path(__file__).absolute().parents[0]
DB_PATH: str = str(Path(BASE_PATH)/r"game_data"/r"gamedata.db")


# 新建用户操作
def new_user(user_id: str) -> None:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    sql1 = f"insert into player_base values(?,?,?,?,?,?,?)"
    sql2 = f"insert into player_equip values(?,?,?)"
    sql3 = f"insert into player_skill values(?,?,?)"
    sql4 = f"insert into player_buff values(?,?,?,?)"
    cursor.execute(sql1,(user_id,100,80,100,80,15,7)) # 基础面板
    cursor.execute(sql2,(user_id,-1,-1)) # 装备
    cursor.execute(sql3,(user_id,0,0)) # 技能
    cursor.execute(sql4,(user_id,0,0,0)) # BUFF
    db.commit()
    db.close()


# 查询用户基本信息
def select_user(user_id: str) -> tuple:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    sql = "SELECT * FROM player_base WHERE user_id=?;"
    cursor.execute(sql, (user_id,))
    results = cursor.fetchall()
    db.close()
    return results


#更新用户数据
def update_user(play_entity) -> None:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()

    sql = f"update player_base set hp=?, mp=?, atk=?, amo=? where user_id=?"

    cursor.execute(sql,(play_entity.hp, play_entity.mp, play_entity.atk, play_entity.amo, play_entity.user_id))
    db.commit()
    db.close()


# 查询用户的装备信息
def select_equip(equip: str, user_id: str) -> tuple:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    sql = "SELECT " + equip + " FROM player_equip WHERE user_id=?;"
    cursor.execute(sql, (user_id,))
    results = cursor.fetchall()
    db.close()
    return results


# 查询用户的BUFF
def select_buff(buff: str, user_id: str) -> tuple:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    sql = "SELECT " + buff + " FROM player_buff WHERE user_id=?;"
    cursor.execute(sql, (user_id,))
    results = cursor.fetchall()
    db.close()
    return results


# 查询用户的SKILL
def select_skill(skill: str, user_id: str) -> tuple:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    sql = "SELECT " + skill + " FROM player_skill WHERE user_id=?;"
    cursor.execute(sql, (user_id,))
    results = cursor.fetchall()
    db.close()
    return results


# BUFF自减
def delete_buff(user_id: str) -> None:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()

    sql_end = ""
    flag = True
    for buff_name in BUFF_TABLE.keys():
        sql_1 = ""
        if flag:
            sql_1 = "set " + buff_name + "= case when " + buff_name + "<1 then 0 else " + buff_name + " -1 end"
            flag = False
        else:
            sql_1 = " , " + buff_name + "= case when " + buff_name + "<1 then 0 else " + buff_name + " -1 end"
        sql_end += sql_1

    sql = f"update player_buff " + sql_end + " where user_id=?"

    cursor.execute(sql,(user_id, ))
    db.commit()
    db.close()