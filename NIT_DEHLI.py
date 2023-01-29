import requests
from bs4 import BeautifulSoup
u = [
   "https://nitdelhi.ac.in/?page_id=13498",
   "https://nitdelhi.ac.in/?page_id=11977",
   "https://nitdelhi.ac.in/?page_id=11979",
   "https://nitdelhi.ac.in/?page_id=11985",
   "https://nitdelhi.ac.in/?page_id=11981",
   "https://nitdelhi.ac.in/?page_id=11993"
]


dept_name = [
"Applied Sciences",
"Civil Engineering",
"Computer Science and Engineering",
"Electronics and Communication Engineering",
"Mechanical Engineering"
]


i = 0

file = open("NIT_Dehli.txt",'a')
file.write("                                             NIT DEHLI                                             ")
file.write("\n")

for url in u:
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html,'html.parser')
    num = soup.find_all(class_ = "table-responsive")
    file.write("-------------------"+dept_name[i]+"------------------\n")
    for e in num:
        detail = e.stripped_strings
        
        for elem in detail:
            if not  elem == "Home Page" and not elem == "See More" and not elem == "Photo" and not elem == "Phone" :
             file.write(elem)
            file.write("\n")
        
    file.write("\n\n")
    i = i+1