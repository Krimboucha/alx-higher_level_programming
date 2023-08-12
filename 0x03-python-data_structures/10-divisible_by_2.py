def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        if num % 2 == 0:
            result += True
#           result.append(True)
        else:
            result += False
#           result.append(False)
    return result
