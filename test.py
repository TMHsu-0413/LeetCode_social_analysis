import requests
from bs4 import BeautifulSoup

req = requests.get(f'https://leetcode.com/dnialh/')
print(req.status_code)
Soup = BeautifulSoup(req.text,'html.parser')
Soup = Soup.find_all('div',class_='flex items-start space-x-[9px]')
company,title,school = None,None,None
print('hee')
for el in Soup:
    # company icon path
    if el.find('path')['d'] == 'M7.5 7V5c0-1.484 1.242-2.667 2.75-2.667h3.5c1.508 0 2.75 1.183 2.75 2.667v2H19a3 3 0 013 3v8a3 3 0 01-3 3H5a3 3 0 01-3-3v-8a3 3 0 013-3h2.5zm2 0h5V5c0-.357-.325-.667-.75-.667h-3.5c-.425 0-.75.31-.75.667v2zM5 9a1 1 0 00-1 1v8a1 1 0 001 1h2.5V9H5zm4.5 0v10h5V9h-5zm7 0v10H19a1 1 0 001-1v-8a1 1 0 00-1-1h-2.5z':
        info = el.text.split('|')
        for i in range(len(info)):
            if i == 0:
                company = info[i].strip()
            elif i == 1:
                title = info[i].strip()
    # scholl icon path
    elif el.find('path')['d'] == 'M13.465 3.862a3 3 0 00-2.957-.048L2.61 8.122a1 1 0 000 1.756L5 11.18v6.27c0 .59.26 1.15.74 1.491 1.216.86 3.75 2.409 6.26 2.409s5.044-1.548 6.26-2.409c.48-.34.74-.901.74-1.491v-6.27l1.4-.98v4.7a.9.9 0 101.8 0V9.572a1 1 0 00-.493-.862l-8.242-4.848zM18.82 9l-5.862 3.198a2 2 0 01-1.916 0L5.18 9l5.862-3.198a2 2 0 011.916 0L18.82 9zM17 16.687a.937.937 0 01-.413.788c-.855.565-2.882 1.774-4.587 1.774-1.705 0-3.732-1.209-4.587-1.774A.936.936 0 017 16.687V12.27l3.562 1.945a3 3 0 002.876 0L17 12.27v4.417z':
        school = el.text
print(company,title,school)