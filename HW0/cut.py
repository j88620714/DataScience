import gspread
from oauth2client.service_account import ServiceAccountCredentials
import jieba
import time
import math

# Open a worksheet from spreadsheet
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users\j8862\Downloads\_      2019                 -c00e35bee958.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WfNdBVQxdRXXkfSpPQQQuWh3AxMlW-8GbyaeqRF8NRE/edit#gid=502122003')
wks1 = sh.worksheet("匯入新聞&設定關鍵字")
wks2 = sh.worksheet("匯入分割詞")
#load dict
jieba.load_userdict('C:/Users\j8862\OneDrive\Desktop\資料科學\文字雲\dict1.txt')
#取出整個試算表資料
data = wks1.get_all_values()
#設定關鍵字
word = input("請輸入關鍵字:\n")
wks1.update_acell('C1',word)
time.sleep(10)
#根據關鍵字決定切那些篇新聞
newslist = wks1.col_values(3)
newslist.pop(0)
print("找到"+str(len(newslist))+"篇文章")
#關掉統計
wks2.update_acell('C1',"false")
#重新設定從第幾行輸入
wks2.update_acell('E1',1)

for j in newslist:
    j = eval(j)
    n = eval(data[j][0])
    a = []
    #分割後存入a
    for i in range(4,n,1):
        words = jieba.cut(data[j][i], cut_all=False)
        for word in words:
            a.append(word)
    #把a存入試算表
    start = eval(wks2.acell('E1').value)+1
    end = start-1+len(a)
    #合成範圍
    str1 = "A"+str(start)+":A"+str(end)
    cell_list1 = wks2.range(str1)
    i = 0
    for cell in cell_list1:
        cell.value = a[i]
        i+=1
    wks2.update_cells(cell_list1)
    #更新
    wks2.update_acell('E1',len(a)+start)
    wks1.update_acell('G1',j+1)
#開啟統計
wks2.update_acell('D1',"true")
    










