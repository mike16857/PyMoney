import sys


# The 5 function definitions here
def initialize():
    try:
        fh = open('records.txt', 'r')
        print('Welcome Back!')
        init_money = int(fh.readline())
        st = ''
        tmp2 = fh.readlines()
        if not tmp2:    
            rcd = []
        else:
            for tp in tmp2:
                st += tp
            rcd = [eval(s) for s in st.split('\n')]
        fh.close()
    
    except FileNotFoundError:  # No original record file
        try:
            init_money = int(input('How much money do you have? '))

        except ValueError:  # User inputs a string that cannot be converted to integer
            sys.stderr.write('Invalid value for money. Set to 0 by default.\n') 
            init_money = 0

        rcd = []

    except:  # Record in the file does not match the format
        sys.stderr.write('Invalid format in records.txt. Deleting the contents.\n')
        open('records.txt','w').close()

        try:
            init_money = int(input('How much money do you have? '))

        except ValueError:  # User inputs a string that cannot be converted to integer
            sys.stderr.write('Invalid value for money. Set to 0 by default.\n') 
            init_money = 0

        rcd = []

    return init_money, rcd


def add(init_money, rcd):
    original_rcd = rcd[:]
    original_init_money = init_money
    try:
        entry_to_add = input('Add an expense or income record with description and amount:\ndesc1 amt1, desc2 amt2, desc3 amt3, ...\n').split(',')
        for i in entry_to_add:
            rcd.append(tuple(i.split()))
            init_money += int(i.split()[1])

        return init_money, rcd

    except IndexError:  # Input string does not follow the format
        sys.stderr.write('The format of a record should be like this: breakfast -50.\nFail to add a record.\n')
        return original_init_money, original_rcd
    
    except ValueError:  # The second string of a record, after splitting, cannot be converted to an integer
        sys.stderr.write('Invalid value for money.\nFail to add a record.\n')
        return original_init_money, original_rcd 
    

def view(init_money, rcd):
    print('Here are your expense and income records:')
    print('Index    Description     Amount')
    print('=====    ==============  ======')

    for i, (item, amount) in enumerate(rcd):
        print(f'{i:<5d}    {item:15s} {int(amount):<6d}')

    print('=====    ==============  ======')
    print(f'Now you have {init_money} dollars.')  


def delete(init_money, rcd):
    if len(rcd) == 0:   # Check if there is record (ADDED FUNCTION)
        print('Currently no record, go and add some records.')
        return init_money, rcd

    tmp = []
    entry_to_delete = tuple(input('Enter an expense or income record you want to delete with description and amount: ').split())

    if len(entry_to_delete) != 2:
        print('Invalid format. Fail to delete a record.')  # Input format is invalid

    elif entry_to_delete not in rcd:
        print('Record not found. Fail to delete a record.')  # The specified record does not exist

    else:
        for i in range(len(rcd)):
            if rcd[i] == entry_to_delete: 
                tmp += [i]

        if len(tmp) == 1:
            rcd.remove(entry_to_delete)
            init_money -= int(entry_to_delete[1])

        else:
            print(f'{len(tmp)} identical records found. Which are')
            for i in tmp:
                print(f'Entry #{i}')

            n = int(input('Which one do you want to delete? '))

            while (n not in tmp):
                if n == -1: # Quit delete mode (ADDED FUNCTION)
                    break
                print('Invalid input, please try again.')   # The specified record does not exist 
                n = int(input('Which one do you want to delete? '))
            else:
                del(rcd[n])
                init_money -= int(entry_to_delete[1])

    return init_money, rcd


def save(init_money, rcd):
    with open('records.txt', 'w') as fh:
        fh.write(f'{init_money}\n')
        fh.writelines('\n'.join([str(s) for s in rcd]))


initial_money, records = initialize()
while True:
    command = input('\nWhat do you want to do (add / view / delete / exit)? ')
    if command == 'add':
        initial_money, records = add(initial_money, records)

    elif command == 'view':
        view(initial_money, records)

    elif command == 'delete':
        initial_money, records = delete(initial_money, records)

    elif command == 'exit':
        save(initial_money, records)
        break

    else:
        sys.stderr.write('Invalid command. Try again.\n')


#region
# entries = []
# tmp = [] # record the index of the entry to be deleted


# try:
#     fh = open('records.txt', 'r')
#     print('Welcome Back!')
#     money = int(fh.readline())
#     st = ''
#     tmp2 = fh.readlines()
#     for tp in tmp2:
#         st += tp
#     entries = [eval(s) for s in st.split('\n')]
#     fh.close()

# except FileNotFoundError:
#     money = int(input('How much money do you have? '))


# flag = True
# while flag:
#     action = input('What do you want to do (add / view / delete / exit)? ')

#     if action == 'add':
#         entry_to_add = input('Add an expense or income record with description and amount:\ndesc1 amt1, desc2 amt2, desc3 amt3, ...\n').split(',')

#         for i in entry_to_add:
#             entries.append(tuple(i.split()))
#             money += int(i.split()[1])
#         # print(entries)
#         # print(money)

#     elif action == 'view':
#         # print(entries)
#         print('Here are your expense and income records:')
#         print('Index    Description     Amount')
#         print('=====    ==============  ======')

#         for i, (item, amount) in enumerate(entries):
#             print(f'{i:<5d}    {item:15s} {int(amount):<6d}')

#         print('=====    ==============  ======')
#         print(f'Now you have {money} dollars.\n')
        
#     elif action == 'delete':
#         entry_to_delete = tuple(input('Enter an expense or income record you want to delete with description and amount: ').split())

#         if entry_to_delete not in entries:
#             print('Record not found.')
#         else:
#             for i in range(len(entries)):
#                 if entries[i] == entry_to_delete: 
#                     tmp += [i]

#             if len(tmp) == 1:
#                 entries.remove(entry_to_delete)
#                 money -= int(entry_to_delete[1])

#             else:
#                 print(f'{len(tmp)} identical records found. Which are')
#                 for i in tmp:
#                     print(f'Entry #{i}')

#                 n = int(input('Which one do you want to delete? '))

#                 while (n not in tmp):
#                     print('Invalid input, please try again.')
#                     n = int(input('Which one do you want to delete? '))
#                 else:
#                     del(entries[n])
#                     money -= int(entry_to_delete[1])
        
#         tmp = []
            

#     elif action == 'exit':
#         with open('records.txt', 'w') as fh:
#             fh.write(f'{money}\n')
#             fh.writelines('\n'.join([str(s) for s in entries]))
        
#         flag = False
#         break

#     else:
#         print('Invalid input, please try again.')
#endregion