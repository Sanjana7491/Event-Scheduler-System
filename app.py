from flask import Flask, request, jsonify
import json
import uuid
from datetime import datetime
from utils import load_events, save_events

app = Flask(__name__)
DATA_FILE = 'events.json'

@app.route('/events', methods=['GET'])
def list_events():
    events = sorted(load_events(), key=lambda x: x['start_time'])
    return jsonify(events), 200

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    required_fields = ['title', 'description', 'start_time', 'end_time']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400
    event = {
        "id": str(uuid.uuid4()),
        "title": data['title'],
        "description": data['description'],
        "start_time": data['start_time'],
        "end_time": data['end_time']
    }
    events = load_events()
    events.append(event)
    save_events(events)
    return jsonify(event), 201

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    events = load_events()
    for event in events:
        if event['id'] == event_id:
            event.update({k: data[k] for k in data if k in event})
            save_events(events)
            return jsonify(event), 200
    return jsonify({'error': 'Event not found'}), 404

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    events = [e for e in events if e['id'] != event_id]
    save_events(events)
    return jsonify({'message': 'Event deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

