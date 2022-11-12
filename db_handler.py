'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 22:12:50
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-11-10 23:41:03
'''
from pathlib import Path
import sqlite3

BASE_PATH: str = Path(__file__).absolute().parents[0]
DB_PATH: str = str(Path(BASE_PATH)/r"gamedata.db")

# 查询用户基本信息
def select_user(user_id: str) -> tuple:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    sql = "SELECT * FROM player_base WHERE user_id=?;"
    cursor.execute(sql, (user_id,))
    results = cursor.fetchall()
    db.close()
    return results[0]


#更新用户数据
def update_user(play_entity) -> None:
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()

    sql = f"update player_base set hp=?, mp=?, atk=?, amo=? where user_id=?"

    cursor.execute(sql,(play_entity.hp, play_entity.mp, play_entity.atk, play_entity.amo, play_entity.user_id))
    db.commit()
    db.close()