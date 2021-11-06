'''
A Python Data Analysis program that handles exceptions and is used for validation 

A validation function is used for the validity of the user input and that the data passed as user input are evenly 
extracted to the new csv file, ensuring always that the program will not crash 
'''

import matplotlib.pyplot as plt 

def validate_data(country_check):
	list_ctlen = len(country_check)
	for inlength in range(0, list_ctlen):
		if list_ctlen > 3:
			print("ERROR: Sorry but at most three countries should be enetered")
			return False 
		'''
		Check if the countries are available in the the dictionary of the initial emission csv file
		
		'''
		if country_check[inlength] not in emissions_dict.keys():
			print(f"Error: Sorry  “{country_check[inlength]}“ is not a valid country", end="\n\n")
			return False
		'''
		here we check for the availability of the country in keys
		'''	

	else:
			write_csv = list(emissions_dict.keys())[0].title() + "," + ",".join(list(emissions_dict.values())[0]) + "\n"
			for mynum in range(0, len(country_check)):
				write_csv += country_check[mynum].title() + "," + ",".join(
					emissions_dict[country_check[mynum]]) + "\n"

			with open('csv/co2emissions_subset.csv', 'w') as new_fd:
				new_fd.writelines(write_csv)
			print(f"Data was successfully for the countries" + ", ".join(country_check).title() + "saved into file Emissions_subset.csv", end="\n\n")
	return True 						


print("A Data Analysis program")
print()

'''
The try except handler will be used for exceotion handling in the program
'''

try:
	emissions_dict  = {}
	'''
	We will read all the countries in lower case

	''' 
	with open('csv/co2emissions.csv', 'r') as fd:
		for data in fd.read().split('\n'):
			emissions_dict.update({data.split(',')[0].lower(): data.split(',')[1:]})
	print("All data from co2emissions.csv file has been read into a dictionary. ", end="\n\n")
	'''
	we will loop until the user does not enter the expected input 

	'''
	while True:
		input_year = input("Please select a year to find the statistics between 1997 and 2010: ")
		if not input_year.isdigit() or not 1997 <= int(input_year) <= 2010:
			print("Sorry but this is not a valid year, please enter another one")
			continue 
		else:
			break

	index_num = int()
	lines = []

	for item in emissions_dict.values():
		if input_year in item:
			index_num = (item.index(input_year))
	
	total = 0
	item = 0 
	tot_emissions_in_year = []

	for val in emissions_dict.values():
		if item!=0:
			total += float(val[index_num])			
			tot_emissions_in_year.append(list(emissions_dict.values())[item][index_num])
		item += 1 
	

	# the len of the countries keys except the first key which is the CO2 per capita is calculated as below
	len_countries = len(list(emissions_dict.keys())) - 1 

	max_country_index = int(tot_emissions_in_year.index(str(max(float(str_value) for str_value in tot_emissions_in_year))))
	min_country_index = int(tot_emissions_in_year.index(str(min(float(str_value) for str_value in tot_emissions_in_year))))
    

	average_emissions = (total) / (len_countries)

	max_emissions = list(emissions_dict.keys())[max_country_index + 1]
	min_emissions = list(emissions_dict.keys())[max_country_index + 1]

	print(f'In {input_year}, the countries with the minimum and maximum CO2 emission level were: [{min_emissions}]'
		  f'and {max_emissions}] respectively.')

	print(f'Average CO2 emissions in {input_year} were {"%.6f" %round(average_emissions,6)}')
	print()

	'''
	Making the input countries that we check case insensitive and check for availability of the country in keys 
	For this reason power of pyython is used to get data into two country variable 
	
	'''

	while True:
		try:
			country1, country2 = input("Please write two comma-separated countries for which you want the data to be viualized: ").lower().split(", ")
		except ValueError:
			print("Please write up to two comma-separated countries for which you wat the data to be visuaized...")
			continue 
		if country1 not in emissions_dict.keys() or country2 not in emissions_dict.keys():
			print("Sorry but this is not a valid country.")
			continue 
		else:
			num1 = list(emissions_dict.keys()).index(country1)
			num2 = list(emissions_dict.keys()).index(country2)
			plt.plot(list(map(float, list(emissions_dict.values())[0])),
					 list(map(float, list(emissions_dict.values())[num1])), label=country1)
			plt.plot(list(map(float, list(emissions_dict.values())[0])),
					 list(map(float, list(emissions_dict.values())[num2])), label=country2)		 		
			plt.title("Year vs Emissions in Capita")
			plt.xlabel("Year")
			plt.ylabel("Emissions in")
			plt.legend()
			plt.show()
			print()
			break 


#Making the input string of the three iserted countries case insensitive 

	while True:
		input_str = input("Write up to three comma-separated countries names for which you want the data to be extracted: ").lower()
		input_country = input_str.split(", ")
		# we loop until the user does not enter expected inout 
		if not validate_data(input_country):
			continue
		else:
			break 

except FileNotFoundError:
	print("File not found...")
except IOError:
	print("Output file cannot be saved")



