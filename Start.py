bank = 100
money = 100

print("Welcome to the banking system!")
print("In this game you manage your own virtual money")
print("You can gamble you way to richness, or spend it on other stuff")
print("You currently have %d dollars in the bank" %bank)
print("And %d dollars in cash" %money)
print("For the moment, you can only do a few things:")
print("1. Deposit money")
print("2. Withdraw money")
print("3. Gamble")
choice_1 = input("> ")


while True:
    if choice_1 = 1:
        print("You chose to deposit money.")
        print("You currently have %d dollars in cash to deposit." %money)
        print("How much of them do you wish to deposit? (quit to exit)")
        deposit = input("> ")
        if deposit = "quit":
            continue
        else:
        	money += deposit
            
            
    if choice_1 = 2:
        print("YOu chose to withdraw money")
        print("You currently have %d dollars in the bank." %bank)
        print("How much do you want to withdraw? (quit to exit)
        withdraw = input("> ")
        if withdraw > bank:
        	print("You do not have that amount")
            continue
        elif withdraw != isdigit():
        	print("That is not a valid amount")
        else:
            money -= withdraw