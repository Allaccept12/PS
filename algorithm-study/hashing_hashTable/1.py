import random



TRIALS = 100000
same_birthday = 0

index = 3 //10000
print(index)

# for _ in range(TRIALS):
#     birthdays = []
#
#     #23명이 모였을때 생일이 같을 경우 same_birthday +=1
#     for i in range(24):
#         birthday = random.randint(1,365)
#         if birthday in birthdays:
#             same_birthday +=  1
#             break
#         birthdays.append(birthday)
#
#
# print(f'{same_birthday / TRIALS * 100}%')