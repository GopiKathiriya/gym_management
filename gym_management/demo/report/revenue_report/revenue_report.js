// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Revenue Report"] = {
	"filters": [
		{
			"fieldname":"select_month",
			"label":"Select Month",
			"fieldtype":"Select",
			"options":["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
			
		}

	]
};


