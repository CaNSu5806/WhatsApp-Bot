import pywhatkit
from datetime import datetime, timedelta 

def get_mobile_number():
    while True:
        mobile = input("Enter Mobile No of Receiver (+90xxxxxxxxxx format): ")
        if mobile.startswith('+') and mobile[1:].isdigit():
            return mobile
        print("Invalid format. Try again.")

def get_message():
    return input("Enter the message you want to send: ")

def get_time():
    now = datetime.now()
    while True:
        try:
            hour = int(input("Enter hour (0-23): "))
            minute = int(input("Enter minute (0-59): "))
            send_time = datetime(now.year, now.month, now.day, hour, minute)
            if send_time < now + timedelta(minutes = 2):
                print("Time must be at least 2 minutes ahead. Try again.")
            else:
                return hour, minute
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            
mobile = get_mobile_number()
message = get_message()
hour, minute = get_time()

print(f"Scheduling message to {mobile} at {hour}:{minute}...")
pywhatkit.sendwhatmsg(mobile, message, hour, minute)
print("Message scheduled successfully!")