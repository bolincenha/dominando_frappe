# Copyright (c) 2024, Guilherme Bolincenha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryMembership(Document):
	# check before submitting this document
	def before_submit(self):
		if frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				# check if the membership's end date is later than this membership's start date
				"to_date": (">", self.from_date),
			},
		):
			frappe.throw("There is an active membership for this member")
