import PIL
from PIL import Image
import pyautogui
import numpy as np
import time


def testgrab():
	im = pyautogui.screenshot(region=(50,50, 350, 350))
	im = PIL.ImageOps.fit(im, (512,512))
	im = np.asarray(im)
	return(im)


def grabscreen():
	topleft = pyautogui.locateOnScreen('images\\naviicon_rslogo.png')
	botright = pyautogui.locateOnScreen('images\\naviicon_music.png')
	im = pyautogui.screenshot(region=(topleft[0],topleft[1], botright[0]-topleft[0], botright[1]-topleft[1]))
	im = PIL.ImageOps.fit(im, (512,512))
	im = np.asarray(im)
	return(im)
	
def img2hist(refim):
	(ny,nx,nz) = refim.shape
	histpix = histim(refim)
	#hist = histpix.sum(axis = 0).sum(axis = 0)
	hist = np.sum(histpix, axis = 0)
	hist = np.sum(hist, axis = 0) #summed both axis
	return(hist/(ny*nx))
	
def importim(imname, size):
	im = Image.open(imname)
	if size == 'small':
		im = PIL.ImageOps.fit(im, (24,24))
	if size == 'med':
		im = PIL.ImageOps.fit(im, (48,48))
	if size == 'big':
		im = PIL.ImageOps.fit(im, (64,64))
	if size == 'huge':
		im = PIL.ImageOps.fit(im, (256,256))
	im = np.asarray(im)
	return(im)
		
def histim(arr):
	nbins = 4
	(ny,nx,nz) = arr.shape
	output = np.zeros([ny, nx, nbins*nz])
	y = range(0, ny)
	x = range(0, nx)
	xv, yv = np.meshgrid(x, y)
	for z in range(0,nz):
		output[yv,xv,z*nbins+arr[yv,xv,z]/(256/nbins)] = 1
	return(output)
	
def intimg(arr):
	(ny,nx,nz) = arr.shape
	#output = np.zeros([ny, nx, nz])
	for z in range(0,nz):
		for y in range(1,ny):
			for x in range(1,nx):
				arr[y,x,z] = arr[y,x-1,z] + arr[y-1,x,z] - arr[y-1,x-1,z] + arr[y,x,z]
	return(arr)


	
	
def intimg2histdiff(arr, zone, searchhist2):
	#print("zone:", zone)
	#print(arr.shape)
	#print("poses", zone[0]+zone[2], zone[1]+zone[3], zone[0], zone[1],  zone[0], zone[1]+zone[3], zone[0]+zone[2], zone[1], zone[2]*zone[3])
	thishist = (arr[zone[0]+zone[2], zone[1]+zone[3],:] + arr[zone[0], zone[1],:] - arr[zone[0], zone[1]+zone[3],:] - arr[zone[0]+zone[2], zone[1],:])/(zone[2]*zone[3])
	thishist = np.array(thishist)
	temp = abs(thishist-searchhist2)
	return sum(temp)

def showarray(arr):
	im = PIL.Image.fromarray(np.uint8(arr))
	im.show()

def findhist(arrih, itemhist, size):
	#integrated histogram of array. histogram of item img. approx size of item img in pixels on a side.
	(ny,nx,nz) = arrih.shape
	output = np.zeros([ny, nx])
	#y = range(0, ny)
	#x = range(0, nx)
	#xv, yv = np.meshgrid(x, y)
	for y in range(size/2+1, ny - size - 1):
		print(y)
		for x in range(size/2+1, nx - size - 1):
			output[y, x] = intimg2histdiff(arrih, [y,x,size, size], itemhist)
	return output
			
	
searchim = importim("images\\npc_banker\\1.png", 'med')
#searchim = importim("images\\naviicon_rslogo.png", 'small')
searchhist3 = np.array(img2hist(searchim))
myarr = testgrab()
#myarr = importim("images\\rsge.png", 'huge')
showarray(myarr)
showarray(searchim)
arr2 = histim(myarr)
arr3 = intimg(arr2)
arr4 = findhist(arr3, searchhist3, 24)
showarray(arr4)





