from collections import UserDict


class Record:
	def __init__(self, name):
		self.name = Name(name)
		self.phones = []

	def add_phone(self, phone):
		ph_num = Phone(phone)
		self.phones.append(ph_num)

	def update_phone(self, phone, new_phone):
		for i in range(len(self.phones)):
			new_ph_num = Phone(new_phone)
			if self.phones[i].value == phone:
				self.phones[i] = new_ph_num

	def delete_phone(self, phone):
		for i in range(len(self.phones)):
			if self.phones[i].value == phone:
				del self.phones[i]
				break


class Field:
	def __init__(self, value):
		self.value = value


class Name(Field):
	pass


class Phone(Field):
	pass


class AddressBook(UserDict):
	def add_record(self, record: Record):
		self.data[record.name.value] = record



