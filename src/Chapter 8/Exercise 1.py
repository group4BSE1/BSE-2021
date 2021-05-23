# A program takes a list modifies removing the first and last elements and returns non.(function chop)
# it also takes a list and returns  a new list  that contains all but the first and last elements(function middle)
list_st = ['lion', 'Tiger', 'Cheetah', 'Cat', 'Dog']
list_nd = ['Red', 'Blue', 'Green', 'Orange', 'Black']


def chop(list_1):
    del list_1[0]
    del list_1[-1]


def middle(list_1):
    new_list = list_1[1:]
    del new_list[-1]
    return new_list


print(chop(list_st))
print(middle(list_nd))
