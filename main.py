import pymysql
from flask import jsonify, request
from config import mysql
from app import app
from datetime import datetime


@app.route('/addaccount', methods=['POST'])
def addAccount():
    try:
        conn = mysql.connect()
        _json = request.form
        name = _json['name']
        phone_number = _json['phone_number']
        whatsapp_number = _json['whatsapp_number']
        state = _json['state']
        pincode = _json['pincode']
        address = _json['address']
        type = _json['type']

        if name and phone_number and whatsapp_number and address and pincode and state and request.method == 'POST':
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO `accounts` (`name`, `phone_number`, `whatsapp_number`, `state`, `pincode`, `address`,`type`) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            bindData = (name, phone_number, whatsapp_number, state, pincode, address, type)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            message = {
                'error': False,
                'message': 'farmer added successfully!'}
            respone = jsonify(message)
            respone.status_code = 200
            return respone
        else:
            not_found()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/accounts/<string:type>')
def getAccounts(type):
    conn = mysql.connect()

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT id, name, phone_number, whatsapp_number, state, pincode, address, type FROM accounts WHERE `type` = %s ",
            type)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/account/<int:id>/<string:type>')
def account(id, type):
    conn = mysql.connect()

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            f"SELECT * FROM accounts WHERE id = {id} AND type = {type}")
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/account/<string:phone>')
def validateAccount(phone):
    conn = mysql.connect()

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            f"SELECT id, name, phone_number, whatsapp_number, state, pincode, address, type FROM accounts WHERE phone_number = {phone}")
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['PUT'])
def accounts():
    try:
        _json = request.form
        _id = _json['id']
        _name = _json['name']
        _phone_number = _json['phone_number']
        _whatsapp_number = _json['whatsapp_number']
        _address = _json['address']
        _pincode = _json['pincode']
        _state = _json['state']
        if _name and _phone_number and _whatsapp_number and _address and _pincode and _state and request.method == 'PUT':
            sqlQuery = "UPDATE accounts SET name=%s, phone_number=%s, whatsapp_number=%s, address=%s, state = %s, pincode= %s WHERE id=%s"
            bindData = (_name, _phone_number, _whatsapp_number, _address, _state, _pincode, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Farmer updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>', methods=['DELETE'])
def deleteAccount(id):
    conn = mysql.connect()

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM accounts WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('Farmer deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Products Calls
@app.route('/addproduct', methods=['POST'])
def addProduct():
    try:
        conn = mysql.connect()
        _json = request.form
        farmerId = _json['farmer_id']
        title = _json['title']
        price = _json['price']
        stock = _json['stock']
        quality = _json['quality']
        status = _json['status']
        today = datetime.now()
        if farmerId and title and quality and stock and price and status and request.method == 'POST':
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO `product` (`farmer_id`, `title`, `price`, `stock`, `quality`,`created_at`,`status`) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            bindData = (farmerId, title, price, stock, quality, today, status)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            message = {
                'error': False,
                'message': 'product added successfully!'}
            respone = jsonify(message)
            respone.status_code = 200
            return respone
        else:
            not_found()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/products')
def products():
    conn = mysql.connect()

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM product")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/products/<int:id>')
def farmerProducts(id):
    conn = mysql.connect()

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM product WHERE farmer_id = %s", id)
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

print()
# Products Calls
@app.route('/addcomment', methods=['POST'])
def addComment():
    try:
        conn = mysql.connect()
        _json = request.form
        productId = _json['product_id']
        customerId=_json['customer_id']
        comment = _json['title']

        if productId and comment and request.method == 'POST':
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO `feedback` (`product_id`,`customer_id`,`comment`) VALUES(%s, %s, %s)"
            bindData = (productId,customerId, comment)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            message = {
                'error': False,
                'message': 'your feedback added successfully!'}
            respone = jsonify(message)
            respone.status_code = 200
            return respone
        else:
            not_found()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/comments/<int:id>')
def comments(id):
    conn = mysql.connect()

    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            f"SELECT * FROM feedback WHERE product_id = {id}")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run(debug=True,ssl_context='adhoc')
