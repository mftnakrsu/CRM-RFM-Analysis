#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
create : Mef

This script is used for performing RFM analysis. RFM analysis is an important method for customer segmentation and marketing strategy development.
"""

import pandas as pd
import datetime as dt

def create_rfm(dataframe, csv=False):
    """
    Performs RFM analysis on the given DataFrame and returns the results.

    Parameters:
        dataframe (pd.DataFrame): The DataFrame on which RFM analysis will be performed.
        csv (bool, optional): Determines whether RFM results will be saved to a CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing RFM analysis results.
    """

    # DATA PREPARATION

    # Calculate total spending per customer
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]

    # Remove missing data
    dataframe.dropna(inplace=True)

    # Remove canceled transactions (containing "C")
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]

    # CALCULATION OF RFM METRICS

    today_date = dt.datetime(2011, 12, 11)

    rfm = dataframe.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                                'Invoice': lambda num: num.nunique(),
                                                "TotalPrice": lambda price: price.sum()})

    rfm.columns = ['recency', 'frequency', "monetary"]

    rfm = rfm[(rfm['monetary'] > 0)]

    # CALCULATION OF RFM SCORES

    # Recency scores
    rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])

    # Frequency scores
    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

    # Monetary scores
    rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

    # Combine RFM scores to create RFM_SCORE
    rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str)

    # SEGMENT NAMING

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

    rfm = rfm[["recency", "frequency", "monetary", "segment"]]
    rfm.index = rfm.index.astype(int)

    if csv:
        rfm.to_csv("rfm.csv")

    return rfm

# CRM analizi yapıldıktan sonra alınan aksiyonlardan sonra takibinin yapılamsı lazım
# bu fonksiyonların zaman geçtikçe tekrar tekrar çalıştırılıp takibinin yapılması gerekiyor

# Copy the DataFrame and perform RFM analysis
df = df_.copy()
rfm_new = create_rfm(df, csv=True)
