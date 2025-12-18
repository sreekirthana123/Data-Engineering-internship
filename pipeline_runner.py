from stage1_exploration import run_stage1
from stage2_transformation import run_stage2
from stage3_analysis import run_stage3
from stage4_reporting import run_stage4

def pipeline_runner():
    # ============================================
    # CONFIGURATION - UPDATE YOUR FILE PATH HERE
    # ============================================
    filepath = r"C:\Users\Sree Kirthana\Documents\Data Engineering Intern\Railway_info.csv"

    # ============================================
    # PIPELINE EXECUTION
    # ============================================
    print("=" * 60)
    print("🚂 DATA ENGINEERING PIPELINE RUNNER 🚂")
    print("=" * 60)

    # Stage 1: Exploration & Cleaning
    df_cleaned = run_stage1(filepath)

    # Stage 2: Transformation & Aggregation
    df_transformed = run_stage2(df_cleaned)

    # Stage 3: Advanced Analysis
    df_analyzed = run_stage3(df_transformed)

    # Stage 4: Visualization & Reporting
    run_stage4(df_analyzed)

    # ============================================
    # FINAL SUMMARY
    # ============================================
    print("\n" + "=" * 60)
    print("🎉 PIPELINE COMPLETED SUCCESSFULLY 🎉")
    print("=" * 60)
    print("All four stages executed:")
    print("1️⃣ Stage 1 - Exploration & Cleaning")
    print("2️⃣ Stage 2 - Transformation & Aggregation")
    print("3️⃣ Stage 3 - Advanced Analysis")
    print("4️⃣ Stage 4 - Visualization & Reporting")
    print("\nOutputs and visualizations generated. Reports ready for stakeholders!")

if __name__ == "__main__":
    pipeline_runner()
