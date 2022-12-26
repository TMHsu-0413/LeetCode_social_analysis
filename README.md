# LeetCode Contest parser

## 環境
- python 3.11.0
- BeautifulSoup
- selenium
- google chrome

## 事前準備
```python=
pip install BeautifulSoup4 selenium requests pandas openpyxl
```

## 執行
```python=
# 爬取Contest答對2,3,4題資料及所有使用者資訊
python main.py
# 爬取所有Contest的參加總人數
python get_contest_pop.py
```

## 結果
- 產出一個Excel檔 data.xlsx，裡面包含2個Sheet
  1. 每場contest分別答對題數的分數加總及人數
    - Xq_sum - 答對X題的ranking總和
    - Xq_pop - 答對X題的人數
    - all_pop - 該次競賽參加總人數

  2. 上述爬到的所有使用者個人資訊(公司，學校，分數等等...，空白代表使用者無填寫)
    - rating - 現在的rating
    - country - 來自哪個國家
    - company - 目前的公司
    - title   - 目前的職稱
    - school  - 目前的學校
    - language - 最常用的語言 
    - Views - 發過的discuss共有幾人看過
    - US獨有
      - Solution - 發過的discuss有幾則(對於題目的,Ex. 第1題內的discuss的發文)
      - discuss - 發過的discuss有幾則(不對於題目的,Ex. Interview question的發文)
      - reputation - 使用者的聲譽 (得到的upvotes數 - downvotes數，包含在別人發問的討論下的回覆)
    - CN獨有
      - reput_level- 使用者的聲譽等級(跟上面的reputation一樣，等級可參考下面這張圖)
      ![image](https://github.com/TMHsu-0413/LeetCode_social_analysis/blob/main/cn_reput_level.png)
   