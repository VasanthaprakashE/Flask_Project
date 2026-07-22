from gspread_config import cred
from flask import  Flask, render_template
import pandas as pd

app = Flask(__name__)

def data():
    config = cred('credential.json')
    sheet = config.open('Gspread')
    print('Succesfully connect with Gspread')
    return sheet, 'Succesfully connect with Gspread'

@app.route('/')
def home():
    sheet, mes = data()

    datasheet = sheet.get_worksheet(0)

    records = datasheet.get_all_records()

    df =pd.DataFrame(records)

    df= df[df['Zone']!='']

    total_rows = len(df)
    total_zone = df["Zone"].nunique()

    html_table = df.to_html(
    classes="table table-hover table-striped table-bordered align-middle text-center",
    index=False,
    border=0
)

    from datetime import datetime
    today = datetime.now().strftime("%d-%m-%Y")
    
    return render_template(
        'index.html',
        message=mes,
        table = html_table,    
        total_rows=total_rows,
        total_zone=total_zone,
        date= today)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)