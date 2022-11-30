import requests
import json
import collections
import bisect
from component import Contest
from bs4 import BeautifulSoup
contest = [i for i in range(321,299,-1)]
bicontest = [i for i in range(92,69,-1)]

weekly_contest_info = Contest.contest(contest,True)
biweekly_contest_info = Contest.contest(bicontest,False)