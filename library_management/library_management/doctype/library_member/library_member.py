# Copyright (c) 2024, Guilherme Bolincenha and contributors
# For license information, please see license.txt

import frappe
import re
from frappe.model.document import Document
from frappe import _

class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'

	@frappe.whitelist()
	def format_phone(self):
		for phone in self.phone:
			phone.phone = self.format_phone_number(phone.phone)
	
	def format_phone_number(self, phone_number: str) -> str:
		match = re.match(r'(\+\d{2})(\d{2})(\d{4,5})(\d{4})$', phone_number)
		
		if match:
			country_code, area_code, first_part, second_part = match.groups()
			
			if len(first_part) == 5:
				return f"{country_code} ({area_code}) {first_part}-{second_part}"
			else:
				return f"{country_code} ({area_code}) {first_part}-{second_part}"
		else:
			frappe.throw(_("Invalid phone number"))
