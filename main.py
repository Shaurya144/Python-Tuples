# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
fruits = ("apple", "banana", "cherry")
print(fruits)

# Tuple items are indexed, the first item has index [0], same as lists

# To get the number of items
# use len()

# for a tuple with only one item you use a .
SecondTuple = ("apple",)

# Tuple items can be of any data type

# Check if "apple" is present in the tuple
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits tuple")

# Tuples are unchangeable but lists aren't 
# so you can convert it to a list, change it then convert it back
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)