#Program to Reverse a Number
input_number = int(input("Enter a number to revers it: "))
old=input_number
rev_num = 0
while input_number>0:
    temp = input_number%10
    rev_num = (rev_num*10)+temp
    input_number=input_number//10
print("Reverse of a given",old,"is:",int(rev_num))                                                                                                                                                                                                                                                                                       