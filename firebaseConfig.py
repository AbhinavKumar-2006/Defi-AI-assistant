import firebase_admin
from firebase_admin import db, firestore, credentials

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://defi-ai-assistant-default-rtdb.firebaseio.com/"
    })

rtdb = db
fs = firestore.client()