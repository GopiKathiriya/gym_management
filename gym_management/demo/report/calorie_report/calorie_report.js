// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Calorie Report"] = {
	"filters": [
		{
			'fieldname': 'gym_member',
            'label': 'Gym Member',
            'fieldtype': 'Link',
			'options': 'Gym Member'
		},	

		// {
		// 	'fieldname': 'From Date',
        //     'label': 'From Date',
        //     'fieldtype': 'Date'
			
		// },

		// {
		// 	'fieldname': 'date',
        //     'label':  'Date',
        //     'fieldtype': 'Date'
			
		// }		

	
	]
};

