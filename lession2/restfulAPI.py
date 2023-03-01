from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(
    'mongodb+srv://hieu5021:15021Koo@cluster0.gi0ijy1.mongodb.net/?retryWrites=true&w=majority')
db = client['mydatabase']
collection = db['mycollection']


@app.route('/api/data/them', methods=['GET'])
def data():
    return render_template('index.html'), 500
# GET all data


@app.route('/api/data', methods=['GET'])
def get_all_data():
    output = []
    for data in collection.find():
        output.append(
            {'id': str(data['_id']), 'name': data['name'], 'age': data['age']})
    return jsonify({'result': output})

# GET single data by id


@app.route('/api/data/<id>', methods=['GET'])
def get_data(id):
    data = collection.find_one({'_id': ObjectId(id)})
    if data:
        output = {'id': str(data['_id']),
                  'name': data['name'], 'age': data['age']}
    else:
        return jsonify({'message': 'Lỗi k có id'}), 404

    return jsonify({'result': output}), 200

# POST new data


@app.route('/api/data', methods=['POST'])
def add_data():
    # data = request.get_json()
    name = data['name']
    # age = data['age']
    data_id = collection.insert_one({'name': name, 'age': age}).inserted_id
    new_data = collection.find_one({'_id': data_id})
    output = {'id': str(new_data['_id']),
              'name': new_data['name'], 'age': new_data['age']}
    # return jsonify({'result': output})


# PUT data by id
@app.route('/api/data/<id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    result = collection.update_one({'_id': ObjectId(id)}, {
                                   '$set': {'name': name, 'age': age}})
    if result.modified_count == 1:
        output = 'Record updated successfully.'
    else:
        output = 'No records found to update.'
    return jsonify({'result': output})

# DELETE data by id


@app.route('/api/data/<id>', methods=['DELETE'])
def delete_data(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        output = 'Record deleted successfully.'
    else:
        output = 'No records found to delete.'
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
