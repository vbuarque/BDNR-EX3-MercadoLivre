from pymongo import MongoClient

def connect():
    client = MongoClient("mongodb+srv://admin:TjoUK0O8nTXlzQ30@vinicius.t09er.mongodb.net")
    mydb = client.mercadolivre
    return mydb


    