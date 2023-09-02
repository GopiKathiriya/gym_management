from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_gym_member(filters)
  
    return columns, data

def get_columns():
    columns = [
        {
            'fieldname': 'class_type',
            'label': 'Class Type',
            'fieldtype': 'Data'
        },
        {
            'fieldname': 'count',
            'label': 'Count',
            'fieldtype': 'Int'
        },
    ]
    return columns

def get_gym_member(filters=None):
    class_counts = {
        "Dance": 0,
        "Yoga": 0,
        "Zumba Class": 0
    }

    data1 = frappe.db.get_list("Group Class", fields=["full_name", "class_type"])
    for group_class in data1:
        class_type = group_class.get("class_type")
        if class_type in class_counts:
            class_counts[class_type] += 1
        else :
            class_counts[class_type] = 1
    data = []
    for class_type, count in class_counts.items():
        data.append({"class_type": class_type, "count": count})

    return data

def before_save(self):









