// Copyright (c) 2024, Guilherme Bolincenha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Member", {
	refresh(frm) {
        frm.add_custom_button(__('Create Membership'), () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            })
        })
        frm.add_custom_button(__('Create Transaction'), () => {
            frappe.new_doc('Library Transaction', {
                library_member: frm.doc.name
            })
        })
	},
});
