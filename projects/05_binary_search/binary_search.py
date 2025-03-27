def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1 

def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1  

    mid = (low + high) // 2 

    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)  
    else:
        return binary_search_recursive(arr, low, mid - 1, target)  

def user_input_binary_search():
    while True:  
        try:
            arr = list(map(int, input("Enter sorted numbers (space-separated): ").split()))
            target = int(input("Enter the number to search: "))

            if arr != sorted(arr):
                print("❌ Error: The list is not sorted. Please enter a sorted list.")
                continue

            while True:  
                method = input("Choose method (iterative/recursive): ").strip().lower()
                
                if method == "iterative":
                    index = binary_search_iterative(arr, target)
                    break
                elif method == "recursive":
                    index = binary_search_recursive(arr, 0, len(arr) - 1, target)
                    break
                else:
                    print("❌ Invalid method. Please choose 'iterative' or 'recursive'.")

            if index != -1:
                print(f"✅ Element {target} found at index {index}.")
            else:
                print("❌ Element not found.")
            
            break  

        except ValueError:
            print("❌ Error: Please enter valid numbers!")

if __name__ == "__main__":
    user_input_binary_search()
