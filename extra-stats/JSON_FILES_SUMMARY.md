# JSON Files Structure Summary

This document provides an overview of the structure and shape of each JSON file in the yellow-taxi-stree-stats directory.

## 1. ratecode_stats.json
**Type:** Array of objects  
**Structure:** Array containing statistics grouped by rate code ID
- `RateCodeID` (integer): Rate code identifier
- `trip_count` (integer): Number of trips for this rate code
- `avg_fare` (float): Average fare amount
- `avg_distance` (float): Average trip distance

**Example entries:** 7 objects (RateCodeIDs: 1, 2, 3, 4, 5, 6, 99)

---

## 2. payment_stats.json
**Type:** Array of objects  
**Structure:** Array containing statistics grouped by payment type
- `payment_type` (integer): Payment type identifier
- `trip_count` (integer): Number of trips for this payment type
- `avg_fare` (float): Average fare amount
- `avg_tip` (float): Average tip amount
- `avg_tip_percent` (float): Average tip percentage

**Example entries:** 5 objects (payment types: 1, 2, 3, 4, 5)

---

## 3. passenger_dist.json
**Type:** Array of objects  
**Structure:** Array containing statistics grouped by passenger count
- `passenger_count` (integer): Number of passengers (1-8)
- `trip_count` (integer): Number of trips with this passenger count
- `avg_fare` (float): Average fare amount
- `avg_tip_percent` (float): Average tip percentage

**Example entries:** 8 objects (passenger counts: 1-8)

---

## 4. monthly_stats.json
**Type:** Array of objects  
**Structure:** Array containing monthly aggregated statistics
- `pickup_year` (integer): Year of pickup
- `pickup_month` (integer): Month of pickup (1-12)
- `trip_count` (integer): Number of trips in this month
- `avg_fare` (float): Average fare amount
- `total_revenue` (float): Total revenue for the month

**Example entries:** 4 objects (covering 2015-01, 2016-01, 2016-02, 2016-03)

---

## 5. model_metrics.json
**Type:** Object (nested structure)  
**Structure:** Contains machine learning model metrics and data summary
- `random_forest` (object):
  - `rmse` (float): Root Mean Squared Error
  - `r2` (float): R-squared score
  - `mae` (float): Mean Absolute Error
  - `num_trees` (integer): Number of trees in the model
  - `max_depth` (integer): Maximum depth of trees
- `kmeans` (object):
  - `num_clusters` (integer): Number of clusters
  - `total_trips_analyzed` (integer): Total trips used for clustering
- `data_summary` (object):
  - `total_records_raw` (integer): Total raw records
  - `total_records_cleaned` (integer): Total records after cleaning
  - `cleaning_retention_rate` (string): Percentage of records retained
  - `date_range_start` (string): Start date (YYYY-MM-DD)
  - `date_range_end` (string): End date (YYYY-MM-DD)
- `feature_importance` (array): Array of objects with:
  - `feature` (string): Feature name
  - `importance` (float): Importance score

---

## 6. hourly_demand.json
**Type:** Array of objects  
**Structure:** Array containing statistics for each hour of the day (0-23)
- `pickup_hour` (integer): Hour of day (0-23)
- `trip_count` (integer): Number of trips in this hour
- `avg_fare` (float): Average fare amount
- `avg_distance` (float): Average trip distance
- `avg_passengers` (float): Average number of passengers
- `total_revenue` (float): Total revenue for this hour

**Example entries:** 24 objects (one for each hour 0-23)

---

## 7. feature_importance.json
**Type:** Array of objects  
**Structure:** Array containing feature importance scores from the model
- `feature` (string): Name of the feature
- `importance` (float): Importance score (0-1)

**Example entries:** 5 objects (features: trip_distance, RateCodeID, pickup_hour, pickup_day, passenger_count)

---

## 8. fare_predictions.json
**Type:** Array of objects  
**Structure:** Array containing fare predictions with actual and predicted values
- `fare_amount` (float): Actual fare amount
- `prediction` (float): Predicted fare amount from the model
- `trip_distance` (float): Distance of the trip
- `passenger_count` (integer): Number of passengers
- `pickup_hour` (integer): Hour of pickup (0-23)
- `pickup_day` (integer): Day of week (1-7, where 1=Monday)

**Size:** ~80,000 records (1.5MB file)

---

## 9. dow_stats.json
**Type:** Array of objects  
**Structure:** Array containing statistics grouped by day of week
- `pickup_day` (integer): Day of week (1-7, where 1=Monday, 7=Sunday)
- `trip_count` (integer): Number of trips on this day
- `avg_fare` (float): Average fare amount
- `avg_distance` (float): Average trip distance
- `avg_tip_percent` (float): Average tip percentage
- `total_revenue` (float): Total revenue for this day of week

**Example entries:** 7 objects (one for each day of the week)

---

## 10. distance_stats.json
**Type:** Array of objects  
**Structure:** Array containing statistics grouped by distance categories
- `distance_category` (string): Distance range category (e.g., "0-2 miles", "2-5 miles", "5-10 miles", "10-20 miles", "20+ miles")
- `trip_count` (integer): Number of trips in this category
- `avg_fare` (float): Average fare amount
- `avg_duration` (float): Average trip duration

**Example entries:** 5 objects (one for each distance category)

---

## 11. cluster_stats.json
**Type:** Array of objects  
**Structure:** Array containing statistics for each K-means cluster
- `cluster_id` (integer): Cluster identifier (0-9)
- `trip_count` (integer): Number of trips in this cluster
- `avg_fare` (float): Average fare amount
- `avg_distance` (float): Average trip distance

**Example entries:** 10 objects (clusters 0-9)

---

## 12. cluster_centers.json
**Type:** Array of objects  
**Structure:** Array containing the center coordinates for each K-means cluster
- `pickup_latitude` (float): Latitude of cluster center pickup location
- `pickup_longitude` (float): Longitude of cluster center pickup location
- `dropoff_latitude` (float): Latitude of cluster center dropoff location
- `dropoff_longitude` (float): Longitude of cluster center dropoff location
- `cluster_id` (integer): Cluster identifier (0-9)

**Example entries:** 10 objects (clusters 0-9)

---

## 13. daily_stats.json
**Type:** Array of objects  
**Structure:** Array containing daily aggregated statistics for each date
- `pickup_date` (string): Date in YYYY-MM-DD format
- `pickup_year` (integer): Year of pickup
- `pickup_month` (integer): Month of pickup (1-12)
- `trip_count` (integer): Number of trips on this date
- `avg_fare` (float): Average fare amount
- `avg_distance` (float): Average trip distance
- `avg_duration` (float): Average trip duration
- `total_revenue` (float): Total revenue for this date
- `avg_passengers` (float): Average number of passengers
- `avg_tip_percent` (float): Average tip percentage
- `max_fare` (float): Maximum fare amount
- `min_fare` (float): Minimum fare amount

**Size:** ~450 records (covering dates from 2015-01-01 to 2016-03-31)

---

## Summary by Data Type

- **Time-based aggregations:** `hourly_demand.json`, `dow_stats.json`, `monthly_stats.json`, `daily_stats.json`
- **Categorical aggregations:** `ratecode_stats.json`, `payment_stats.json`, `passenger_dist.json`, `distance_stats.json`
- **Machine learning outputs:** `model_metrics.json`, `feature_importance.json`, `fare_predictions.json`
- **Clustering outputs:** `cluster_stats.json`, `cluster_centers.json`

