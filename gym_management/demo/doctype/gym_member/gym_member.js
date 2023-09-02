// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {
	refresh: function(fm) {
		fm.add_custom_button('Go to Membership',() =>{
			frappe.new_doc('Gym Membership', {
				gym_member: fm.doc.name		
		})
		
		
		})
		fm.add_custom_button('Create A User', ()=>{
			frappe.new_doc('User',{
				gym_member: fm.doc.name
			})
		})
		
	}
});
