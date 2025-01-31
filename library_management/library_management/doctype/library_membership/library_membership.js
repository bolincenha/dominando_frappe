// Copyright (c) 2024, Guilherme Bolincenha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Membership", {
	from_date(frm) {
        if(frm.doc.from_date){
            frm.call('set_membership_period')
                .then(r => {
                    frm.refresh_field('to_date');
                });
        }
	},
});
