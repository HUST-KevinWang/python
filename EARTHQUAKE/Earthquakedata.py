import requests
from bs4 import BeautifulSoup

'''爬虫获得数据'''
def gethtmltext(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


f = open("sheet1.txt", 'w')
for j in range(1, 3580):
    data = ""
    txt = gethtmltext("http://www.csi.ac.cn/eportal/ui?pageId=636&startDate=2000-01-01%2000:00:00&endDate=2020-08-02%2023:59:59&startMagnitude=3&endMagnitude=10&eq_catalog=all&startLatitude=-90&endLatitude=90&startLongitude=-180&endLongitude=180&isshow=yes&currentPage="+str(j))
    sp = BeautifulSoup(txt, "html.parser")
    for child in sp.tbody.find_all():
        if child.string != "\n":
            data += str(child.string)
    datasheet = data.split("None")
    for i in range(len(datasheet)):
        datasheet[i] = datasheet[i].split(" ")
        while '' in datasheet[i]:
            datasheet[i].remove('')
    for item in datasheet[2:]:
        f.write(','.join(item) + '\n')
f.close()


