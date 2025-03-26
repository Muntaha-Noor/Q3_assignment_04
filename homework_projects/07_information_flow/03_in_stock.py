# Function jo store ke andar kisi fruit ka stock check karega
def num_in_stock(fruit: str) -> int:
    inventory = {
        "apple": 2,
        "lychee": 4,
        "pear": 1000
    }
    return inventory.get(fruit, 0)  

def main():
    fruit = input("Enter a fruit: ")  
    stock = num_in_stock(fruit)  

    if stock == 0:
        print("This fruit is not in stock.") 
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == '__main__':
    main()
