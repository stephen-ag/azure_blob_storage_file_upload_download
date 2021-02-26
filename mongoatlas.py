import pymongo

client = pymongo.MongoClient("mongodb+srv://stephen-ag:stephen1@cluster0.tpqna.mongodb.net/Projectdb?retryWrites=true&w=majority")

db = client.get_database('Projectdb')

records = db.new1_db

a=records.count_documents({})
print(a)
