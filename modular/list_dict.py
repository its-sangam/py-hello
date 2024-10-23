"""
array on js is list on py
object on js is dict on py
"""
a_list = [3,4,5,10]
b_list = [1,11,111]
a_dict = {'name':'John', 'gender':'male'}

# print(f"last item of list is {a_list[len(a_list)-1]}")

merged_list = a_list+b_list
# merged_list.slice(0,6)
print(merged_list)
'''
"""
push in js is append in py
"""
a_list.append(5)
print(f"last item of list is {a_list[len(a_list)-1]}")

a_list.pop()
print(f"last item of list is {a_list[len(a_list)-1]}")
'''