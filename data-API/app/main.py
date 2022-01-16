import json
from typing import Optional

import pytz
from dateutil.parser import parse
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from kafka import KafkaProducer
from pydantic import BaseModel


# define the schema (data shape) for the request body
class InvoiceItem(BaseModel):
    InvoiceNo: str
    StockCode: str
    Description: Optional[str] = None
    Quantity: int
    InvoiceDate: str  # InvoiceDate is ingested as string and then converted to ISO 8601  # noqa: E501
    UnitPrice: float
    CustomerID: Optional[
        float
    ] = None  # CustomerID is ingested as a float and converted into string
    Country: str


# if you change the name remember to pass it correctly to uvicorn
app = FastAPI()

@app.get("/")
async def test_api_connection():
    return {"msg": "API is connected"}


@app.post("/invoiceitem")
async def post_invoice_item(item: InvoiceItem):
    """POST a new invoice item.

    Dates are converted to ISO-8601 and CustomerID is cast as a string.
    The item is then converted to a JSON string and sent to Kafka as a
    message.
    """
    try:
        # convert date to ISO-8601 and add timezone information
        date = parse(item.InvoiceDate, dayfirst=False)
        date_tz = pytz.timezone("Europe/London").localize(date)
        item.InvoiceDate = date_tz.isoformat()

        # cast CustomerID into string
        if item.CustomerID:
            item.CustomerID = str(item.CustomerID).split(".")[0]

        # parse item back to json and dumpt it as JSON string
        item_json = jsonable_encoder(item)
        item_json_str = json.dumps(item_json)

        # send message to Kafka
        produce_kafka_string(item_json_str)

        # return JSON to the client
        return JSONResponse(content=item_json, status_code=201)

    except ValueError:
        return JSONResponse(content=jsonable_encoder(item), status_code=400)


def produce_kafka_string(json_as_string):
    """Create Kafka Producer.

    A Kafka Producer needs to be created with a bootstrap-server.
    This will be address of the server the producer first connects to
    in order to discover the Kafka network.

    If the producer runs locally (i.e. external to the Docker network
    where we set Kafka up), the address must be the one for external clients
    (e.g. localhost:9093 in our Docker compose file example).

    If the producer runs within the same Docker network, the address must be
    the one for internal clients (e.g. kafka:9092 in our Docker compose file).

    Acks is set to 1 because we want to have a confirmation message
    from the broker but we don't have a replication strategy in our set-up.
    If you do, you can set acks='all'.

    Finally, this function assumes that a topic called `ingestion-tipic` has been
    created on Kafka.
    """
    producer = KafkaProducer(bootstrap_servers="kafka:9092", acks=1)

    # Kafka messages are stored as bytes
    producer.send("ingestion-topic", bytes(json_as_string, "utf-8"))
    producer.flush()
