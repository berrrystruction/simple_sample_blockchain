#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: berrystruction
This implementation comes after reading the following online material:
- https://www.youtube.com/watch?v=pRG1kh85zwI
- https://applicature.com/blog/blockchain-technology/blockchain-code-examples
- https://lhartikk.github.io/jekyll/update/2017/07/13/chapter2.html
"""

import argparse
import hashlib
from datetime import datetime

# Argument parsing
ap = argparse.ArgumentParser();
ap.add_argument("n1", default=15, help="Number of blocks to add to the chain")
args = vars(ap.parse_args())


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

def main(num_of_blocks_to_add_str):
    print('MyBlockchain v1.1.0')
    print('---------------------------------')
    #print(num_of_blocks_to_add_str)

    num_of_blocks_to_add = int(num_of_blocks_to_add_str)
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    
    if num_of_blocks_to_add < 0: # num_of_blocks_to_add == '{}':
    # default value    
        num_of_blocks_to_add = 1

    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}n".format(block_to_add.hash))

if __name__ == '__main__':
    main(args['n1'])