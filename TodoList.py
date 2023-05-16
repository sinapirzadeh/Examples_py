my_List = ['Home Work', 'boy food']

# ================ Functions ============
def add_Todo(my_List):
    todo_name = input("Enter your todo name : ")
    my_List.append(todo_name)
    for i in my_List:
        print(i)


def del_Todo(my_List):
    name = input("Enter your todo Name : ")
    my_List.remove(name)
    for i in my_List:
        print(i)


def show_Todo(my_List):
    for i in my_List:
        print(i)


while True:
    print("Help => add del show")
    msg = input("Enter your do : ")

    match msg:
        case "add":
            add_Todo(my_List)
        case "del":
            del_Todo(my_List)
        case "show":
            show_Todo(my_List)

    msg = input("you want Exit App : Help => [yes or NO : y n]")
    if msg == 'y':
        break
