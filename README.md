# Batch Rename

Author: Cam Smith
Initday: 2016-10-18

### What?

A simple python program which is given a prefix and a list of files as arguments, and will
then rename the provided files as `PREFIX_001.ext` -> `PREFIX_999.ext`

### Why?

One day I needed to do such an operation, I knew I needed to do this in the future too, so
I wanted to make a bash script, however I knew python would make dealing with the logic of
generating the new names far simpler.

I looked around a bit and realised this is the perfect opportunity to learn to use the 
argparse module.
