frappe.listview_settings['Article'] = {
    hide_name_column: true, // hide the last column which shows the `name`
    hide_name_filter: true, // hide the default filter field for the name column
    get_indicator(doc) {
        // customize indicator color
        if (doc.status === "Available") {
            return [__("Available"), "green", "status,=,Available"];
        } else {
            return [__("Issued"), "red", "status,=,Issued"];
        }
    },
}