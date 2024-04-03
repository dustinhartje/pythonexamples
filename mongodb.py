# Copied directly from ChatGPT3.5 results using the following prompt:
# Write a python script to interact with MongoDB Atlas in AWS.  It should
# include functions to create a database, crud records that are created from
# complex python class instances, search for patterns, and remove the database

from pymongo import MongoClient
import re
import json

class MongoDBAtlas:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = None

    def connect_to_database(self, database_name):
        self.db = self.client[database_name]

    def create_record(self, collection_name, instance):
        if not self.db:
            raise Exception("Please connect to a database first.")

        collection = self.db[collection_name]
        record = instance.__dict__
        result = collection.insert_one(record)
        return result.inserted_id

    def read_record(self, collection_name, query_class, query):
        if not self.db:
            raise Exception("Please connect to a database first.")

        collection = self.db[collection_name]
        document = collection.find_one(query)
        if document:
            return query_class(**document)

    def update_record(self, collection_name, query, new_values):
        if not self.db:
            raise Exception("Please connect to a database first.")

        collection = self.db[collection_name]
        result = collection.update_one(query, {"$set": new_values})
        return result.modified_count

    def delete_record(self, collection_name, query):
        if not self.db:
            raise Exception("Please connect to a database first.")

        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count

    def search_records(self, collection_name, pattern, query_class):
        if not self.db:
            raise Exception("Please connect to a database first.")

        collection = self.db[collection_name]
        regex = re.compile(pattern, re.IGNORECASE)
        documents = collection.find({"$or": [{"name": regex}, {"description": regex}]})
        return [query_class(**doc) for doc in documents]

    def drop_database(self, database_name):
        self.client.drop_database(database_name)


# Example usage:

class Person:
    def __init__(self, name, age, description):
        self.name = name
        self.age = age
        self.description = description

if __name__ == "__main__":
    # Replace '<connection_string>' with your MongoDB Atlas connection string
    connection_string = "<connection_string>"
    mongo_client = MongoDBAtlas(connection_string)

    # Connect to the database
    mongo_client.connect_to_database("test_database")

    # Create a record
    person_instance = Person("John", 30, "Engineer")
    record_id = mongo_client.create_record("test_collection", person_instance)
    print("Inserted record ID:", record_id)

    # Read a record
    retrieved_record = mongo_client.read_record("test_collection", Person, {"name": "John"})
    print("Retrieved record:", json.dumps(retrieved_record.__dict__, indent=4))

    # Update a record
    update_result = mongo_client.update_record("test_collection", {"name": "John"}, {"age": 35})
    print("Updated", update_result, "record(s).")

    # Search for records
    search_results = mongo_client.search_records("test_collection", "engineer", Person)
    print("Search results:", [json.dumps(record.__dict__, indent=4) for record in search_results])

    # Delete a record
    delete_result = mongo_client.delete_record("test_collection", {"name": "John"})
    print("Deleted", delete_result, "record(s).")

    # Drop the database
    mongo_client.drop_database("test_database")