#PRICE ALERT FOR AMAZON and SENDING MAIL and PUSH NOTIFICATION
#CREATED BY AYUSH MISHRA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import requests,time,smtplib
from bs4 import  BeautifulSoup
from notify_run import Notify
from datetime import datetime
'''
url = input("Enter your URL here : ")
dp = int(input("Enter your desired price : "))
'''
#-----------------------------------------------
url = "https://www.amazon.in/HP-Chrom-11-6-N3060-16G/dp/B01KWCIC8C/ref=pd_sbs_147_7?_encoding=UTF8&pd_rd_i=B01KWCIC8C&pd_rd_r=49259425-6622-48ec-96e6-cc18c90cdd69&pd_rd_w=rQXI3&pd_rd_wg=cbo19&pf_rd_p=00b53f5d-d1f8-4708-89df-2987ccce05ce&pf_rd_r=GV1J135GRPJ8PEB7SGKQ&psc=1&refRID=GV1J135GRPJ8PEB7SGKQ"
dp = 30000
URL = url
#pnmsg = "Below Rs. "+str(dp)+" you can get your laptop"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
 
def check_price():
  page = requests.get(URL, headers=headers)
  soup= BeautifulSoup(page.content,'html.parser')
  #----------------------------------------------------- TO CHECK WHETHER soup IS WORKING OR NOT
  
  '''m=open('soupw.txt',"wb")
  m.write(soup.prettify().encode("utf-8"))
  m.close'''
  
  #--------------------------------------------------------------------------------------
  title = soup.find(id="productTitle").get_text()
  price = soup.find(id="priceblock_saleprice").get_text()
  main_price = price[2:]
  #LETS MAKE IT AN INTEGER---------------------------------------------------------------
  l = len(main_price)
  if (l<=6) :
      main_price = price[2:5]
  else:
      p1 =  price[2:4]
      p2 =  price[5:8]
      pf = str(p1)+str(p2)
      main_price = int(pf)
 
  price_now = int(main_price)
  #VARIABLES FOR SENDING MAIL AND PUSH NOTIFICATION---------------------------------------
  title1=str(title.strip())
  main_price1 = main_price
  print("NAME : "+ title1)
  print("CURRENT PRICE : "+ str(main_price1))
  print("DESIRED PRICE : "+ str(dp))
  #-----------------------------------------------Temporary fixed for values under Rs.  9,999
  #FUNCTION TO CHECK THE PRICE-------------------------------------------------------
 
  count = 0
  if(price_now <= dp):
      send_mail()
      push_notification()
  else:
      count = count+1
      print("Rechecking... Last checked at "+str(datetime.now()))
 
#Lets send the mail-----------------------------------------------------------------
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  try:
      server.login('ayushm6635@gmail.com','ypjuoigfnwzqahzt')
  except:
      print("Wrong Mail_id or password..!")
      exit()
  subject = "Amazon: Product available at desired price, i.e,  "+str(dp)
  body = "Hey Ayush \n The price of the selected laptop on AMAZON has fallen down below Rs."+str(dp)+".\n So, hurry up & check the amazon link right now : "+url
  msg = f"Subject: {subject} \n\n {body} "
  server.sendmail(
  'ayushm6635@gmail.com',
  'champayush11@gmail.com',
  msg
  )
  print("HEY AYUSH, EMAIL HAS BEEN SENT SUCCESSFULLY.")
 
  server.quit()
#Now lets send the push notification-------------------------------------------------
def push_notification():
  notify = Notify()
  notify.send("Below Rs."+str(dp)+" you can get your Laptop")
  print("HEY AYUSH, PUSH NOTIFICATION HAS BEEN SENT SUCCESSFULLY ON ANDROID")
 
  print("Will check again after an hour.")
#Now lets check the price after 1 min ----------------------------------------------- 
count = 0
while(True):
  count += 1
  print("Count : "+str(count))
  check_price()
  time.sleep(3600)
