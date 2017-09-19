import requests
import re

found = False
counter = 0
while found == False:
    r = requests.get('http://whatthecommit.com')
    text = r.text
    m = re.compile('FUCKING ERIC')
    x = m.search(text)
    
    if x:
        found = True
        print(r.text)
        break

    print('not found yet')