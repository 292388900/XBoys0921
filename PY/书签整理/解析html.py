# coding=utf-8
# code from www.361way.com
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def fancy_dendrogram(*args, **kwargs):
	max_d = kwargs.pop('max_d', None)
	if max_d and 'color_threshold' not in kwargs:
		kwargs['color_threshold'] = max_d
	annotate_above = kwargs.pop('annotate_above', 0)

	ddata = dendrogram(*args, **kwargs)

	if not kwargs.get('no_plot', False):
		plt.title('Hierarchical Clustering Dendrogram (truncated)')
		plt.xlabel('sample index or (cluster size)')
		plt.ylabel('distance')
		for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
			x = 0.5 * sum(i[1:3])
			y = d[1]
			if y > annotate_above:
				plt.plot(x, y, 'o', c=c)
				plt.annotate("%.3g" % y, (x, y), xytext=(0, -5), textcoords='offset points', va='top', ha='center')
		if max_d:
			plt.axhline(y=max_d, c='k')
	return ddata

from bs4 import BeautifulSoup


soup = BeautifulSoup(open("templates/bookmarks_2017_10_7.html"))

#
# print soup.dt
# print soup.dl
#   "urls":[{"url":"www.baidu.com","date":"1222","description":"baidu"}]

# "adddate":"1",
#             "lastmodified":"null",
#             "name":"name",
Groups={"chrome":{"name":u"chorme extenstion","adddate":"null","lastmodified":"null","urls":[]}
    ,"http":{"name":u"http website","adddate":"null","lastmodified":"null","urls":[]}
        ,"other":{"name":u"the other thing","adddate":"null","lastmodified":"null","urls":[]}}
wordlist=[]
for item in soup.find_all(["a", "href"]):
    # print item["href"]
    wordlist.append(item.contents[0])
    if (item["href"]+"").startswith(u"chrome"):
        group=Groups["chrome"]
        alinkmap={}
        alinkmap["date"]= item['add_date']
        alinkmap["url"]= item['href']
        alinkmap["description"]=item.contents[0]
        group["urls"].append(alinkmap)
        Groups["chrome"]=group
    elif (item["href"]+"").startswith(u"http"):
        group=Groups["http"]
        alinkmap={}
        alinkmap["date"]= item['add_date']
        alinkmap["url"]= item['href']
        alinkmap["description"]=item.contents[0]
        group["urls"].append(alinkmap)
        Groups["http"]=group
    else:
        group=Groups["other"]
        alinkmap={}
        alinkmap["date"]= item['add_date']
        alinkmap["url"]= item['href']
        alinkmap["description"]=item.contents[0]
        group["urls"].append(alinkmap)
        Groups["other"]=group


print Groups["other"]["urls"]
content=""
for word in wordlist:
    content+=(word+"").lower()
import jieba
thesize=2000

import jieba.analyse as al
word_topk = al.extract_tags(content,topK=thesize)
top=[]
for t in word_topk:
    top.append(t)
top=["android", "studio", "jni",  "netandroid", "net", "ndk",    "adb", "linux", "rom", "java",  "aapt", "gradle", "开源",  "平台", "apk",  "系统", "北京科技大学",  "unix", "mk",  "fork", "c++", "ubuntu", "测试", "手机",   "文件", "程序员", "免费",  "网易", "校园", "源码", "bpel",  "进程",  "间通信",  "监控", "neu6", "testing", "javah", "binder",   "sdk", "tools", "python", "php", "apktool", "数据库",  "全局变量", "图标", "程序", "无法访问",  "字节",  "机制", "chrome", "知乎",  "ipv6", "baidu", "mongodb", "hosts", "mutation", "高速下载",   "中国", "官方", "安全",      "内核",  "文本编辑", "校园网",  "命令", "服务",  "win7", "bootstrap",  "neo4j", "wd", "ws", "dalvik", "client", "runtime",  "ipc", "ieee", "sublime" , "screenshot", "rest", "lol", "webservice", "helloworld", "github",  "openshift", "头文件", "pdf",  "stack", "...", "ide", "link",  "youtube", "hello", "app", "0.0", "native", "常用命令", "monkey",  "url", "chmod", "capture",  "tomcat","框架", "播放", "代码", "后缀",  "应用程序", "维基百科",  "音频",  "内存", "篡改" ]
#
#
#


print "["
for t in top:
    print "\""+t+"\",",
print "]"
print top.__len__()
wordmap={}
import numpy
j=0
for word in wordlist:
    j+=1
    wordv =numpy.zeros((1,top.__len__()+1))
    i=0;
    for t in top:
        if t in (word+"").lower():
            wordv[0][i]=1
        i+=1
    wordmap[word]=wordv[0]
print j
values=numpy.zeros((j,top.__len__()+1))
j=0
for k in wordmap.keys():
    values[j]=wordmap[k]
    j+=1

from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt

linkage_matrix = ward(values)
# fig, ax = plt.subplots(figsize=(15, 20))

# ax=fancy_dendrogram(linkage_matrix, truncate_mode='lastp', p=25, leaf_rotation=90., leaf_font_size=12., show_contracted=True, annotate_above=10,max_d=max_d)
# plt.show()
def genoutputhtml(max_d=5):

    from scipy.cluster.hierarchy import fcluster
    clusters = fcluster(linkage_matrix, max_d, criterion='distance')
    # print clusters

    j=0
    max=0
    cmap={}
    for c in clusters:
        cmap[wordlist[j]]=c
        if c>max:
            max=c
        j+=1
    print max
    alinkmaplist=Groups["http"]["urls"]
    for alinkmap in alinkmaplist:
        Groups[max_d*10000+cmap[alinkmap["description"]]]={"name":str(max_d*10000)+"_"+str(cmap[alinkmap["description"]]),"adddate":"null","lastmodified":"null","urls":[]}
    for alinkmap in alinkmaplist:
        Groups[max_d*10000+cmap[alinkmap["description"]]]["urls"].append(alinkmap)
    group2keyword={}
    for alinkmap in alinkmaplist:
        for t in top:
            if t in (alinkmap["description"]+"").lower():
                group2keyword[max_d*10000+cmap[alinkmap["description"]]]={}
    for alinkmap in alinkmaplist:
        for t in top:
            if t in (alinkmap["description"]+"").lower():
                group2keyword[max_d*10000+cmap[alinkmap["description"]]][t]=group2keyword[max_d*10000+cmap[alinkmap["description"]]].get(t,0)+1;


    for alinkmap in alinkmaplist:
        try:
            thekeyword= sorted(group2keyword[max_d*10000+cmap[alinkmap["description"]]].items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
            s=""
            for x in range(thekeyword.__len__()):
                if x<=5:
                    s+="+"+thekeyword[x][0]
            Groups[max_d*10000+cmap[alinkmap["description"]]]["name"]=str(max_d*10000)+"_"+str(cmap[alinkmap["description"]])+"_"+s
        except :
             pass

    print group2keyword


    # for k in Groups.keys():
    #         print k

    import os
    from jinja2 import Environment, FileSystemLoader
    PATH = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(PATH, 'templates')),
        trim_blocks=False)
    def render_template(template_filename, context):
        return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
    def create_index_html():
        fname = "out/output_"+str(max_d)+"_"+str(max)+".html"
        theGroup=[]
        for k in range(max_d*10000,max_d*10000+max+1):
            # print k
            if k in Groups.keys():
                theGroup.append(Groups[k])
        context = {
            'Groups':  theGroup
        }
        with open(fname, 'w') as f:
            html = render_template('bookmarks.html', context)
            f.write(html)

    create_index_html()

genoutputhtml(max_d=3)
