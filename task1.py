# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HgfSmjKQccicTLp3berGZLrLMFIx5Kzr
"""

import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
df_train = pd.read_excel('train.xlsx')
df_test = pd.read_excel('test.xlsx')

# Extract features from train data and standardize the data
features_train = df_train.drop(['target'], axis=1)
scaler = StandardScaler()
scaled_data_train = scaler.fit_transform(features_train)

# Apply k-means clustering on the train data
kmeans = KMeans(n_clusters=3, random_state=42)
df_train['cluster'] = kmeans.fit_predict(scaled_data_train)

# Streamlit app
st.title("K-Means Clustering")

# Sidebar for user input
st.sidebar.header("New Data Point (Test Set)")
new_data_point_test = {}
for col in df_test.columns:
    if col != 'target':
        new_data_point_test[col] = st.sidebar.number_input(f"Enter {col}", value=df_test[col].iloc[0])

# Create a DataFrame for the new data point
new_data_point_test = pd.DataFrame([new_data_point_test])

# Standardize the new data point
scaled_new_data_point_test = scaler.transform(new_data_point_test)

# Predict the cluster for the new data point using the k-means model trained on the train data
predicted_cluster = kmeans.predict(scaled_new_data_point_test)[0]

# Explain the cluster assignment
cluster_assignment = f"The new data point from the test set belongs to Cluster {predicted_cluster}."

# Display cluster assignment
st.write(cluster_assignment)

# Display the train dataset with clusters
st.header("Train Data with Clusters")
st.write(df_train)
