import time

def countdown_timer(seconds):
    """Function to run a countdown timer."""
    while seconds:
        mins, secs = divmod(seconds, 60)  
        timer_display = f"{mins:02}:{secs:02}"
        print(f"⏳ Time Remaining: {timer_display}", end="\r")  
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")

if __name__ == "__main__":
    try:
        total_time = int(input("Enter countdown time in seconds: "))
        countdown_timer(total_time)
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
