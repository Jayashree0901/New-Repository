# print('hello')

# from collections import deque
# q = deque([5,7,3,9])
# q.popleft()
# print(q)

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
print(json.dump(emp_det))
print(json.dumps(emp_det, indent=2))