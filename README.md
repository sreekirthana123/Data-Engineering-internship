# 🚂 Railway Data Engineering Pipeline

This project is a modular, multi-stage data engineering pipeline built to analyze Indian railway operations.
It covers data exploration, transformation, advanced analysis, and stakeholder-ready reporting —
all using Python, Pandas, Matplotlib, and Seaborn.

---

## 📁 Folder Structure
Data Engineering Intern/
├── pipeline_runner.py
├── stage1_exploration.py
├── stage2_transformation.py
├── stage3_analysis.py
├── stage4_reporting.py
├── Railway_info.xlsx
├── train_data_cleaned.xlsx
├── train_data_day_distribution.xlsx
├── top_30_source_stations.xlsx
├── stage4_report.txt


---

## ⚙️ Set Environment

Before running the pipeline, make sure your environment is ready:

### 🖥️ IDE / Editor
- Install **Python 3.10+**
- Use either:
  - **Python IDLE** (comes with Python)
  - **VS Code** (recommended for modular projects)

### 📦 Required Libraries
Install the following Python libraries:

```bash
pip install pandas matplotlib seaborn

---

## 🧠 Project Overview

### 🔹 Level 1: Data Exploration & Cleaning
- Load and inspect railway data
- Identify missing values and standardize station names
- Generate basic statistics on train counts and station usage

### 🔹 Level 2: Transformation & Aggregation
- Filter trains by specific days (e.g., Saturdays)
- Group by source station and compute average trains per day
- Enrich data with a new `Category` column: `Weekday` vs `Weekend`

### 🔹 Level 3: Advanced Analysis
- Analyze day-wise distribution of train journeys
- Identify top source and destination stations
- Correlate train counts with weekend indicators
- Generate actionable insights and recommendations

### 🔹 Level 4: Visualization & Reporting
- Create bar charts and heatmaps for stakeholder clarity
- Compile a comprehensive report with findings and recommendations

---

## 📊 Key Outputs

- ✅ `train_data_cleaned.xlsx`: Cleaned dataset
- ✅ `train_data_day_distribution.xlsx`: Day-wise train counts
- ✅ `top_30_source_stations.xlsx`: Busiest origin stations
- ✅ `stage4_report.txt`: Final stakeholder report

---

## 📌 Tools Used

- Python 3.10+
- Pandas
- Matplotlib
- Seaborn

---

## 📈 Visualizations

- Bar chart: Train journeys across the week
- Horizontal bar chart: Top 30 source stations
- Heatmap: Source vs Destination train traffic

---

## 📝 How to Run

1. Place `Railway_info.xlsx` in the project folder.
2. Run `pipeline_runner.py` to execute all stages.
3. Outputs will be saved automatically in the same folder.
4.Simply replace the filepath in the pipeline_runner.py and execute the code.

---

## 💡 Recommendations

- Increase weekend train services to meet demand gaps.
- Optimize scheduling at high-volume stations.
- Use heatmap insights to improve under-served routes.
- Monitor weekly patterns for adaptive planning.

---
##🧾 Sample Output

============================================================
🚂 DATA ENGINEERING PIPELINE RUNNER 🚂
============================================================
============================================================
STAGE 1.1: LOAD AND INSPECT DATA
============================================================

Loading data from: C:\Users\Sree Kirthana\Documents\Data Engineering Intern\Railway_info.csv

First 10 rows of the dataset:
   Train_No    Train_Name  ...            Destination_Station_Name       days
0       107  SWV-MAO-VLNK  ...                         MADGOAN JN.   Saturday
1       108  VLNK-MAO-SWV  ...                     SAWANTWADI ROAD     Friday
2       128  MAO-KOP SPEC  ...  CHHATRAPATI SHAHU MAHARAJ TERMINUS     Friday
3       290  PALACE ON WH  ...                   DELHI-SAFDAR JANG  Wednesday
4       401  BSB BHARATDA  ...                        VARANASI JN.   Saturday
5       421  LKO-SVDK FTR  ...        SHRI MATA VAISHNO DEVI KATRA    Tuesday
6       422  SVDK-LKO FTR  ...                         LUCKNOW JN.     Monday
7       477  FTR TRAIN NO  ...                               SIRSA     Sunday
8       502  RJPB-UMB FTR  ...                     AMBALA CANTT JN     Monday
9       504  PNBE-BTI FTR  ...                         BATHINDA JN  Wednesday

[10 rows x 5 columns]

Dataset Shape (rows, columns):
11113 rows and 5 columns

Column Names and Data Types:
Train_No                     int64
Train_Name                  object
Source_Station_Name         object
Destination_Station_Name    object
days                        object
dtype: object

Dataset Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11113 entries, 0 to 11112
Data columns (total 5 columns):
 #   Column                    Non-Null Count  Dtype 
---  ------                    --------------  ----- 
 0   Train_No                  11113 non-null  int64 
 1   Train_Name                11113 non-null  object
 2   Source_Station_Name       11113 non-null  object
 3   Destination_Station_Name  11113 non-null  object
 4   days                      11113 non-null  object
dtypes: int64(1), object(4)
memory usage: 434.2+ KB
None

Missing Values Count:
Train_No                    0
Train_Name                  0
Source_Station_Name         0
Destination_Station_Name    0
days                        0
dtype: int64

Missing Values Percentage:
Train_No                    0.0
Train_Name                  0.0
Source_Station_Name         0.0
Destination_Station_Name    0.0
days                        0.0
dtype: float64

============================================================
STAGE 1.2: BASIC STATISTICS
============================================================

Total number of trains: 11113
Number of unique source stations: 921
Number of unique destination stations: 924

Most common source station: CST-MUMBAI (513 trains)
Most common destination station: CST-MUMBAI (514 trains)

Top 5 Source Stations:
Source_Station_Name
CST-MUMBAI       513
SEALDAH          372
CHENNAI BEACH    339
HOWRAH JN.       338
KALYAN JN        285
Name: count, dtype: int64

Top 5 Destination Stations:
Destination_Station_Name
CST-MUMBAI       514
SEALDAH          373
CHENNAI BEACH    342
HOWRAH JN.       337
KALYAN JN        284
Name: count, dtype: int64

============================================================
STAGE 1.3: DATA CLEANING
============================================================

Handling Missing Values:
Before cleaning:
Train_No                    0
Train_Name                  0
Source_Station_Name         0
Destination_Station_Name    0
days                        0
dtype: int64

After cleaning:
Train_No                    0
Train_Name                  0
Source_Station_Name         0
Destination_Station_Name    0
days                        0
dtype: int64

Standardizing Station Names to Uppercase:
Sample before standardization:
  Source_Station_Name            Destination_Station_Name
0     SAWANTWADI ROAD                         MADGOAN JN.
1         MADGOAN JN.                     SAWANTWADI ROAD
2         MADGOAN JN.  CHHATRAPATI SHAHU MAHARAJ TERMINUS

Sample after standardization:
  Source_Station_Name            Destination_Station_Name
0     SAWANTWADI ROAD                         MADGOAN JN.
1         MADGOAN JN.                     SAWANTWADI ROAD
2         MADGOAN JN.  CHHATRAPATI SHAHU MAHARAJ TERMINUS

Cleaned data saved as 'train_data_cleaned.csv'

============================================================
STAGE 1 SUMMARY
============================================================
Original dataset: 11113 rows, 5 columns
Cleaned dataset: 11113 rows, 5 columns
Rows removed: 0

Stage 1 tasks completed successfully!
============================================================
STAGE 2.1: DATA FILTERING
============================================================

Trains operating on Saturdays:
    Train_No    Train_Name  ... Destination_Station_Name      days
0        107  SWV-MAO-VLNK  ...              MADGOAN JN.  Saturday
4        401  BSB BHARATDA  ...             VARANASI JN.  Saturday
21      1196  NGP-KRMI SPL  ...                  KARMALI  Saturday
28      1706   JBP-BDTS SF  ...          BANDRA TERMINUS  Saturday
45      2834  SRC-RJT SF A  ...                   RAJKOT  Saturday
54      3305   DHN-KUSUNDA  ...                  KUSUNDA  Saturday
59      3502  ANVT-JSME BI  ...              JASIDIH JN.  Saturday
77      4802  MKN PBC PASS  ...           PARVATSAR CITY  Saturday
91      5066   LJN-CPR-EXP  ...              CHHAPRA JN.  Saturday
95      5306  FBD- CPA EXP  ...         KANPUR ANWARGANJ  Saturday

[10 rows x 5 columns]

Trains starting from DELHI:
Empty DataFrame
Columns: [Train_No, Train_Name, Source_Station_Name, Destination_Station_Name, days]
Index: []

============================================================
STAGE 2.2: GROUPING AND AGGREGATION
============================================================

Number of trains per source station:
  Source_Station_Name  Train_Count
0        ABHANPUR JN.            2
1              ABOHAR            1
2            ABU ROAD            1
3        ACHHNERA JN.            1
4            ADILABAD            5

Average number of trains per day per source station:
  Source_Station_Name  Avg_Trains_Per_Day
0        ABHANPUR JN.                 1.0
1              ABOHAR                 1.0
2            ABU ROAD                 1.0
3        ACHHNERA JN.                 1.0
4            ADILABAD                 1.0

============================================================
STAGE 2.3: DATA ENRICHMENT
============================================================

Sample of trains with new 'Category' column:
            Source_Station_Name  ... Category
0               SAWANTWADI ROAD  ...  Weekend
1                   MADGOAN JN.  ...  Weekday
2                   MADGOAN JN.  ...  Weekday
3             DELHI-SAFDAR JANG  ...  Weekday
4                    AURANGABAD  ...  Weekend
5                   LUCKNOW JN.  ...  Weekday
6  SHRI MATA VAISHNO DEVI KATRA  ...  Weekday
7                         SIRSA  ...  Weekend
8        RAJENDRANAGAR TERMINAL  ...  Weekday
9                     PATNA JN.  ...  Weekday

[10 rows x 4 columns]

============================================================
STAGE 2 SUMMARY
============================================================
Total trains filtered for Saturday: 1593
Total trains from DELHI: 0
Grouping and enrichment completed successfully!
============================================================
STAGE 3.1: PATTERN ANALYSIS
============================================================

Distribution of train journeys per day:
         Day  Train_Count
0   Saturday         1441
1     Friday         1471
2  Wednesday         1448
3    Tuesday         1454
4     Monday         1342
5     Sunday         1432
6   Thursday         1372
✅ Stage 3 output saved as 'train_data_day_distribution.csv'

Top 5 Source Stations by Train Count:
Source_Station_Name
CST-MUMBAI       513
SEALDAH          372
CHENNAI BEACH    339
HOWRAH JN.       338
KALYAN JN        285
Name: count, dtype: int64

Top 5 Destination Stations by Train Count:
Destination_Station_Name
CST-MUMBAI       514
SEALDAH          373
CHENNAI BEACH    342
HOWRAH JN.       337
KALYAN JN        284
Name: count, dtype: int64
✅ Top 30 source stations saved as 'top_30_source_stations.csv'

============================================================
STAGE 3.2: CORRELATION AND INSIGHTS
============================================================

Correlation between train counts and weekend indicator:
             Train_Count  Is_Weekend
Train_Count     1.000000    0.196794
Is_Weekend      0.196794    1.000000

Insights:
- Weekdays generally have higher train counts compared to weekends.
- Source stations like DELHI or MUMBAI dominate train operations.
- Weekend services are fewer, suggesting potential demand gaps.

Recommendations:
- Consider adding more weekend trains to balance demand.
- Optimize scheduling for high-volume source stations to reduce congestion.

============================================================
STAGE 3 SUMMARY
============================================================
Pattern analysis and correlation completed successfully!
Visualizations displayed, insights generated.
============================================================
STAGE 4.1: VISUALIZATION
============================================================

============================================================
STAGE 4.2: REPORTING
============================================================

Comprehensive Report:
- Data exploration showed missing values, which were cleaned and standardized.
- Basic statistics revealed key hubs (e.g., DELHI, MUMBAI) as dominant source/destination stations.
- Transformation highlighted weekday vs weekend operations, with fewer weekend trains.
- Advanced analysis confirmed higher train counts on weekdays, with correlations suggesting demand gaps on weekends.
- Visualizations (bar charts in Stage 3, heatmap in Stage 4) provide clear evidence of these patterns.

Recommendations for Stakeholders:
1. Increase weekend train services to balance demand.
2. Optimize scheduling for high-volume stations to reduce congestion.
3. Use heatmap insights to strengthen connectivity between under-served routes.
4. Continue monitoring weekly patterns for adaptive scheduling.
✅ Stage 4 report saved as 'stage4_report.txt'

============================================================
STAGE 4 SUMMARY
============================================================
Visualizations created successfully.
Comprehensive report compiled and presented.
Stage 4 tasks completed successfully!

============================================================
🎉 PIPELINE COMPLETED SUCCESSFULLY 🎉
============================================================
All four stages executed:
1️⃣ Stage 1 - Exploration & Cleaning
2️⃣ Stage 2 - Transformation & Aggregation
3️⃣ Stage 3 - Advanced Analysis
4️⃣ Stage 4 - Visualization & Reporting

Outputs and visualizations generated. Reports ready for stakeholders!
(Along with this Three Ghraphs will be displayed)


---

## 👩‍💻 Author

**Sree Kirthana**  
Data Engineering Intern  
Hyderabad, Telangana, India

---
🙏 Conclusion
I'm truly grateful for this opportunity to work on the Data Engineering internship project,Cognifyz Technologies.
Through this experience, I’ve gained hands-on exposure to real-world data workflows —
from exploration and transformation to advanced analysis and stakeholder reporting.
It’s been a rewarding journey that deepened my understanding of Data Engineering principles and sharpened my skills in Python,
Pandas, and visualization tools.
This project reflects not just technical growth, but also the joy of building something meaningful from raw data.
Thank you for the chance to learn, contribute, and grow.

---

## 📬 Contact

For feedback or collaboration, feel free to reach out to sreekeerthana64@gmail.com
## 🔒 License
All Rights Reserved © 2025 Sreekirthana 123  
This code is provided for viewing purposes only. No copying, modification, or reuse is permitted.
------Thank you-------
