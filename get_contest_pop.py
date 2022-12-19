import requests
import pandas as pd

df = pd.DataFrame(columns = ['all_pop'])
wcontest = [i for i in range(323,19,-1)]
# Biweekly contest 抓25場
bicontest = [i for i in range(93,0,-1)]

for idx in wcontest:
    print(idx)
    if idx <= 57:
        res = requests.get(f'https://leetcode.com/contest/api/ranking/leetcode-weekly-contest-{idx}?pagination=1&region=global')
    else:
        if idx == 62:
            cur = 'by-app-academy'
        else:
            cur = idx
        res = requests.get(f'https://leetcode.com/contest/api/ranking/weekly-contest-{cur}?pagination=1&region=global')
    res = res.json()
    all_pop = res["user_num"]

    df.loc[len(df)] = all_pop
    n = len(df) - 1
    df.rename(index={n:'Weekly Contest ' + str(idx)},inplace=True)

for idx in bicontest:
    print(idx)
    res = requests.get(f'https://leetcode.com/contest/api/ranking/biweekly-contest-{idx}?pagination=1&region=global')
    res = res.json()
    all_pop = res["user_num"]

    df.loc[len(df)] = all_pop
    n = len(df) - 1
    df.rename(index={n:'Biweekly Contest ' + str(idx)},inplace=True)


# 在最後一格插入這次競賽的總人數
writer = pd.ExcelWriter('all_pop.xlsx',engine = 'openpyxl')
df.to_excel(writer,sheet_name='contest')
writer.save()
writer.close()