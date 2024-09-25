import json
from bson import ObjectId

def json_serializable(data):
    """Convert ObjectId to a string for JSON serialization."""
    if isinstance(data, list):
        for item in data:
            if isinstance(item.get('_id'), ObjectId):
                item['_id'] = str(item['_id'])
    elif isinstance(data, dict):
        if isinstance(data.get('_id'), ObjectId):
            data['_id'] = str(data['_id'])
    return data

def save_to_json(submissions):
    """Save submissions to a JSON file."""
    submissions = json_serializable(submissions)  
    with open('submissions.json', 'w') as file:
        json.dump(submissions, file, indent=4)
