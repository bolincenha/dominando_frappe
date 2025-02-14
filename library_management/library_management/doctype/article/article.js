// Copyright (c) 2024, Guilherme Bolincenha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Article", {
	refresh(frm) {
        if (frm.is_new()) {
            if (!frm.doc.description) {
                frm.set_intro('Please set the value of description', 'blue');
            }
        }
	},
});
