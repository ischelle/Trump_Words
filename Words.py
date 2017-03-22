from bs4 import BeautifulSoup
import requests
from operator import itemgetter
from collections import OrderedDict

url_list = ['https://www.whitehouse.gov/the-press-office/2017/02/27/remarks-president-trump-listening-session-health-insurance-company-ceos',
            'https://www.whitehouse.gov/the-press-office/2017/02/26/remarks-president-trump-2017-governors-ball',
            'https://www.whitehouse.gov/the-press-office/2017/02/25/president-trumps-weekly-address',
            'https://www.whitehouse.gov/the-press-office/2017/02/24/remarks-president-trump-conservative-political-action-conference',
            'https://www.whitehouse.gov/the-press-office/2017/02/24/remarks-president-trump-signing-executive-order-regulatory-reform',
            'https://www.whitehouse.gov/the-press-office/2017/02/23/remarks-president-trump-listening-session-domestic-and-international',
            'https://www.whitehouse.gov/the-press-office/2017/02/23/remarks-president-trump-meeting-manufacturing-ceos',
            'https://www.whitehouse.gov/the-press-office/2017/02/22/remarks-president-trump-budget-meeting',
            'https://www.whitehouse.gov/the-press-office/2017/03/03/president-trumps-weekly-address',
            'https://www.whitehouse.gov/the-press-office/2017/03/03/remarks-president-trump-parent-teacher-conference-listening-session',
            'https://www.whitehouse.gov/the-press-office/2017/03/02/remarks-president-trump-aboard-uss-gerald-r-ford',
            'https://www.whitehouse.gov/the-press-office/2017/02/28/remarks-president-trump-joint-address-congress',
            'https://www.whitehouse.gov/the-press-office/2017/02/28/remarks-president-trump-signing-hbcu-executive-order',
            'https://www.whitehouse.gov/the-press-office/2017/02/28/remarks-president-trump-signing-waters-united-states-wotus-executive',
            'https://www.whitehouse.gov/the-press-office/2017/02/28/remarks-president-trump-signing-hr-321-and-hr-255',
            'https://www.whitehouse.gov/the-press-office/2017/02/21/remarks-president-trump-national-museum-african-american-history-and',
            'https://www.whitehouse.gov/the-press-office/2017/02/20/remarks-president-trump-announcing-designation-lieutenant-general-hr',
            'https://www.whitehouse.gov/the-press-office/2017/02/18/remarks-president-trump-and-first-lady-melania-trump-make-america-grea-0',
            'https://www.whitehouse.gov/the-press-office/2017/02/17/remarks-president-trump-unveiling-boeing-787-dreamliner-aircraft',
            'https://www.whitehouse.gov/the-press-office/2017/02/17/president-trumps-weekly-address',
            'https://www.whitehouse.gov/the-press-office/2017/02/16/remarks-president-trump-signing-hj-resolution-38',
            'https://www.whitehouse.gov/the-press-office/2017/02/16/remarks-president-trump-press-conference',
            'https://www.whitehouse.gov/the-press-office/2017/02/16/remarks-president-trump-listening-session-members-congress',
            'https://www.whitehouse.gov/the-press-office/2017/02/15/remarks-president-trump-listening-session-retail-industry-leaders',]

text = ""

for link in url_list:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    speech = (soup.find_all(id="content-start"))

    for x in speech:
        text+= x.get_text()

wordlist = text.split()
wordlist_lowercase = [x.lower() for x in wordlist]
wordfreq = []
for w in wordlist_lowercase:
    wordfreq.append(wordlist_lowercase.count(w))

pair = list(zip(wordlist_lowercase, wordfreq))

sorted_words = sorted(pair, key=itemgetter(1), reverse=True)
no_duplicate = list(OrderedDict.fromkeys(sorted_words))
print(no_duplicate)
