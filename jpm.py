
number = [1,4,0]
goal = [1,8]
moves = 6



# Usefull functions:

def zero_checker(number):
    """Checks if the number starts with one or multiple zeros, and returns the number with the zeros removed.

    Args:
        number (List): List with each entry being a number 0-9.

    Returns:
        list: List with each entry being a number 0-9, and it is no longer starting with 0.
    """
    start = 0
    if number == []:
        return number
    if(number[0] == 0):
        for i in range(len(number)):
            if(number[i] != 0):
                start = i
                break
            if(i >= len(number) - 1):
                return [0]

    return number[start:]
            
# Main functions for the game

def transform(number, initial_value = [9,9], transformed_value = [6,0]):
    """Checks if a sequence (initial_value) of numbers is present inside number, it then replaces the sequence with transformed_value

    Args:
        number (list): List with each entry being a number 0-9.
        initial_value (list): List with each entry being a number 0-9.. Defaults to [0].
        transformed_value (list): List with each entry being a number 0-9.. Defaults to [5,0].

    Returns:
        list: number with initial value replaced with transformed_vlaue.
    """
    i = 0
    while i < len(number):
        bo = True
        if(number[i] == initial_value[0]):
            for j in range(1, len(initial_value)):
                if((i + j) >= len(number)):
                    bo = False
                    break
                if(initial_value[j] != number[i + j]):
                    bo = False
                    break
            if(bo):
                temp = []
                for j in range(i):
                    temp.append(number[j])
                
                for j in range(len(transformed_value)):
                    temp.append(transformed_value[j])
                    
                for j in range(i+len(initial_value), len(number)):
                    temp.append(number[j])
                
                number = temp
                i = i + len(transformed_value)
            else:
                i += 1
        else:
            i += 1
    number = zero_checker(number)
    return number


def reverse(number):
    """Takes in a list of intgers, called number, and returns it in reverse order.

    Args:
        number (list): List with each entry being a number 0-9.

    Returns:
        list: List in reverse order
    """
    result = number[::-1]
    print('reversed: ', result)
    return zero_checker(result)


def shift_left(number):
    """Takes in a list of integers, number, and returns number with its left most integer removed and appended at the end

    Args:
        number (list): List with each entry being a number 0-9.

    Returns:
        list: List with its left most integer removed and appended at the end
    """
    if number == []:
        return number
    overflow = number[0]
    result = number[1:]
    result.append(overflow)
    return zero_checker(result)


def shift_right(number):
    """Takes in a list of integers, number, and returns number with its right most integer removed and attached to the start

    Args:
        number (list): List with each entry being a number 0-9.

    Returns:
        list: List with its right most integer removed and attached to the start.
    """
    if number == []:
        return number
    overflow = [number[-1]]
    result = number[:-1]
    for i in range(len(result)):
        overflow.append(result[i])
    return zero_checker(overflow)


def mirror(number):
    """Mirrors a number by appending the number in reverse order to the initial number

    Args:
        number (list): List with each entry being a number 0-9.

    Returns:
        list: List where the reverse of the inital number is appended to the inital number.
    """
    temp = []
    rev = number[::-1]
    for element in number:
        temp.append(element)
    for element in rev:
        temp.append(element)
    return zero_checker(temp)
  
        
def add_number(number, a):
    """Adds a value to the back of the number.

    Args:
        number (list): List with each entry being a number 0-9.
        a (list): List with each entry being a number 0-9..

    Returns:
        list: appends each element in a to number
    """
    for element in a:
        number.append(element)
    return zero_checker(number)


def addition(number, a = [2]):
    """Does an aditon to both numbers

    Args:
        number (list): List with each entry being a number 0-9.
        a (list): List with each entry being a number 0-9.
        
    Returns:
        list: Adds both numbers
    """
    
    counter = len(number) - 1
    number_value = 0
    a_value = 0
    for element in number:
        number_value += element * (10 ** counter)
        counter -= 1
    
    counter = len(a) - 1
    for element in a:
        a_value += element * (10 ** counter)
        counter -= 1
        
    total = number_value + a_value
    temp = []
    while total > 0:
        temp.append(total%10)
        total = total//10
    
    return zero_checker(temp[::-1])


def addition2(number, a = [8]):
    """Does an aditon to both numbers

    Args:
        number (list): List with each entry being a number 0-9.
        a (list): List with each entry being a number 0-9.
        
    Returns:
        list: Adds both numbers
    """
    
    counter = len(number) - 1
    number_value = 0
    a_value = 0
    for element in number:
        number_value += element * (10 ** counter)
        counter -= 1
    
    counter = len(a) - 1
    for element in a:
        a_value += element * (10 ** counter)
        counter -= 1
        
    total = number_value + a_value
    temp = []
    while total > 0:
        temp.append(total%10)
        total = total//10
    
    return zero_checker(temp[::-1])


def multiplication(number, a = [3]):
    """Does a multiplication to both numbers

    Args:
        number (list): List with each entry being a number 0-9.
        a (list): List with each entry being a number 0-9.
        
    Returns:
        list: Multiplies both numbers
    """
    
    counter = len(number) - 1
    number_value = 0
    a_value = 0
    for element in number:
        number_value += element * (10 ** counter)
        counter -= 1
    
    counter = len(a) - 1
    for element in a:
        a_value += element * (10 ** counter)
        counter -= 1
        
    total = number_value * a_value
    temp = []
    if(total == 0):
        return [0]
    while total > 0:
        temp.append(total%10)
        total = total//10
    
    return zero_checker(temp[::-1])


def division(number, a = [3]):
    """Does a division between number and a, and it returns the number if the number is not divisible by a.

    Args:
        number (list): List with each entry being a number 0-9.
        a (list): List with each entry being a number 0-9.
        
    Returns:
        list: divides both numbers
    """
    
    counter = len(number) - 1
    number_value = 0
    a_value = 0
    for element in number:
        number_value += element * (10 ** counter)
        counter -= 1
    
    counter = len(a) - 1
    for element in a:
        a_value += element * (10 ** counter)
        counter -= 1
        
    if (number_value%a_value != 0):
        return number
    
    total = number_value // a_value
    temp = []
    if(total == 0):
        return [0]
    while total > 0:
        temp.append(total%10)
        total = total//10
    
    return zero_checker(temp[::-1])
        

def get_path(number, goal, list_of_functions, depth=1, path=[]):
    print(number)
    available_functions = []
    if(number == goal):
        return path
    if (depth > moves):
        return -1
    for element in list_of_functions:
        if (element(number) != number):
            available_functions.append(element)
    for element in available_functions:
        temp = []
        for thing in path:
            temp.append(thing)
        temp_number = element(number)
        temp.append(element.__name__)
        route = get_path(temp_number, goal, list_of_functions, depth + 1, temp)
        
        if (route != -1):
            return route
    return -1
  
  
list_of_functions = [mirror, transform, multiplication, shift_right, division]

path = get_path(number, goal, list_of_functions)
print(path)
  
  
  
  
  
  
  
  
  
  
  
    
# print(get_path(number, goal, list_of_functions))
# list_of_functions = [transform1, transform2, transform3, shift_left]
# Problem with a function, try using a dictionnary as the path to see what function isnt working well
# Add 0 checker to all functions