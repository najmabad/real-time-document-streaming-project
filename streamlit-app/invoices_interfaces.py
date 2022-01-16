# color is ffde59
import pymongo
import streamlit as st
from pandas import DataFrame

client = pymongo.MongoClient(
    "mongodb://localhost:27017/", username="root", password="example"
)
db = client["docstreaming"]
collection = db["invoices"]


st.title("What did your customer buy?")


# add a input field for the customer id
cust_id = st.sidebar.text_input("CustomerID:")  # example: 17850

if cust_id:
    query = {"CustomerID": cust_id}
    docs = collection.find(
        query,
        {
            "_id": 0,
            "StockCode": 0,
            "Description": 0,
            "Quantity": 0,
            "Country": 0,
            "UnitPrice": 0,
        },
    )

    # create dataframe from resulting documents to use drop_duplicates
    df = DataFrame(docs)

    # drop duplicates, but keep the first one
    df.drop_duplicates(subset="InvoiceNo", keep="first", inplace=True)

    # add the table with a headline
    st.header("Customer Invoices")
    table = st.dataframe(data=df)


# add a input field for the invoice number
inv_no = st.sidebar.text_input("InvoiceNo:")

if inv_no:
    query = {"InvoiceNo": inv_no}
    docs = collection.find(
        query, {"_id": 0, "InvoiceDate": 0, "Country": 0, "CustomerID": 0}
    )

    # create the dataframe
    df = DataFrame(docs)

    # sort columns
    df = df[["InvoiceNo", "StockCode", "Description", "Quantity", "UnitPrice"]]

    # add the table with a headline
    st.header("Items by Invoice ID")
    table = st.dataframe(data=df)
