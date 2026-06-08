import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

cred = credentials.Certificate("firebase_key.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://traffic-analytics-b32b5-default-rtdb.firebaseio.com/"
    })

def upload_data(vehicle_count, fps):
    ref = db.reference("traffic_data")

    ref.push({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vehicle_count": vehicle_count,
        "fps": round(fps, 2)
    })