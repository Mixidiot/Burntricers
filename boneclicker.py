import pyautogui
import random as rand
print("hello")
print(rand.random())
pyautogui.moveRel(250*(rand.random()-0.5), 250*(rand.random()-0.5), duration=rand.random())
loc = pyautogui.locateAllOnScreen('images\inventorybones.png')
def somechaos():
	if (rand.random() > 0.9):
		pyautogui.moveRel(300*(rand.random()-0.5), 300*(rand.random()-0.5), duration=rand.random()/2)

def openbank():
	topleft = pyautogui.locateOnScreen('images\\naviicon_rslogo.png')
	botright = pyautogui.locateOnScreen('images\\naviicon_music.png')
	print('finding banker')
	bankerPos = [topleft[0] + 0.55*(botright[0] - topleft[0]), topleft[1] + 0.4*(botright[1] - topleft[1])]
	somechaos()
	pyautogui.moveTo(bankerPos[0], bankerPos[1], duration=0.5+rand.random())
	time.sleep(rand.random()/10)
	pyautogui.click(button='right')
	somechaos()
	print('finding menu')
	popupPos = pyautogui.locateOnScreen('images\\navitext_bankbanker.png')
	pyautogui.moveTo(popupPos[0], popupPos[1], duration=0.5+rand.random())
	time.sleep(rand.random()/10)
	pyautogui.click(button='left')

for pos in loc:
	pyautogui.moveTo(pos[0]+rand.random()*pos[2], pos[1]+rand.random()*pos[3], duration=rand.random())
print(loc[0])
print(loc[1])
