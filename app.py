from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['search_term']
    results = []
    with open('data/breaches.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if query.lower() in row['Name'].lower():
                results.append(row)
    with open('data/breaches.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        for item in data:
            if isinstance(item, dict) and 'Name' in item and query.lower() in item['Name'].lower():
                results.append(item)
    with open('data/passwords.txt', 'r') as txtfile:
        for line in txtfile:
            if query.lower() in line.lower():
                results.append({'Name': 'Password', 'Description': line.strip()})
    return render_template('search.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)