import numpy as np
import cv2
cap = cv2.VideoCapture(r'C:\Users\lenovo\Downloads\source code\source code\Datasets\Meena Lotchani\Video Capture posture\Normal.mp4')
i = 0
while(cap.isOpened()):
  ret, frame = cap.read()
  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  if ret == False:
     break
  cv2.imwrite(r'C:\Users\lenovo\Downloads\source code\source code\Meena-Train\Frame'+str(i)+'.jpg', frame)
  i += 1


cap.release()
cv2.destroyAllWindows()
