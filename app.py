from flask import Flask, render_template, redirect, url_for
import random
app = Flask(__name__)

count = 0
@app.route('/')
def home():  # put application's code here
    global count
    display = False
    rand = random.randint(1, 5)
    if rand == 1:
        display = True
    return render_template('home.html',count=count,display=display)
@app.route('/internet_protocol_addresses')
def internet_protocol_addresses():
    return render_template('internet_protocol_addresses.html')
@app.route('/data_packets')
def data_packets():
    name="<i>John</i>"
    return render_template('data_packets.html', person=name)
@app.route('/domain_name_systems')
def domain_name_systems():
    return render_template('domain_name_systems.html')
@app.route('/submit', methods=['POST'])
def counter():
    global count
    count += 1
    return redirect(url_for('home'))
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
