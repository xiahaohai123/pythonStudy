import requests
import time

time.sleep(5)
r = requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia')
print(r.text)
f = open('aaa.txt', 'w')
f.write(r.text)
