DAYS_PER_YEAR: int = 365
HOUR_PER_DAY: int = 24
MINUTES_PER_HOUR: int = 60
SECONDS_PER_MINUTE: int = 60

def main():
    total_seconds: int = DAYS_PER_YEAR * HOUR_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    
    print("There are", total_seconds, "seconds in a year.")

if __name__ == "__main__":
    main()