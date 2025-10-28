# Project Proposal: Temporal Correlation Between Food Purchases and YouTube Activity

## Project Idea

The main goal of this project is to investigate whether there is a meaningful temporal relationship between my **food purchasing times** (from both **Yemeksepeti** and **vending machine transactions**) and my **YouTube watching activity**.

I often notice that I tend to watch YouTube videos while eating or shortly after buying food. This observation led me to wonder if there is a measurable correlation between these two behaviors.

The project will analyze my personal behavioral data to answer the following question:

> **“Do my food purchasing times align with my YouTube watching times?”**

By examining these activities as time series, I aim to uncover daily or weekly patterns that might connect eating and media consumption habits.

---

## Data to Be Used

- **Yemeksepeti order timestamps:**  
  Historical data from my Yemeksepeti account showing when I placed food delivery orders.

- **Vending machine purchase timestamps:**  
  Transaction records from campus or public vending machines, including only the purchase times.

- **YouTube watch history:**  
  Timestamps of my video-watching activity, obtained through Google Takeout.

> No personal identifiers, food types, prices, or video titles will be included — only **timestamp information** will be analyzed to focus purely on temporal patterns.

---

## Data Collection Plan

### Yemeksepeti Data
I will manually collect or export my order history, focusing only on order timestamps.

### Vending Machine Data
I will access my vending machine purchase history through campus card or transaction records and extract the exact purchase times.

### YouTube Data
I will download my YouTube watch history via **Google Takeout**, which includes the precise time each video was viewed.

### Data Integration
After collecting all three datasets, I will clean and standardize the timestamps (e.g., converting to a unified format and local time zone).  
Then, I will merge them into a single dataset to perform **time-series correlation analysis**.
