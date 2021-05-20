#pow(co so, luy thua)
from time import sleep
import sys

def tamgiacvuong():
	canha=int(input('Nhap canh A:'))
	canhb=int(input('Nhap canh B:'))
	canhc=int(input('Nhap canh C:'))
	if pow(canha,2)==pow(canhb,2)+pow(canhc,2) or pow(canhb,2)==pow(canha,2)+pow(canhc,2) or pow(canhc,2)==pow(canha,2)+pow(canhb,2):
		print('Đây là tam giác vuông.')
	elif pow(canha,2)!=pow(canhb,2)+pow(canhc,2) or pow(canhb,2)!=pow(canha,2)+pow(canhc,2) or pow(canhc,2)!=pow(canha,2)+pow(canhb,2):
		print('Đây không phải là tam giác vuông.')
	sleep(2)

	a=input('Again?')
	if a == ('yes' or 'Yes'):
		tamgiacvuong()
	elif a=='no':
		sys.exit(0)
tamgiacvuong()