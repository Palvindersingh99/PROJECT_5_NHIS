# =========================================================
# PROJECT 5
# USER ANALYTICS IN TELECOMMUNICATION INDUSTRY
# COMPLETE PYTHON PROJECT CODE
# =========================================================

# -----------------------------
# STEP 1 : IMPORT LIBRARIES
# -----------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# STEP 2 : LOAD DATASET
# -----------------------------

# Replace file name with your dataset name
data = pd.read_csv(r"E:\pgp\INTERSHIP PROJECT\PROJECT 5\telcom_data.csv")

# Display first 5 rows
print("\nFIRST 5 ROWS OF DATASET\n")
print(data.head())

# -----------------------------
# STEP 3 : BASIC INFORMATION
# -----------------------------

print("\nDATASET INFORMATION\n")
print(data.info())

print("\nDATASET SHAPE\n")
print(data.shape)

print("\nMISSING VALUES\n")
print(data.isnull().sum())

# -----------------------------
# STEP 4 : DATA CLEANING
# -----------------------------

# Remove duplicate values
data.drop_duplicates(inplace=True)

# Fill missing numeric values with mean
numeric_columns = data.select_dtypes(include=np.number).columns

for col in numeric_columns:
    data[col].fillna(data[col].mean(), inplace=True)

# Fill missing object values with mode
object_columns = data.select_dtypes(include='object').columns

for col in object_columns:
    data[col].fillna(data[col].mode()[0], inplace=True)

print("\nMISSING VALUES AFTER CLEANING\n")
print(data.isnull().sum())

# -----------------------------
# STEP 5 : DESCRIPTIVE ANALYSIS
# -----------------------------

print("\nSTATISTICAL SUMMARY\n")
print(data.describe())

# -----------------------------
# TASK 1 : USER OVERVIEW ANALYSIS
# -----------------------------

print("\n==============================")
print("TASK 1 : USER OVERVIEW ANALYSIS")
print("==============================")

# Top 10 handset types
if 'Handset Type' in data.columns:
    print("\nTOP 10 HANDSET TYPES\n")
    print(data['Handset Type'].value_counts().head(10))

# Top manufacturers
if 'Handset Manufacturer' in data.columns:
    print("\nTOP MANUFACTURERS\n")
    print(data['Handset Manufacturer'].value_counts().head(10))

# -----------------------------
# VISUALIZATION : HANDSET TYPES
# -----------------------------

if 'Handset Type' in data.columns:

    plt.figure(figsize=(12,6))

    data['Handset Type'].value_counts().head(10).plot(kind='bar')

    plt.title("Top 10 Handset Types")
    plt.xlabel("Handset Type")
    plt.ylabel("Count")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

# -----------------------------
# TASK 2 : USER ENGAGEMENT ANALYSIS
# -----------------------------

print("\n==============================")
print("TASK 2 : USER ENGAGEMENT ANALYSIS")
print("==============================")

# Example engagement analysis

if 'Dur. (ms)' in data.columns:

    print("\nAVERAGE SESSION DURATION\n")
    print(data['Dur. (ms)'].mean())

# Total download data
if 'Total DL (Bytes)' in data.columns:

    print("\nTOTAL DOWNLOAD DATA\n")
    print(data['Total DL (Bytes)'].sum())

# Total upload data
if 'Total UL (Bytes)' in data.columns:

    print("\nTOTAL UPLOAD DATA\n")
    print(data['Total UL (Bytes)'].sum())

# -----------------------------
# SESSION DURATION HISTOGRAM
# -----------------------------

if 'Dur. (ms)' in data.columns:

    plt.figure(figsize=(10,6))

    plt.hist(data['Dur. (ms)'], bins=30)

    plt.title("Session Duration Distribution")
    plt.xlabel("Duration")
    plt.ylabel("Frequency")

    plt.show()

# -----------------------------
# TASK 3 : USER EXPERIENCE ANALYSIS
# -----------------------------

print("\n==============================")
print("TASK 3 : USER EXPERIENCE ANALYSIS")
print("==============================")

# Average TCP retransmission
if 'TCP DL Retrans. Vol (Bytes)' in data.columns:

    print("\nAVERAGE TCP RETRANSMISSION\n")
    print(data['TCP DL Retrans. Vol (Bytes)'].mean())

# Average RTT
if 'Avg RTT DL (ms)' in data.columns:

    print("\nAVERAGE RTT\n")
    print(data['Avg RTT DL (ms)'].mean())

# Average Throughput
if 'Avg Bearer TP DL (kbps)' in data.columns:

    print("\nAVERAGE THROUGHPUT\n")
    print(data['Avg Bearer TP DL (kbps)'].mean())

# -----------------------------
# CORRELATION HEATMAP
# -----------------------------

plt.figure(figsize=(12,8))

numeric_data = data.select_dtypes(include=np.number)

sns.heatmap(
    numeric_data.corr(),
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# -----------------------------
# DOWNLOAD VS UPLOAD GRAPH
# -----------------------------

if 'Total DL (Bytes)' in data.columns and 'Total UL (Bytes)' in data.columns:

    plt.figure(figsize=(10,6))

    plt.scatter(
        data['Total DL (Bytes)'],
        data['Total UL (Bytes)']
    )

    plt.title("Download vs Upload")
    plt.xlabel("Download")
    plt.ylabel("Upload")

    plt.show()

# -----------------------------
# USER SATISFACTION ANALYSIS
# -----------------------------

if 'MSISDN/Number' in data.columns and 'Dur. (ms)' in data.columns:

    user_duration = data.groupby(
        'MSISDN/Number'
    )['Dur. (ms)'].sum()

    print("\nTOP 10 ACTIVE USERS\n")
    print(user_duration.sort_values(
        ascending=False
    ).head(10))

# -----------------------------
# FINAL CONCLUSION
# -----------------------------

print("\n==============================")
print("FINAL CONCLUSION")
print("==============================")

print("""
1. Telecom users use different handset types.

2. Session duration analysis helps identify active users.

3. Download and upload traffic show internet usage behavior.

4. Network metrics like RTT and TCP retransmission help
   measure user experience.

5. Visualization helps understand customer behavior clearly.

6. Telecom companies can use this analysis to improve
   customer satisfaction and network quality.
""")

# -----------------------------
# SAVE CLEANED DATASET
# -----------------------------

data.to_csv("cleaned_telecom_data.csv", index=False)

print("\nCLEANED DATASET SAVED SUCCESSFULLY")

# =========================================================
# END OF PROJECT
# =========================================================