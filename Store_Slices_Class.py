tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming'
]

print(tags[:2])
# ['python', 'development']

print(tags[1:4:2])
# ['development', 'code']

slice_obj = slice(2)
# slice(None, 2, None) 
# 1st position start point, 2nd interval-step, 3rd end point
slice_obj2 = slice(1, 4)
# ['development', 'tutorials', 'code']
slice_obj3 = slice(1, 4, 2)
# ['development', 'code']
print(slice_obj3.start)
print(slice_obj3.stop)
print(slice_obj3.step)
# 1
# 4
# 2
print(slice_obj)
print(tags[slice_obj])
print(tags[slice_obj2])
print(tags[slice_obj3])




