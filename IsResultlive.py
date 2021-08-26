import time
import requests
while(1):
  count = 0 
  for i in range(800,900): 
     
    res = requests.get('https://www.osmania.ac.in/res07/20210'+str(i)+'.jsp')
    if res.status_code!=404:   
      print(i)
      count+=1
  # print(count)
  if count!=16:
    print('Results aagaye!!!!!!!!!!')
  else:
    print('Take it easy. Results nahi aaye')  

  time.sleep(60)
    

