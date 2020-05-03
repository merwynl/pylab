"""
[summary]
"""

# Simple if else statement that prints a statement if a boolean value is set to True or false
is_male = True


if is_male: 
    print('君は男だった')
else:
    print('君は女の子だった')


"""
Use an 'or' conditional statement if you want more than one variable to be paseed through"
"Only requires one of the provided conditions to be true
"""
is_man = True
is_tall = True

if is_man or is_tall: 
    print('君は男性だったと背が高い')
else:
    print('君は女性だったと背が高くない')


""" 
Use an 'and' conditional statement if you want more than one variable to be passed through
Required all of the provided conditions to be true
ElseIf statement provides another level of condition.
"""
are_male = False
are_tall = True

if are_male and are_tall: 
    print('君は男性だったと背が高い')
elif are_male and not(are_tall):
    print('君は男性だったと背が高い')
elif are_tall and not(are_male):
    print('君は女性だったと背が高くない')
else:
    print('人間じゃない')


# If statement that compares different values and prints the largest of three provided argument values
def max_num(num1, num2, num3):
    """[summary]
    
    Arguments:
        num1 {[type]} -- [description]
        num2 {[type]} -- [description]
        num3 {[type]} -- [description]
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

result = max_num(300, 40, 5)
print(result)
