import json
import firebase_admin
from firebase_admin import credentials, firestore
from validate import validate_wandertrack_json

# 1. Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

if not validate_wandertrack_json("wandertrack.json"):
    exit(1)  # Cancel script if invalid

# 2. Load structured country & city data
with open('wandertrack.json', encoding='utf-8') as f:
    countries = json.load(f)

# 3. Upload each country document
for country in countries:
    doc_id = country["code"]
    db.collection("meta").document("countries").collection("all").document(doc_id).set(country)

print(f"✅ Uploaded {len(countries)} countries to Firestore.")
