import requests
from bs4 import BeautifulSoup
u = [
   "http://www.mnnit.ac.in/index.php/department/engineering/biotech/biotechfp",
   "http://www.mnnit.ac.in/index.php/department/engineering/ce/cefp",
   "http://www.mnnit.ac.in/index.php/department/engineering/csed/csedfp" ,
   "http://www.mnnit.ac.in/index.php/department/engineering/ee/eefp" ,
   "http://www.mnnit.ac.in/index.php/department/engineering/ee/eefp" ,
   "http://www.mnnit.ac.in/index.php/department/engineering/me/mefpa"
]



dept_name = [

"Biotech Engineering",
"Civil Engineering" ,
"Computer Engineering " ,
"Electrical Engineering" ,
"Electronics and Communication Engineering" ,
"Mechanical Engineering"

]


i = 0

file = open("NIT_Allahbad.txt",'a')
file.write("                                             NIT Allahbad                                            ")
file.write("\n")

for url in u:
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html,'html.parser')
    num = soup.find_all("table")
    file.write("-------------------"+dept_name[i]+"------------------\n")
    for e in num:
        detail = e.stripped_strings
        
        for elem in detail:
            if not  elem == "View Profile" and not elem == "Google Scholar Profile" and not elem == "Photo" and not elem == "Phone" :
             file.write(elem)
            file.write("\n")
        file.write("\n")
        
        
    file.write("\n\n")
    i = i+1