#!/usr/bin/python3

import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser(description="rename a group of files sequentially")
parser.add_argument("prefix", type=str)
parser.add_argument("files", type=str, nargs="+")
parser.add_argument("-d", "--dirs", action="store_true", help="Enable renaming of\
					directiories.")
parser.add_argument("-i", "--index", type=int, default=0, 
					help="starting index for sequence numbers")
parser.add_argument("-n", "--no_op", action="store_true", 
					help="print move operations without executing them.")
parser.add_argument("-p", "--pad", type=int, default=-1,
					help="amount of zeros to pad sequence numbers to, will pad to longest\
					sequence number by default. -p 0 disables padding entirely")
args = parser.parse_args()

def change_path(old_path, prefix, seq, sep="_"):
	"""
	Returns as a string the new pathname to be used by the move function
	"""
	directory = os.path.dirname(old_path)
	extension = os.path.splitext(old_path)[1]

	new_path = directory + "/" + prefix + sep + seq + extension

	return new_path

start = args.index
stop  = args.index + len(args.files)
padding = len(str(stop))
padding = args.pad if args.pad > -1 else padding

for i in range(start, stop):
	path = args.files[i - start]
	if not args.dirs and os.path.isdir(path):
	# skips second check if dirs are enabled
		continue
	seq = str(i).zfill(padding)
	new  = change_path(path, args.prefix, seq)
	if args.no_op:
		print("mv", path, new)
	else:
		subprocess.run(["mv",path, new])

