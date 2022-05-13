#Initalizing (moduals)
import random
import time
import timeit

#Don't attention not really charming things here, but important
power = True
score = 0
finall_answer = 0
num_list = []

#Defining a func to add numbers (+)
def add(x,y):

    global finall_answer
    finall_answer = x + y
    global num_list
    num_list = [x,y]

#Defining a func to tosubtraction numbers (-)
def subtraction(x,y):

    global finall_answer
    finall_answer = x - y if x >= y else y - x
    global num_list
    num_list = [x,y]
    num_list.sort()

#Defining a func for closig the program in a fancy way
def shut_time(v):
    print(f'\n Shuting down in {v} second')
    for i in range(v,0,-1):
        time.sleep(1)
        print(' ',i)


start = input(" Press anything to start the MathQuiez : ")
start_time = timeit.default_timer()

#Most important part of our code , loop is like a main core , power ....
while power:

    #generating random numbers
    x = random.randrange(1,1000)
    y = random.randrange(1,1000)

    #Choising math operations [+ -]
    math = ['+','-']
    global operation
    o = start
    if o == '+' :
        operation = '+'
    elif o == '-' :
        operation = '-'
    else :   
        operation = random.choice(math)

    #Here we go the IFs part (decision room)
    if operation == '+':
        add(x,y)
        
    elif operation == '-':
        subtraction(x,y)

    #We using 'try except' becauz wr are cool and wanna handeling the possible error 
    try:
        answer=int(input('\n What is the answer of ' + str(num_list[-1]) + ' ' + str(operation) + ' ' + str(num_list[0]) + ' ? ' ))

        if answer == finall_answer :
            print(' Correct!')
            score += 1
            print(f' Score is {score}')

        else:
            print(f'\n False, the correct answer is {finall_answer} ')
            respawn=input('\n would you like to try again? (press \'Y\' to confirm, anything else to exit) ')
            print(('\n Your final score is {}').format(score))

            if respawn in ('y','Y') :
                score = 0
                continue
            else:
                #Shuting down 
                end_time=timeit.default_timer() - start_time
                run_time= str(round(end_time/60,3)) +' min' if end_time > 60.0 else str(round(end_time,3)) + ' second'
                print(f' Run time is {run_time}')
                print(shut_time(10))
                power=False

    except ValueError:       
        print("\n Error, the input must be an integer number")