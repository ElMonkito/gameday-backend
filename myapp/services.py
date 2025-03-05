import os
import pandas as pd
from django.conf import settings

from backend.settings import BASE_DIR

UPLOAD_FOLDER = settings.UPLOAD_FOLDER

def get_latest_csv():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.csv')]
    if not files:
        return None

    files.sort(key=lambda x: os.path.getmtime(os.path.join(UPLOAD_FOLDER, x)), reverse=True)
    latest_file = os.path.join(UPLOAD_FOLDER, files[0])
    return latest_file

def read_csv():
    latest_csv = get_latest_csv()
    if not latest_csv:
        return {"error": "No CSV file found"}, 400

    try:
        df = pd.read_csv(latest_csv, sep=';')
        df = df.fillna("")
        return df.to_dict(orient='records'), 200
    except pd.errors.EmptyDataError:
        return {"error": "CSV file is empty"}, 400
    except pd.errors.ParserError:
        return {"error": "CSV file is not properly formatted"}, 400
    except Exception as e:
        return {"error": str(e)}, 500
