import bdConnect as connectDB
from pprint import pprint

def findSort():
    mydb = connectDB.connect()
    mycol = mydb.product
    print("\n==============================")
    print("============PRODUTOS==========") 
    print("==============================\n")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        pprint(x)
    print("Todos os produtos cadastrados no sistema.")

def insert(name, description):
    mydb = connectDB.connect()
    mycol = mydb.product
    print("\n==========================")
    print("===========INSERT=========") 
    print("==========================\n")
    mydict = { "nome": name, "descricao": description }
    x = mycol.insert_one(mydict)
    pprint(x.inserted_id)
    print("Seu produto foi cadastrado no sistema.")

def findQuery(name):
    mydb = connectDB.connect()
    mycol = mydb.product
    print("\n===========================")
    print("============SEARCH=========") 
    print("===========================\n")
    myquery = { "nome": name }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        pprint(x)
    print("Seu produto foi pesquisado no sistema.")

def update(name, newName):
    mydb = connectDB.connect()
    mycol = mydb.product
    print("\n============================")
    print("============UPDATE==========") 
    print("============================\n")
    myquery = { "nome": name }
    newvalues = { "$set":   { "nome": newName } }
    mycol.update_one(myquery, newvalues)
    pprint("Seu produto foi atualizado no sistema.")

def delete(name):
    mydb = connectDB.connect()
    mycol = mydb.product
    print("\n==========================")
    print("============DELETE==========") 
    print("==========================\n")
    myquery = { "nome": name }
    mycol.delete_one(myquery)
    pprint("Seu produto foi deletado do sistma.")