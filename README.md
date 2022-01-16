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


## Set up
This was built on a Linux machine, if you are on a Mac you can probably avoid `sudo` in front of most commands.

- **Step 1.** Clone the repository to your local machine
- **Step 2.** Activate the virtual environment with `source venv/bin/activate` and then install the requirements `pip install -r requirements.txt`
- **Step 3.** Create a folder `mongodb-data` to save data locally
- **Step 4.** Downlaod the data from [here](https://www.kaggle.com/carrie1/ecommerce-data)
- **Step 5.** Convert csv data into JSON: `sudo python data/csv_to_json.py`. This will transform the data and saved them as `output.txt`
- **Step 6.** Start docker containers: `sudo docker-compose -f docker-compose-kafka-spark-mongodb.yml up`
- **Step 7.** Set up the kafka topic:
    1. Check the name of the container: `sudo docker ps`
    2. Connect to the bash: `sudo docker exect -it <container_name> /bin/bash`
    3. List all topics: `/opt/bitnami/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092`
    4. Create a topic: `opt/bitnami/kafka/bin/kafka-topics.sh --create --topic ingestion-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
- **Step 8.** Create the `data-api` image:
    1. Nvigate to the `Data API` folder: `cd data-api`
    2. Run `sudo docker build -t data-api.
    3. This creates a new image called `data-api` on your machine that Docker can build. To check all available images, run `sudo docker images`  
- **Step 9.** Open the Jupyter Notebook PySpark. This should be on `localhost:8888`. This might ask you for a passwork/token that you can find in the logs generated when you started the containers.
- **Step 10.** Open the UI of Mongo DB. This should be on `localhost:8081` and:
    1. Create a database called `documentstreaming` 
    2. Create a collection called `invoices




