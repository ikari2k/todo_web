import os 
FILEPATH = 'todos.txt'
if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as file:
        pass

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local    

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
            file_local.writelines(todos_arg)