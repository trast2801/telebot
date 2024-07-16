import sqlite3
from asyncio import sleep

path = "C:\\Users\\Konst\\PycharmProjects\\telebot2\\pythonProject\\sale_bot\\files\\"
path_media = "C:\\Users\\Konst\\PycharmProjects\\telebot2\\pythonProject\\sale_bot\\files\\media\\"
def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            id_telegram INTEGER NOT NULL,
            adress  TEXT NOT NULL
        );
    ''')
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS product(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             product_name TEXT NOT NULL,
             polotno TEXT NOT NULL,
             size TEXT NOT NULL,
             photo BLOB
    
         );
     """)

    cursor.execute("""
         CREATE TABLE IF NOT EXISTS price(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             id_product  INTEGER,
             price INTEGER NOT NULL
         );
     """)

    cursor.execute("""
         CREATE TABLE IF NOT EXISTS order_customer(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             id_user INTEGER,
             id_product INTEGER,
             id_price INTEGER,
             id_size INTEGER,
             data_order DATE NOT NULL,
             number_order TEXT NOT NULL,
             quantity INTEGER NOT NULL        
         );
     """)

def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_blob(name, photo, size, polotno):

        insert_blob_query = """INSERT INTO product
                                  (name, photo, size, polotno) VALUES (?, ?, ?, ?)"""
        emp_photo = convert_to_binary_data(photo)
        # Преобразование данных в формат кортежа
        data_tuple = (name, emp_photo, size, polotno)
        cursor.execute(insert_blob_query, data_tuple)
        connection.commit()
        #"Изображение и файл успешно вставлены как BLOB в таблиу"
        cursor.close()

def get_id_product():
    result = ()
    #conn = sqlite3.connect(path +' db_product.db')
    conn = sqlite3.connect(path + ' db_product.db')
    cur = conn.cursor()
    print("Подключен к SQLite")
    query =  """SELECT id FROM product"""
    cur.execute(query)
    result = cur.fetchall()
    return result

def get_product_from_basket(id, cursor):

    sql_fetch_blob_query = """SELECT  product.name, product.polotno,	product.size, price.pric 
                            FROM product, price
                            WHERE
                            product.id = price.id_product and product.id = ?"""
    cursor.execute(sql_fetch_blob_query, (id,))
    record = cursor.fetchall()

    for row in record:
        size    = row[2]
        name    = row[0]
        polotno = row[1]
        price   = row[3]

    #sql_get_price = """SELECT price from price where id = ? """
    #cursor.execute(sql_get_price, 2)
    #record = cursor.fetchone()

    rezult = f'{name}  из {polotno}  размер {size} цена за штуку {price} '
    return rezult

def get_product(id, cursor):

    global all_id
    #try:
    #conn = sqlite3.connect(path +'db_product.db')
    #cursor = conn.cursor()
    print("Подключен к SQLite")

    sql_fetch_blob_query = """SELECT * from product where id = ?"""
    cursor.execute(sql_fetch_blob_query, (id,))
    record = cursor.fetchall()
    query = """SELECT Count(*) FROM product"""
    cursor.execute(query)
    vsego_zapisei = cursor.fetchone()[0]
    query = """SELECT id FROM product"""
    cursor.execute(query)
    all_id = cursor.fetchall()
    print(all_id)
    return record, vsego_zapisei, all_id
'''        #for row in record:
         #   id      = row[0]
         #   name    = row[1]
         #   photo   = row[2]
         #   size    = row[3]
         #   polotno = row[4]
         # 
         #   print( id, name, photo, count)
        #cursor.close()
    #except sqlite3.Error as error:
    #    print("Ошибка при работе с SQLite", error)
    #finally:
    #    if conn:
    #       conn.close()
    #        print("Соединение с SQLite закрыто")
'''


def insert_user(name, id_teleg, adress, phone,cursor, connection):

    ss = """ SELECT id_telegram  FROM users WHERE id_telegram = ?"""
    data_tuple = (id_teleg,)
    cursor.execute(ss, data_tuple)
    record = cursor.fetchone()
    if record == None:
        try:
            insert_blob_query = """INSERT INTO users
                                               (name, id_telegram, adress, phone) VALUES (?, ?, ?, ?)"""
            data_tuple = (name, id_teleg, adress, phone)
            cursor.execute(insert_blob_query, data_tuple)
        except sqlite3.Error as err:
            print(err)
        finally:
            connection.commit()

def write_order_bd(id_user, custom_basket, number_order, data_order, cursor, connection):
    if custom_basket == {}:
        return
    else:
        for key in custom_basket:
            product = key
            quantity = custom_basket[key]
            sql_get = """ SELECT size FROM product WHERE id = ?"""
            data_tuple = (product,)
            cursor.execute(sql_get, data_tuple)
            size = cursor.fetchall()
            sql_get = """ SELECT pric FROM price WHERE id = ?"""
            data_tuple = (product,)
            sql_write = """ INSERT INTO order_customer 
                            (id_user, id_product, id_price, id_size, data_order, number_order, quantity)
                            VALUES (?,?,?,?,?,?,?)"""
            data_tuple = (id_user, product, price, size, data_order, number_order, quantity)
            cursor.execute(sql_write,data_tuple)
            connection.commit()


'''
    ss = """ SELECT id_telegram  FROM users WHERE id_telegram = ?"""
    
    data_tuple = (id_teleg,)
    cursor.execute(ss,data_tuple)
    record = cursor.fetchone()
    #if record != None:
'''


'''
#convert_to_binary_data('C:\\Users\\Konst\\PycharmProjects\\telebot2
# \\pythonProject\\sale_bot\\files\\media\\2.jpg')

ss='C:\\Users\\Konst\\PycharmProjects\\telebot2\\pythonProject\\sale_bot\\files\\media\\4.jpg'
connection = sqlite3.connect(path +'db_product.db')
cursor = conn.cursor()
init_db()
connection.commit()
cursor.close()
#insert_blob('4 футболка', ss, 40, 'красивое')
rr = get_product(3)
insert_user('Иванов', 19292929, 'Москва, красная площадь, дом 1')
'''