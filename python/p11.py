#Program to Find Sum of digits of a number
input_num=int(input('Enter a number to find its sum of digits'))
#conver no. into string to access all digits 
number_str=str(input_num)
total_sum=0
for char in number_str:
    total_sum+=int(char)
print(f"The sum of digits of {input_num} is {total_sum}")    