// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Services', {
	refresh: function(frm) {
		frm.add_custom_button('Go to Rating',() =>{
			frappe.new_doc('Trainer Rating', {
				gym_member: frm.doc.name		//Refrens name
		})
		frm.add_custom_button('Go To Payment', ()=>{
			frappe.new_doc('Gym Payment',{
				gym_member: frm.doc.name
			})

		}
		)
		
		})
	}
});
