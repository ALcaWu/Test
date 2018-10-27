# # counting
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# # 用户选择退出
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
#
# # cities
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# # continue
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#
#     print(current_number)
#
# # confirmed_users
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# Test 1
text = "\n请输入您的年龄:"
text += "\n输入'0'退出系统。"
while True:
    age = int(input(text))
    if 0 < age < 3:
        print("可免费观看")
    elif 3 <= age <= 12:
        print("票价为10元")
    elif age > 12:
        print("票价为15元")
    elif age == 0:
        print("谢谢使用")
        break
