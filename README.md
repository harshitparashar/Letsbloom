# Letsbloom Placement Drive Assignment

Name : Harshit Parashar 
IIT Delhi

For this assignment we have used Flask.

libraries to import: pymongo, flask, json

Step 1: create a virtual environment 
step 2: import all dependencies
step 3: connect the monogodb localhost:27017 database using mongodb compass (we have used database named - 'library' and collection named - 'books')
step 4: open the directory in which our app.py file is located in powershell
step 5: run the code using script - 'python .\app.py'
step 6: api could be tested using the endpoints :-
        get/api/books
        post/api/books
        put/api/books/{book_id}
I have used 'book_id' as the primary key in our database
I have tested API using 'thunderclient' and for body of query JSON format was used as follows:
  {
               'name':_String_,
               'author':_String_,
               'price':_int_,
               'book_id':_int_
  }

