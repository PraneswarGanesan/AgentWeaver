import time
import pyautogui

# Delay before starting (adjust as needed)
time.sleep(3)

# Open Any app or code space 
# Ensure that the application or codespace is already open and visible on your screen

# Move the mouse to the coordinates of the WhatsApp chat window
# Replace the (x, y) values with the appropriate coordinates
# These coordinates can be determined by using the pyautogui.position() function
x =  100 # Replace with the x-coordinate of the chat window
y = 200  # Replace with the y-coordinate of the chat window
pyautogui.moveTo(x, y)

# Read the contents of the text file and remove leading tab spaces
file_path = r"C:\Python programs\type.txt" #add your location
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Remove leading tab spaces from each line
contents = [line.lstrip() for line in lines]

# Now 'contents' is a list of lines without leading tab spaces
# You can join them back into a single string if needed
contents = "".join(contents)

# Set the typing speed (adjust as needed)
typing_speed =  8 # Words per minute

# Calculate the delay between each character
delay = 0.05 # Delay in seconds

# Type the contents of the file with the desired typing speed
for char in contents:
    pyautogui.typewrite(char)
    time.sleep(delay)

# Press Enter to send the message
pyautogui.press("enter")
