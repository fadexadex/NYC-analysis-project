#!/bin/bash
# Simple bash script to import all JSON files to MongoDB using mongoimport

DB_NAME="yellow_taxi_stats"
HOST="localhost"
PORT="27017"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "Importing JSON files to MongoDB..."
echo "Database: $DB_NAME"
echo "Host: $HOST:$PORT"
echo ""

# Check if mongoimport is available
if ! command -v mongoimport &> /dev/null; then
    echo "Error: mongoimport not found. Please install MongoDB Database Tools."
    echo "Or use the Python script instead: python import_to_mongodb.py"
    exit 1
fi

# Import each JSON file
for file in *.json; do
    if [ -f "$file" ]; then
        collection=$(basename "$file" .json)
        echo -e "${YELLOW}Importing $file -> collection: $collection${NC}"
        mongoimport --host "$HOST:$PORT" --db "$DB_NAME" --collection "$collection" --file "$file" --jsonArray --drop
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✓ Successfully imported $file${NC}"
        else
            echo "✗ Failed to import $file"
        fi
        echo ""
    fi
done

echo "Import complete!"
echo ""
echo "To verify, run: mongosh $DB_NAME --eval 'db.getCollectionNames()'"

