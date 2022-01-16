# Document Streaming Project for E-commerce dataset

## Introduction & Goals

## Contents
- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
- [Set Up](#set-up)


## The Data Set
- This project uses an e-commerce dataset that you can downlaod [here](https://www.kaggle.com/carrie1/ecommerce-data).
- It consists of invoices from a UK retailer between December 2010 and December 2011 (~540k rows and ~26k unique invoices).
- Fields in the datasets are: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, and Country.
- InvoiceNo is the invoice ID.
- One invoice can have one or more stock codes.
- Description, Quantity, and UnitPrice relate to stock codes.
- InvoiceDate, CustomerID, and Country relate to invoice numbers.
- Some invoices don't have a CustomerID and Quantity can be a negative number.

# Used Tools
- FastAPI and uvicorn: I created a Python API using the FastAPI framework and uvicorn as server to serve request.
- Kafka

## Set up

- **Step 1:** Clone the repository
- **Step 2:** Activate the virtual environment with `source venv/bin/activate`
- **Step 3[Optional]:** The data have already been converted into JSON. If you want to replicate this step, you can open the terminal and run `python data/csv_to_json.py`.
This will transform the data and saved them as `output.txt`.

Set up Kafka Topics:
1. Run the docker container: `sudo docker-compose -f docker-compose-kafka up`
2. Check the name of the container: `sudo docker ps`
3. Connect to the bash: `sudo docker exect -it <container_name> /bin/bash`
4. List all topics: `/opt/bitnami/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092`

