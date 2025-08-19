'''
🧩 Mini Mission 6: Dictionary Merge Tool
Objective:
Write a program that merges two dictionaries — if a key appears in both, update the value in the original dictionary.
✅ Your Task
Take two dictionaries: store_a and store_b

Merge the second into the first

If any keys already exist, update the value

Show the merged dictionary at the end

🔍 Example:

store_a = {'apple': 30, 'banana': 10}
store_b = {'banana': 15, 'milk': 25}
After merge:

{'apple': 30, 'banana': 15, 'milk': 25}
'''
def dict_merge_tool(store_a,store_b):
    final_dict = {}
    for key1, value1 in store_a.items():
        final_dict[key1] = value1
    for key2, value2 in store_b.items():
        if key2 in final_dict:
            final_dict[key2] = value2
        else:
            final_dict[key2] = value2
    print(final_dict)

store_a = {
    "apple": 30,
    "banana": 10
}
store_b = {
    "banana": 15,
    "milk": 25
}

dict_merge_tool(store_a,store_b)