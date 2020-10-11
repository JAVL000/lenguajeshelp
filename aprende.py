print('APRENDE PROGRAMACION')
print('===================================================================')
print('Hola Bienvenido A Este programa Este Programa fue hecho para aquellos que quieren aprender programacion desde cero. Gracias.')

print('===================================================================')
print('VERSION:1.0')
name = input('Ingresa tu nombre en el siguiente espacio ->')
print('Gracias :D')

print('===================================================================')
print('---------Menu---------')
print('1. Lenguajes de Programacion')
print('2. Creador')
print('3. Salir')
print('---------Menu---------')
op = int(input('Ingresa Una Opcion ->'))

if op==1:
	print('================================')
	print('Lenguajes de Programacion')
	print('================================')
	print('Perl')
	print('Python')
	print('Java')
	print('JavaScript')
	print('Ruby')
	print('Html5') 
	print('~Salir~')
	print('================================')
	
	opc = (input('Ingrese Un Lenguaje->'))
	
	print('=============================')
		
	if opc=='Perl':
		print("Copea Y Pega En Tu Navegador")
		print('https://www.youtube.com/playlist?list=PLjARR1053fYmN9oYz-H6ZI1fOkrjLz6L2')
	
	elif opc=='Python':
		print('Copea Y Pega En tu Navegador')
		print('https://www.youtube.com/playlist?list=PLWtYZ2ejMVJnh0KVllw24XklzJ62WNFsj')
	
	elif opc=='Java':
		print('Copea Y Pega En tu Navegador Favorito :D')
		print('https://www.youtube.com/playlist?list=PLyvsggKtwbLX9LrDnl1-K6QtYo7m0yXWB')
	
	elif opc=='JavaScript':
		print('Copea Y Pega En tu Navegador')
		print('https://www.youtube.com/playlist?list=PLhSj3UTs2_yVC0iaCGf16glrrfXuiSd0G')
	
	elif opc=='Ruby':
		print('Copea y Pega En tu Navegador')
		print('https://www.youtube.com/playlist?list=PL954bYq0HsCUG5_LbfZ54YltPinPSPOks')
	
	elif opc=='Html5':
		print('Copea Y Pega En Tu Navegador')
		print('https://www.youtube.com/playlist?list=PLU8oAlHdN5BnX63lyAeV0LzLnpGudgRrK')
	
	elif opc=='Salir':
		print('Gracias Por Usar El Programa Que la Pase Bien Programando :D')
	
	else:
		print("Esa Opcion No Se Encuentra D:")

elif op==2:
	print('JAVL')
elif op==3:
	print("Gracias por Usar el Programa :D")
else:
	print('La Opcion No Se Encuentra Por el Momento')