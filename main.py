import requests
import json
import collections
import bisect
import pandas as pd
import openpyxl
from component import Contest
from bs4 import BeautifulSoup
# weekly contest 抓30場
wcontest = [i for i in range(321,310,-1)]
# Biweekly contest 抓25場
bicontest = [i for i in range(92,71,-1)]
# key:user value:rank
used_info = collections.defaultdict(tuple)

df = pd.DataFrame(columns = ['2題總和','2題人數','3題總和','3題人數','4題總和','4題人數'])
weekly_info = Contest.contest(wcontest,True,df,used_info)

#biweekly_info = Contest.contest(bicontest,False,df,used_info)

print(used_info)
writer = pd.ExcelWriter('test.xlsx',engine = 'openpyxl')
df.to_excel(writer,sheet_name='x1')
df2 = pd.DataFrame(data = used_info)
df2 = df2.T
df2.columns = ['分數','國家']
df2.to_excel(writer,sheet_name='x2')
writer.save()
writer.close()