import requests
from bs4 import BeautifulSoup
u = [
    "https://nitkkr.ac.in/?page_id=791",
    "https://nitkkr.ac.in/?page_id=1100",
    "https://nitkkr.ac.in/?page_id=1154",
    "https://nitkkr.ac.in/?page_id=1026",
    "https://nitkkr.ac.in/?page_id=875",
"https://nitkkr.ac.in/?page_id=1953",
"https://nitkkr.ac.in/?page_id=1748",
"https://nitkkr.ac.in/?page_id=2028",
"https://nitkkr.ac.in/?page_id=1986",
"https://nitkkr.ac.in/?page_id=952",
"https://nitkkr.ac.in/?page_id=1819",
"https://nitkkr.ac.in/?page_id=1889"
]


dept_name = [
    "Computer Engineering Department",
    "Electronics and Communication Department",
    "Electrical Engineering Department",
    "Civil Engineering Department",
    "Business Administration",
"Chemistry Department",
"Computer Application",
"Humanities and Social Science",
"Mathematics",
"Mechanical Engineering Department",
"Physics Department",
"School of Renewable Energy and Efficiency"
]

i = 0

file = open("NITKKR1.txt",'a')
file.write("NITKurukshetra")

for url in u:
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html,'html.parser')
    num = soup.find_all(class_ = "col-md-12 pr_20")
    file.write("-------------------"+dept_name[i]+"------------------\n")
    for e in num:
        name = e.find('h3')
        file.write(name.text+"\n")
        j = 0 
        detail = e.find(class_ = "left-sec")
        for elem in detail.stripped_strings:
            file.write(elem)
            if j%2 != 0:
                file.write("\n")
            j = j+1    
        file.write("\n\n")
    i = i+1