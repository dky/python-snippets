# Fetch all the methods you can call on an object, there are a lot!
# Because everything in Python is an object.
# You technically aren't supposed to call methods that have __ in them.

arr = [25]
attrs = dir(arr)

print(attrs)
