#pow(co so, luy thua) hàm dùng để tính thừa số.
from time import sleep
import sys
ạ
def tamgiacvuong():
	canha=int(input('Nhập cạnh A:'))
	canhb=int(input('Nhập cạnh B:'))
	canhc=int(input('Nhập cạnh C:'))
	if pow(canha,2)==pow(canhb,2)+pow(canhc,2) or pow(canhb,2)==pow(canha,2)+pow(canhc,2) or pow(canhc,2)==pow(canha,2)+pow(canhb,2):
		print('Đây là tam giác vuông.')
	elif pow(canha,2)!=pow(canhb,2)+pow(canhc,2) or pow(canhb,2)!=pow(canha,2)+pow(canhc,2) or pow(canhc,2)!=pow(canha,2)+pow(canhb,2):
		print('Đây không phải là tam giác vuông.')
	sleep(2)

	a=input('Again?')
	if a == ('yes' or 'Yes'):
		tamgiacvuong()
	elif a==('no'or'No'):
		sys.exit(0)
tamgiacvuong()
