from app_config import app, g, request, flash, render_template, DEBUG
from models import Model

model = Model(app)


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = model.connect_db()
        print(g.link_db)
    return True


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/', methods=['POST', 'GET'])
def index():
    if get_db():
        if request.method == 'POST':
            print(request.form)
            if request.form['btn'] == 'add':
                if len(request.form['product']) > 1 and float(request.form['quantity']) > 0:
                    res = model.add_product(request.form['product'], request.form['quantity'])
                else:
                    flash('ошибка1', category='error')
            elif request.form['btn'] == 'update':
                if len(request.form['quantity']) > 0 and float(request.form['quantity']) > 0:
                    res = model.update_product(request.form['product_id'], request.form['quantity'])
            else:
                print(request.form['product_id'])
                res = model.del_product(request.form['product_id'])
        return render_template('index.html', list=model.get_product(), title='Список продуктов')


if __name__ == '__main__':
    app.run(debug=DEBUG)
