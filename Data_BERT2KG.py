import os
path = "."
file = path + "/BERT_Seq.txt"
#file = path + "/output_file.txt" #output_file changes every time as items get masked with some probs.
total_train = 780549
total_test = 70679
print(os.getcwd())

with open(file, 'r') as f:
    all_lines = f.read().splitlines()
print("Train_begins", all_lines[0])
print("Train_ends", all_lines[total_train-1])
print("Test_begins", all_lines[total_train])
print("Test_ends", all_lines[-1])

train_lines = all_lines[:total_train]
test_lines = all_lines[total_train:]

def write_to_txt(lines, end_idx,file_name):
    for i in range(0,end_idx):
        line = lines[i].strip()
        line = line.replace("item_", "")
        line = line.replace("[MASK]", "")
        line = ' '.join(line.split())
        if i==0 or i == end_idx-1: print(file_name, line)
        with open(file_name+"amazon2KG.txt", "a") as myfile:
            myfile.write(str(line)+"\n")

write_to_txt(train_lines, total_train, "Train")
write_to_txt(test_lines, total_test, "Test")

  