import cv2
import numpy as np

thisdict ={
  "0":"عن",
  "1":"عبد",
  "2":"عبد",
  "3":"علي",
  "4":"علي",
  "5":"العام",
  "6":"العام",
  "7":"اليوم",
  "8":"اليوم",
  "9":"عن"

}

       


x=0
y=0
while x<10:
    y=0
    while y<10:
        img1 = cv2.imread(str(x)+'.jpg')
        img2 = cv2.imread(str(y)+'.jpg')
        vis = np.concatenate((img1, img2), axis=1)
        cv2.imwrite(str(x)+str(y)+ '.jpg', vis)
        with open(str(x)+str(y)+'.gt.txt', 'w',encoding="utf-8") as f:
            a = thisdict.get(str(x))
            b = thisdict.get(str(y))
            f.write(str(b) + " "+str(a) )
        print("y= "+str(y))
        y=y+1
    x=x+1
    print("x= "+str(x))
    

