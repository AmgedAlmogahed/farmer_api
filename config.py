from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'farmer_stock'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
