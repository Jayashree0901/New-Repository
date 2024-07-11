# print('hello')

# from collections import deque
# q = deque([5,7,3,9])
# q.popleft()
# print(q)

# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]
# print({k:v for k,v in zip(keys, values)})

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# f = [[row[i] for row in matrix] for i in range(4)]

# print(f)
# print(list(zip(*matrix)))

# s = '[1,2,3,4]'
# print(eval(s))

# import os
# print(type(os.mkdir))

import json
# x = json.loads('"\\"foo\\\\bar"')
# print(x)

emp_det = {'id':1, 'name':'Jaya', 'age':23, 'gender':'female', 'hobbies':['singing', 'badminton', 'drawing']}

# with open('try.json', mode='w', encoding='utf-8') as wfile:
    # print(json.dump(emp_det))  #this dump() function needs a positional arguement fp, i.e. a file to store the json output
    # json.dump(emp_det, wfile, indent=2)
    
wfile = open('try.json', 'w')
json.dump(emp_det, wfile, indent=2)
wfile.close()
# print(json.dumps(emp_det, indent=2))

# json_var ="""
# {
# 	"Country": {
# 		"name": "INDIA",
# 		"Languages_spoken": [
# 			{
# 				"names": ["Hindi", "English", "Bengali", "Telugu"]
# 			}
# 		]
# 	}
# }
# """
# var = json.loads(json_var)
# print(json_var)