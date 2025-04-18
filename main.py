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


# 3. sWAP-cASE
def swap_case(s):
    x = []
    for cha in s:
        if cha.isupper():
            cha = cha.lower()
            x.append(cha)   
        else:
            cha = cha.upper()
            x.append(cha) 
    return ''.join(x)


# 4. Merge the Tools!
def merge_the_tools(string, k):
    main_dict = {}
    n = len(string)
    for char in range(0, (n//k)):
        sub_list = []
        s = string[char*k:((char*k)+(k-1))+1]
        for ch in s:
            if ch not in sub_list:
                sub_list.append(ch)
            else:
                pass
        else:
            print(''.join(sub_list))


# 5.  Map and Lambda Function
cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2: 
        return [0, 1]
    else:
        my_list = [0, 1]
        while len(my_list) < n:
            answer = my_list[len(my_list)-1] + my_list[len(my_list)-2]
            my_list.append(answer)
        return my_list
    

# 6. List Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())
list_ = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != n]


# 7. Sring Formatting
def print_formatted(number):
    sdp = len(bin(number)) - 2
    for num in range(1, number + 1):
        answer = f'{num:{sdp}} {num:{sdp}o} {num:{sdp}x} {num:{sdp}b}'
        print(answer.upper())


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
