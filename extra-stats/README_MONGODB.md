# Importing Yellow Taxi Stats to MongoDB

## Quick Start

### Option 1: Using Python Script (Recommended - Easiest)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Make sure MongoDB is running:**
   - If using local MongoDB: `mongod` should be running
   - If using MongoDB Atlas: You'll need connection string (see below)

3. **Run the import script:**
   ```bash
   python import_to_mongodb.py
   ```

   This will:
   - Connect to MongoDB at `localhost:27017`
   - Create/use database `yellow_taxi_stats`
   - Import each JSON file as a separate collection

### Option 2: Using mongoimport (Command Line)

If you have MongoDB tools installed, you can use `mongoimport` directly:

```bash
# For each JSON file (example):
mongoimport --db yellow_taxi_stats --collection cluster_centers --file cluster_centers.json --jsonArray

mongoimport --db yellow_taxi_stats --collection cluster_stats --file cluster_stats.json --jsonArray

mongoimport --db yellow_taxi_stats --collection daily_stats --file daily_stats.json --jsonArray

# ... and so on for each file
```

Or use a loop:
```bash
for file in *.json; do
    collection=$(basename "$file" .json)
    mongoimport --db yellow_taxi_stats --collection "$collection" --file "$file" --jsonArray
done
```

## Custom Connection Options

### Local MongoDB with Authentication
```bash
python import_to_mongodb.py --host localhost --port 27017 --username myuser --password mypass
```

### MongoDB Atlas (Cloud)
```bash
python import_to_mongodb.py --host cluster0.xxxxx.mongodb.net --port 27017 --username myuser --password mypass --database yellow_taxi_stats
```

### Custom Database Name
```bash
python import_to_mongodb.py --database my_custom_db_name
```

## Collections Created

The script will create the following collections (one per JSON file):
- `cluster_centers`
- `cluster_stats`
- `daily_stats`
- `distance_stats`
- `dow_stats`
- `fare_predictions`
- `feature_importance`
- `hourly_demand`
- `model_metrics`
- `monthly_stats`
- `passenger_dist`
- `payment_stats`
- `ratecode_stats`

## Verify Import

After importing, you can verify in MongoDB shell:
```javascript
use yellow_taxi_stats
show collections
db.cluster_centers.countDocuments()
db.daily_stats.findOne()
```

## Troubleshooting

1. **Connection Error**: Make sure MongoDB is running
   ```bash
   # Check if MongoDB is running
   mongosh --eval "db.adminCommand('ping')"
   ```

2. **Permission Error**: Make sure you have write permissions to the database

3. **Large Files**: The script handles large files like `fare_predictions.json` automatically

4. **Duplicate Data**: The script clears existing collections before importing. Remove the `collection.delete_many({})` line if you want to append instead.

