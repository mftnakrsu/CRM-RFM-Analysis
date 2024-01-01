#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
RFM Analysis Script

Author: Mef

This script is designed to perform RFM (Recency, Frequency, Monetary) analysis, a crucial method for customer segmentation and marketing strategy development. RFM analysis evaluates customer behavior based on their transaction recency, frequency, and monetary value.

The RFMAnalysis class in this script provides functionality to process and analyze customer transaction data, creating a segmentation map that categorizes customers into distinct segments based on their RFM scores.

Usage:
1. Load your dataset into a DataFrame.
2. Create an instance of RFMAnalysis by passing the DataFrame.
3. Call the methods in sequence: prepare_data() for data preparation, calculate_rfm() for RFM analysis, and save_to_csv() to export the results to a CSV file.

Example Usage:

# Load your DataFrame (df) here
rfm_analyzer = RFMAnalysis(df)
rfm_analyzer.prepare_data()
rfm_analyzer.calculate_rfm()
rfm_analyzer.save_to_csv()

"""

import pandas as pd
import datetime as dt

class RFMAnalysis:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def prepare_data(self):

    """
    Performs data preparation:
    
    - Creates the 'TotalPrice' column from the product of 'Quantity' and 'Price' columns.
    - Removes rows containing missing data (NaN).
    - Filters out rows containing canceled transactions (identified by 'C' in 'Invoice' column).
    
    """
        self.dataframe["TotalPrice"] = self.dataframe["Quantity"] * self.dataframe["Price"]
        self.dataframe.dropna(inplace=True)
        self.dataframe = self.dataframe[~self.dataframe["Invoice"].str.contains("C", na=False)]

    def calculate_rfm(self):

    """
    Calculates RFM (Recency, Frequency, Monetary) analysis:
    
    - Calculates recency, frequency, and monetary values for each customer.
    - Assigns scores for recency, frequency, and monetary values based on quantiles.
    - Generates RFM_SCORE by combining recency, frequency, and monetary scores.
    - Maps RFM_SCORE to customer segments using predefined segmentation rules.
    """
        
        today_date = dt.datetime(2011, 12, 11)
        rfm = self.dataframe.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                                         'Invoice': lambda num: num.nunique(),
                                                         "TotalPrice": lambda price: price.sum()})
        rfm.columns = ['recency', 'frequency', "monetary"]
        rfm = rfm[(rfm['monetary'] > 0)]

        rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
        rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
        rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])
        rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))

        seg_map = {
            r'[1-2][1-2]': 'hibernating',
            r'[1-2][3-4]': 'at_risk',
            r'[1-2]5': 'cant_loose',
            r'3[1-2]': 'about_to_sleep',
            r'33': 'need_attention',
            r'[3-4][4-5]': 'loyal_customers',
            r'41': 'promising',
            r'51': 'new_customers',
            r'[4-5][2-3]': 'potential_loyalists',
            r'5[4-5]': 'champions'
        }

        rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
        self.rfm_results = rfm[["recency", "frequency", "monetary", "segment"]]
        self.rfm_results.index = self.rfm_results.index.astype(int)

    def save_to_csv(self, filename="rfm.csv"):

   """
    Saves RFM analysis results to a CSV file.

    Parameters:
    filename (str, optional): The name of the CSV file to save the results. Default is 'rfm.csv'.
    """
        
        self.rfm_results.to_csv(filename)
        print(f"RFM analysis results saved to {filename}")

# df = pd.read_csv("......")
rfm_analyzer = RFMAnalysis(df)
rfm_analyzer.prepare_data()
rfm_analyzer.calculate_rfm()
rfm_analyzer.save_to_csv()

