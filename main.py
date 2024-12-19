import function
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete, exit: ")
    user_action=user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos=function.get_todos()

        todos.append(todo + '\n')

        function.write_todos(todos)

    elif user_action.startswith('show'):
        todos = function.get_todos("todos_item.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number=number-1

            todos = function.get_todos()

            new_todo = input("Vendos todo e re: ")
            todos[number] = new_todo + '\n'

            function.write_todos(todos)
        except ValueError:
            print("Komanda e vendosur nuk eshte e vlefshme!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = function.get_todos()
            index=number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            function.write_todos(todos)

            message=f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Komanda e vendosur nuk eshte e vlefshme!")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Komanda e vendosur nuk eshte e vlefshme!")

print("Bye!")
