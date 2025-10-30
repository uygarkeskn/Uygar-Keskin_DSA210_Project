# YouTube Watching & Food Purchasing Correlation Analysis

## Project Proposal

### Project Idea
The main objective of this project is to analyze the relationship between my **eating times** and **YouTube watching activity** over the **past year**.
Instead of focusing on what I eat or what I watch, the goal is to explore **when** these two activities occur and whether they overlap in time.

I aim to investigate whether I tend to watch YouTube videos while eating, or shortly before or after meals. By examining these behaviors as **time-based events**, the project seeks to uncover recurring temporal patterns that connect food consumption and media engagement.

The key research question is:
> “Do my eating times align with my YouTube watching times during the past year?”

Through this analysis, I hope to identify daily or weekly cycles that reveal consistent behavioral relationships between eating habits and digital entertainment.

---

### Data to Be Used
- **Card Transaction Data (Yemeksepeti, Just Eat & Vending Machines):**
  I will extract timestamps of my food-related purchases from my **personal card transaction history** over the last 12 months.
  This includes **online orders from Yemeksepeti and Just Eat**, as well as **physical purchases from vending machines**.
- **YouTube Watch History:**
  My personal YouTube viewing history obtained from **Google Takeout**, which contains the exact timestamps of videos watched within the same time period.

Only **timestamp data** will be used — no food details, restaurant names, prices, or video titles.
The focus will be purely on identifying **time-based correlations** between eating and watching patterns across the past year.

---

### Data Collection Plan
1. **Card Transaction Data**
   - Retrieve my transaction records from my personal bank or card provider.
   - Filter for food-related purchases (Yemeksepeti, Just Eat, vending machines).
   - Extract only timestamps representing when food was purchased or ordered.

2. **YouTube Data**
   - Export my full YouTube watch history via **Google Takeout**.
   - Keep only timestamps of video views within the same 12-month period.

3. **Integration and Cleaning**
   - Convert all timestamps to a unified format and local timezone (UTC+3).
   - Remove duplicates or incomplete entries.
   - Merge the datasets chronologically to compare time overlaps between eating and watching activities.
   - Resample data into hourly or daily intervals for trend visualization.

4. **Exploratory and Statistical Analysis**
   - Visualize daily and weekly distributions of eating and watching events.
   - Compute **Pearson or Spearman correlation coefficients** to measure temporal alignment.
   - Use **cross-correlation** to detect time lags (e.g., watching videos 15–30 minutes after eating).
   - Compare weekday and weekend behaviors to observe differences in routine patterns.

---

### Expected Outcome
I expect to identify noticeable **temporal correlations** between eating and YouTube watching behaviors over the past year. Possible results include:
- Overlaps between eating and video-watching periods.

Even if no strong statistical correlation is found, the analysis will still provide **valuable behavioral insights** — showing how media consumption fits into everyday life patterns.
Ultimately, this project demonstrates how **personal digital and financial data** can be combined to perform meaningful **data-driven self-analysis** using data science tools.
