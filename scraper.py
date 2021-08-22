import requests
htNo='160317733020'
url = f"https://www.osmania.ac.in/res07/20210763.jsp?mbstatus=&htno={htNo}"


response = requests.get(url)

print(response.text)