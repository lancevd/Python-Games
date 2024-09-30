


# print("Roll a dice? (y/n) \n"  )
answer = input("Roll a dice? (y/n) \n")

if (answer == 'y' or answer == 'Y'):
    import random
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f"{die1}, {die2}")
elif (answer == 'n' or answer == 'N'):
    print("Okay, you can try later!")
else: 
    print("Invalid input!")
# print(answer)

