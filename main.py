import collections
import pandas as pd
import openpyxl
from component import Contest
# weekly contest 抓30場
wcontest = [i for i in range(321,291,-1)]
# Biweekly contest 抓25場
bicontest = [i for i in range(92,72,-1)]
# key:user value:rank
used_info = collections.defaultdict(list)

df = pd.DataFrame(columns = ['2q_sum','2q_pop','3q_sum','3q_pop','4q_sum','4q_pop','all_pop'])
weekly_info = Contest.contest(wcontest,True,df,used_info)

#biweekly_info = Contest.contest(bicontest,False,df,used_info)

print(used_info)
#writer = pd.ExcelWriter('data.xlsx',engine = 'openpyxl')
#df.to_excel(writer,sheet_name='contest')
#df2 = pd.DataFrame(data = used_info)
#df2 = df2.T
#df2.columns = ['ranking','country','company','title','school','language','attend_times','views','solution','discuss','reputation','reput_level']
#df2.to_excel(writer,sheet_name='user')
#writer.save()
#writer.close()