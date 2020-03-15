import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request 

app = Flask(__name__)

# Подключение google sheets

scope = ['https://www.googleapis.com/auth/analytics', 
         'https://www.googleapis.com/auth/drive', 
         'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
        if request.method == 'POST':
                unit = request.form['unit']
                quantity = request.form['quantity']
                action = request.form['action']
                print(unit, quantity, action)
                if unit == '' or quantity == '':
                        return render_template('index.html', message = 'Указаны не все данные')
                sheet1 = client.open('easy-st-storage').sheet1
                if action == 'add':
                        index = 2
                        row = [unit, quantity]
                        print(row, index)
                        sheet1.insert_row(row, index)
                        return render_template('index.html', message = 'Добавлено')
                if action == 'remove':
                        index = 2
                        quantity = "-" + quantity
                        print (quantity)
                        row = [unit, quantity]
                        print(row, index)
                        sheet1.insert_row(row, index)
                        return render_template('index.html', message = 'Взято')





# 

# row = ["I'm", "Updating", "Spreadsheet"]
# index = 3
# sheet.insert_row(row, index)

# records = sheet.get_all_records()

# pp = pprint.PrettyPrinter()

# pp.pprint(records)

if __name__ == '__main__':
        app.debug = True
        app.run()