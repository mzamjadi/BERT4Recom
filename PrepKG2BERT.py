import os

path = "./amazon-book"

train_file = path + '/train.txt'
test_file = path + '/test.txt'

train_lines = open(train_file, 'r').readlines()
test_lines = open(test_file, 'r').readlines()
for i in range(0,len(train_lines)):
    merged = []
    tmps_train = train_lines[i].strip()
    split_train = [int(i) for i in tmps_train.split(' ')]
    
    tmps_test = test_lines[i].strip()
    split_test = [int(i) for i in tmps_test.split(' ')]
    if i == 0 or i == len(train_lines)-1:
        print(split_train)
        print(split_test)
    
    split_train.extend(split_test[1:])
    
   
    for j in range(1, len(split_train)):
        if i == 0 or i == len(train_lines)-1:print(""+str(split_train[0])+" "+str(split_train[j]))
        with open("amazon2BERT.txt", "a") as myfile:
            myfile.write(""+str(split_train[0])+" "+str(split_train[j])+"\n")
            
with open("amazon2BERT.txt", 'r') as f:
    lines = f.read().splitlines()
print("last", lines[-1])

                


            