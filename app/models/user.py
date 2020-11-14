from app.models import users

def find(filter = {}):
	return list(users.find(filter))

def find_one(filter = {}):
	return users.find_one(filter)
