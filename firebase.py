import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("service_account_dev.json")
firebase_admin.initialize_app(cred)