#Author:Alwan Putra
#gataungoding.id

def back():
	back = input('back/exit [y/n]:')
	if back == 'y':
		menu()
	elif back == 'n':
		exit()
	else:
		print('print yang bener ajg')

	back()

def modulus():
	print('-'* 50)
	print('program modulus')
	a = int(input('masukkan angka pertama:'))
	b = int(input('masukkan angka kedua:'))

	print ('hasilnya adalah', a % b)
	back()

def kurang():
	print('-'* 50)
	print('program mengurang')
	a = int(input('masukkan angka pertama:'))
	b = int(input('masukkan angka kedua:'))

	print ('hasilnya adalah', a - b)
	back()

def tambah():
	print('-'* 50)
	print('program tambah ')
	a = int(input('masukkan angka pertama:'))
	b = int(input('masukkan angka kedua:'))


	print ('hasilnya adalah:', a + b )

	back()

def pangkat():
	print('-'* 50)
	print('program pangkat')
	a = int(input('masukkan angka pertama:'))
	b = int(input('masukkan angka kedua:'))

	print ('hasilnya adalah:', a ** b)

	back()

def menu():
	print('selamat datang di program kalkulator sederhana')
	print('-'* 50)
	print('1.tambah [+]')
	print('2.kurang[*]')
	print('3.modulus[%]')
	print('4.pangkat[**]')

	menu = input('pilih angka =>')
	if menu == '1':
		tambah()
	elif menu == '2':
		kurang()
	elif menu == '3':
		modulus()
	elif menu == '4':
		pangkat()
	else:
		print('input yg bener ya asw')	

menu()