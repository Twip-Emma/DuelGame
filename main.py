'''
Author: 七画一只妖 1157529280@qq.com
Date: 2022-11-10 22:10:30
LastEditors: 七画一只妖 1157529280@qq.com
LastEditTime: 2022-12-04 19:47:08
'''
from game_load.entity.Player import Player
from game_load.entity.Skill import NormalAttack
from os import system
from game_load.db_handler import select_user, new_user
from time import sleep


if __name__ == "__main__":
    account = ""  # 玩家账号
    target = ""  # 锁定的目标

    while True:
        account = input("登入宁的账号\n>>>")
        re = select_user(account)

        # 是否需要新建账号流程
        if re == []:
            print("没有这个账号，是否需要创建？(y/n)\n>>>")
            choice = input()
            if choice == "y" or choice == "Y":
                new_user(user_id = account)
            else:
                system("cls")
                print("退出了捏~")
        
        # 已有帐号，继续
        else:
            system("cls")
            user_data = re[0]
            while True:
                system("cls")
                print(f"欢迎您,{user_data[0]}!")
                print("""
                    #######选择你的行为#######
                    以下行为发送编号即可
                    1.锁定目标 <目标账号>
                        例如：1 114514
                    2.个人信息
                        例如：2
                    3.攻击 <技能名>
                        例如：3 普通攻击
                """)
                choice:str = input(">>>")
                choice_list = choice.strip().split()
                try:
                    if choice_list[0] == "1" and len(choice_list) == 2:
                        re2 = select_user(choice_list[1])
                        if re2 == [] or choice_list[1] == account:
                            print("目标不存在或者不可以选自己，3秒后返回...")
                            print("可选目标有: 12581")
                            sleep(3)
                        else:
                            target = choice_list[1]
                            print(f"当前目标为:{target}!")
                            print("2秒后返回...")
                            sleep(2)
                    elif choice_list[0] == "1" and len(choice_list) != 2:
                        print(f"请输入正确的指令!\n例如：1 12581\n\n3秒后返回...")
                        sleep(3)
                    elif choice_list[0] == "2":
                        a = Player(account)
                        print(a)
                        print("5秒后返回...")
                        sleep(5)
                    elif choice_list[0] == "3" and len(choice_list) != 2:
                        print(f"请输入正确的指令!\n例如：1 12581\n\n3秒后返回...")
                        print("####可选技能####\n普通攻击")
                        sleep(3)
                    elif choice_list[0] == "3" and len(choice_list) == 2:
                        a = Player(account)
                        b = Player(target)
                        if choice_list[1] == "普通攻击":
                            try:
                                print(a.attack(NormalAttack, b))
                            except:
                                print("你没有学会这个技能!")
                            print("5秒后返回...")
                            sleep(5)
                        else:
                            print("技能不存在\n\n3秒后返回...")
                            sleep(3)
                    else:
                        print("指令不存在\n\n1秒后返回...")
                        sleep(1)
                except:
                    print("错误！可能是指令不存在\n\n1秒后返回...")
                    sleep(1)
                    

