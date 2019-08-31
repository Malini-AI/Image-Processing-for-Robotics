import cv2 

imagelist=[]
for imageName in glob.glob("....path/*.PNG"): 
    imagelist.append(imageName)

v=1
for image in imagelist:
    img = cv2.imread(image)  
    blurImg = cv2.blur(img,(21,21))  
    cv2.imwrite("blur"+str(v)+"_21.png", blurImg)  
    v+=1
