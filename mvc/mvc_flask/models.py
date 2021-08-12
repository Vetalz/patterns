import sqlite3


class Model:
    def __init__(self, app):
        self.app = app
        self.db = None
        self.cur = None
        self.table_name = 'product_list'

    def connect_db(self):
        db = sqlite3.connect(self.app.config['DATABASE'])
        db.row_factory = sqlite3.Row
        self.cur = db.cursor()
        self.db = db
        return db

    def create_table(self, data_base):
        db = sqlite3.connect(data_base)
        cur = db.cursor()
        sql = f'CREATE TABLE IF NOT EXISTS {self.table_name} ' \
              f'(id integer PRIMARY KEY AUTOINCREMENT, ' \
              f'product text NOT NULL, ' \
              f'quantity float NOT NULL);'
        cur.execute(sql)
        db.commit()
        db.close()

    def get_product(self):
        sql = f'SELECT * FROM {self.table_name}'
        try:
            self.cur.execute(sql)
            res = self.cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка чтения бд ' + str(e))
        return []

    def add_product(self, product, quantity):
        try:
            sql = f'INSERT INTO {self.table_name} VALUES (NULL, "{product}", "{quantity}")'
            self.cur.execute(sql)
            self.db.commit()
        except sqlite3.Error as e:
            print('Error ' + str(e))
            return False
        return True

    def del_product(self, product_id):
        try:
            sql = f'DELETE FROM {self.table_name} WHERE id="{product_id}"'
            print(sql)
            self.cur.execute(sql)
            self.db.commit()
        except sqlite3.Error as e:
            print('Error ' + str(e))
            return False
        return True

    def update_product(self, product_id, quantity):
        try:
            sql = f'UPDATE {self.table_name} SET quantity = {quantity} WHERE id="{product_id}"'
            print(sql)
            self.cur.execute(sql)
            self.db.commit()
        except sqlite3.Error as e:
            print('Error ' + str(e))
            return False
        return True


if __name__ == '__main__':
    model = Model(None)
    model.create_table('products.sqlite')
