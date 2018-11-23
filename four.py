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

w=0
x=0
y=0
z=0

while x<10:
    y=0
    while y<10:
        z=0
        while(z<10):
            w=0
            while(w<10):
            
                img1 = cv2.imread(str(x)+'.jpg')
                img2 = cv2.imread(str(y)+'.jpg')
                img3 = cv2.imread(str(z)+'.jpg')
                img4 = cv2.imread(str(w)+'.jpg')
            
                vis = np.concatenate((img1, img2,img3,img4), axis=1)
                cv2.imwrite(str(x)+str(y)+str(z)+str(w)+'.jpg', vis)
                with open(str(x)+str(y)+str(z)+str(w)+'.gt.txt', 'w',encoding="utf-8") as f:
                    a = thisdict.get(str(x))
                    b = thisdict.get(str(y))
                    c = thisdict.get(str(z))
                    d = thisdict.get(str(w))
                
                    f.write(str(d) + " "+str(c)+" "+str(b)+" "+str(a) )
                    w=w+1
            z=z+1
            print("z=" + str(z))
        print("y= "+str(y))
        y=y+1
    x=x+1
    print("x= "+str(x))
