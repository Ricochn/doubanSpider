# -*- coding: utf-8 -*-
import urllib.request
import re

page = urllib.request.urlopen("https://movie.douban.com/")
cnt = page.read().decode("utf-8")

#首次过滤
name = re.findall(r'href="https://movie\.douban\.com/subject/\d+?/\?from=showing" class="">.+?</a>',cnt)
rate = re.findall(r'<span class="subject-rate">\d\.\d</span>|<span class="text-tip">暂无评分</span>|<span class="rating-type-score">\d\.\d</span>',cnt)

#进一步匹配和过滤
name2=[]
for na in name:
    nametmp = re.search(r'class="">.+?</a>', na).group(0)
    nametmp = nametmp[9:]
    nametmp = nametmp[:-4]
    name2.append(nametmp)
rate2=[]
for ra in rate:
    ratmp = re.search(r">.+?<", ra).group(0)
    ratmp = ratmp[1:]
    ratmp = ratmp[:-1]
    rate2.append(ratmp)

print(len(name2), len(rate2))

#print("豆瓣网热门电影：")
#i=0
#聚合电影名字和评分
ziped = zip(name2, rate2)
#迭代输出
#for na,ra in ziped:
#    print(na,'\t',ra)
#    i+=1
#print("热门电影共计：",i,"部")

with open("douban.html",'+w', encoding="utf-8") as f:
    f.write("""
<!DOCTYPE html>
<head>
<meta charset="utf-8">
<style>
h3{
color:#71c084
}
</style>
</head>
<body>
<h3>豆瓣网热门集锦-Powered by python</h3>
<ul>
""")
    for na,ra in ziped:
        f.write("<li>"+na+"\t"+ra+"</li>\n")
    f.write("""
</ul>
</body>
<html>
""")
    f.close()


