import db
from flask import Flask, render_template , session , redirect , request
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'B&S'
app.config['DEBUG']=True 

def authenticate(func):
    @wraps(func)
    def inner():
        if 'username'in session:
            return func()
        else:
            return redirect('/')


@app.route("/",methods=['GET','POST'])
def login():
    if request.method== 'POST':
        
        
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        
        if button == 'Submit':
            criteria = {'username': username, 'password': password}
            user = db.find_user(criteria)
            if user!=None and username!= "":
                session['username'] = username
                
            
                return redirect('/home')
            
            else:
                return render_template('login.html',error="wrong info")
        else:
            return redirect('/register')
    else:
        if 'username' in session:
            return redirect('/home')
        return render_template('login.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        
        return render_template('register.html')
    button = request.form['button']
    username = request.form['username']
    password = request.form['password']
    first = request.form['first']
    last = request.form['last']
    if button == 'Cancel':
        return redirect('/')
    else:
        if not password or not first or not last:
            return render_template('register.html',error='incomplete')
        criteria = {'username': username}
        if db.find_user({'username':username}):
            return render_template('register.html',error='username taken')
        else:
            
            user_params = {'username': username, 'password': password, 'first': first, 'last': last}
            db.new_user(user_params)
            
            return redirect('/')

@authenticate 
@app.route("/home")
def home():
  return render_template('home.html')
@authenticate
@app.route("/view_items")
def view_items():
    itemList= db.view_items(session['username'])
    return render_template('view_items.html',itemList=itemList)
@authenticate
@app.route("/all_items", methods=['GET','POST'])
def all_items():
    user=session['username']
    itemList= db.all_items()
    if request.method=='GET':
       
        return render_template('all_items.html',itemList=itemList,user=user)
    toAdd=[]
    button=request.form['button']
    for items in itemList:
        try:
            request.form[str(items[1])+"add"]
            add=True
        except:
            add=False
        if add==True:
            toAdd.append(items)
    if len(toAdd)==0:
        return render_template('all_items.html',error='None',itemList=itemList,user=user)
    for add in toAdd:
       
        try:
            exist= db.find_item({'name':add[1]})
        except:
            return render_template('all_items.html',itemList=itemList,user=user,error='Taken')
    for add in toAdd:
        
        add.append(session['username'])
        db.new_trans(add)
        db.items.remove({'name':add[1]})
    return render_template('all_items.html',error='Added')



@authenticate
@app.route('/trans',methods=['GET','POST'])
def trans():
    tran=db.all_trans(session['username'])
    
    if request.method=='GET':
        
        return render_template('trans.html',tran=tran,user=session['username'])
    toHis=[]
    for trans in tran:
        try:
            
            request.form[str(trans['name'])+'fin']
            his= True
        except:
            his=False
        if his==True:
            toHis.append(trans)
    if len(toHis)==0:
        return render_template('trans.html',tran=tran,user=session['username'],error='None')
    for his in toHis:
        db.transactions.remove({'name':his['name']})
    tran=db.all_trans(session['username'])
    return render_template('trans.html',tran=tran,user=session['username'],error='Complete')
  

    
@authenticate 
@app.route("/upload",methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html',error=False)
    button = request.form['button']
    name= request.form['name']
    category= request.form['category']
    desc= request.form['desc']
    quan= request.form['quantity']
    cond= request.form['cond']
    price=request.form['price']
    auction=request.form['auc'] 
    if not price or not desc or not quan or not name:
        return render_template('upload.html',error="Wrong info")
    if db.find_item({'name':name}):
        print db.find_item({'name':name})
        return render_template('upload.html',error="Name Taken")
        
            
    else:
        if auction == 'True':
            auction= True
        else:
            auction= False
        item_params={'name':name,'category':category,'desc':desc,'quantity':quan,'cond':cond,'price':price,'seller':session['username'],'auction':auction}
        item = db.new_item(item_params)
        
        
        return redirect('/upload')
@authenticate
@app.route('/message',methods=['POST','GET'])
def message():
    messageList= db.view_messages(session['username'])
    
    if request.method=='GET':
        
        return render_template('message.html',itemList=messageList)
    reciever=request.form['reciever']
    message=request.form['message']
    if not message or not reciever:
        return render_template('message.html',itemList=messageList,error='None')
    db.messages.insert({'reciever':reciever,'message':message,'sender':session['username']})
    return render_template('message.html',itemList=messageList,error='Sent')
@authenticate
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')   
if __name__ == "__main__":
    app.secret_key='B&S'
    app.debug = True
    app.run()
    
    
