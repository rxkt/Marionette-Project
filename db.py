from pymongo import Mongoclient

client = MongoClient()
db=client['account_manager']
users=db['users']

def new_user(user_params):
    user_id=users.insert(user_params)
    return user

def find_user(criteria):
    user= users.find_one(criteria)
    return user

def find_things(criteria):
    things=users.find(criteria)
    return things

