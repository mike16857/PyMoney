money = int(input('How much money do you have?'))
item, change = input('Add an expense or income record with description and amount:\n ').split()
change = int(change)
print('Now you have %d dollars.' %(money + change))