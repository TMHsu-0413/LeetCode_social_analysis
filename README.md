# LeetCode Contest parser

## 環境
- python 3.11.0
- BeautifulSoup
- selenium
- Firefox (比較不會出錯) or Edge

## 事前準備
```python=
pip install BeautifulSoup4 selenium requests
```

## 執行
```python=
python main.py
```

## 結果
- 產出一個Excel檔 data.xlsx，裡面包含2個Sheet
  1. 每場contest分別答對題數的分數加總及人數
  2. 上述爬到的所有使用者個人資訊(公司，學校，分數等等...)
