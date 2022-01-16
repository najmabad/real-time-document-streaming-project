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


## data-API image
This project uses a customer docker image to run the data API with docker. To recreate the image on your local machine navigate to the `Data API` folder and run `sudo docker build -t data-api. This creates a new image called `data-api` on your machine that Docker can build.
To check all available images, run `sudo docker images`

## Access Spark Jupyter Notebooks
Spark is also run on a Docker container. This is automatically set-up with the `docker-compose-kafka-spark-mongo.yml` file.
To work with the notebooks, open with your browser the `localhost:/8888`. This might ask you for a passwork/token that you can find in the logs generated when you started the containers.

Once you ran the containers:
- go to mongodb and create a database called `docstreaming` and a collection called `invoices`



### Push the Data API to Docker
Once you have created your data API locally, you might want to push it to Docker. This can be done as follows:
1. Create a `dockerfile` to be able to build your container. See example in the `data API` folder.
2. Create a `requirements.txt` which contains the necessary libraries. See example in the `data API` folder.
3. Before deploying, change the `bootstrap_server` parameter of the KafkaProducer to the address available to internal clients (in our case this is `kafka:9092).
4. Navigate to the `Data API` folder and run `sudo docker build -t <image_name>`. This creates a new image on your machine that Docker can build.
5. To check all available images, run `sudo docker images`


Is important that your API, Kafka, Spark, and MongoDB container all run under the same docker container network.

