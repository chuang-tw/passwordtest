
while True:
	password = input('請輸入你的密碼')
	
	if password == '123456':
		print('登入成功!')
		break
	elif password != '123456':
		print('你還剩3次機會')
		password = input('請輸入你的密碼')
		if password != '123456':
			print('你還剩兩次機會')
			password = input('請輸入你的密碼')
			if password != '123456':
				print('你還剩一次機會')
				password = input('請輸入你的密碼')
				if password != '123456':
					print('登入失敗')
					break
			
			


	


