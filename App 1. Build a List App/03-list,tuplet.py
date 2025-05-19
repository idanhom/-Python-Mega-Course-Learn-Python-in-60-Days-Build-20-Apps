""" filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentations.txt"]

for filename in filenames:
    print(filename)
    filename = filename.replace(".", "-", 1)
    
    print(f"new: {filename}")

 """
 

# seconds = [1.23, 1.45, 1.02]
# current = 1.11

# seconds.append(current)

# elements = ['a', 'b', 'c']
# print(elements[1])

# elements = ['a', 'b', 'c']
# elements[1] = "x"
# print(elements)

# elements = ['a', 'b', 'c']
# new = 'x'
# new = elements[1]
# print(elements)

# rainfall = [
#     3.14,
#     3,
#     "item1",
#     []
#     ]
    
# print(type(rainfall[0]))

# products = ['table', 'chair', 'door']

# for product in products:
#     print(f"Product: {product}")

# filenames = ['document', 'report', 'presentation']

# for idx, filename in enumerate(filenames):
#     print(f"{idx}-{filename.capitalize()}.txt")

# help(list.pop)

# print(dir(list))

# help(list.pop)


# print(dir(list))

# help(list.sort)

"""
Length Calculation in For-Loop

See this list:
mylist = ['a', 'b', 'c', 'd']

Add some code that:
(1) iterates over the items of mylist,
(2) prints out the current length of the list in each iteration

Here is how the output would look like:
4
4
4
4


"""

"""### Understanding the Problem: Thinking Through the For-Loop and List Length

You're given a list:

```python
mylist = ['a', 'b', 'c', 'd']
```

You're supposed to **loop through each item in this list**, and during each loop iteration, **print the current length of the list**.

Let’s break down the reasoning and concepts to help you get started without giving away the exact code.

---

### Key Concepts to Understand

#### 1. **List Length Doesn't Change (Here)**

* The list `mylist` has 4 items.
* If you don’t add or remove items during the loop, the list length stays **constant**.

#### 2. **`for` Loop Behavior**

* A `for` loop like `for item in mylist:` goes through the list **one item at a time**.
* The variable (e.g., `item`) holds the current element during each iteration, but this **does not change the list itself**.

#### 3. **Getting the List Length**

* You can get the length of a list using the built-in function `len(mylist)`.
* This can be called **anywhere in the code**—before, during, or after the loop.

---

### Putting the Thoughts Together

So, imagine each time you’re looping over the list, you ask:

> "Hey Python, how long is this list right now?"

You know how to ask that (with `len(...)`), and you know where to ask it (inside the loop).

---

### Next Step: Mental Model

Try thinking like this:

* I’ll loop through the list, like reading each item.
* On each read, I’ll pause and ask Python to tell me how long the whole list is.
* Since nothing’s being added or removed, it should give the same answer each time.

Try implementing a few lines of code based on this thought process! Let me know if you'd like a hint or want to check your result.
"""





mylist = ['a', 'b', 'c', 'd']
