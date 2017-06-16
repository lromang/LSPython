##################################################
## Chapter 2
## ----------------------------------------
## Sjardin, Bastiaan, Luca Massaron, and
## Alberto Boschetti.
## Large Scale Machine Learning with Python.
## Packt Publishing Ltd, 2016.
##################################################


## ------------------------------
## Libraries
## ------------------------------
import os, csv
import pandas as pd

## ------------------------------
## Read in data
## ------------------------------
source     = '../data/bikesharing/hour.csv'
CHUNK_SIZE = 1000
with open(source, 'rb') as R:
    iterator = pd.read_csv(R, chunksize = CHUNK_SIZE)
    for n, data_chunk in enumerate(iterator):
        print ('Size of uploaded chunk: %i instances, %i features' % (data_chunk.shape))
