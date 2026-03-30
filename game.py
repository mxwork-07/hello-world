# 猜数字游戏
import random

print("=== 猜数字游戏 ===")
print("我想了一个 1-100 的数字，你来猜！")

number = random.randint(1, 100)
count = 0

while True:
    guess = input("请输入你的猜测：")
    
    # 检查输入是否为数字
    if not guess.isdigit():
        print("请输入数字！")
        continue
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("太小了！")
    elif guess > number:
        print("太大了！")
    else:
        print(f"恭喜你猜对了！答案是 {number}")
        print(f"你一共猜了 {count} 次")
        break

print("游戏结束！")