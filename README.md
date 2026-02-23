# Supermarket-Sales-Performance-Analysis
Built an end-to-end batch data pipeline to process supermarket sales data, including extraction, cleaning, validation, and loading using Airflow and PostgreSQL. Applied data quality checks with Great Expectations and delivered business insights through Elasticsearch and Kibana dashboards to support data-driven sales and pricing decisions.

# Repository Outline

Bagian ini menjelaskan secara singkat konten dari file yang dipush ke repository.

P2M3_Kevin_Hibatul_DAG_graph.png

Berisi visualisasi alur ETL yang diotomasi menggunakan Apache Airflow.

P2M3_Kevin_Hibatul_ddl.txt

Berisi query SQL untuk membuat tabel dan melakukan insert data ke PostgreSQL.

P2M3_Kevin_Hibatul_GX.ipynb

Notebook Great Expectations untuk validasi kualitas data setelah proses ETL.

P2M3_Kevin_Hibatul_DAG.py

Berisi script DAG untuk melakukan ekstraksi data dari PostgreSQL, transformasi data, dan load data ke Elasticsearch.

P2M3_Kevin_Hibatul_data_raw.csv

Data mentah hasil ekstraksi dari PostgreSQL.

P2M3_Kevin_Hibatul_data_clean.csv

Data hasil transformasi yang sudah siap dimasukkan ke Elasticsearch.

# Problem Background

Sebuah perusahaan supermarket nasional ingin memahami performa penjualan produknya berdasarkan kategori, region, waktu, dan strategi diskon. Meskipun perusahaan memiliki data transaksi yang lengkap, data tersebut belum terstruktur dengan baik untuk dianalisis secara konsisten dan berkelanjutan.

Manajemen menghadapi beberapa tantangan, seperti:

Perbedaan kontribusi penjualan antar region

Ketidakseimbangan profit antar kategori produk

Strategi diskon yang berpotensi menurunkan margin keuntungan

Fluktuasi penjualan dalam periode waktu tertentu

Project ini dibuat untuk membangun pipeline data terstruktur dan dashboard analitik yang mendukung pengambilan keputusan berbasis data (data-driven decision making).

# Project Output

Project ini menghasilkan sistem end-to-end data pipeline dan dashboard analitik yang mencakup:

1. Automated Data Pipeline

Ekstraksi data dari PostgreSQL

Transformasi dan pembersihan data

Load data ke Elasticsearch

Orkestrasi proses menggunakan Apache Airflow

2. Data Validation

Validasi kualitas data menggunakan Great Expectations

Penerapan 7 data quality expectations

Menjamin data bersih dan siap dianalisis

3. Interactive Dashboard (Kibana)

Dashboard menampilkan:

Total Sales

Sales Trend (time series)

Sales by Category

Sales by Region

Profit vs Discount analysis

Insight & Business Recommendation (Markdown)

Dashboard ini membantu manajemen memahami pola penjualan dan dampak strategi diskon terhadap profit.

# Data

Dataset yang digunakan adalah Supermart Grocery Sales Dataset yang diperoleh dari Kaggle:

URL:
https://www.kaggle.com/datasets/brijbhushannanda1979/supermart-grocery-sales-retail-analytics-dataset

Dataset terdiri dari sekitar 9.900+ baris data transaksi dengan kolom sebagai berikut:

Order ID

Customer Name

Category

Sub Category

City

Order Date

Region

Sales

Discount

Profit

State

Data merepresentasikan transaksi supermarket di berbagai region dan digunakan untuk analisis performa penjualan dan profitabilitas.

# Method

Tahapan yang dilakukan dalam project ini:

Extract

Mengambil data dari PostgreSQL sebagai source database.

Transform

Membersihkan data (data cleaning).

Menyesuaikan tipe data.

Standarisasi nama kolom.

Load

Menyimpan data bersih ke Elasticsearch sebagai data warehouse untuk analitik.

Data Validation (Quality Control)

Menggunakan Great Expectations untuk memastikan:

Keunikan data

Validasi range nilai

Validasi tipe data

Validasi domain value

Visualization

Membuat dashboard interaktif menggunakan Kibana untuk eksplorasi dan insight bisnis.

# Stacks
Programming Language

Python

SQL

# Libraries

pandas

psycopg2

datetime

airflow

airflow.operators.python

elasticsearch (Elasticsearch, helpers)

great_expectations

csv

re

# Container

Docker

# Database

PostgreSQL

Elasticsearch

# Orchestrator

Apache Airflow

# Visualization

Kibana

# Reference

Dataset URL:
https://www.kaggle.com/datasets/brijbhushannanda1979/supermart-grocery-sales-retail-analytics-dataset

Documentation:

https://airflow.apache.org/

https://greatexpectations.io/

https://www.elastic.co/kibana

https://www.postgresql.org/
