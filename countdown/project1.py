import time

def countDown_timer(second):
    while second > 0:
        mins, secs = divmod(second, 60)  # Minutes and seconds calculation
        time_format = "{:02d}:{:02d}".format(mins, secs)  # MM:ss format
        print(time_format, end="\r")  # Overwrite the previous line
        time.sleep(1)  # Delay for 1 second
        second -= 1
    print("00:00 \nTime is up!")  # Display message after countdown ends

# User input for timer
total_seconds = int(input("Enter time in seconds for countdown: "))
countDown_timer(total_seconds)
https://play.google.com/store/apps/details?id=com.instagram.android&pcampaignid=web_share