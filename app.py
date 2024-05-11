from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Read the Excel file
df = pd.read_excel('sales.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/age_group')
def age_group():
    return render_template('age_group.html')
 
@app.route('/aov')
def aov():
    return render_template('aov.html')
 
@app.route('/business')
def business():
    return render_template('business.html')
 
@app.route('/channel')
def channel():
    return render_template('channel.html')
 
@app.route('/gender')
def gender():
    return render_template('gender.html')

 
@app.route('/gender3d')
def gender3d():
    return render_template('gender3d.html')

 
@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/demographics')
def demographics():
    return render_template('demographics.html')

@app.route('/top_selling')
def top_selling():
    return render_template('top_selling.html')
 



@app.route('/data')
def get_data():
    # Convert DataFrame to JSON
    data_json = df.to_json(orient='records')
    return data_json








if __name__ == '__main__':
    app.run(debug=True)