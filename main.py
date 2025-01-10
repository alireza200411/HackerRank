# author : alireza200411


# 1. write the function
def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            pass
             
    
    return leap


# 2. Nested Lists
main_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    tuple_stu = (name, score)
    list_stu = list(tuple_stu)
    main_list.append(list_stu)
    score_list = []
for data in main_list:
    score = data[1]
    score_list.append(score)

answer_list = []
score_list = list(set(score_list))
score_list.sort()
answer = score_list[1]
for data in main_list:
    if data[1] == answer:
        answer_list.append(data)
answer_list.sort()

for name in answer_list:
    print(name[0])