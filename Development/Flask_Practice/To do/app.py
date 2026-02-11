from flask import Flask,render_template,request,redirect,url_for,jsonify
app=Flask(__name__)

## inital data in my to do list
items=[
    {"id":1,"name":"item 1","description": "This is item 1"},
    {"id":2,"name":"item 2","description": "This is item 2"}
]

@app.route("/")
def home():
    return "Welcome to the sample to do list app"

# # GET:= Tetrive all the items
@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)

# get: Retrive  a specific item by id
@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
    item=next((item for item in items if item ["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not Found"})
    return jsonify(item)


## post:  create a new task 
@app.route("/items",methods=["POST"])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Item not found"})
    new_item={
        "id":items[-1]['id']+1 if items else 1,
        "name":request.json["name"],
        "description":request.json["description"]
    }

    items.append(new_item)
    return jsonify(new_item)


# put: update the existing item
@app.route("/item/<int:item_id>",methods=["PUT"])
def update_item(item_id):
    item =next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error ": "item not found "})
    item["name"]=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])

    return jsonify(item)

# Delete: delete item
@app.route('/item/<int:item_id>',methods=["DELETE"])
def delete_item(item_id):
    global item
    item =[item for item in items if item['id']!=item_id]

    return jsonify({"result":"item deleted"})\
    

if __name__=="__main__":
    app.run(debug=True)
