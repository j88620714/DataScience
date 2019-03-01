import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import jieba
import time
import math

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users\j8862\Downloads\_      2019                 -c00e35bee958.json', scope)
gc = gspread.authorize(credentials)
# Open a worksheet from spreadsheet with one shot
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WfNdBVQxdRXXkfSpPQQQuWh3AxMlW-8GbyaeqRF8NRE/edit#gid=502122003')
wks4 = sh.worksheet("新聞內容")

for k in range(1,7):
    #從新聞列表爬連結
    url1 = 'https://news.ltn.com.tw/list/breakingnews/politics/'+str(k)
    response = requests.get(url1)
    soup = BeautifulSoup(response.text,'lxml')
    allstring = soup.find_all('ul',{'class':'list imm'})
    string = str(allstring)
    pattern = "//news.ltn.com.tw/news/politics/breakingnews/[0-9]{7}"
    a = re.findall(pattern,string)
    links = []
    texts = []
    for link in a:
        links.append('https:'+link)
    links = np.unique(links)
    #從連結爬文章
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text,'lxml')
        string = soup.find_all("div", class_="text")[0].find_all("p")
        text = []
        for a in string:
            text.append(a.text)
        texts.append(''.join(text))
    #寫入試算表
    start = eval(wks4.acell('B1').value)+1
    end = start-1+len(links)
    str1 = "A"+str(start)+":A"+str(end)
    cell_list1 = wks4.range(str1)
    i = 0
    for cell in cell_list1:
        cell.value = texts[i]
        i+=1
    wks4.update_cells(cell_list1)
    wks4.update_acell("B1",end)






