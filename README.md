# NYC Yellow Taxi Analytics Dashboard

**End-to-End Big Data Pipeline Using Apache Spark, MongoDB, and Python Dash**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.14+-informational?style=flat&logo=plotly)](https://dash.plotly.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?style=flat&logo=mongodb)](https://www.mongodb.com/)

> A comprehensive big data analytics project demonstrating the full data engineering pipeline from raw data ingestion to interactive visualization.

---

## Table of Contents

- [Overview](#overview)
- [Team Members](#team-members)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Dataset](#dataset)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Analytics & Insights](#analytics--insights)

---

## Overview

This project showcases a complete **big data analytics pipeline** built for analyzing over **46 million NYC Yellow Taxi trip records**. The system processes large-scale datasets using **Apache Spark**, stores aggregated insights in **MongoDB Atlas**, and presents interactive visualizations through a modern **Python Dash** dashboard.

**Course:** DTS 301 – Big Data Computing
**Institution:** [Your Institution]
**Lecturer:** Mrs Joceline
**Group:** 19
**Date:** December 10th, 2025

### Key Objectives

- Demonstrate end-to-end ETL pipeline design
- Process and analyze 7GB+ of taxi trip data
- Implement distributed computing with Apache Spark
- Build scalable NoSQL storage with MongoDB
- Create interactive data visualizations
- Deploy production-ready analytics dashboard

---

## Team Members

| Name | Role | Responsibilities |
|------|------|------------------|
| **Ojerinde Oluwasemilore** | Project Manager | Project planning, coordination, timeline management |
| **Mbata Caleb Isaac** | Presentation Lead | Presentation slides development |
| **Olawale-Ojo Iremide** | Presentation Team | Presentation content creation |
| **Johnson Michael Moyosore** | QA Engineer | Quality assurance, testing, editing |
| **Ayodele-Peters Charles** | QA & Presentation | Testing, quality assurance, presentation support |
| **Oyeniyi Adejoro Daniel** | Presentation Team | Presentation slides design |
| **Matti Titilolaoluwa** | Project Coordinator | Project management and team coordination |
| **Daniel Fadehan** | Data Engineer | Data pipeline development, Spark processing, MongoDB integration |
| **Awotunde Kayode** | Frontend Developer | Dashboard UI/UX design and implementation |
| **Refo Shalom** | Frontend Developer | Dashboard component development |

---

## Features

### Real-Time Analytics
- **Interactive Dashboard**: Modern, responsive UI with smooth animations
- **Multi-View Analytics**: 10+ different analytical perspectives
- **Real-time Updates**: Dynamic data fetching from MongoDB

### Comprehensive Metrics
- **Hourly Demand Patterns**: Trip distribution across 24-hour cycles
- **Day-of-Week Analysis**: Weekly trends and patterns
- **Monthly Trends**: Long-term performance tracking
- **Payment Analytics**: Payment method distribution and tipping behavior
- **Distance Analysis**: Trip categorization by distance ranges
- **Passenger Distribution**: Occupancy patterns and fare analysis
- **Rate Code Insights**: Fare type distribution and pricing

### Machine Learning Insights
- **Fare Prediction Model**: Random Forest regression (R² = 0.92, RMSE = $2.82)
- **Route Clustering**: K-Means clustering of popular pickup/dropoff locations
- **Feature Importance Analysis**: Key factors affecting fare amounts

### Technical Features
- **Modular Architecture**: Clean component-based structure
- **Responsive Design**: Mobile-first, works on all screen sizes
- **Performance Optimized**: Efficient data loading and caching
- **Modern UI/UX**: Material Design inspired with custom animations

---

## Technology Stack

### Data Processing
- **Apache Spark 3.x**: Distributed data processing (PySpark)
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

### Database & Storage
- **MongoDB Atlas**: Cloud-hosted NoSQL database
- **PyMongo**: MongoDB Python driver

### Web Framework & Visualization
- **Python Dash 2.14+**: Interactive web application framework
- **Plotly 5.18+**: Advanced charting and visualization
- **Dash Bootstrap Components**: Responsive UI components
- **Dash Iconify**: Modern icon system (Lucide icons)

### Deployment & Infrastructure
- **Railway**: Cloud deployment platform
- **Gunicorn**: Production WSGI server
- **Python-dotenv**: Environment variable management

### Development Tools
- **Jupyter Notebook**: Data exploration and pipeline development
- **Git & GitHub**: Version control and collaboration

---

## System Architecture

```
┌─────────────────┐
│   Raw Dataset   │  NYC Taxi Trip Data (7GB, 46M+ records)
│   (CSV Files)   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────────────────┐
│              Apache Spark (PySpark)                 │
│  ┌───────────────────────────────────────────────┐  │
│  │  • Data Extraction (Read CSV)                 │  │
│  │  • Data Cleaning & Validation                 │  │
│  │  • Feature Engineering                        │  │
│  │  • Aggregations & Statistics                  │  │
│  │  • Machine Learning (Random Forest, K-Means)  │  │
│  └───────────────────────────────────────────────┘  │
└────────┬────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────┐
│              MongoDB Atlas (Cloud)                  │
│  ┌───────────────────────────────────────────────┐  │
│  │  Collections:                                 │  │
│  │  • hourly_demand      • dow_stats            │  │
│  │  • monthly_stats      • daily_stats          │  │
│  │  • payment_stats      • passenger_dist       │  │
│  │  • distance_stats     • cluster_stats        │  │
│  │  • feature_importance • ratecode_stats       │  │
│  └───────────────────────────────────────────────┘  │
└────────┬────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────┐
│           Python Dash Application                   │
│  ┌───────────────────────────────────────────────┐  │
│  │  • Interactive Sidebar Navigation            │  │
│  │  • Dynamic Chart Generation                  │  │
│  │  • Statistics Cards with Trends              │  │
│  │  • Responsive Grid Layout                    │  │
│  │  • Custom Animations & Theming               │  │
│  └───────────────────────────────────────────────┘  │
└────────┬────────────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│   End Users     │  Browser-based Interactive Dashboard
│  (Web Browser)  │
└─────────────────┘
```

### ETL Pipeline Flow

1. **Extract**: Spark reads 46M+ records from CSV files (yellow_tripdata_2015-01.csv, 2016-01/02/03.csv)
2. **Transform**:
   - Data type conversion and validation
   - Outlier removal and data cleaning
   - Feature engineering (trip duration, speed, tip percentage)
   - Temporal features (hour, day, month, year)
   - Statistical aggregations
   - Machine learning model training
3. **Load**: Processed data exported to MongoDB collections via Spark-MongoDB connector

---

## Dataset

**Source**: [NYC Yellow Taxi Trip Data](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data)

### Dataset Statistics
- **Total Records**: 47,248,845 trips
- **After Cleaning**: 46,873,693 trips (99.21% retention)
- **Size**: ~7GB (raw CSV)
- **Time Period**: January 2015 - March 2016
- **Columns**: 19 attributes per trip

### Key Attributes
| Column | Type | Description |
|--------|------|-------------|
| `tpep_pickup_datetime` | Timestamp | Trip start date and time |
| `tpep_dropoff_datetime` | Timestamp | Trip end date and time |
| `passenger_count` | Integer | Number of passengers (1-8) |
| `trip_distance` | Float | Trip distance in miles |
| `pickup_latitude/longitude` | Float | Pickup GPS coordinates |
| `dropoff_latitude/longitude` | Float | Dropoff GPS coordinates |
| `RateCodeID` | Integer | Rate type (standard, JFK, Newark, etc.) |
| `payment_type` | Integer | Payment method (1=Credit, 2=Cash, etc.) |
| `fare_amount` | Float | Base fare in USD |
| `tip_amount` | Float | Tip amount in USD |
| `total_amount` | Float | Total charge in USD |

### Data Quality
- **Cleaning Retention Rate**: 99.21%
- **Removed Records**: Invalid coordinates, negative fares, outlier distances
- **Date Range**: 2015-01-01 to 2016-03-31 (15 months)
- **Average Fare**: $12.33
- **Average Distance**: 2.89 miles

---

## Installation

### Prerequisites
- Python 3.10 or higher
- MongoDB Atlas account (or local MongoDB instance)
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/fadexadex/NYC-analysis-project.git
cd NYC-analysis-project
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the project root:
```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME=yellow_taxi_stats
```

5. **Import data to MongoDB** (if needed)
```bash
cd extra-stats
chmod +x import_to_mongodb.sh
./import_to_mongodb.sh
```

6. **Run the dashboard**
```bash
python dashboard.py
```

7. **Access the dashboard**
Open your browser and navigate to: `http://localhost:8050`

---

## Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `MONGO_URI` | MongoDB connection string | `mongodb+srv://user:pass@cluster.mongodb.net/` |
| `DB_NAME` | Database name | `yellow_taxi_stats` |

### MongoDB Collections

The following collections are expected in your MongoDB database:

- `hourly_demand` - Trip statistics by hour (0-23)
- `dow_stats` - Day of week patterns (Monday-Sunday)
- `monthly_stats` - Monthly aggregations
- `daily_stats` - Daily trip statistics
- `payment_stats` - Payment method analysis
- `passenger_dist` - Passenger count distribution
- `distance_stats` - Distance category analysis
- `cluster_stats` - Route clustering results
- `feature_importance` - ML feature importance scores
- `ratecode_stats` - Rate code distribution

---

## Usage

### Navigation

The sidebar provides access to 10 analytical views:

1. **Hourly Demand**: Trip patterns across 24-hour periods
2. **Day Stats**: Weekly distribution (Monday-Sunday)
3. **Monthly Trends**: Long-term performance tracking
4. **Daily Stats**: Day-by-day trip analysis
5. **Payments**: Payment method distribution and tipping
6. **Passengers**: Occupancy analysis
7. **Distances**: Trip categorization by distance
8. **Clusters**: ML-based route clustering
9. **Features**: Model feature importance
10. **Rate Codes**: Fare type distribution

### Interactive Features

- **Click** on sidebar items to switch between views
- **Hover** over charts for detailed tooltips
- **Responsive** layout adapts to screen size
- **Animated** transitions for smooth UX

---
## Project Structure

```
NYC-analysis-project/
│
├── dashboard.py                 # Main Dash application
├── requirements.txt             # Python dependencies
├── Procfile                     # Railway deployment config
├── .env                         # Environment variables (not in repo)
├── DEPLOYMENT_GUIDE.md          # PythonAnywhere deployment guide
├── README.md                    # This file
│
├── components/                  # Modular UI components
│   ├── __init__.py
│   ├── sidebar.py              # Navigation sidebar
│   ├── cards.py                # Stat & chart card components
│   └── charts.py               # Chart creation utilities
│
├── assets/                      # Static assets (CSS)
│   ├── styles.css              # Main stylesheet
│   ├── animations.css          # Animation definitions
│   └── responsive.css          # Responsive breakpoints
│
├── extra-stats/                 # MongoDB import scripts & data
│   ├── import_to_mongodb.py    # Data import script
│   ├── import_to_mongodb.sh    # Bash import wrapper
│   ├── JSON_FILES_SUMMARY.md   # Data schema documentation
│   ├── README_MONGODB.md       # MongoDB setup guide
│   └── *.json                  # Pre-aggregated statistics
│       ├── hourly_demand.json
│       ├── dow_stats.json
│       ├── monthly_stats.json
│       ├── daily_stats.json
│       ├── payment_stats.json
│       ├── passenger_dist.json
│       ├── distance_stats.json
│       ├── cluster_stats.json
│       ├── cluster_centers.json
│       ├── feature_importance.json
│       ├── fare_predictions.json
│       ├── model_metrics.json
│       └── ratecode_stats.json
│
└── data-extraction-notebook.ipynb  # Spark ETL pipeline notebook
```

### Key Files

- **dashboard.py**: Core application logic, callbacks, and layout
- **components/**: Reusable UI components (sidebar, cards, charts)
- **assets/**: Custom CSS for styling and animations
- **extra-stats/**: Pre-processed JSON data and MongoDB import tools
- **data-extraction-notebook.ipynb**: Complete Spark data processing pipeline

---

## Analytics & Insights

### Machine Learning Models

#### 1. Fare Prediction (Random Forest Regression)
- **Algorithm**: Random Forest with 30 trees, max depth 10
- **Features**: trip_distance, passenger_count, pickup_hour, pickup_day, RateCodeID
- **Performance**:
  - R² Score: **0.9235** (92.35% variance explained)
  - RMSE: **$2.82**
  - MAE: **$1.53**

#### 2. Route Clustering (K-Means)
- **Algorithm**: K-Means clustering (k=10)
- **Features**: pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude
- **Purpose**: Identify popular route patterns and geographic hotspots

### Key Statistics

- **Total Trips Processed**: 46,873,693
- **Average Fare**: $12.33
- **Average Distance**: 2.89 miles
- **Peak Hour**: 6-7 PM
- **Busiest Day**: Friday
- **Most Common Payment**: Credit Card (70%+)
- **Average Passengers**: 1.6 per trip

---

<div align="center">
Made with ❤️ by Group 19 | Powered by Apache Spark, MongoDB & Python Dash
</div>
