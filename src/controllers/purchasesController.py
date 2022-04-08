import bdConnect as connectDB
from pprint import pprint

def findSort():
    mydb = connectDB.connect()
    mycol = mydb.purchases
    print("\n============================")
    print("==== COMPRAS =======") 
    print("=============================\n")
    mydoc = mycol.find().sort("data")
    for x in mydoc:
        pprint(x)
    pprint("Todas as suas compras.")

def insert(user, sellerName, price):
    mydb = connectDB.connect()
    mycol = mydb.purchases
    print("\n=======================")
    print("=== INSERT ===") 
    print("=======================\n")
    mydict = { "usuario": user, "vendedor": sellerName, "total": price }
    x = mycol.insert_one(mydict)
    pprint(x.inserted_id)
    pprint("Sua compra foi cadastrada no sistema.")

def findQuery(id):
    mydb = connectDB.connect()
    mycol = mydb.purchases
    print("\n========================")
    print("==== SEARCH ====") 
    print("========================\n")
    myquery = { "_id": id }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        pprint(x)
    pprint("Sua compra pesquisada no sistema.")

def update(id, newPrice):
    mydb = connectDB.connect()
    mycol = mydb.purchases
    print("\n===========================")
    print("==== UPDATE ====") 
    print("===========================\n")
    myquery = { "_id": id }
    newvalues = { "$set":   { "preco_total": newPrice } }
    mycol.update_one(myquery, newvalues)
    pprint("Sua compra foi atualizada no sistema.")

def delete(id):
    mydb = connectDB.connect()
    mycol = mydb.purchases
    print("\n=========================")
    print("==== DELETE ====") 
    print("=========================\n")
    myquery = { "_id": id }
    mycol.delete_one(myquery)
    pprint("Sua compra foi removida do sistema.")