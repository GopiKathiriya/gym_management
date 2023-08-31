# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data


def get_columns():
	columns = [
		"gym_member::100",
		"total_amount::100",
		"date::100"
    ]
	return columns
		
		


def get_data(filters=None):
		data=[]
		date1=None
		month_mapping = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
		if filters and filters.get("select_month"):
			selected_month = filters.get("select_month")
			date1 = month_mapping.get(selected_month)	

	

		gym_members = frappe.get_all('Gym Membership',fields=['gym_member','total_amount','from_date'])
		for gym_member in gym_members:
			date = gym_member.from_date
			if date1 is None or date.month == date1: 
				row = {
					"gym_member": gym_member.gym_member,
					"total_amount": gym_member.total_amount,
					"date": gym_member.from_date
				}
				data.append(row)

		return data

















