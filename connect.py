import pymongo

from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "your database url"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']


dbname = get_database()
collection_name = dbname["user_1_items"]
item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}
item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}
collection_name.insert_many([item_1,item_2])

dbname = get_database()
 
# Create a new collection
collection_name = dbname["user_1_items"]
 
item_details = collection_name.find()
for item in item_details:
   # This does not give a very readable output
   print(item)
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
    