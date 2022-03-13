
import pyautogui as pg
import time

time.sleep(10)

txt = open("animals.txt", "r")
line = "Hey John! You are a "

for i in txt:
    pg.write(f"{line} {i}")
    pg.press("Enter")

