from pymongo import MongoClient

client = MongoClient()
db=client['account_manager']
users=db['users']
transactions=db['transactions']
items =db['items']
messages=db['messages']
def new_user(user_params):
    user_id=users.insert(user_params)
    return user_id

def find_user(criteria):
    
    user= users.find_one(criteria)
    return user

def find_things(criteria):
    things=users.find(criteria)
    return things
def find_transactions(criteria):
    trans= transactions.find(criteria)
    return trans
def new_trans(criteria):
    crit={'buyer':criteria[7],'seller':criteria[0],'name':criteria[1],'category':criteria[2],'desc':criteria[3],'quantity':criteria[4],'cond':criteria[5],'price':criteria[6],'auction':criteria[7]}
    trans=transactions.insert(crit)
    return trans
def new_transBid(criteria):
    crit={'buyer':criteria[7],'seller':criteria[8],'name':criteria[0],'category':criteria[1],'desc':criteria[2],'quantity':criteria[3],'cond':criteria[4],'price':criteria[5],'auction':criteria[6]}
    trans=transactions.insert(crit)
    return trans
def all_trans(name):
    transList=[]
    for trans in transactions.find({'buyer':name}):
        transList.append(trans)
    for trans in transactions.find({'seller':name}):    
        transList.append(trans)
    return transList
def find_item(criteria):
    item= items.find_one(criteria)
    return item
def new_item(item_params):
    item= items.insert(item_params)
    return item
def all_items():
    itemList=[]
    for item in items.find():
        itemList.append([item['seller'],item['name'],item['category'],item['desc'],item['quantity'],item['cond'],item['price'],item['auction'],item['bidder']])
    return itemList
def view_items(user):
    itemList=[]
    for item in items.find({"seller":user}):
        itemList.append([item['name'],item['category'],item['desc'],item['quantity'],item['cond'],item['price'],item['auction'],item['bidder']])

    return itemList


def view_messages(user):
    messageList=[]
    for item in messages.find({"reciever":user}):
        messageList.append(item)
        
        
    return messageList
