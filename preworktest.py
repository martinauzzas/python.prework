#QUESTION 1
#write a function to print hello_USERNAME! USARNAME is the input of the function

def hello_name(user_name):
    user_name = input("What is your username? ")
    print ("hello_" + user_name.upper().rstrip())

hello_name(input)


#QUESTION 2
#Write a python function, first_odds that prints the odds numbers from 1-100 and returns nothing

def first_odds(numbers):
    for number in numbers:
        if number % 2 != 0:
            print (number)


numbers = list(range(1, 100,))

first_odds(numbers)


#QUESTION 3
# Write a python function, max_num_in_list to return the max number of a given list. 

def max_num_in_list(a_list):
    print (max(a_list))

a_list = list(range(3, 71))  
 
max_num_in_list(a_list)    
    

#QUESTION 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but non divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type

def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    if (a_year % 100) and (a_year % 400) == 0:
        return True
    else: 
        return False
    
a_year = 2024


print(is_leap_year(a_year))


# QUESTION 5
# Write a function to check to see if all number in list are consecutive numbers. For example [2, 3, 4, 5, 6, 7] 
# are cosecutive numbers, but [1, 2 , 4, 5] are not. The return should be boolean type

def is_consecutive(a_list, n):
	a_list.sort()
	for i in range (1,n):
		if(a_list[i]!=a_list[i-1]+1):
			return False
			
	return True

a_list = [5, 4, 3, 2, 1, 3]
n = len(a_list)

print(is_consecutive(a_list, n))
 