#导入模块
import getpass

#定义字典格式
digits_mapping = {
    "1" : u"石头",
    "2" : u"剪刀",
    "3" : u"布"
}

# f = input("输入：\n")
# c = input("输入：\n")
# print(f,c)

#隐藏玩家输入
player1 = getpass.getpass("请玩家一输入1(石头)、2(剪刀)或3(布): ")
player2 = getpass.getpass("请玩家二输入1(石头)、2(剪刀)或3(布): ")
#按照字典定义转换玩家输入格式
user1 = digits_mapping.get(player1)
user2 = digits_mapping.get(player2)


#显示玩家输入结果
print(player1,player2)
print(user1,user2)

#输赢结果判定
if user1 == '石头':
    if user2 == '石头':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  平局！！！ ' %(user1,user2))
    elif user2 == '剪刀':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  游戏结束!玩家1赢了！！！ ' %(user1,user2))
    elif user2 == '布':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  游戏结束!玩家2赢了！！！ ' %(user1,user2))
    else:
        print('玩家2的输入有误！！！拜拜！！！')

elif user1 == '剪刀':
    if user2 == '石头':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  游戏结束!玩家2赢了！！！ ' %(user1,user2))
    elif user2 == '剪刀':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  游戏结束!本轮平局！！！ ' %(user1,user2))
    elif user2 == '布':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  游戏结束!玩家1赢了！！！ ' %(user1,user2))
    else:
        print('玩家2的输入有误！！！拜拜！！！')
elif user1 == '布':
    if user2 == '石头':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  游戏结束!玩家1赢了！！！ ' %(user1,user2))
    elif user2 == '剪刀':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  游戏结束!玩家2赢了！！！ ' %(user1,user2))
    elif user2 == '布':
        print('>>>玩家1输入的是%s！ 玩家2输入的是%s！  游戏结束!本轮平局！！！ ' %(user1,user2))
    else:
        print('玩家2的输入有误！！！拜拜！！！')

else:
    if user2 == '石头':
        print('玩家1的输入有误！！！拜拜！！！')
    elif user2 == '剪刀':
        print('玩家1的输入有误！！！拜拜！！！')
    elif user2 == '布':
        print('玩家1的输入有误！！！拜拜！！！')
    else:
        print('玩家1和玩家2的输入均有误！！！拜拜！！！')









# import getpass
#
# player1 = getpass.getpass("请玩家一输入: ")
# if player1 == "1":
#     user1 = "石头"
# elif player1 == "2":
#     user1 = "剪刀"
# elif player1 == "3":
#     user1 = "布"
# else:
#     print("无效输入！")
#
# player2 = getpass.getpass("请玩家二输入: ")
# if player2 == "1":
#     user2 = "石头"
# elif player2 == "2":
#     user2 = "剪刀"
# elif player2 == "3":
#     user2 = "布"
# else:
#     print("无效输入！")
#
# print(user1,user2)