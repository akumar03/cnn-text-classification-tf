import random, sys

folder = "/Users/anoopk/code/cnn-text-classification-tf/data/outcall/"
input_file = folder+ "dataset_140_outcall_label_ak.txt"
pct_split = 0.8
train_file = folder+"dataset_140_train.txt"
test_file = folder+"dataset_140_test.txt"
train_pos = folder+"dataset_140_train.pos"
train_neg = folder+"dataset_140_train.neg"
test_pos = folder+"dataset_140_test.pos"
test_neg = folder+"dataset_140_test.neg"

lines = open(input_file).readlines()
random.seed(1)
#random.shuffle(lines)
file = open(train_file,"w")
train_pos_file = open(train_pos,"w")
train_neg_file = open(train_neg,"w")
for i in range(0,int(pct_split*len(lines))):
    file.write(lines[i])
    if lines[i].startswith("__label__TRUE"):
        line =  lines[i].replace("__label__TRUE ","")
        train_pos_file.write(line)
    if lines[i].startswith("__label__FALSE"):
        line = lines[i].replace("__label__FALSE ","")
        train_neg_file.write(line)
file.close()
train_pos_file.close()
train_neg_file.close()
file = open(test_file, "w")
start = int(pct_split*len(lines)+1)
print("Test start:{} stop: {}",start,len(lines))
test_pos_file = open(test_pos,"w")
test_neg_file = open(test_neg,"w")
for i in range(start-1, len(lines)):
    file.write(lines[i])
    if lines[i].startswith("__label__TRUE"):
        line =  lines[i].replace("__label__TRUE ","")
        test_pos_file.write(line)
    if lines[i].startswith("__label__FALSE"):
        line = lines[i].replace("__label__FALSE ","")
        test_neg_file.write(line)
test_pos_file.close()
test_neg_file.close()
file.close()