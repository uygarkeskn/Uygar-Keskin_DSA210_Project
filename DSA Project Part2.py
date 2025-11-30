import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import re
import json
import numpy as np
import os

# --- CONFIGURATION ---
DELIVERY_DELAY_MIN = 30   # Time to wait for food
EATING_WINDOW_MIN = 30    # Duration of eating

def clean_rtf_json(file_path):
    print(f"Loading YouTube data from: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    #
    time_pattern = r'"time"(?:[\s\S]*?):(?:[\s\S]*?)"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)"'
    times = re.findall(time_pattern, content)
    
    print(f"Found {len(times)} video records.")
    return times

def load_data():
    print("--- Loading Data ---")
    
    food_file = 'Yemeksepeti_Data.xlsx'
    if not os.path.exists(food_file):
        raise FileNotFoundError(f"Could not find {food_file}.")

    food_df = pd.read_excel(food_file, header=1)
    
    food_df['datetime_str'] = food_df['İşlem Tarihi'].astype(str) + ' ' + food_df['İşlem Saati'].astype(str)
    food_df['datetime'] = pd.to_datetime(food_df['datetime_str'])
    
    print(f"Loaded {len(food_df)} food orders.")
    
    yt_file = '2025_youtube_data.JSON'
    if not os.path.exists(yt_file):
        raise FileNotFoundError(f"Could not find {yt_file}.")
        
    yt_times = clean_rtf_json(yt_file)
    yt_df = pd.DataFrame({'time_str': yt_times})
    yt_df['datetime'] = pd.to_datetime(yt_df['time_str'])
    
    # Convert to Turkey Time and remove timezone info for comparison
    yt_df['datetime'] = yt_df['datetime'].dt.tz_convert('Europe/Istanbul').dt.tz_localize(None)
    yt_df = yt_df.sort_values('datetime').reset_index(drop=True)
    
    return food_df, yt_df

def analyze_with_delivery_lag(food_df, yt_df):
  
    print("\n--- Analyzing with Delivery Lag ---")
    print(f"Settings: Delivery Lag = {DELIVERY_DELAY_MIN}m, Eating Window = {EATING_WINDOW_MIN}m")
    
    results = []
    
    for idx, row in food_df.iterrows():
        order_time = row['datetime']
        estimated_arrival = order_time + pd.Timedelta(minutes=DELIVERY_DELAY_MIN)
        
        # 1. WINDOW A: Before Order (Baseline)
        # Checking window BEFORE order
        videos_before = yt_df[
            (yt_df['datetime'] >= order_time - pd.Timedelta(minutes=EATING_WINDOW_MIN)) & 
            (yt_df['datetime'] < order_time)
        ].shape[0]
        
        # 2. WINDOW B: Eating Window (Starts after delivery)
        # Checking window AFTER arrival
        videos_eating = yt_df[
            (yt_df['datetime'] >= estimated_arrival) & 
            (yt_df['datetime'] < estimated_arrival + pd.Timedelta(minutes=EATING_WINDOW_MIN))
        ].shape[0]
        
        results.append({
            'videos_before': videos_before,
            'videos_eating': videos_eating
        })
        
    results_df = pd.DataFrame(results)
    return results_df

def plot_activity_heatmap(food_df, yt_df):
    
    print("Generating Lag Heatmap...")
    
    offsets = []
    
    for idx, row in food_df.iterrows():
        order_time = row['datetime']
        
        nearby_videos = yt_df[
            (yt_df['datetime'] >= order_time - pd.Timedelta(minutes=120)) &
            (yt_df['datetime'] <= order_time + pd.Timedelta(minutes=120))
        ]
        
        for _, vid in nearby_videos.iterrows():
            diff = (vid['datetime'] - order_time).total_seconds() / 60
            offsets.append(diff)
            
    plt.figure(figsize=(12, 6))
    sns.histplot(offsets, bins=range(-60, 121, 10), kde=True, color='teal')
    
    
    plt.axvline(0, color='red', linestyle='--', label='Order Placed')
    plt.axvline(DELIVERY_DELAY_MIN, color='orange', linestyle='--', label=f'Avg Delivery ({DELIVERY_DELAY_MIN}m)')
    
    
    plt.axvspan(DELIVERY_DELAY_MIN, DELIVERY_DELAY_MIN + EATING_WINDOW_MIN, color='orange', alpha=0.1, label='Eating Window')
    
    plt.title('When do you watch videos relative to ordering food?')
    plt.xlabel('Minutes Relative to Order Time (0 = Order Placed)')
    plt.ylabel('Video Count')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('eating_lag_analysis.png')
    plt.close()

def plot_time_gap_distribution(food_df, yt_df):

    
    print("Generating Time Gap Distribution...")
    gaps = []
    
    for idx, row in food_df.iterrows():
        order_time = row['datetime']
        # Find videos AFTER the order
        future_videos = yt_df[yt_df['datetime'] > order_time]
        
        if not future_videos.empty:
            # Get the very first one
            next_vid_time = future_videos.iloc[0]['datetime']
            diff_minutes = (next_vid_time - order_time).total_seconds() / 60
            
            # Only consider "sessions" that start within 2 hours.
            if diff_minutes <= 120:
                gaps.append(diff_minutes)
    
    plt.figure(figsize=(10, 6))
    sns.histplot(gaps, bins=20, kde=True, color='purple')
    
    mean_gap = np.mean(gaps)
    median_gap = np.median(gaps)
    plt.axvline(mean_gap, color='red', linestyle='--', label=f'Mean Wait: {mean_gap:.1f}m')
    plt.axvline(median_gap, color='yellow', linestyle='--', label=f'Median Wait: {median_gap:.1f}m')
    
    plt.title('Time Gap Distribution: How long until the FIRST video?')
    plt.xlabel('Minutes after Order')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('time_gap_distribution.png')
    plt.close()

def test_hypothesis_lag(results_df):
    print("\n" + "="*50)
    print("      HYPOTHESIS TEST (WITH DELIVERY LAG)      ")
    print("="*50)
    
    before = results_df['videos_before']
    eating = results_df['videos_eating']
    
    count_with_watch = results_df[results_df['videos_eating'] > 0].shape[0]
    consistency = (count_with_watch / len(results_df)) * 100
    
    print(f"Sample Size: {len(results_df)} orders")
    print(f"Habit Consistency Score: {consistency:.1f}%") 
    print(f"(You watched at least one video in {consistency:.1f}% of your eating windows)")
    print("-" * 50)

    print(f"Avg Videos ({EATING_WINDOW_MIN}m Before Order): {before.mean():.2f}")
    print(f"Avg Videos ({EATING_WINDOW_MIN}m Eating Window): {eating.mean():.2f} (Starts {DELIVERY_DELAY_MIN}m after order)")
    
    # --- TEST 1: Paired T-Test (Parametric) ---
    t_stat, p_val_t = stats.ttest_rel(eating, before, alternative='greater')
    print("-" * 50)
    print("1. Paired T-Test (Comparing Means)")
    print(f"   p-value: {p_val_t:.4f}")
    if p_val_t < 0.05:
        print("   Result: Significant increase found.")
    else:
        print("   Result: No significant difference.")

    # --- TEST 2: Pearson Correlation ---
    if len(eating) > 1:
        corr_coef, p_val_c = stats.pearsonr(before, eating)
        print("-" * 50)
        print("2. Pearson Correlation (Checking Continuity)")
        print(f"   Correlation (r): {corr_coef:.4f}")
        print(f"   p-value: {p_val_c:.4f}")
        
        if p_val_c < 0.05:
            if corr_coef > 0:
                print("   Result: Positive Correlation. (If you watch before, you keep watching while eating).")
            else:
                print("   Result: Negative Correlation. (If you watch before, you stop while eating).")
        else:
            print("   Result: No correlation found between pre-order and eating behavior.")
    
    print("="*50)

if __name__ == "__main__":
    try:
        food_df, yt_df = load_data()
        results_df = analyze_with_delivery_lag(food_df, yt_df)
        plot_activity_heatmap(food_df, yt_df)
        plot_time_gap_distribution(food_df, yt_df) 
        test_hypothesis_lag(results_df)
        print("\nAnalysis Complete.")
    except Exception as e:
        print(f"\nCRITICAL ERROR: {e}")