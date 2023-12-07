from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import db as dataBase
import json 

def connect(client_id):
     try:
          client = MongoClient(client_id) #localhost:27017
          db = client['library'] 
          collection = db['books'] 
          return collection
     except Exception as e:
          return e     
     

app = Flask(__name__)

@app.route('/')
def hello_name():
     return 'hello main page'

@app.route('/get/api/books',methods = ['GET'])
def get():
     
     collection = connect('mongodb://localhost:27017/')
     ls = []
     # returning from mongodb database
     cursor = collection.find({})
     for i in cursor:
          ls.append({
               'name':i['name'],
               'author':i['author'],
               'price':i['price'],
               'book_id':i['book_id']
          })
     
     return jsonify(ls)

@app.route('/post/api/books', methods=['POST'])
def post():
     try:
          dat = request.get_json()
     except Exception as e:
          return e
     
     ds = {
          'name'    : dat['name'],
          'author'  : dat['author'],
          'price'   : dat['price'],
          'book_id' : dat['book_id']
     }

     collection = connect('mongodb://localhost:27017/')
     
     if collection.count_documents({'book_id':dat['book_id']}) ==0:
          collection.insert_one(ds)
          return 'data added for book id : ' + str(ds['book_id'])
     else:
          return 'Duplicate entry book_id already exits'
     

@app.route('/put/api/books/<book_id>',methods=['PUT'])
def update(book_id):
     try:
          dat = request.get_json()
     except Exception as e:
          return e
     
     collection = connect('mongodb://localhost:27017/')
     if collection.count_documents({'book_id':book_id }) ==1:
          try:     
               collection.update_one({'book_id': book_id},  {"$set":dat})
               return 'change made to book id : '+ str(book_id)
          except Exception as e:
               return e
     else:
          return 'non-existant entry ( book_id not found )'
          

if __name__ == '__main__':
     app.run(debug=True,port=5000)
