import functools

sorted_ignore_case = functools.partial(sorted,key=str.upper)

print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))