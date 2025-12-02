#!/usr/bin/env python3
"""
Script to import all JSON files from the yellow-taxi-stree-stats directory into MongoDB.
Each JSON file will be imported as a separate collection.

Usage:
    python import_to_mongodb.py
"""

import json
from pathlib import Path
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# ============================================================================
# CONFIGURATION - Edit these values
# ============================================================================
# MongoDB Atlas connection string
# Format: mongodb+srv://username:password@cluster.mongodb.net/
MONGO_CONNECTION_STRING = "mongodb+srv://fadehandaniel2006:J5Eo957IeSwn49fR@cluster0.dobfa6u.mongodb.net/"

# Database name
DATABASE_NAME = "yellow_taxi_stats"

# Directory containing JSON files (default: current directory)
JSON_DIRECTORY = "."
# ============================================================================


def import_json_file(client, db_name, file_path):
    """Import a single JSON file into MongoDB."""
    collection_name = Path(file_path).stem  # Get filename without extension
    
    print(f"Importing {file_path} into collection '{collection_name}'...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        db = client[db_name]
        collection = db[collection_name]
        
        # Clear existing data (optional - remove if you want to append)
        collection.delete_many({})
        
        # Insert data
        if isinstance(data, list):
            # If it's a list, insert many documents
            if data:  # Only insert if list is not empty
                result = collection.insert_many(data)
                print(f"  ✓ Inserted {len(result.inserted_ids)} documents")
            else:
                print(f"  ⚠ File is empty, skipping...")
        elif isinstance(data, dict):
            # If it's a single object, insert one document
            result = collection.insert_one(data)
            print(f"  ✓ Inserted 1 document")
        else:
            print(f"  ⚠ Unexpected data type: {type(data)}, skipping...")
            
    except json.JSONDecodeError as e:
        print(f"  ✗ Error parsing JSON: {e}")
    except Exception as e:
        print(f"  ✗ Error importing file: {e}")


def main():
    # Connect to MongoDB
    print("Connecting to MongoDB...")
    try:
        client = MongoClient(MONGO_CONNECTION_STRING)
        # Test connection
        client.admin.command('ping')
        print(f"✓ Connected to MongoDB")
        print(f"✓ Using database: {DATABASE_NAME}\n")
        
    except ConnectionFailure as e:
        print(f"✗ Failed to connect to MongoDB")
        print(f"  Error: {e}")
        print("  Make sure MongoDB is running and the connection details are correct.")
        print(f"  Connection string: {MONGO_CONNECTION_STRING.split('@')[0]}@...")
        return
    except Exception as e:
        print(f"✗ Connection error: {e}")
        print("  Please check your connection string and credentials.")
        return
    
    # Find all JSON files in the directory
    directory = Path(JSON_DIRECTORY)
    json_files = list(directory.glob('*.json'))
    
    if not json_files:
        print(f"✗ No JSON files found in {directory.absolute()}")
        return
    
    print(f"Found {len(json_files)} JSON file(s) to import:\n")
    
    # Import each file
    for json_file in sorted(json_files):
        import_json_file(client, DATABASE_NAME, json_file)
    
    print(f"\n✓ Import complete!")
    print(f"\nCollections created in database '{DATABASE_NAME}':")
    db = client[DATABASE_NAME]
    for collection_name in sorted(db.list_collection_names()):
        count = db[collection_name].count_documents({})
        print(f"  - {collection_name}: {count} documents")
    
    client.close()


if __name__ == '__main__':
    main()

