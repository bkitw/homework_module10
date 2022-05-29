from collections import UserDict


class Record:
	def __init__(self, name, phone=None):
		self.name = name
		self.phones = []

		if phone:
			self.add_phone(phone)

	def add_phone(self, phone):
		self.phones.append(phone)

	def update_phone(self, phone, new_phone):
		for i in range(len(self.phones)):
			if self.phones[i].value == phone.value:
				self.phones[i] = new_phone

	def delete_phone(self, phone):
		for i in range(len(self.phones)):
			if self.phones[i].value == phone.value:
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


print("Проверки записей в классе Record:")
name_1 = Name('Жданов Андрей Павлович')
phone_1 = Phone('+7 (921) 123-45-67')
rec = Record(name_1, phone_1)
rec.update_phone(phone_1, Phone('+38 (098) 123-45-67'))
rec.add_phone(Phone('+93 (799) 920-00-00'))
print(rec.name.value)
print(rec.phones[0].value)
print(rec.phones[1].value)
...
print("-" * 20)
...
print("Проверки записей в классе AddressBook:")
address_book_1 = AddressBook()
address_book_1.add_record(rec)
print(address_book_1.data)
for i in address_book_1.data['Жданов Андрей Павлович'].phones:
	print(i.value)
for j in address_book_1.data:
	print(j)
...
print("-" * 20)
...
print("Проверки записей в классе AddressBook после добавления второй записи:")
name_2 = Name('Дукалис Анатолий Валентинович')
phone_2 = Phone('+380 (93) 123-45-67')
rec_2 = Record(name_2, phone_2)
rec_2.add_phone(Phone('+380 (96) 123-00-67'))
address_book_1.add_record(rec_2)
print(address_book_1.data)
for i in address_book_1.data['Дукалис Анатолий Валентинович'].phones:
	print(i.value)
for j in address_book_1.data:
	print(j)
