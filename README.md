Project Proposal: Behavioral Coupling of Food & Media Consumption

Project Overview

This project applies data science methodologies to analyze the "Quantified Self," specifically investigating the behavioral coupling between food ordering (physical consumption) and media streaming (digital consumption).

Instead of merely observing if these events overlap, this project aims to determine if food delivery acts as a statistically significant trigger event for high-engagement media sessions. The goal is to quantify the "Dinner-and-a-Show" phenomenon—measuring how predictable and intense this habit is.

Research Questions & Analytical Focus

Based on feedback regarding analytical depth, this analysis focuses on two specific dimensions of behavior:

Habit Consistency (Probability):

Question: How reliably does ordering food lead to watching a video?

Metric: The conditional probability $P(\text{Watch} | \text{Order})$. A high probability indicates a deeply ingrained behavioral loop, while a low one suggests randomness.

Behavioral Latency (The "Eating Window"):

Question: What is the precise time lag between the transaction (ordering) and the start of consumption (watching)?

Metric: We define a dynamic "Eating Window" (Order Time + 30 mins lag) to isolate the consumption phase from the waiting phase.

Data Sources

The project utilizes two personal datasets representing activity from the past 12 months:

Transaction Data (Yemeksepeti/Just Eat/Vending): Extracted from personal archives. Contains timestamps and location metadata (Turkey/Netherlands) for food orders.

YouTube Watch History: Extracted via Google Takeout. Contains ISO 8601 timestamps for every video watched.

Methodology

1. Data Processing & Synchronization

Timezone Alignment: Since the dataset covers transactions in different time zones (Turkey UTC+3 vs. Netherlands UTC+1), timestamps are normalized to UTC to ensure accurate lag calculation.

Session Parsing: YouTube data is parsed using Regex to identify distinct viewing events.

2. Statistical Analysis

We perform the following tests to validate the "Food as a Trigger" hypothesis:

Paired T-Test: To compare video volume in the "Eating Window" (post-delivery) vs. a "Baseline Window" (pre-order).

Pearson Correlation: To test for habit continuity (does pre-meal watching predict during-meal watching?).

Expected Outcomes

I expect to move beyond "I watch videos when I eat" to specific behavioral insights, such as:

"I have a 60% probability of starting a video within 30 minutes of food delivery."

"My video consumption volume significantly increases during the eating window compared to the baseline."

This project ultimately demonstrates how personal transactional and behavioral data can be combined to model daily habit loops.
