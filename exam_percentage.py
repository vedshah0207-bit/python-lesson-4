#Take scores from input from user
print("Enter scores obtained in 4 subjects of yours.")
math = int(input("Maths: "))
science = int(input("Science: "))
hindi = int(input("Hindi: "))
english = int(input("English: "))

#we will calculate the percentage of marks
sum = math + science + hindi + english
print("Total score:", sum)

#now the percentages
percentages = (sum / 400) * 100
print("Average percentages are:", percentages)
