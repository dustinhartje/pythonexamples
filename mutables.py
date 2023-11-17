# mutable objects, notable Lists and Dictionaries, by default are modified when passed to a function
# In order to keep the original in tact it needs to be copied within the function before use
# Most of the time this would probably be my intention

original_list = [1, 2, 3]

def do_not_change_me(my_list: list):
    working_my_list = my_list.copy()
    working_my_list.append(4)
    print(f"working_my_list = {working_my_list}")


def change_me(my_list: list):
    my_list.append(4)
    print(f"my_list = {my_list}")

print(f"original_list = {original_list}")
# original_list = [1, 2, 3]
print('Running do_not_change_me(original_list)')
# Running do_not_change_me(original_list)
do_not_change_me(original_list)
# working_my_list = [1, 2, 3, 4]
print(f"original_list = {original_list}")
# original_list = [1, 2, 3]
print('Running change_me(original_list)')
# Running change_me(original_list)
change_me(original_list)
# my_list = [1, 2, 3, 4]
print(f"original_list = {original_list}")
# original_list = [1, 2, 3, 4]

    
