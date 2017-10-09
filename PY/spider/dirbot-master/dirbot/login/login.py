# coding=utf8
import httplib
import subprocess
import re


# 获得本地ipv6
def getipv6():
    output = subprocess.Popen("ipconfig", stdout=subprocess.PIPE).stdout.read()
    # print (str(output))
    ipv6_pattern = '(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})'
    m = re.findall(ipv6_pattern, str(output))
    if m is not None:
        print 'temp ipv6:',m[1][0]
        return m[1][0]
    else:
        return None

# 登陆校园网
def login():
    username = 's20160743'
    password = '123456'
    headers = {"Connection": "keep-alive",
               "Cookie": "myusername=%s; username=%s; smartdot=%s" % (username, username, password)}
    body = "DDDDD=%s&upass=%s&0MKKey=123456789&v6ip=%s" % (username, password, getipv6())
    conn = httplib.HTTPConnection("202.204.48.66")
    conn.request("POST", "/", body=body, headers=headers)
    response = conn.getresponse()
    print response.status, response.reason

def openurl():
    import sys
    import webbrowser
    sys.path.append("libs")
    url = 'http://202.204.48.66'
    webbrowser.open(url)
# 运行当前文件时，执行sendmaill函数
if __name__ == "__main__":
    login()
    openurl()
