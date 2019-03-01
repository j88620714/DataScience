import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np

def get_wordcloud_of_keywords(a, image_path=False):  
    if image_path:
        coloring = np.array(Image.open(os.path.join(image_path)))
        color_func = ImageColorGenerator(coloring)
        wc = WordCloud(max_font_size=60,
                       background_color="white",
                       mask=coloring,
                       color_func=color_func,
                       font_path=font_path,
                       width=100, height=100,
                       max_words=10000)
    else:
        wc = WordCloud(max_font_size=60,
                       background_color="white",
                       colormap='Set2',
                       font_path=font_path,
                       width=400, height=300,
                       max_words=10000)

    im = wc.generate_from_frequencies(frequencies=a)
    return im


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users\j8862\Downloads\_      2019                 -c00e35bee958.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WfNdBVQxdRXXkfSpPQQQuWh3AxMlW-8GbyaeqRF8NRE/edit#gid=502122003')
wks1 = sh.worksheet("統計結果")

#匯入統計好的頻率
dict1={}
words = wks1.col_values(8)
freq = wks1.col_values(9)
for i in range(len(words)):
    dict1[words[i]] = eval(freq[i])
    
#製圖
font_path = r'msjh.ttc'
pic = 'C:/Users\j8862\OneDrive\Desktop\資料科學\文字雲\還願.png'
wc = get_wordcloud_of_keywords(dict(dict1),pic)
wc.to_image()

#顯示用
plt.figure( figsize=(100,75), facecolor='k')
plt.imshow(ten_wc,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()









