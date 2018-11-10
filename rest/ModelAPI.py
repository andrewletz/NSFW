from tensorflow.keras.layers import Dense, Dropout, Embedding, Flatten, SimpleRNN, LSTM, CuDNNLSTM, MaxPooling1D, Conv1D
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import optimizers, losses
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

import pickle
import numpy as np
import pandas as pd


# length of tokens to consider in video title
SEQ_LEN = 10

# loads keras model for classifying clickbait videos
clickbait_model = load_model('../DeepLearning/Clickbait_model.h5')

# loads keras model for classifying Education video types
classify_model = load_model('../DeepLearning/Classify_Youtube_Model.h5')

# loads tokenizer for clickbait model preprocessing
with open('../DeepLearning/clickbait_tokenizer.pickle', 'rb') as handle:
    clickbait_tokenizer = pickle.load(handle)

# loads tokenizer for classify model preprocessing
with open('../DeepLearning/classify_tokenizer.pickle', 'rb') as handle:
    classify_tokenizer = pickle.load(handle)

# processes and predicts if a video is clickbait based off of the video title
def process_and_predict_clickbait_data(video_title):

	sequence = clickbait_tokenizer.texts_to_sequences([video_title])
	padded_sequence = pad_sequences(sequence, maxlen=SEQ_LEN)
	result = clickbait_model.predict(padded_sequence)[0][0]

	return int(round(result))

# processes and predicts the class of a video based off of the video title
# Math: 0, CS: 1, Drawing: 2, Chemistry: 3, Economics: 4
def process_and_predict_classify_data(video_title):

	sequence = classify_tokenizer.texts_to_sequences([video_title])
	padded_sequence = pad_sequences(sequence, maxlen=SEQ_LEN)
	result = classify_model.predict(padded_sequence)

	return np.argmax(result)


# Clickbait Tests
# print("Prediction: ", process_and_predict_clickbait_data("You won't believe what happens next"), " Actual: 1")
# print("Prediction: ", process_and_predict_clickbait_data("BFS Algorithm Tutorial"), " Actual: 0")

# print('')

# Classify Tests Math': 0, 'CS': 1, 'Drawing': 2, 'Chemistry': 3, 'Economics': 4})
# print("Prediction: ", process_and_predict_classify_data("What Is Statistics: Statistics #1"), " Actual: 0")
# print("Prediction: ", process_and_predict_classify_data("Early Computing: Computer Science #1"), " Actual: 1")
# print("Prediction: ", process_and_predict_classify_data("Learn To Draw Like A Pro"), " Actual: 2")
# print("Prediction: ", process_and_predict_classify_data("Network Solids and Carbon: Chemistry #34"), " Actual: 3")
# print("Prediction: ", process_and_predict_classify_data("Supply and Demand: Economics #4"), " Actual: 4")












