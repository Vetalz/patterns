import os
from flask import Flask, g, request, flash, render_template

DEBUG = True
SECRET_KEY = 'vgr54ftrbr3'

app = Flask('product_list')
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'products.sqlite')))



