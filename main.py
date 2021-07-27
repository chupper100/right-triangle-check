#pow(co so, luy thua) hàm dùng để tính thừa số.
from time import sleep
import sys

def tamgiacvuong():
	canha=int(input('Enter A side: '))
	canhb=int(input('Enter B side: '))
	canhc=int(input('Enter C side: '))
	if pow(canha,2)==pow(canhb,2)+pow(canhc,2) or pow(canhb,2)==pow(canha,2)+pow(canhc,2) or pow(canhc,2)==pow(canha,2)+pow(canhb,2):
		print('This is a right triangle.')
	elif pow(canha,2)!=pow(canhb,2)+pow(canhc,2) or pow(canhb,2)!=pow(canha,2)+pow(canhc,2) or pow(canhc,2)!=pow(canha,2)+pow(canhb,2):
		print('This is not a right triangle.')
	sleep(2)

	user_choice=input('Do you want to check another one? \n y: yes, n: no').lower()
	if user_choice == ('yes' or 'y'):
		tamgiacvuong()
	elif user_choice==('no'or'n'):
		sys.exit(0)
tamgiacvuong()
