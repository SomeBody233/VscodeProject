import random

def guess_number():
    true_num = random.randint(1, 100)
    user_num = int(input("请输入一个整数:"))
    count = 1
    while true_num != user_num:
        if true_num > user_num:
            print("太小了，请重新输入！")
        elif true_num < user_num:
            print("太大了，请重新输入！")
        count += 1
        user_num = int(input("请输入一个整数："))
    print("恭喜您，您猜中了！您一共猜了%d次" %count)

guess_number()