import pandas as pd

def run_stage1(filepath: str) -> pd.DataFrame:
    """
    Stage 1: Data Exploration and Basic Operations
    - Task 1.1: Load and Inspect Data
    - Task 1.2: Basic Statistics
    - Task 1.3: Data Cleaning
    """

    # ============================================
    # TASK 1.1: LOAD AND INSPECT DATA
    # ============================================
    print("=" * 60)
    print("STAGE 1.1: LOAD AND INSPECT DATA")
    print("=" * 60)

    print(f"\nLoading data from: {filepath}")
    df = pd.read_csv(filepath)

    # Display first 10 rows
    print("\nFirst 10 rows of the dataset:")
    print(df.head(10))

    # Display basic structure
    print("\nDataset Shape (rows, columns):")
    print(f"{df.shape[0]} rows and {df.shape[1]} columns")

    print("\nColumn Names and Data Types:")
    print(df.dtypes)

    print("\nDataset Information:")
    print(df.info())

    print("\nMissing Values Count:")
    print(df.isnull().sum())

    print("\nMissing Values Percentage:")
    print((df.isnull().sum() / len(df) * 100).round(2))

    # ============================================
    # TASK 1.2: BASIC STATISTICS
    # ============================================
    print("\n" + "=" * 60)
    print("STAGE 1.2: BASIC STATISTICS")
    print("=" * 60)

    total_trains = df.shape[0]
    print(f"\nTotal number of trains: {total_trains}")

    unique_sources = df['Source_Station_Name'].nunique()
    print(f"Number of unique source stations: {unique_sources}")

    unique_destinations = df['Destination_Station_Name'].nunique()
    print(f"Number of unique destination stations: {unique_destinations}")

    most_common_source = df['Source_Station_Name'].mode()[0]
    source_count = df['Source_Station_Name'].value_counts().iloc[0]
    print(f"\nMost common source station: {most_common_source} ({source_count} trains)")

    most_common_destination = df['Destination_Station_Name'].mode()[0]
    dest_count = df['Destination_Station_Name'].value_counts().iloc[0]
    print(f"Most common destination station: {most_common_destination} ({dest_count} trains)")

    print("\nTop 5 Source Stations:")
    print(df['Source_Station_Name'].value_counts().head())

    print("\nTop 5 Destination Stations:")
    print(df['Destination_Station_Name'].value_counts().head())

    # ============================================
    # TASK 1.3: DATA CLEANING
    # ============================================
    print("\n" + "=" * 60)
    print("STAGE 1.3: DATA CLEANING")
    print("=" * 60)

    df_cleaned = df.copy()

    print("\nHandling Missing Values:")
    print("Before cleaning:")
    print(df_cleaned.isnull().sum())

    for col in df_cleaned.columns:
        if df_cleaned[col].isnull().any():
            if df_cleaned[col].dtype == 'object':
                df_cleaned[col].fillna('Unknown', inplace=True)
            else:
                df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)

    print("\nAfter cleaning:")
    print(df_cleaned.isnull().sum())

    print("\nStandardizing Station Names to Uppercase:")
    print("Sample before standardization:")
    print(df_cleaned[['Source_Station_Name', 'Destination_Station_Name']].head(3))

    df_cleaned['Source_Station_Name'] = df_cleaned['Source_Station_Name'].str.upper().str.strip()
    df_cleaned['Destination_Station_Name'] = df_cleaned['Destination_Station_Name'].str.upper().str.strip()

    print("\nSample after standardization:")
    print(df_cleaned[['Source_Station_Name', 'Destination_Station_Name']].head(3))

    df_cleaned.to_csv('train_data_cleaned.csv', index=False)
    print("\nCleaned data saved as 'train_data_cleaned.csv'")

    # Summary
    print("\n" + "=" * 60)
    print("STAGE 1 SUMMARY")
    print("=" * 60)
    print(f"Original dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Cleaned dataset: {df_cleaned.shape[0]} rows, {df_cleaned.shape[1]} columns")
    print(f"Rows removed: {df.shape[0] - df_cleaned.shape[0]}")
    print("\nStage 1 tasks completed successfully!")

    return df_cleaned
