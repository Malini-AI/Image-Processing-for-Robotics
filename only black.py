import glob
import cv2
import numpy as np


img = []
c = 0
for i in glob.glob('C:/Users/malin/OneDrive/Desktop/Robotics/ADV_ROBOTICS/png/Carpet/Type1/SQUARE/300/I-300-2-CROP/*.png'):
    n = cv2.imread(i)
    img.append(n)
    c = c+1
print("no: of images: "+str(c))
print(img[0].shape)

# # Create a gradient filter
img_ = np.zeros((200, 200, 3), np.uint8)
cnt = 0

z = cv2.circle(img_, (100, 100), 40, (0, 0, 0), -2)
for i in range(img_.shape[0]):
    z = cv2.circle(img_, (100, 100), 40 + i, (0 + i, 0 + i, 0 + i), 2)
    cnt = cnt + 1

cv2.imwrite("C:/Users/malin/fzW.jpg", z)
# print(z.shape)

w = np.zeros(shape=(z.shape[0],z.shape[1], z.shape[2]))

for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        for k in range(z.shape[2]):
            w[i][j][k] = z[i][j][k] * (-0.7)
            blur = cv2.blur(w[i][j][k], (2, 2))
cv2.imwrite("C:/Users/malin/pt5W.jpg", w)

z = z / z.max()  # compressing the pixel range
for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        for k in range(z.shape[2]):
            if z[i][j][k] == 1:
                z[i][j][k] = 0.5
z1 = 1 - z

for m in range(c+1):

    img1 = img[m]
    print(img1.shape)
    res = np.zeros(shape=(img1.shape[0], img1.shape[1], img1.shape[2]))

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            for k in range(img1.shape[2]):
                res[i][j][k] = (w[i][j][k]) + np.multiply(z1[i][j][k], img1[i][j][k])

    cv2.imwrite("C:/Users/malin/filterW2/B" + str(m) + ".jpg", res)
