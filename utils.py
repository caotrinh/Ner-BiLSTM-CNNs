from gensim.models.word2vec import Word2Vec
import logging
import sys
import gzip
import numpy as np

def get_logger(name, level=logging.INFO, handler=sys.stdout,
               formatter='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(formatter)
    stream_handler = logging.StreamHandler(handler)
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

def print_FLAGS(FLAGS,logger):
    Flags_Dict = {}
    logger.info("\nParameters:")
    for attr, value in sorted(FLAGS.__flags.items()):
      logger.info("{} = {}".format(attr, value))
      Flags_Dict[attr] = value
    logger.info("\n")
    return Flags_Dict

def get_max_length(word_sentences):
    max_len = 0
    for sentence in word_sentences:
        length = len(sentence)
        if length > max_len:
            max_len = length
    return max_len

def padSequence(dataset,max_length,beginZero=True):
    dataset_p = []
    actual_sequence_length =[]
    #added np.atleast_2d here
    for x in dataset:
        row_length = len(x)
        actual_sequence_length.append(row_length)
        if(row_length <=max_length):
            if(beginZero):
                dataset_p.append(np.pad(x,pad_width=(max_length-len(x),0),mode='constant',constant_values=0))
            else:
                dataset_p.append(np.pad(x,pad_width=(0,max_length-len(x)),mode='constant',constant_values=0))
        else:
            dataset_p.append(x[0:max_length])
    return np.array(dataset_p),actual_sequence_length
