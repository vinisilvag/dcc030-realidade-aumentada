import cv2
import numpy as np

cam = cv2.VideoCapture("./entrada.mp4", 0)
template = cv2.imread("./alvo.jpg", 0)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

while(True):
    ret, frame = cam.read()

    if ret:
        # for method in methods:
        #     copy = frame.copy()
            
        #     result = cv2.matchTemplate(copy, template, method)
        #     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
        #     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        #         location = min_loc
        #     else:
        #         locaction = max_loc
            
        #     template_shape = template.shape
        #     bottom_right = (location[0] + template_shape[1], location[1] + template_shape[0])
            
        #     cv2.rectangle(copy, location, bottom_right, 255, 5)
        #     cv2.imshow('Match', copy)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
      
        break
    else:
        break

cam.release()
cv2.destroyAllWindows()