// Copyright (c) 2024, Guilherme Bolincenha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Membership", {
	setup(frm) {
        frm.set_query("library_member", function() {
            return {
                filters: {
                    "enabled": 1,
                }
            };
        });
	},
	from_date(frm) {
        if(frm.doc.from_date){
            frm.call('set_membership_period')
                .then(r => {
                    frm.refresh_field('to_date');
                });
        }
	},
});
