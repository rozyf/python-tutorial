from pymongo import MongoClient

mongo_uri = 'mongodb+srv://bajigur-cloth:1234@bajigur-cloth.x1nyx.mongodb.net/<dbname>?retryWrites=true&w=majority'

client = MongoClient(mongo_uri)
db = client['bajigur-cloth']
users = db['users']