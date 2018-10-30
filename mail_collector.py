# Tohfa Akib
# tnishan7@gmail.com

from google import google
import re
num_page = 50
j = 0
que = "@gmail.com "
query = input("Enter Search Query: ")

query = que + query


search_results = google.search(
    query,
    num_page,
    lang='en',
    area='com',
    ncr=False,
    void=True,
    time_period=False)



for result in search_results:    
    descR = result.description

    match = re.findall(r'[\w\.-]+@[\w\.-]+', descR)
    for i in match:
        if i[-1] == '.':
            i = i.replace(i[len(i) - 1], '')

            if i[-3:] == 'com' or i[-3:] == 'net' or i[
                    -3:] == 'org' or i[-3:] == 'edu' and i[-4] != '.':
                i = list(i)
                i.insert(-3, '.')
                i = ''.join(i)

        valid = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', i, re.I)

        if valid:
            i = i.lstrip("%&*-+)(^$#@")
            i = i.lower()

            j = j + 1
            print(j, ". ", i)
