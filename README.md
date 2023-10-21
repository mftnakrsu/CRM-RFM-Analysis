# Customer Segmentation with RFM

## Project Introduction

Welcome to the "Customer Segmentation with RFM" project! In this project, we aim to demonstrate the process of customer segmentation using RFM analysis, a valuable technique for marketing and business strategy.  



### Project Goals

- Segment the e-commerce company's customers into meaningful groups.
- Develop targeted marketing strategies based on these customer segments.
- Gain insights into customer behavior and preferences.

This project will guide you through the steps of data understanding, preparation, RFM metrics calculation, and the creation of RFM segments. It will provide you with valuable insights into the dataset and demonstrate the power of RFM analysis in improving marketing efforts.

<div align="center">
  <img src="https://www.next4biz.com/wp-content/webp-express/webp-images/uploads/2022/12/rfm-analizi-blog.jpg.webp" alt="RFM Analysis">
</div>

Let's get started with the project steps!

## Project Steps
1. [Business Problem](#business-problem)
2. [Data Understanding](#data-understanding)
3. [Data Preparation](#data-preparation)
4. [Calculating RFM Metrics](#calculating-rfm-metrics)
5. [Calculating RFM Scores](#calculating-rfm-scores)
6. [Creating & Analysing RFM Segments](#creating--analysing-rfm-segments)
7. [Functionality of the Whole Process](#functionality-of-the-whole-process)

## Dataset Story

An e-commerce company wants to segment its customers and determine marketing strategies based on these segments.

The dataset, named [Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II), includes the sales of an online retail store based in the UK between 01/12/2009 and 09/12/2011.

## Data Source

[Download the dataset here](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)

## Features

- **InvoiceNo:** Invoice number. A unique number for each transaction or invoice. If it starts with 'C', it's a canceled transaction.
- **StockCode:** Product code. A unique number for each product.
- **Description:** Product name.
- **Quantity:** Product quantity. Indicates how many of each product were sold in invoices.
- **InvoiceDate:** Invoice date and time.
- **UnitPrice:** Product price (in GBP).
- **CustomerID:** Unique customer number.
- **Country:** Country name. The country where the customer resides.

---

## How to Use
- Clone the project to your local machine.
- Use `pip install -r requirements.txt` to install the necessary dependencies.
- Run the main analysis file: `python main.py`.

## Contributing
If you would like to contribute, please submit a "Pull Request" or open an "Issue." Contributions are welcome!

## License
This project is open-source and licensed under the [MIT License](LICENSE).
