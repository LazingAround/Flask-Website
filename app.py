from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

count = 0
@app.route('/')
def home():  # put application's code here
    global count
    return render_template('home.html',count=count)
@app.route('/internet_protocol_addresses')
def internet_protocol_addresses():
    return render_template('internet_protocol_addresses.html')
@app.route('/data_packets')
def data_packets():
    name="John"
    return render_template('data_packets.html', person=name)
@app.route('/domain_name_systems')
def domain_name_systems():
    return render_template('domain_name_systems.html')
@app.route('/submit', methods=['POST'])
def submit():
    global count
    count += 1
    return redirect(url_for('home'))
@app.errorhandler(404)
def page_not_found():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
