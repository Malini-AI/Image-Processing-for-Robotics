import numpy as np
import cv2

# # Create a gradient filter
img = np.zeros((200, 200, 3), np.uint8)
cnt = 0

z = cv2.circle(img, (100, 100), 40, (0, 0, 0), -2)
for i in range(img.shape[0]):
    z = cv2.circle(img, (100, 100), 40 + i, (0 + i, 0 + i, 0 + i), 2)
    cnt = cnt + 1

cv2.imwrite("C:/Users/malin/fzB.jpg", z)
print(cnt)

w=np.zeros(shape=(z.shape[0],z.shape[1],z.shape[2]))

for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        for k in range(z.shape[2]):
            w[i][j][k] = z[i][j][k] * (-0.7)
            blur=cv2.blur(w[i][j][k],(2,2))
cv2.imwrite("C:/Users/malin/pt5B.jpg",w)

# Apply the formula given:
img1 = cv2.imread(
    "C:/Users/malin/OneDrive/Desktop/Robotics/ADV_ROBOTICS/png/Carpet/Type1/SQUARE/300/I-300-1-CROP/crop0.png")
# img2 = cv2.blur(img1, (5, 5))
res = np.zeros(shape=(img1.shape[0], img1.shape[1], img1.shape[2]))
res1 = np.zeros(shape=(img1.shape[0], img1.shape[1], img1.shape[2]))
res2 = np.zeros(shape=(img1.shape[0], img1.shape[1], img1.shape[2]))

z = z / z.max()  # compressing the pixel range

for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        for k in range(z.shape[2]):
            if (z[i][j][k] == 1):
                z[i][j][k] = 0.5

z1 = 1 - z
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        for k in range(img1.shape[2]):
            res1[i][j][k] = (w[i][j][k]) + np.multiply(z1[i][j][k], img1[i][j][k])

cv2.imwrite("C:/Users/malin/filterB.jpg", res1)
# # Create a gradient filter
