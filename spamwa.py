import pyautogui as pt
import time, random, sys
import variables

class ansi:
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  BLUE = '\033[94m'
  MAGENTA = '\033[95m'
  CYAN = '\033[96m'
  WHITE = '\033[97m'
  COLOR_RESET = '\033[0m'
  BOLD = '\033[1m'
  BOLD_RESET = '\033[0m'

print(f"\n{ansi.BOLD}{ansi.GREEN}{'=' * 42}\n##### WhatsApp spammer v2.0 by Zafee #####\n{'=' * 42}{ansi.COLOR_RESET}{ansi.BOLD_RESET}")
print("Available modes:\n1. Typing mode\n2. Paste mode\n3. Sticker spammer\n")

selected_mode = int(input("Select a mode: "))
i = 0

def running():
  return print(f"{ansi.BLUE}Program is running...{ansi.COLOR_RESET}")

def confirmation():
  choice = input(f"{ansi.YELLOW}Run the program? (y/n): {ansi.COLOR_RESET}").lower()

  if choice == "n":
    print(f"{ansi.BOLD}{ansi.RED}You canceled the program.{ansi.COLOR_RESET}{ansi.BOLD_RESET}\n")
    sys.exit()
  elif choice == "y": return
  else: 
    print(f"{ansi.BOLD}{ansi.RED}Invalid input!{ansi.COLOR_RESET}{ansi.BOLD_RESET}")
    sys.exit()

def typing_mode(i):
  print(f"{ansi.RED}{'-' * 15}\n| TYPING MODE |\n{'-' * 15}{ansi.COLOR_RESET}")
  limit = input("Enter limit: ")
  message = input("Your message: ")
  confirmation()
  running()
  time.sleep(5)

  while i < int(limit):
    pt.typewrite(message)
    # pt.typewrite(random.choice(variables.suruh_diam))
    pt.press("enter")
    pt.sleep(0.100)
    i += 1

def paste_mode(i):
  print(f"{ansi.RED}{'-' * 14}\n| PASTE MODE |\n{'-' * 14}{ansi.COLOR_RESET}")
  limit = input("Enter limit: ")
  confirmation()
  running()
  time.sleep(5)

  while i < int(limit):
    pt.hotkey('ctrl', 'v')
    pt.press("enter")
    pt.sleep(0.050)
    i += 1

def sticker_spammer(i):
  print(f"{ansi.RED}{'-' * 19}\n| STICKER SPAMMER |\n{'-' * 19}{ansi.COLOR_RESET}")
  limit = input("Enter limit: ")
  confirmation()
  running()
  time.sleep(5)

  while i < int(limit):
    pt.leftClick()
    i += 1

if selected_mode == 1:
  typing_mode(i)
elif selected_mode == 2:
  paste_mode(i)
elif selected_mode == 3:
  sticker_spammer(i)
else:
  print(f"{ansi.BOLD}{ansi.RED}Invalid input! There's no mode {selected_mode}!{ansi.COLOR_RESET}{ansi.BOLD_RESET}\n")
  sys.exit()

print(f"\n{ansi.BOLD}{ansi.GREEN}DONE! Stopping program.\nAll messages have been sent successfully!{ansi.COLOR_RESET}{ansi.BOLD_RESET}\n")