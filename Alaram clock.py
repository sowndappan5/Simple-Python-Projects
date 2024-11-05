from datetime import datetime
from playsound import playsound

# Get user input for alarm time in HH:MM:SS AM/PM format
alarm_time = input("Enter the time of alarm to be set (e.g., 07:30:00 AM):\n")

# Extract hour, minute, second, and period (AM/PM) from the input
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()  # Convert period to uppercase for consistency

print("Setting up alarm...")

# Infinite loop to keep checking the current time until it matches the alarm time
while True:
    # Get the current time
    now = datetime.now()
    
    # Format the current time to match the alarm time format
    current_hour = now.strftime("%I")        # Hour in 12-hour format
    current_minute = now.strftime("%M")      # Minute
    current_seconds = now.strftime("%S")     # Second
    current_period = now.strftime("%p")      # AM or PM
    
    # Check if the current period, hour, minute, and second match the alarm time
    if (alarm_period == current_period and
        alarm_hour == current_hour and
        alarm_minute == current_minute and
        alarm_seconds == current_seconds):
        
        # If all conditions are met, play the alarm sound and exit the loop
        print("Wake Up!")
        playsound('audio.mp3')
        break
