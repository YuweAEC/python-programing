"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
my_str = "Hello"
num = 100 
num2 = 10.5
# num3 = check complex number
my_bool = True 
dic1 = { "name": "Alice" , "age": 36 } 
arr = [1, 2, 3]
arr2 = [1,1,5,4,3,3]
set1 = set(arr2)
x = None
print(type(my_str),type(my_bool),type(num), type(dic1),type(arr),type(x))
print(set1,type(set1))