#laptop git test

#!/usr/bin/python

def sorter(var_restaurants):

	# NB: the following could be written as a one liner, but that would make
	# adjusting to possible changes in the structure annoying

	var_restaurants = var_restaurants[2:-3] # parse first and last brackets
	var_restaurants = var_restaurants.split('},{') # split the restaurants

	tmp_restaurants = [['name', 'lat', 'lon', 'address', 'open at']]

	for restaurant in var_restaurants:
		tmp = restaurant.split(',')

		#print("DEBUG: tmp =", tmp)

		tmp_restaurants.append([])
		for data_pair in tmp:
			tmp_restaurants[-1].append(data_pair.split(':')[1][1:-1])

		# remove unnecessary fields:

		tmp_restaurants[-1].pop(10)
		tmp_restaurants[-1].pop(9)
		tmp_restaurants[-1].pop(8)
		tmp_restaurants[-1].pop(7)
		tmp_restaurants[-1].pop(5)
		tmp_restaurants[-1].pop(1)
			

	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n') # cba to find out how to clear terminal in windows

	for restaurant in tmp_restaurants:
		print('\n')
		print(restaurant)


# an example query of restaurants at Otaniemi, Espoo:	
sorter('[{"name":"Armis Pizzeria","open":true,"latitude":"60.1841510000","longitude":"24.8052500000","address":"Mimerkinkuja 3","city":"Espoo","open_times":"11.00 - 22.30","has_delivery":true,"delivery_times":"11.00 - 22.30","url":"\/ravintolat\/espoo\/armispizzeria","delivery_range":"7.00"},{"name":"Tapiola Pizza","open":true,"latitude":"60.1753650000","longitude":"24.8099900000","address":"Tapiolantie 9","city":"Espoo","open_times":"10.00 - 22.00","has_delivery":true,"delivery_times":"10.00 - 21.30","url":"\/ravintolat\/espoo\/tapiolapizza","delivery_range":"5.00"},{"name":"Pizza de Paris","open":true,"latitude":"60.1762920000","longitude":"24.8060320000","address":"Oravannahkatori 3","city":"Espoo","open_times":"11.00 - 23.00","has_delivery":true,"delivery_times":"11.00 - 22.30","url":"\/ravintolat\/espoo\/pizzadeparis","delivery_range":"8.00"},{"name":"Otaniemi Pizza","open":true,"latitude":"60.1724780000","longitude":"24.8134290000","address":"Tapiolantie 9","city":"Espoo","open_times":"10.00 - 22.00","has_delivery":true,"delivery_times":"10.00 - 21.30","url":"\/ravintolat\/espoo\/otaniemipizza","delivery_range":"5.00"},{"name":"Alex\u2018s Bar & Restaurant","open":true,"latitude":"60.1873890000","longitude":"24.7968560000","address":"Louhentie 16","city":"Espoo","open_times":"11.00 - 24.00","has_delivery":true,"delivery_times":"11.00 - 22.00","url":"\/ravintolat\/espoo\/alexsbar","delivery_range":"7.00"},{"name":"Ravintola Han","open":true,"latitude":"60.1873660000","longitude":"24.7967280000","address":"Louhentie 16","city":"Espoo","open_times":"11.00 - 24.00","has_delivery":true,"delivery_times":"11.00 - 22.00","url":"\/ravintolat\/espoo\/ravintolahan","delivery_range":"7.00"},{"name":"Pizza Duhok","open":true,"latitude":"60.1686520000","longitude":"24.8064750000","address":"Westendinkatu 1","city":"Espoo","open_times":"10.00 - 04.00","has_delivery":true,"delivery_times":"10.00 - 03.45","url":"\/ravintolat\/espoo\/pizzaduhok","delivery_range":"7.50"},{"name":"Westend Paras Pizzeria","open":true,"latitude":"60.1688230000","longitude":"24.8052100000","address":"Westendinkatu 2","city":"Espoo","open_times":"10.00 - 04.00","has_delivery":true,"delivery_times":"10.00 - 03.45","url":"\/ravintolat\/espoo\/westendparaspizzeria","delivery_range":"8.00"},{"name":"Pizza Express - Tapiola","open":true,"latitude":"60.1758800000","longitude":"24.7931040000","address":"Oravannahkatori 3","city":"Espoo","open_times":"11.00 - 23.00","has_delivery":true,"delivery_times":"11.00 - 22.30","url":"\/ravintolat\/espoo\/pizzaexpress-tapiola","delivery_range":"6.50"},{"name":"Salam Mumbai","open":true,"latitude":"60.1758800000","longitude":"24.7931040000","address":"Oravannahkatori 3","city":"Espoo","open_times":"11.00 - 23.00","has_delivery":true,"delivery_times":"11.00 - 22.30","url":"\/ravintolat\/espoo\/mumbai","delivery_range":"8.00"},{"name":"Drunch Ravintola & Lounge","open":true,"latitude":"60.1952170000","longitude":"24.8733250000","address":"Hollantilaisentie 32","city":"Helsinki","open_times":"11.00 - 23.00","has_delivery":true,"delivery_times":"11.00 - 22.30","url":"\/ravintolat\/helsinki\/drunch","delivery_range":"7.00"},{"name":"D\u00f6ner King","open":true,"latitude":"60.1952314000","longitude":"24.8732874000","address":"Hollantilaisentie 32","city":"Helsinki","open_times":"11.00 - 23.00","has_delivery":true,"delivery_times":"11.00 - 22.30","url":"\/ravintolat\/helsinki\/dnerking","delivery_range":"7.00"},{"name":"Westend House","open":true,"latitude":"60.1628190000","longitude":"24.7908880000","address":"Westendintie 99-101","city":"Espoo","open_times":"11.00 - 21.30","has_delivery":true,"delivery_times":"11.00 - 21.30","url":"\/ravintolat\/espoo\/westendhouse","delivery_range":"6.00"},{"name":"Kiinalainen Ravintola Ju Xiang Lou","open":true,"latitude":"60.1695180000","longitude":"24.7601760000","address":"Niittykummuntie 2","city":"Espoo","open_times":"12.00 - 20.00","has_delivery":true,"delivery_times":"12.00 - 20.00","url":"\/ravintolat\/espoo\/juxianglou","delivery_range":"8.00"},{"name":"Persian Cuisine","open":true,"latitude":"60.2210200000","longitude":"24.8157140000","address":"Harakantie 20 C","city":"Espoo","open_times":"11.00 - 20.30","has_delivery":true,"delivery_times":"11.00 - 20.30","url":"\/ravintolat\/espoo\/persiancuisine","delivery_range":"8.00"},{"name":"Himitsu Sakura Sushi","open":false,"latitude":"60.2240720000","longitude":"24.8130700000","address":"Muurarinkuja 1 D","city":"Espoo","open_times":"16.00 - 22.00","has_delivery":true,"delivery_times":"16.00 - 22.00","url":"\/ravintolat\/espoo\/sushisakura","delivery_range":"10.00"},{"name":"Kings Pizza- Espoo","open":true,"latitude":"60.2239650000","longitude":"24.8129560000","address":"Muurarinkuja 1 B","city":"Espoo","open_times":"11.00 - 24.00","has_delivery":true,"delivery_times":"11.00 - 23.30","url":"\/ravintolat\/espoo\/leppavaaranpizza","delivery_range":"8.00"},{"name":"Pizzakuningas Lepp\u00e4vaara","open":true,"latitude":"60.2239650000","longitude":"24.8129560000","address":"Muurarinkuja 1 B","city":"Espoo","open_times":"11.00 - 24.00","has_delivery":true,"delivery_times":"11.00 - 23.30","url":"\/ravintolat\/espoo\/kuningas","delivery_range":"8.00"},{"name":"Ravintola Marhaba - Lepp\u00e4vaara","open":true,"latitude":"60.2242850000","longitude":"24.8133490000","address":"Harakantie 6 A 2","city":"Espoo","open_times":"11.00 - 23.00","has_delivery":true,"delivery_times":"11.00 - 22.30","url":"\/ravintolat\/espoo\/marhaba","delivery_range":"8.00"},{"name":"Pizza Master - Lepp\u00e4vaara","open":true,"latitude":"60.2240680000","longitude":"24.8256820000","address":"Harakantie 6","city":"Espoo","open_times":"11.00 - 23.00","has_delivery":true,"delivery_times":"11.00 - 22.30","url":"\/ravintolat\/espoo\/indianroyalcurry","delivery_range":"8.00"}];')