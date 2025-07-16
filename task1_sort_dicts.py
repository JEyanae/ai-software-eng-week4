data = [
    {"name": "Joseph", "age": 25},
    {"name": "Eyanae", "age": 20},
    {"name": "Longoli", "age": 30}
]
Copilot said: Got it! You provided a Python variable
Got it! You provided a Python variable named data containing a list of dictionaries, each representing a person with their name and age:

Python
data = [
    {"name": "Joseph", "age": 25},
    {"name": "Eyanae", "age": 20},
    {"name": "Longoli", "age": 30}
]
Let me know what you'd like to do with this data!

You said: Manual function to sort a list of
anual function to sort a list of dictionaries by a given key
def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

# Example usage
data = [
    {"name": "Joseph", "age": 25},
    {"name": "Eyanae", "age": 20},
    {"name": "Longoli", "age": 30}
]

sorted_data = sort_dicts_by_key(data, "age")
print("Sorted (Manual):", sorted_data)
Copilot said: Your function `sort_dicts_by_key` is a simple and
Your function sort_dicts_by_key is a simple and effective way to sort a list of dictionaries by a given key in Python. Here’s a breakdown and a slightly expanded example for clarity:


sort_example.py
def sort_dicts_by_key(data, key):
    # Sorts the list of dictionaries by the given key
    return sorted(data, key=lambda x: x[key])

# Example usage
data = [
Output:

Code
Sorted (Manual): [{'name': 'Eyanae', 'age': 20}, {'name': 'Joseph', 'age': 25}, {'name': 'Longoli', 'age': 30}]
How it works:

sorted() sorts the list.
key=lambda x: x[key] tells sorted() to use the value at key in each dictionary for sorting.
If you want to sort in descending order, you can add reverse=True:

Python
sorted_data_desc = sort_dicts_by_key(data, "age")
print("Sorted Descending:", sorted(data, key=lambda x: x["age"], reverse=True))