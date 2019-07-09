import webbrowser

# webaddress = ['www.google.com', 'www.naver.com','www.baidu.com']

idols = ['bts','hot','god','babyvox']

url = 'https://search.naver.com/search.naver?query='

for idol in idols: 
    webbrowser.open_new(url + idol)


# import requests

# response = requests.get('https://www.naver.com/').status_code
# print(response)

