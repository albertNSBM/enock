import random
friend_number =int(input("Enter the number of friends joining (including you):\n"))
if friend_number<= 0:
    print("No one is joining for the party")
else:
    friend_patty = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(1,friend_number+1):
        frend_Name = input()
        friend_patty.update({ frend_Name: 0}) 
    print("Enter the total bill value:")
    pay_bill = int(input())
    my_fiends = list(friend_patty.keys())
    every_one_bill = pay_bill/friend_number
    for m in my_fiends:
        friend_patty.update({m: round(float(every_one_bill), 2)})
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    luck_answer = input()
    if luck_answer=='YES' or luck_answer =='yes' or luck_answer == 'Yes':
        choosen = random.choice(my_fiends)
        print("{} is lucky one!".format(choosen))
        for h in my_fiends:
            if h == choosen:
                friend_patty.update({h: 0})
            else:
                every_one_bill = float(pay_bill/(friend_number - 1))
                friend_patty.update({h: round(float(every_one_bill), 2)})
        print(friend_patty)    
    else:
        print("No one is going to be lucky")
        print(friend_patty)