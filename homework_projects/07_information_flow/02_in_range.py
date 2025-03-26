def in_range(n: int, low: int, high: int) -> bool:
    return low <= n <= high  

def main():
    n = int(input("Enter a number: "))  
    low = int(input("Enter lower bound: "))  
    high = int(input("Enter upper bound: "))  

    print(in_range(n, low, high))  

if __name__ == '__main__':
    main()
