def access_element(lst, index):
    try:
        return lst[index]  
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value  
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    return lst[start:end]  

def index_game():
    lst = [1, 2, 3, 4, 5]  
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        try:
            index = int(input("Enter index to access: "))
            print(access_element(lst, index))
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif operation == "modify":
        try:
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print("Updated List:", modify_element(lst, index, new_value))
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif operation == "slice":
        try:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(lst, start, end))
        except ValueError:
            print("Invalid input. Please enter numbers.")
    else:
        print("Invalid operation.")

if __name__ == '__main__':
    index_game()
