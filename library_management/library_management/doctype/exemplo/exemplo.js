// Copyright (c) 2025, Guilherme Bolincenha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Exemplo", {
	refresh(frm) {
        frm.add_custom_button(__('Set Title Reqd'), () => {
            frm.set_df_property('title', 'reqd', 1)
        }, __("Actions"))
        frm.add_custom_button(__('Set Status Read Only'), () => {
            frm.set_df_property('status', 'read_only', 1)
        }, __("Actions"))
        frm.set_df_property('status', 'options', ['Open', 'Closed']);
        // 0 = desabilitado e 1 = habilitado
        frm.toggle_enable('status', frm.doc.status ? 0 : 1);
	},
});
