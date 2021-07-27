#pow(co so, luy thua) hàm dùng để tính thừa số.
from time import sleep
import sys

running=False
def tamgiacvuong():
	running=True
	canha=int(input('Enter A side: '))
	canhb=int(input('Enter B side: '))
	canhc=int(input('Enter C side: '))
	if pow(canha,2)==pow(canhb,2)+pow(canhc,2) or pow(canhb,2)==pow(canha,2)+pow(canhc,2) or pow(canhc,2)==pow(canha,2)+pow(canhb,2):
		print('This is a right triangle.')
	elif pow(canha,2)!=pow(canhb,2)+pow(canhc,2) or pow(canhb,2)!=pow(canha,2)+pow(canhc,2) or pow(canhc,2)!=pow(canha,2)+pow(canhb,2):
		print('This is not a right triangle.')
	sleep(1)
	running=False

while running==False:    
  user_choice=str(input('y: yes, n: no\nDo you want to check another one?'))
  if user_choice == 'yes' or user_choice == 'y':
    tamgiacvuong()
  elif user_choice == 'no'or user_choice == 'n':
    sys.exit('Leaving...')