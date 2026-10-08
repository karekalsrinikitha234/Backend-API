from flask import Flask, jsonify
app=Flask(__name__)
users=[
    {"id":1,"name":"Alice", "email": "alice@ex.com"},
    {"id":2,"name":"Bob", "email": "bob@ex.com"},
    {"id":3,"name":"Charlie", "email": "charlie@ex.com"},
    {"id":4,"name":"Diana", "email": "diana@ex.com"},
    {"id":5,"name":"Eve", "email": "eve@ex.com"}
]
@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users)
@app.route('/users/<int:user_id>', methods=['GET'])
def grt_user(user_id):
    user=next((u for u in users if u['id']== user_id),None)
    if user:
        return jsonify(user)
    return jsonify({"error":"User not found"}),404
if __name__ == '__main__':
    app.run(debug=True)