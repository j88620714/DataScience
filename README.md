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
### HW1:
* [**爬蟲**](https://script.google.com/d/MoFMifnPZJWSCCY-qUiHSjPRWp2vJfyNW/edit?mid=ACjPJvERJyEGyupYcceMP2zgbi-XBuoeIsc0jfoRDNc5MlD6BwZz1y98hUQGoXpna_Td5fKbbZpZ7mjLOxd_ttiI0JYeVDz0v2bUWugd56YlQ25FS8iYvWkyBGtfK9-uGZXbtfreI9hibGE&uiv=2):因為台北市政府開放平台上的資料是每五分鐘更新一次的即時資料，所以必須每五分鐘就爬一次資料，然後把這些資料記錄下來。我們選擇的方式是用google的apps script來達成，因為它可以設定在雲端自動執行，而且爬下來的資料也能很容易地寫入試算表中儲存。
* [**交通資料整理**](https://docs.google.com/spreadsheets/d/1FJPf9S2vpimDZvefrpnfq31cq3JpmySHse74WQoEgu4/edit?usp=sharing):資料爬下來後，我們就直接在試算表中做簡單的統計，像是把平日同樣時段的速度做平均。
      
    
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
* Q1:交控中心以往所判斷市區幹道尖峰時間為7:00\~9:00與17:00\~19:00，因此我們希望透過分析來看看是否適用於復興南北路。   
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
     從上圖平均速度搭配T檢定的結果就可以清楚的看到，過了7:10後會有明顯且大幅的降速，13:30後也會有小幅度的降速，到了17:40附近又會有一波降速，而過了19:20後車速則終於開始回升。這樣的結果與交控中心的定義其實蠻符合的，差別大概就在於白天沒有所謂真正"離峰"的時段，因為車速只是隨著時間越來越慢，而"尖峰"則是車速有明顯下降的時段
     這樣的分析我覺得可以運用在號誌秒數週期的調整，根據我每天上學的觀察，號誌的秒數如果有變化幾乎都是在整點的時候，因此如果能透過分析精準的知道什麼時候需要調整周期，我覺得會更有效率。
* Q1(補充):我們從上面的結果訂出了7:00~22:00為較多人使用道路的時段，並以這個區間做各站點的箱型圖                             
     [**程式碼**](https://github.com/j88620714/DataScience/blob/master/HW1/Box.ipynb)                  
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/box.png)                     

## 2019-04-04-Week6
### HW1:EDA
* Q2:兩相鄰站點間是否有關連?
     除了上面做過的gif之外，我們也嘗試做熱圖來看看透過顏色的深淺能不能觀察到其他性質
     [**程式碼**](https://github.com/j88620714/DataScience/blob/master/HW1/%E7%86%B1%E5%9C%96.ipynb)    
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/heatmap.png)      
     圖中顏色越深代表速度越慢，我們可以看到如同gif做出來的結果，第三站的速度一直維持在50Km/Hr左右，但其他站與站之間的關聯性似乎還不是很明顯。於是我們接下來以V-t圖來觀察兩觀測站的速度關系。                
     以第一、二站為例:[**程式碼**](https://github.com/j88620714/DataScience/blob/master/HW1/linePlots.ipynb)                        
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E4%B8%80%E3%80%81%E4%BA%8C%E7%AB%99V-t.png)                   
     我們可以看到，這兩站有明顯的速度差，可能會有類似的趨勢，但因為速差太大不好比較，所以我們決定把蒐集到的速度資料在試算表中直接標準化。接著再做一次標準化後的V-t圖。       
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E4%B8%80%E3%80%81%E4%BA%8C%E7%AB%99%E6%A8%99%E6%BA%96%E5%8C%96V-t%E5%9C%96.png)           
     如果單看7:00~22:00的線段，就可以看到它們有高度重疊的趨勢。接著以同樣的方法對四、五站也做一次          
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%9B%9B%E3%80%81%E4%BA%94%E7%AB%99V-t.png)
     ![](https://github.com/j88620714/DataScience/blob/master/HW1/%E5%9B%9B%E3%80%81%E4%BA%94%E7%AB%99%E6%A8%99%E6%BA%96%E5%8C%96V-t%E5%9C%96.png)       
     分析完上面幾站後，我們大概可以得出幾個結論。
     * 一、二站的車流應該有類似的性質，但可能因為道路性質的不同(車道、紅綠燈數目)，導致車子到了第二觀察站的路段時降低速度。
     * 第三站車速始終保持定值
     * 五、六站的各項性質都很接近        
     至於以上現象發生的可能原因，我們會在接下來的時間繼續討論
    
## 2019-05-02-Week13
### HW4~6:PCA
* [**練習**](https://github.com/j88620714/DataScience/blob/master/HW4-6/practice.ipynb):這次的作業比較偏向文字處理，而我們先前的資料都以數值居多，因此我們到台北市開放平台上找到了[107年度A1及A2類交通事故明細](https://docs.google.com/spreadsheets/d/1A3V6ncj7VLNDiDkchaYPIYmqrA0trkEj8L-tHoaAyZs/edit#gid=154609684)來做為我們的文本，並試圖分析事故間的關聯性。
  1. 首先先對資料做預處裡，我們將資料表中的代碼先全部換回文字([對照表](https://docs.google.com/spreadsheets/d/1A3V6ncj7VLNDiDkchaYPIYmqrA0trkEj8L-tHoaAyZs/edit#gid=1255796576))，例如:A1代表造成人員當場或二十四小時內死亡之交通事故、C03代表普通重型機車等。  
  2. 接著，我們把[資料](https://docs.google.com/spreadsheets/d/1A3V6ncj7VLNDiDkchaYPIYmqrA0trkEj8L-tHoaAyZs/edit#gid=1061450930)分成兩個類別，分別為A1(死亡)、A2(受傷)。然後皆使用jeiba來斷詞，分別計算兩類別的詞頻，並各取出現頻率最高的前20個詞。(直接用jieba而不使用TF-IDF是因為我們的原始資料中每一格都是有意義的資料，不像一般的文本有會有大量的贅詞)
  3. 仿照老師對兩種類別fb粉專的分析，把前一步驟得到關鍵詞對每一項事故紀錄做共現矩陣(有出現則true反之則false)，最後從networkx跑出的圖上可以看出，有產生關連性的很大一部分都是同一場車禍，但是是對不同人所做的紀錄(一場車禍如果是4台車相撞，在明細中就會有4筆紀錄)。
* [**PCA**](https://github.com/j88620714/DataScience/blob/master/HW4-6/PCA2.ipynb):上面得出結論是蠻合理的，但是僅有這樣的關聯性似乎沒有太大意義。所以我們重新選擇了A1類的死亡車禍，希望能從共現性來看出有沒有什麼樣的特徵跟死亡車禍比較相關。比方說能以"死亡車禍"這個標籤為中心，根據相關程度向外發散到其他標籤。
  1. 如同上面的文字預處理，不同的是這次我們先在試算表中，把同一場車禍的所有資料合併成一個文本形成新的[資料](https://docs.google.com/spreadsheets/d/1A3V6ncj7VLNDiDkchaYPIYmqrA0trkEj8L-tHoaAyZs/edit#gid=1460764096)，否則如果像是摩托車與汽車相撞，不合併的話就不會有摩托車-汽車的共現性了。除此之外，為了避免年齡及車道速限中的數字跟路名中的數字混淆，所以一律換成以中文表示。
  2. 接著，我們把對照表中的標籤作為我們的關鍵詞，然後計算兩兩關鍵詞在所有車禍紀錄同時出現的次數做出共現矩陣。
  3. 在跑networkx的圖時，我們改變了權重、線段粗細和節點大小，如此一來共現性高的兩個標籤就會距離較近且線斷較粗，總出現次數大的則會讓標籤放大。   
  ![](https://github.com/j88620714/DataScience/blob/master/HW4-6/%E5%85%B1%E7%8F%BE%E5%9C%96.png)     
  
  結論:由分析結果來看，我們可以透過點與點之間的距離與粗細判斷名詞之間的關聯性，進而改善環境、加強宣導以降低意外發生。
  * 機車與行人較容易發生死亡車禍，我們去閱讀相關事件內容發現，機車車禍事件多發生在台北市連接外縣市的機車道，而行人則多發生於近交叉口的地方。(聯外橋樑的機車引道真的超恐怖的......)
  * 天氣導致車禍發生的關聯性相較於其他道路條件低，不能因為天氣晴朗忽略道路安全。
  * 年輕族群(20至30歲)較其他年齡層易發生車禍，而總體而言男性比例又高於女性。
  * 快車道較慢車道與死亡更相關，時速50的道路也較易發生死亡車禍，可知高速行駛提高意外風險之外，也更易在事故發生時造成巨大傷害。
* [**Neural Network**](https://github.com/j88620714/DataScience/blob/master/HW4-6/NeuralNetwork.ipynb):先前的作業中，已經爬了幾條路的車速資料，在爬下了車流量的資料後我們就開使思考，有沒有可能像流體力學中，用一個間單的模型透過帶入密度、壓力、溫度等來計算空間中某一點某一個時刻的流速，改變為輸入車流、道路性質(紅綠燈數、車道數...等)來判斷車速。剛好老師教到了Neural Network，所以我們就決定把蒐集到的數萬筆資料丟進Keras中訓練，看看能不能真的預測車速。
  1. 首先還是資料預處理的部分，因為車流車速兩筆資料是分別爬的，所以必須篩選同時有車流與車速資料的時刻，並將該時刻的資料抓取下來依照站點再與實地走訪後的道的道路資料整理成3個變數的X輸入、對應的車速整理成1項Y輸出。[code](https://script.google.com/d/1uNK7is3reReGsmvhh-zyPPKZXEQzlzOwPqbY2FEuSH4gBnKUuYxVBp5x/edit?usp=sharing)
  2. 把整理完的[資料](https://docs.google.com/spreadsheets/d/1abC0kNTX9YRXDCMU-v9c9aYlXSGakNKbVcIR9t-YgH0/edit#gid=0)分別存成xtrain.csv、ytrain.csv就可以丟進keras開始運算了。  
    
  結論:透果跑出來的模型去預測33筆車速，再去對照真正觀測到的車速，我們發現有30筆的誤差是在10%以內。接下來我們會繼續蒐集數據，也許還會新增X輸入的變數，希望能得到更精準的預測。我想這套預測模型應該會蠻適合用在像是針對目前經常壅塞的道路，政府可以拿來評估改變什麼道路性質可以最有效率的提升車速，或者是需要臨時封閉道路時，可以預測對車速的影響，如果有必要分流到其他道路的話，也可以分析在不嚴重影響那條道路的車速情況下，可以負擔分流多少車過去。






	
  




