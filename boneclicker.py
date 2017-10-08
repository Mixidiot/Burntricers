import pyautogui
import random as rand
print("hello")
print(rand.random())
pyautogui.moveRel(250*(rand.random()-0.5), 250*(rand.random()-0.5), duration=rand.random())
loc = pyautogui.locateAllOnScreen('images\inventorybones.png')


for pos in loc:
	pyautogui.moveTo(pos[0]+rand.random()*pos[2], pos[1]+rand.random()*pos[3], duration=rand.random())
print(loc[0])
print(loc[1])