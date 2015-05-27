#!/bin/bash
#copies app.py to a new file, replaces app.run() to include host and runs it
#therefore editing app.py would not affect the server
#and we can develop on our end efficiently
file="server.py"

#---------------------------------------------
# declare what we are searching/replacing with
search="app.run()"
new="app.run(host='0.0.0.0',port=5000)"
#-------------------------
# copy the new file to run
echo "copying file..."
#we sleep to make it look fancy
sleep 1
cp app.py $file
#------------------
# apply replacement
echo "replacing search"
sleep 1
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
sleep 1
python $file
