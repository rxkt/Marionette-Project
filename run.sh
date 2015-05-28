#!/bin/bash
#copies app.py to a new file, replaces app.run() to include host and runs it
#therefore editing app.py would not affect the server
#and we can develop on our end efficiently

cd ~/Softdev2-Final
file="server.py"

#---------------------------------------------
# declare what we are searching/replacing with
search="app.run()"
new="app.run(host='0.0.0.0',port=5000)"
#-------------------------
# copy the new file to run
echo "copying app.py to server.py..."
#we sleep to make it look fancy
sleep 0.3
cp app.py $file
#------------------
# apply replacement
echo "replacing app.run() with app.run(host='0.0.0.0',port=5000)..."
sleep 0.3
for each in $(fgrep -l $search $file)
do
    ex $each <<EOF
:%s/$search/$new/g
:wq
EOF
done
#--------------
#run the server
echo "running "$file
sleep 0.3
python $file
