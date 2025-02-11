// Copyright (c) 2024, Guilherme Bolincenha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Member", {
	refresh(frm) {
        frm.add_custom_button(__('Add Phone'), () => {
            frm.add_child('phone', {
                phone: ''
            })
            frm.refresh_field('phone');
        })
        frm.change_custom_button_type(__('Add Phone'), null, 'primary');
        frm.add_custom_button(__('Create Membership'), () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            })
        }, __("Actions"))
        frm.add_custom_button(__('Clear Phones'), () => {
            frm.doc.phone.forEach((row) => {
                frappe.model.set_value(row.doctype, row.name, 'phone', '');
            })
        }, __("Actions"))
        frm.add_custom_button(__('Create Transaction'), () => {
            frappe.new_doc('Library Transaction', {
                library_member: frm.doc.name
            })
        }, __("Actions"))
        frm.add_custom_button(__('Set Full Name'), () => {
            frm.set_value('full_name', `${frm.doc.first_name} ${frm.doc.last_name}`)
        }, __("Actions"))
	},
    enable(frm){
        frm.set_value('enabled', 1);
    },
    disable(frm){
        frm.set_value('enabled', 0);
    }
});

frappe.ui.form.on("Library Member Phone", {
	phone(frm, cdt, cdn) {
        // let row = locals[cdt][cdn];
        // console.log(row)
        // row.phone = "";
        // frm.refresh_field('phone');
        frm.call('format_phone')
            .then(r => {
                frm.refresh_field('phone');
            });
	},
});
