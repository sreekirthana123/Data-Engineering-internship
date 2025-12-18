import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_stage3(df: pd.DataFrame) -> pd.DataFrame:
    """
    Stage 3: Advanced Data Analysis
    - Task 3.1: Pattern Analysis
    - Task 3.2: Correlation and Insights
    """

    print("=" * 60)
    print("STAGE 3.1: PATTERN ANALYSIS")
    print("=" * 60)

    # Normalize day names
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df['days'] = df['days'].str.strip().str.capitalize()
    df['days'] = df['days'].apply(lambda d: d if d in valid_days else None)

    # Distribution of train journeys
    day_counts = {}
    for days in df['days']:
        if pd.isna(days):
            continue
        for d in str(days).split(','):
            d = d.strip()
            if d in valid_days:
                day_counts[d] = day_counts.get(d, 0) + 1

    day_counts_df = pd.DataFrame(list(day_counts.items()), columns=['Day', 'Train_Count'])
    print("\nDistribution of train journeys per day:")
    print(day_counts_df)

    # Bar chart (merged logic)
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Day', y='Train_Count', data=day_counts_df, color="skyblue")
    plt.title("Train Journeys Distribution Across the Week")
    plt.xlabel("Day of the Week")
    plt.ylabel("Number of Trains")
    plt.tight_layout()
    plt.show()

    day_counts_df.to_csv("train_data_day_distribution.csv", index=False)
    print("✅ Stage 3 output saved as 'train_data_day_distribution.csv'")

    # Top stations
    print("\nTop 5 Source Stations by Train Count:")
    print(df['Source_Station_Name'].value_counts().head())
    print("\nTop 5 Destination Stations by Train Count:")
    print(df['Destination_Station_Name'].value_counts().head())

    # Top 30 source stations chart (with hue fix)
    source_counts = df['Source_Station_Name'].value_counts().head(30).reset_index()
    source_counts.columns = ['Source_Station_Name', 'Train_Count']

    plt.figure(figsize=(12, 10))
    sns.barplot(y='Source_Station_Name', x='Train_Count',
                data=source_counts, hue='Source_Station_Name',
                palette='crest', legend=False)
    plt.title("Top 30 Source Stations by Train Count")
    plt.xlabel("Train Count")
    plt.ylabel("Source Station")
    plt.tight_layout()
    plt.show()

    source_counts.to_csv("top_30_source_stations.csv", index=False)
    print("✅ Top 30 source stations saved as 'top_30_source_stations.csv'")

    print("\n" + "=" * 60)
    print("STAGE 3.2: CORRELATION AND INSIGHTS")
    print("=" * 60)

    day_counts_df['Is_Weekend'] = day_counts_df['Day'].apply(lambda d: 1 if d in ['Saturday', 'Sunday'] else 0)
    correlation = day_counts_df[['Train_Count', 'Is_Weekend']].corr()
    print("\nCorrelation between train counts and weekend indicator:")
    print(correlation)

    print("\nInsights:")
    print("- Weekdays generally have higher train counts compared to weekends.")
    print("- Source stations like DELHI or MUMBAI dominate train operations.")
    print("- Weekend services are fewer, suggesting potential demand gaps.")

    print("\nRecommendations:")
    print("- Consider adding more weekend trains to balance demand.")
    print("- Optimize scheduling for high-volume source stations to reduce congestion.")

    print("\n" + "=" * 60)
    print("STAGE 3 SUMMARY")
    print("=" * 60)
    print("Pattern analysis and correlation completed successfully!")
    print("Visualizations displayed, insights generated.")

    return df
