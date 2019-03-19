def is_leapyear(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False
	
def days_in_month(year,month):
	if month in [1, 3, 5, 7, 8, 10, 12]:
		return 31
	else:
		if month == 2:
			if is_leapyear(year):
				return 29
			else:
				return 28
		else:
			return 30

def next_day(year,month,day):
	if day < days_in_month(year,month):
		return year, month, day + 1
	else:
		if month < 12:
			return year, month + 1, 1
		else:
			return year + 1, 1, 1

def date_is_before(year1,month1,day1,year2,month2,day2):
	if year1 < year2:
		return True
	if year1 == year2:
		if month1 < month2:
			return True
		if month1 == month2:
			return day1 < day2
	return False
	
def days_between_dates(year1,month1,day1,year2,month2,day2):
	days = 0
	assert date_is_before(year1,month1,day1,year2,month2,day2)
	while date_is_before(year1,month1,day1,year2,month2,day2):
		year1, month1, day1 = next_day(year1,month1,day1)
		days += 1
	return days
	
print(days_between_dates(1997,3,31,2017,9,24))										 										