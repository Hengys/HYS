# Lab 1.2 get input two numbers and display the sum of the two numbers



number_1 = int(input("Please enter number 1:"))
number_2 = int(input("Please enter number 2:"))

total = number_1+number_2

# print("The total number is", total)
# Display --> The sum of 5 and 6 is 11
print("The Sum is ",total," ",number_1,"and ",number_2 )
print("The sum of {} and {} is {}".format(number_1,number_2,total))
print("number 1 is :",number_1)
print("number 2 is :",number_2)
print("total :",total)