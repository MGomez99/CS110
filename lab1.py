def main():
	weeks_str = input("Please enter the number of weeks this semester: ")
	#print(weeks_str)
	classes_str = input("Enter the number of classes you are taking :")
	#print(classes_str)	
	tuition_str = input("Please enter your tuition: ")
	#print(tuition_str)
	classes_per_week_str = input("How many times does your class meet per week?")

	classes_per_week = int(classes_per_week_str)
	weeks = int(weeks_str)
	classes = int(classes_str)
	tuition = int(tuition_str)
	
	cost_per_week = ((tuition / classes) / weeks)
	print("Cost per week: ", cost_per_week)
	cost_per_class = (cost_per_week / classes_per_week)
	print("Cost per class: ", cost_per_class)

main()
