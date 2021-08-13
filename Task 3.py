def my_func(my_list, value):
    s = 0
    for element in my_list:
        if element % value == 0:
            s = element
            print(s)
        else:
            element += 1
mylist = [1,4,5,10,9,12,6]
print( "the numbers in " , mylist , "that are divisble by 2 are : ")
my_func(mylist,2)
