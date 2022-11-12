'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 22:12:50
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-12 22:12:45
'''
from pathlib import Path
import sqlite3

BASE_PATH: str = Path(__file__).absolute().parents[0]
DB_PATH: str = str(Path(BASE_PATH)/r"gamedata.db")


# 新建用户操作
def new_user(user_id: str) -> None:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    sql1 = f"insert into player_base values(?,?,?,?,?,?,?)"
    sql2 = f"insert into player_equip values(?,?,?)"
    cursor.execute(sql1,(user_id,100,80,100,80,15,7))
    cursor.execute(sql2,(user_id,-1,-1))
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