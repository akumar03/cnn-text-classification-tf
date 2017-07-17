import argparse

parser = argparse.ArgumentParser(description="Prepare input files for tensorflow")

parser.add_argument("-root_folder", default="/Users/anoopk/Dropbox/isi/code/usc-isi-i2/dig-indicators-data", help="Root data input folder")
parser.add_argument("-indicator_type",default="Incall", help="Type of indicator")
parser.add_argument("-positive_set", default="pos,sp_n")
parser.add_argument("-negative_set",default="neg,p_n,sn_p,spn_sn", help="Suffix for negative sets")
args = parser.parse_args()
print(args.root_folder)
print(args.indicator_type)