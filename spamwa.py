import pyautogui as pt
import time

limit = input("limit :")
message = input("message :")
i = 0
time.sleep(5)

while i < int(limit):
  pt.typewrite(message)
  pt.press("enter")
  time.sleep(0.200)
  i += 1
