import requests
from bs4 import BeautifulSoup

u = [
    "https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Qk06QmlvdGVjaG5vbG9neSBhbmQgTWVkaWNhbCBFbmdpbmVlcmluZw%3d%3d-xybnEmSfLx0%3d",
    "https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Q0U6Q2l2aWwgRW5naW5lZXJpbmc%3d-ki5qRrzXDBk%3d",
    "https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Q1M6Q29tcHV0ZXIgU2NpZW5jZSBhbmQgRW5naW5lZXJpbmc%3d-MBb7wMG%2fNVo%3d",
    "https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=RUM6RWxlY3Ryb25pY3MgYW5kIENvbW11bmljYXRpb24gRW5naW5lZXJpbmc%3d-6xL4rgmtWLc%3d",
    "https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=TUU6TWVjaGFuaWNhbCBFbmdpbmVlcmluZw%3d%3d-muzHrU86jFw%3d"

]

dept_name = [
    "Biotechnology and Medical Engineering",
    "Civil Engineering",
    "Computer Science and Engineering",
    "Electronics and Communication Engineering",
    "Mechanical Engineering"
]

i = 0

file = open("NIT_Rourkela", 'a')
file.write("                                             NIT ROURKELA                                             ")
file.write("\n")

for url in u:
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    num = soup.find_all(class_="row mb-25 blog-inner")
    file.write("-------------------" + dept_name[i] + "------------------\n")
    for e in num:
        detail = e.find(class_="blog-content-faculty")
        text = detail.stripped_strings
        for elem in text:
            if not elem == "View Profile":
                file.write(elem)
            file.write("\n")

    file.write("\n\n")
    i = i + 1