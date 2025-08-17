products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = [name, price] #小清單
	products.append(p) #小清單裝入大清單
print(products)
for product in products:
	print(product[0]) #記得加上product，不然只會印出[0]
	print(product[0], '的價格是', product[1])



