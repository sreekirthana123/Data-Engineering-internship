import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_stage4(df: pd.DataFrame) -> None:
    """
    Stage 4: Data Visualization and Reporting
    - Task 4.1: Visualization
    - Task 4.2: Reporting
    """

    print("=" * 60)
    print("STAGE 4.1: VISUALIZATION")
    print("=" * 60)

    # Heatmap: Source vs Destination train counts
    pivot = df.pivot_table(index="Source_Station_Name",
                           columns="Destination_Station_Name",
                           values="Train_No",
                           aggfunc="count",
                           fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, cmap="YlGnBu")
    plt.title("Heatmap of Train Counts (Source vs Destination)")
    plt.tight_layout()
    plt.show()

    # ============================================
    # TASK 4.2: REPORTING
    # ============================================
    print("\n" + "=" * 60)
    print("STAGE 4.2: REPORTING")
    print("=" * 60)

    print("\nComprehensive Report:")
    print("- Data exploration showed missing values, which were cleaned and standardized.")
    print("- Basic statistics revealed key hubs (e.g., DELHI, MUMBAI) as dominant source/destination stations.")
    print("- Transformation highlighted weekday vs weekend operations, with fewer weekend trains.")
    print("- Advanced analysis confirmed higher train counts on weekdays, with correlations suggesting demand gaps on weekends.")
    print("- Visualizations (bar charts in Stage 3, heatmap in Stage 4) provide clear evidence of these patterns.")

    print("\nRecommendations for Stakeholders:")
    print("1. Increase weekend train services to balance demand.")
    print("2. Optimize scheduling for high-volume stations to reduce congestion.")
    print("3. Use heatmap insights to strengthen connectivity between under-served routes.")
    print("4. Continue monitoring weekly patterns for adaptive scheduling.")

    # Save report summary as text file
    with open("stage4_report.txt", "w") as f:
        f.write("Comprehensive Report\n")
        f.write("- Data exploration showed missing values, which were cleaned and standardized.\n")
        f.write("- Basic statistics revealed key hubs (e.g., DELHI, MUMBAI) as dominant source/destination stations.\n")
        f.write("- Transformation highlighted weekday vs weekend operations, with fewer weekend trains.\n")
        f.write("- Advanced analysis confirmed higher train counts on weekdays, with correlations suggesting demand gaps on weekends.\n")
        f.write("- Visualizations (bar charts in Stage 3, heatmap in Stage 4) provide clear evidence of these patterns.\n\n")
        f.write("Recommendations for Stakeholders:\n")
        f.write("1. Increase weekend train services to balance demand.\n")
        f.write("2. Optimize scheduling for high-volume stations to reduce congestion.\n")
        f.write("3. Use heatmap insights to strengthen connectivity between under-served routes.\n")
        f.write("4. Continue monitoring weekly patterns for adaptive scheduling.\n")

    print("✅ Stage 4 report saved as 'stage4_report.txt'")

    # ============================================
    # SUMMARY
    # ============================================
    print("\n" + "=" * 60)
    print("STAGE 4 SUMMARY")
    print("=" * 60)
    print("Visualizations created successfully.")
    print("Comprehensive report compiled and presented.")
    print("Stage 4 tasks completed successfully!")
