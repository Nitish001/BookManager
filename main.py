import requests
from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

mysql = MySQL()


def create_database():
    cursor.execute('''create table books_description(id int auto_increment primary key,book_id varchar(50),book_title varchar(500),stock_count int);''')

def update1(isbn,title,count):
    print(isbn,title,count)
    count = int(count)
    # cursor.execute('''select * from books_description;''')
    # rv = cursor.fetchall()
    # return str(rv)
    cursor.execute("""insert into books_description(book_id,book_title,stock_count) values (%s,%s,%s)""",(isbn,title,count))
    conn.commit()


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'shopclues'
app.config['MYSQL_DATABASE_DB'] = 'Project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/search/<str>')
def hello(str):
    data = requests.get('https://www.googleapis.com/books/v1/volumes?q='+str)
    # print(data)
    response = data.json()
    item = response['items']
    # list = {}
    # for i in item:
    #     x = i['volumeInfo']
    #     sportsArray = x.getJSONArray("industryIdentifiers");
    #     firstIsbn = sportsArray.getJSONObject(0);
    #     isbn = firstIsbn.getString("name");
    # # return item
    return render_template('view_search.html', data=item)

@app.route('/update' , methods=['POST'])
def updateInventory():
    stock = request.form['field1']
    book_id = request.form['field2']
    # count = request.form['field3']
    result = cursor.execute("""update books_description set stock_count=%s where book_id = %s""",
                   (stock,book_id))
    conn.commit()
    return result
@app.route('/search')
def search():
    return render_template('search.html')
# ..............
# @app.route('/hello')
# def hellodata():
#
#     r = requests.get('http://www.google.com')
#     return r.text
@app.route('/insert' ,methods=['POST','GET'])
def insert():
    if(request.method == "POST"):
        isbn = request.form['field1']
        title = request.form['field2']
        count = request.form['field3']
        count = int(count)
        # print(isbn+title+count)
        update1(isbn,title,count)
        list()
        return "none"
    else:
        return render_template('insert_books.html')

@app.route('/')
def list():
    cursor.execute('''select * from books_description;''')
    rv = cursor.fetchall()
    # print(rv)
    # return "none"
    return render_template('existing_books.html', data=rv)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)

