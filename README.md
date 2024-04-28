# whatsapp-spammer
A python program for spamming whatsapp messages with [pyautogui](https://pyautogui.readthedocs.io/en/latest/) library.

Method description:
- **Typing Method**: This method is typing words into a message box and sending it by pressing Enter. Because of its typing style, it would affect WhatsApp performance and make the app laggy if you have long messages and too fast delay settings (I have set the minimum delay for 100ms). So this method works best with short messages but you can customize the message as you want like picking a random value from a list of strings, predefined variables, etc. so you can send different messages each loop.
- **Paste Method**: This method is pasting content from the clipboard and sending it. It works best for long messages. Since it's blazingly fast, with no delay you may encounter double-paste in a message so I have set a delay for 100ms. To use it, copy any content to your clipboard first and make sure it pastes the content you want. Yes, it can paste anything like images or videos but you have to set the delay longer like more than 500ms to avoid slow WhatsApp performance.

⚠ NOTE: If something wrong happens, activate the failsafe by moving your cursor to the top left corner of your screen to break the loop and exit the program.

### Demo

https://github.com/zafiramdhani/whatsapp-spammer/assets/96897164/379fda35-7feb-48ff-98ba-11af820fbf82

