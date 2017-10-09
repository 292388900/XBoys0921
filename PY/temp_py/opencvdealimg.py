#coding=utf-8
import cv2

img = cv2.imread("lena.jpg")

def detect(img, cascade):
    divisor=8
    h, w = img.shape
    minSize=(w/divisor, h/divisor)
    print minSize
    rects= classfier.detectMultiScale(img, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    print rects
    return rects

#在img上绘制矩形
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


#转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
#直方图均衡处理
gray = cv2.equalizeHist(gray)
cv2.imshow('gray2', gray)

classfier=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

#通过分类器得到rects
rects = detect(gray, classfier)


#vis为img副本
vis = img.copy()
#画矩形
draw_rects(vis, rects, (0, 255, 0))

cv2.imshow('facedetect', vis)

cv2.waitKey(0)
cv2.destroyAllWindows()
