# YouTube Watching & Food Purchasing Correlation Analysis

## Project Proposal

### Project Idea
The goal of this project is to explore whether there is a meaningful temporal relationship between my **food purchasing times** (from both *Yemeksepeti* and vending machine transactions) and my **YouTube watching activity**.

I often notice that I tend to watch YouTube videos while eating or shortly after buying food. This project aims to test that observation using data analysis.

The main research question is:
> “Do my food purchasing times align with my YouTube watching times?”

By examining these activities as time series, I hope to identify daily or weekly patterns that link food consumption and media engagement.

---

### Data to Be Used
- **Yemeksepeti Order Timestamps:**
  Historical order data showing when I placed food delivery orders.
- **Vending Machine Purchase Timestamps:**
  Transaction logs from campus or public vending machines (time only).
- **YouTube Watch History:**
  Timestamps of videos watched, obtained from **Google Takeout**.

Only **timestamps** will be used — no personal details, food types, prices, or video content.
The goal is to analyze **temporal overlap patterns**, not consumption details.

---

### Data Collection Plan
1. **Yemeksepeti Data**
   Export or manually record order timestamps from my account.
2. **Vending Machine Data**
   Retrieve transaction times from campus card or payment logs.
3. **YouTube Data**
   Download my watch history via **Google Takeout** (includes view timestamps).
4. **Integration & Cleaning**
   - Convert all timestamps to the same format and timezone.
   - Merge them into a single dataset.
   - Conduct time-series correlation analysis to detect overlaps and patterns.

---

### Expected Outcome
I expect to find observable correlations between food-related activities and YouTube viewing behavior. Possible outcomes include:
- Temporal overlaps, such as increased YouTube watching during or shortly after food purchases.
- Daily rhythm patterns, where peaks in both activities occur around lunch or dinner times.
- Identification of habitual cycles, reflecting consistent behavioral links between eating and entertainment.

Even if no significant correlation is discovered, the analysis will still provide valuable insights into personal behavioral rhythms and how digital activity relates to daily routines.

---
