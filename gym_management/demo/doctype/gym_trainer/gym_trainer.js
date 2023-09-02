// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Trainer', {
	refresh: function(frm) {
		frm.add_custom_button('Go To Gym Workout Plan', ()=>{
			frappe.new_doc('Gym Workout Plan',{
				gym_member: frm.doc.name			
			})

		}
		)

	}
});



