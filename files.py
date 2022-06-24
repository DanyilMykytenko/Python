f = open('poem.txt') # если не указан режим, по умолчанию подразумевается
# режим чтения ('r'eading)
while True:
	line = f.read()
	print(line, end='')
f.close() # закрываем файл
