height = input('請輸入您的身高(cm): ')
weight = input('請輸入您的體重(kg): ')

height = int(height)
weight = int(weight)

BMI = weight / ((height/100) * (height/100))
print("您的BMI為: ",BMI)

if BMI < 18.5: 
	print('體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('正常範圍')
elif BMI >= 24 and BMI < 27:
	print('過重')
elif BMI >= 27 and BMI < 30:
	print('輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('中度肥胖')
elif BMI >= 35:
	print('重度肥胖')
else:
	print('請確認輸入資料是否正確!')
