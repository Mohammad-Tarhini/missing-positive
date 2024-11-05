# finds the smallest positive integer that is missing from a given list
def first_missing_positive(numbers):
    #step1:find min postive number in numbers and if all numbers less then 0 ,will give us 1
    m=1
    for i in range(len(numbers)):
        if numbers[i]>0 and numbers[i]<m:
            m=numbers[i]
    if m-1>0: #check if there  positive number small then min
       return m-1
    while m in numbers:
        m+=1
    return m
        


