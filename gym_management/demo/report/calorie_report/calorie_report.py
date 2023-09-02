# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt

import frappe
from frappe import _



def execute(filters=None):
    columns = get_columns()
    data=get_customer_metrix(filters)
    labels = []
    values = []
    for k in data:
        labels.append(k['date'])
        values.append(k['burn_calories'])
        chart = {
        "type": "bar",
        "data": {
			"labels": labels,
			"datasets": [
				    {"values": values},	
        	],
        },
    }
    return columns, data, "calories report", chart
        
    

def get_columns():
    columns = [
         {
            'fieldname':'gym_member',
            'label':'Gym Member',
            'fieldtype':'Link',
            "options":"Gym Member"
         
           
        },
       
          {
            'fieldname':'weight',
            'label':'weight',
            'fieldtype':'Data',
           
        },
         {
            'fieldname':'burn_calories',
            'label':'Burnc alories',
            'fieldtype':'Data',
           
        },
         {
            'fieldname':'date',
            'label':'Date',
            'fieldtype':'Date',
           
        },
           
    ]
    return columns

def get_customer_metrix(filters):
    data = []
    filter_list = [] 
  
    # print(filters)
    if filters['gym_member']:
        filter_list.append({'name':filters['gym_member']})

    # if filters.get('date'):
    #     date=filters.get('date')
    #     filter_list.append({'date':date}) 
           
    doc= frappe.get_list("Gym Member",filters=filter_list , fields=["name"])
    for b in doc:
        doc1 = frappe.db.get_all("Customer Metrix",filters={"parent":b.name }, fields=["weight","burn_calories","date"]) 
        for a in doc1:
            row={
                    "gym_member":b.name,
                    "burn_calories":a.burn_calories,
                    "date":a.date
                    }
            data.append(row)
    return data
    


    

    # data = frappe.db.get_all("Customer Metrix",filters=filter, fields=["weight","burn_calories","date"]) 
   
 
