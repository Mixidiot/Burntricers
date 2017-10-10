import pyautogui
import time
import random as rand
import cv2
print("hello")

def oldstuff():
	print(rand.random())
	pyautogui.moveRel(250*(rand.random()-0.5), 250*(rand.random()-0.5), duration=rand.random())


def somechaos():
	if (rand.random() > 0.9):
		pyautogui.moveRel(300*(rand.random()-0.5), 300*(rand.random()-0.5), duration=rand.random()/2)

def openbank():
	topleft = pyautogui.locateOnScreen('images\\naviicon_rslogo.png')
	botright = pyautogui.locateOnScreen('images\\naviicon_music.png')
	print('finding banker')
	bankerPos = [topleft[0] + (0.005*(rand.random()-0.5)+0.52)*(botright[0] - topleft[0]), topleft[1] + (0.005*(rand.random()-0.5)+0.38)*(botright[1] - topleft[1])]
	somechaos()
	pyautogui.moveTo(bankerPos[0], bankerPos[1], duration=0.5+rand.random())
	time.sleep(rand.random()/100)
	pyautogui.click(button='right')
	somechaos()
	print('finding menu')
	popupPos = pyautogui.locateOnScreen('images\\navitext_bankbanker.png')
	pyautogui.moveTo(popupPos[0]+rand.random()*popupPos[2], popupPos[1]+rand.random()*popupPos[3], duration=rand.random())
	time.sleep(rand.random()/100)
	pyautogui.click(button='left')


def closebank():
	print('finding x')
	xPos = pyautogui.locateOnScreen('images\\naciicon_closepopup.png')
	somechaos()
	pyautogui.moveTo(xPos[0], xPos[1], duration=0.5+rand.random())
	time.sleep(rand.random()/100)
	pyautogui.click(button='left')
	
def bank_withdraw(item, num):
	# only coded for withdrawing full inventory so far
	openbank()
	print('finding item')
	time.sleep(1.2)
	pos = pyautogui.locateOnScreen('images\\'+item+'.png')
	print('images\\'+item+'.png')
	print(pos)
	somechaos()
	pyautogui.moveTo(pos[0]+rand.random()*pos[2], pos[1]+rand.random()*pos[3], duration=rand.random())
	time.sleep(rand.random()/100)
	pyautogui.click(button='right')
	if num > 0: #>= 28:
		pos = pyautogui.locateOnScreen('images\\navitext_withdrawall.png')
		pyautogui.moveTo(pos[0]+rand.random()*pos[2], pos[1]+rand.random()*pos[3], duration=rand.random())
		time.sleep(rand.random()/100)
		pyautogui.click(button='left')
	closebank()
	
	
def burybones():
	print('finding bones')
	loc = pyautogui.locateAllOnScreen('images\\inventory_bones.png')
	for pos in loc:
		somechaos()
		print('burying bones')
		pyautogui.moveTo(pos[0]+rand.random()*pos[2], pos[1]+rand.random()*pos[3], duration=rand.random())
		time.sleep(0.5+rand.random())
		pyautogui.click(button='left')
	

#pos = pyautogui.locateOnScreen('images\\bankinventory_bigbones.png')
#yautogui.moveTo(pos[0]+rand.random()*pos[2], pos[1]+rand.random()*pos[3], duration=rand.random())
#print(pos)

	

for i in range(3):
	burybones()
	bank_withdraw('bankinventory_bigbones', 30)
	burybones()











