import requests
import json
import collections
import bisect
from component import get_user_info

# state True  -> weekly Contest
#       False -> Biweekly Contest 
def contest(contest,state,df,used): 
    for contest_idx in contest:
        page = 1
        flag = True
        all_pop = 0
        # 紀錄答對2題,3題,4題的所有ranking
        gang = collections.defaultdict(list)
        while page:
            print('Weekly Contest' + str(contest_idx),page)
            if state == True:
                res = requests.get(f'https://leetcode.com/contest/api/ranking/weekly-contest-{contest_idx}?pagination={page}&region=global')
            else:
                res = requests.get(f'https://leetcode.com/contest/api/ranking/biweekly-contest-{contest_idx}?pagination={page}&region=global')

            res = res.json()
            cur_sum = 0
            # 計算答對2,3,4題的分數
            score = []
            if all_pop == 0:
                all_pop = res["user_num"]
            for e in res["questions"]:
                cur_sum += e['credit']
                score.append(cur_sum)

            # 一頁25筆資料
            for e in res["total_rank"]:
                user,point,region,country = e['username'],e['score'],e['data_region'],e['country_name']
                idx = bisect.bisect_right(score,point)
                print(idx)
                if idx == 1 or idx == 0:
                    # idx => 答對idx題
                    flag = False
                    break
                if user in used:
                    rank = used[user][0]
                    used[user][-1] += 1
                else:
                    rank,company,title,school,language = get_user_info.get_info(user,region)
                    if rank == 0:
                        continue
                    used[user].append(rank)
                    if region == 'CN':
                        used[user].append('China')
                    elif country == "" or country == None:
                        used[user].append('Unknown')
                    else:
                        used[user].append(country)
                    used[user].extend([company,title,school,language,1])
                gang[idx].append(rank)
            if not flag:
                break
            page += 1
        ans = []
        info = []
        for i in range(2,5):
            info.append(sum(gang[i]))
            info.append(len(gang[i]))
        info.append(all_pop)
        df.loc[len(df)] = info
        n = len(df) - 1
        if state == True:
            df.rename(index={n:'Weekly Contest ' + str(contest_idx)},inplace=True)
        else:
            df.rename(index={n:'Biweekly Contest ' + str(contest_idx)},inplace=True)
    
    # 在最後一格插入這次競賽的總人數
    ans.append(all_pop)
    return ans