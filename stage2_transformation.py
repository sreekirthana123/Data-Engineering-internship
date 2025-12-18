import pandas as pd

def run_stage2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Stage 2: Data Transformation and Aggregation
    - Task 2.1: Data Filtering
    - Task 2.2: Grouping and Aggregation
    - Task 2.3: Data Enrichment
    """

    # ============================================
    # TASK 2.1: DATA FILTERING
    # ============================================
    print("=" * 60)
    print("STAGE 2.1: DATA FILTERING")
    print("=" * 60)

    # Example: filter trains that operate on Saturdays
    saturday_trains = df[df['days'].str.contains("Saturday", case=False, na=False)]
    print("\nTrains operating on Saturdays:")
    print(saturday_trains.head(10))

    # Example: extract trains starting from a specific station (e.g., DELHI)
    specific_station = "DELHI"
    trains_from_station = df[df['Source_Station_Name'] == specific_station]
    print(f"\nTrains starting from {specific_station}:")
    print(trains_from_station.head(10))

    # ============================================
    # TASK 2.2: GROUPING AND AGGREGATION
    # ============================================
    print("\n" + "=" * 60)
    print("STAGE 2.2: GROUPING AND AGGREGATION")
    print("=" * 60)

    # Group by source station and count trains
    trains_per_source = df.groupby('Source_Station_Name').size().reset_index(name='Train_Count')
    print("\nNumber of trains per source station:")
    print(trains_per_source.head())

    # Average number of trains per day for each source station
    # Assuming 'Days' column contains comma-separated days like "Mon,Tue,Wed"
    df['days_Count'] = df['days'].apply(lambda x: len(str(x).split(',')))
    avg_trains_per_day = df.groupby('Source_Station_Name')['days_Count'].mean().reset_index(name='Avg_Trains_Per_Day')
    print("\nAverage number of trains per day per source station:")
    print(avg_trains_per_day.head())

    # ============================================
    # TASK 2.3: DATA ENRICHMENT
    # ============================================
    print("\n" + "=" * 60)
    print("STAGE 2.3: DATA ENRICHMENT")
    print("=" * 60)

    # Categorize trains based on operating days
    def categorize_days(days: str) -> str:
        if pd.isna(days):
            return "Unknown"
        days_list = [d.strip().lower() for d in days.split(',')]
        if any(d in ['saturday', 'sunday'] for d in days_list):
            return "Weekend"
        return "Weekday"

    df['Category'] = df['days'].apply(categorize_days)

    print("\nSample of trains with new 'Category' column:")
    print(df[['Source_Station_Name', 'Destination_Station_Name', 'days', 'Category']].head(10))

    # ============================================
    # SUMMARY
    # ============================================
    print("\n" + "=" * 60)
    print("STAGE 2 SUMMARY")
    print("=" * 60)
    print(f"Total trains filtered for Saturday: {len(saturday_trains)}")
    print(f"Total trains from {specific_station}: {len(trains_from_station)}")
    print("Grouping and enrichment completed successfully!")

    return df
