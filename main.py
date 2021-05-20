from random import randint
first_run = bool(0)

def f1_fun_nums():
    num_1 = randint(-100,100)
    num_2 = randint(-100,100)
    print(f'number 1 = {num_1}')
    print(f'number 2 = {num_2}')
    if num_2 == num_1:
        print(f'sum is {num_2 + num_1} \n difference is {num_1 - num_2} \n they are equal')
    elif num_2 < num_1:
        biger = num_1
        print(f'\n sum is {num_2 + num_1} \n difference is {num_1-num_2} the bigger one is number 1 or {num_1}')
    elif num_2 > num_1:
        print(f'sum is {num_2 + num_1} \n difference is {num_1 - num_2} \n the bigger one is number 2 or {num_2}')
    pass


def f2_backward(name):
    print(name)
    print(name[::-1])

def high_low(l,h):
    try:
        i = randint(int(l),int(h))
        print(i)
        even = bool()
        div_5 = bool()
        div_6 = bool()
        if i/2 == i//2:
            even = True
        if i/5 == i//5:
            div_5 = True
        if i / 6 == i // 6:
            div_6 = True
        print(f'Even = {even}')
        print(f'divisible by 5  = {div_5}')
        print(f'divisible by 6  = {div_6}')
    except:
        print('Exception occurred try again')



def list_sorter(new_list_item):
    list = ['cups','plates','dogs','cats','i dont know what else']
    list.append(new_list_item)
    list.sort()
    print(*list,sep=' ,')
    return list[-1]

def menu():
    global first_run
    if first_run == 0:
        name = input('What is your name?_')
        print(f'Hello, {name}! Welcome to this program.')
    else :
        pass
    print('Here are the available functions to run:\n1. funNums()\n2. backwards()\n3. isDivisible()\n4. listSorter()\nW'
          'hich function would you like to run?')
    funtion_to_run = input('(1,2,3,4)')
    if funtion_to_run.isnumeric():
        funtion_to_run = int(funtion_to_run)
        if funtion_to_run == 1:
            f1_fun_nums()
            print('\n')
        elif funtion_to_run == 2:
            f2_backward(input('Enter phrase to reverse'))
            print('\n')
        elif funtion_to_run == 3:
            high_low(input('bottom of range'), input('top of range'))
        elif funtion_to_run == 4:
            list_sorter(input('What would you like to append?'))


    first_run = True
    menu()


menu()