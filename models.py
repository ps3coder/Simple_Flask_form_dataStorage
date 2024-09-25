from config import get_db_connection
from datetime import datetime

class SubmissionModel:
    def __init__(self):
        self.db = get_db_connection()
        self.collection = self.db["data"]

    def save_submission(self, data):
        data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Add timestamp
        self.collection.insert_one(data)

    def get_submissions(self):
        submissions = list(self.collection.find({}, {"_id": 0}))  # Omit ObjectId
        return submissions
