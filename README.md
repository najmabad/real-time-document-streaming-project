# Document Streaming Project for e-commerce dataset

## Introduction & Goals

This project is an end-to-end pipeline.
It processes invoices data and creates a dashboard where it's possible to:
- fetch all invoices related to a customer
- fetch all items related to an invoice

## Contents
- [The Data Set](#the-data-set)
- [Set Up](#set-up)


## The Data Set
- This project uses an e-commerce dataset that you can download [here](https://www.kaggle.com/carrie1/ecommerce-data).
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
- **Step 2.** Create a virtual env with `sudo python3 -m venv ./venv` and activate it with `source venv/bin/activate`. Once this is done, install the requirements `pip install -r requirements.txt`
- **Step 3.** Create a folder `mongodb-data` to save data locally
- **Step 4.** Download the data from [here](https://www.kaggle.com/carrie1/ecommerce-data) and save the under the `data` folder.
- **Step 5.** Convert csv data into JSON: `sudo python data/csv_to_json.py`. This will transform the data and saved them as `output.txt`
- **Step 6.** Create the `data-api` image:
    1. Navigate to the `Data API` folder: `cd data-api`
    2. Run `sudo docker build -t data-api`.
    3. This creates a new image called `data-api` on your machine that Docker can build. To check all available images, run `sudo docker images`  
- **Step 7.** Start docker containers: `sudo docker-compose -f docker-compose-kafka-spark-mongodb.yml up`. Verify that all containers are runnign with `sudo docker ps`.
- **Step 8.** Set up the kafka topic:
    1. Check the name of the container: `sudo docker ps`
    2. Connect to the bash: `sudo docker exect -it <container_name> /bin/bash`
    3. List all topics: `/opt/bitnami/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092`
    4. Create a topic: `opt/bitnami/kafka/bin/kafka-topics.sh --create --topic ingestion-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
- **Step 9.** Open the Jupyter Notebook PySpark. This should be on `localhost:8888`. This might ask you for a passwork/token that you can find in the logs generated when you started the containers. Leave this open (it will process messages as they are ingested by Kafka). Run all cell of the PySpark notebook.
- **Step 10.** Open the UI of Mongo DB. This should be on `localhost:8081` with the password set in the docker compose file. Then:
    1. Create a database called `docstreaming` 
    2. Inside docstreaming, create a collection called `invoices`
- **Step 11.** Go to the `data` directory and run `python data-api-client.py` to send the data to MongoDB. If everything is running correctly, you should see documents population the MongoDB interface.
- **Step 12.** Run `streamilit run invoices_interfaces.py`. This will open a window in your browser (localhost:8501) from which you can query invoices by customer ID and invoices items by Invoice ID.

I hope you enjoyed it!

## Presentation

![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/1.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/2.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/3.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/4.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/5.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/6.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/7.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/8.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/9.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/10.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/11.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/12.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/13.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/14.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/15.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/16.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/17.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/18.png)

---
![alt text](https://github.com/najmabad/document-streaming-project/blob/master/presentation/19.png)



