#Taking total amount as input from the user.
amount = int(input("Please enter amount to withdraw. "))
#Calculating the number of notes of different denominations
note_1 = amount // 100
note_2 = (amount % 100) // 50
note_3 = ((amount % 100) % 50) // 20
note_4 = (((amount % 100) % 50) % 20) // 10
note_5 = ((((amount % 100) % 50) % 20) % 10) // 1

print("Amount of 100s notes: ", note_1)
print("Amount of 50s notes: ", note_2)
print("Amount of 20s notes: ", note_3)
print("Amount of 10s notes: ", note_4)
print("Amount of 1s coins: ", note_5)