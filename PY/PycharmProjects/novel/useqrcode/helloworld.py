# -*- coding: utf-8-*-
import qrcode

char = raw_input('please input string: ').decode('gbk')
img = qrcode.make(char)
img.save('test.png')
img.show()
