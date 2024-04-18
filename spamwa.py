import pyautogui as pt
import time

limit = input("Enter limit: ")
message = input("Your message: ")
print("Running...")
i = 0
time.sleep(5)

# ============!!USE ONLY ONE METHOD AT A TIME!!==============

# TYPING METHOD (slower for long messages & limited chars)
# while i < int(limit):
#   pt.typewrite(message)
#   pt.press("enter")
#   time.sleep(0.100)
#   i += 1

# PASTE METHOD (faster for long messages, input message value will be ignored)
while i < int(limit):
  pt.hotkey('ctrl', 'v')
  pt.press("enter")
  time.sleep(0.100)
  i += 1

print("Stopped.")