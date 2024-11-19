#In python provide us with a short and consive way to contruct new sequence such as 
#(list,set,dict..etc.).using previously define sequence.

def islist():
    input_list=[1,2,3,4,4,5,5,6,6,6]
    output_set=set()
    for var in input_list:
        if var%2==0:
           output_set.add(var)
    print("output set using for loop:",output_set)

    input_list=[1,2,3,4,4,5,5,6,6,6]
    set_using_comp={var for var in input_list if(var%2==0)}
    print("output set using for set comprehensions:",set_using_comp)
islist()