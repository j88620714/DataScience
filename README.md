# **資料科學**
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
* Q1:交控中心以往所判斷市區幹道尖峰時間為7~9時與17~19時，因此我們希望透過分析來看看是否適用於復興南北路。   
     首先，我們先將原本每5分鐘更新的資料，以10分鐘為平均製成[表格](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%BE%A9%E8%88%88%E5%8D%97%E6%99%82%E9%80%9F%E8%A1%A8.pdf)，表中只將收集到的平日資料進行運算，接著以時間和速度做出不同觀測站的折線圖  
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%85%A8%E9%83%A8%E8%B7%AF%E6%AE%B5%E6%8A%98%E7%B7%9A%E5%9C%96.png)
     但因為線段太多不太好觀察，所以我們製做了gif來觀察規律。[**程式碼**](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%BE%A9%E8%88%88%E5%BE%80%E5%8D%97.ipynb)  
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%BE%A9%E8%88%88%E5%BE%80%E5%8D%97.gif)
     從gif中大致上可以看出，速度在過了早上7點之後確實有明顯的下降，然而下降後直到晚上8點前都沒有明顯的回升，因此我們接著將以分析車速時常用的T檢定來分析是否有明顯的壅塞情況。除此之外，從gif中也可以看出民生東路-八德路這個觀測站的車速似乎不受時間影響，也與周邊的觀測站有非常大的差異，因此接下來我們也會對相鄰的觀測站做分析比較。
### 參考資料
* 高雄市區建國路段旅行時間差異性檢定與推估 : [https://research.kcg.gov.tw/upload/RelFile/Research/1069/635852659299120887.pdf](https://research.kcg.gov.tw/upload/RelFile/Research/1069/635852659299120887.pdf) 
* 五福路車流特性分析與應用 : [https://www.tbkc.gov.tw/upload/WebList/141/3bb52ea3-d744-43ef-a84d-b7dc2dc6c117/AllFiles/105%E4%BA%94%E7%A6%8F%E8%B7%AF%E8%BB%8A%E6%B5%81%E7%89%B9%E6%80%A7%E5%88%86%E6%9E%90%E8%88%87%E6%87%89%E7%94%A8.pdf](https://www.tbkc.gov.tw/upload/WebList/141/3bb52ea3-d744-43ef-a84d-b7dc2dc6c117/AllFiles/105%E4%BA%94%E7%A6%8F%E8%B7%AF%E8%BB%8A%E6%B5%81%E7%89%B9%E6%80%A7%E5%88%86%E6%9E%90%E8%88%87%E6%87%89%E7%94%A8.pdf)
## 2019-03-28-Week６
* Q1:在前兩分參考資料中，它們都是拿單一觀測站的資料，以一個小時為單位交錯後，做單一樣本T檢定來區隔尖峰離峰時段。但是當我們用同樣的方法分析之後卻發現，復興南北路似乎沒有明顯的壅塞情況。後來我們就想到，因為我們在同一條路上其實就有7個觀測站，如果把7個站的速度當作一組數據，經過10分鐘後的速度當另一組數據，這樣就可以對前後兩個時刻的速度做成對樣本T檢定，來判斷是否有顯著差異。我們直接用試算表內的T.TEST函式進行運算，只要P值小於0.05就視為顯著速度差異，並將這些時間點標註在整條路段平均速度與時間的折線圖上。(因為半夜的車速不太穩定，分析起來沒有太大意義，所以我們只分析5:00~23:00的數據)      
     [**程式碼**](https://github.com/j88620714/DataScience/blob/master/HW1/%E6%A8%99%E8%A8%98%E9%A1%AF%E8%91%97%E9%80%9F%E5%BA%A6%E5%B7%AE%E7%95%B0.ipynb)       
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E6%A8%99%E8%A8%98%E9%A1%AF%E8%91%97%E9%80%9F%E5%BA%A6%E5%B7%AE%E7%95%B0.png)      
從上圖平均速度搭配T檢定的結果就可以清楚的看到，過了7:10後會有明顯且大幅的降速，13:30後也會有小幅度的降速，到了17:40附近又會有一波降速，而過了19:20後車速則終於開始回升。這樣的結果與交控中心的定義其實蠻符合的，差別大概就在於白天沒有所謂真正"離峰"的時段，因為車速只是隨著時間越來越慢，而"尖峰"則是車速有明顯下降的時段。這樣的分析我覺得可以運用在號誌秒數週期的調整，根據我每天上學的觀察，號誌的秒數如果有變化幾乎都是在整點的時候，因此如果能透過分析精準的知道什麼時候需要調整周期，我覺得會更有效率。



	




