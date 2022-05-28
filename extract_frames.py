import cv2
import os

cam = cv2.VideoCapture("./entrada.mp4")

current_frame = 0

while(True):
	ret, frame = cam.read()

	if ret:
		name = './frames/frame' + str(current_frame) + '.jpg'
		print ('Creating... ' + name)
  
		cv2.imwrite(name, frame)
  
		current_frame += 1
	else:
		break

cam.release()
cv2.destroyAllWindows()