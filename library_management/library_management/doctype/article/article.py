# Copyright (c) 2024, Guilherme Bolincenha and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe import _

class Article(WebsiteGenerator):
	@property
	def book_holder(self):
		if self.status != "Issued" and not self.is_new():
			return ""

		last = frappe.get_all("Library Transaction",
			filters={
				"article": self.name,
				"docstatus": 1
			},
			fields=["type", "library_member"],
			order_by="creation desc",
			limit=1,
		)
		if not last:
			return ""

		if last[0].type != "Issue":
			return ""

		if not frappe.db.exists("Library Member", last[0].library_member):
			frappe.throw(_("Library Member not found"))

		return frappe.get_value("Library Member", last[0].library_member, "full_name")