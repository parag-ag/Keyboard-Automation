import pyautogui
import time

time.sleep(5)
n = 11
while(n<41):
    pyautogui.write('Introduction to Database Systems {}-{}'.format(n, n+1))
    n = n + 2
    time.sleep(1)
    pyautogui.press('enter')