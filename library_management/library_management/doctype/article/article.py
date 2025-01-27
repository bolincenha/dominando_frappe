# Copyright (c) 2024, Guilherme Bolincenha and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe import _

class Article(WebsiteGenerator):
	@frappe.whitelist()
	def get_book_holder(self):
		if self.status != "Issued":
			frappe.throw(_("Article is not issued"))

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
			return None

		if last[0].type != "Issue":
			return None

		if not frappe.db.exists("Library Member", last[0].library_member):
			frappe.throw(_("Library Member not found"))

		return frappe.get_value("Library Member", last[0].library_member, "full_name")