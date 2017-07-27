import random, sys

folder = "/Users/anoopk/code/cnn-text-classification-tf/data/incall_exp2/"
input_file = folder+ "test_dataset_140_label_ak.txt"
pct_split = 0.8
train_file = folder+"dataset_140_train.txt"
test_file = folder+"dataset_140_test.txt"

lines = open(input_file).readlines()
random.seed(1)
#random.shuffle(lines)
file = open(train_file,"w")
for i in range(0,int(pct_split*len(lines))):
    file.write(lines[i])
file.close()
file = open(test_file, "w")
start = int(pct_split*len(lines)+1)
print("Test start:{} stop: {}",start,len(lines))
for i in range(start-1, len(lines)):
    file.write(lines[i])
file.close()