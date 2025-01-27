// Copyright (c) 2024, Guilherme Bolincenha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Article", {
	refresh(frm) {
		if(frm.doc.status=="Issued"){
			frm.add_custom_button(__('Book Holder'), () => {
				frm.call("get_book_holder")
					.then(r => {
						if(r){
							frappe.msgprint(r.message)
						}else{
							frappe.msgprint(__("No holder found"))
						}
					})
			})
		}
	},
});
