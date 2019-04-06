﻿# **資料科學**
姓名:歐陽智文  
學號:b06502024

## 2019-02-28-Week2
### HW0:
1. 試算表作為資料庫 : [**Link**](https://docs.google.com/spreadsheets/d/1WfNdBVQxdRXXkfSpPQQQuWh3AxMlW-8GbyaeqRF8NRE/edit?usp=sharing)  
2. 流程:          
→[**crawler**](https://github.com/j88620714/DataScience/blob/master/HW0/%E7%A8%8B%E5%BC%8F/crawler.py):從自由時報政治新聞列表，將2/22~2/28日間的新聞內容匯入試算表     
→[**cut**](https://github.com/j88620714/DataScience/blob/master/HW0/%E7%A8%8B%E5%BC%8F/cut.py):輸入關鍵字後，試算表回傳新聞內容並分割，再將結果匯入試算表      
→[**draw**](https://github.com/j88620714/DataScience/blob/master/HW0/%E7%A8%8B%E5%BC%8F/draw.py):根據試算表統計結果製作文字雲     
3. 成果:   
	* 以"**還願**"為關鍵字 :
![以"還願"為關鍵字](https://github.com/j88620714/DataScience/blob/master/HW0/%E7%85%A7%E7%89%87/%E9%82%84%E9%A1%98wordcloud2.png)
	* 以"**柯文哲**"為關鍵字 :
 ![以"柯文哲"為關鍵字](https://github.com/j88620714/DataScience/blob/master/HW0/%E7%85%A7%E7%89%87/%E6%8A%93%E9%A0%ADwordcloud.png)
	* 以"**土包子**"為關鍵字 :
![以"包子"為關鍵字](https://github.com/j88620714/DataScience/blob/master/HW0/%E7%85%A7%E7%89%87/%E5%8C%85%E5%AD%90wordcloud.png)

### 參考資料
* gspread:[https://github.com/burnash/gspread](https://github.com/burnash/gspread)
* jieba:[https://github.com/fxsjy/jieba](https://github.com/fxsjy/jieba)
* 爬蟲slideshare:[https://www.slideshare.net/tw_dsconf/python-78691041](https://www.slideshare.net/tw_dsconf/python-78691041)
* Markdown:[https://kakapontw.blogspot.com/2017/01/markdown-syntax.html#img](https://kakapontw.blogspot.com/2017/01/markdown-syntax.html#img)
* 助教sample code:[https://github.com/MiccWan/Political-News-Analysis/blob/master/final_demo/final_report.ipynb](https://github.com/MiccWan/Political-News-Analysis/blob/master/final_demo/final_report.ipynb)

## 2019-03-07-Week３
### HW1:北市府交通資料整理 : [**Link**](https://docs.google.com/spreadsheets/d/1FJPf9S2vpimDZvefrpnfq31cq3JpmySHse74WQoEgu4/edit?usp=sharing)
### 參考資料
* 台北市政府資料開放平台道路速率:[https://data.taipei/dataset/detail/preview?id=b5aaf33a-a6dc-4836-bce6-09986241fe11&rid=8a2ea001-f483-4441-a458-af697653296c](https://data.taipei/dataset/detail/preview?id=b5aaf33a-a6dc-4836-bce6-09986241fe11&rid=8a2ea001-f483-4441-a458-af697653296c)
* Parse XML using Google Apps Script:[https://stackoverflow.com/questions/26531907/parse-xml-using-google-apps-script](https://stackoverflow.com/questions/26531907/parse-xml-using-google-apps-script)

## 2019-03-14-Week４
### HW1:將資料製成gif : [**程式碼**](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%BE%A9%E8%88%88%E5%BE%80%E5%8D%97gif.ipynb)
![gif](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%BE%A9%E8%88%88%E5%BE%80%E5%8D%97.gif)

### 參考資料
* 視覺化資料 - Matplotlib:[https://ithelp.ithome.com.tw/articles/10201004](https://ithelp.ithome.com.tw/articles/10201004)
* Matplotlib 製作Gif:[https://blog.csdn.net/briblue/article/details/84940997](https://blog.csdn.net/briblue/article/details/84940997)

## 2019-03-21-Week５
### HW1:EDA
* Q1:交控中心以往所判斷市區幹道尖峰時間為 7~9 時與 17~19 時，因此我們希望透過分析來看看是否適用於復興南北路。   
     首先，我們先將原本每5分鐘更新的資料，以10分鐘為平均製成[下表](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%BE%A9%E8%88%88%E5%8D%97%E6%99%82%E9%80%9F%E8%A1%A8.pdf)，表中只將收集到的平日資料進行運算，接著以時間和速度做出不同觀測站的折線圖  
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%85%A8%E9%83%A8%E8%B7%AF%E6%AE%B5%E6%8A%98%E7%B7%9A%E5%9C%96.png)
     但因為線段太多不太好觀察，所以我們製做了gif來觀察規律。
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%BE%A9%E8%88%88%E5%BE%80%E5%8D%97.gif)
     

     
## 2019-03-28-Week６


	




