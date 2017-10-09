#!/usr/bin/env python
# coding: utf-8
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print type(frame)

while frame is not None:
    cv2.imshow('Video', frame)

    key = cv2.waitKey(100)
    if key == ord('s'):     # 当按下"s"键时，将保存当前画面
        cv2.imwrite('screenshot.bmp', frame)
    elif key == ord('q'):   # 当按下"q"键时，将退出循环
        break

    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()



