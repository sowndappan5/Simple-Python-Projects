import nltk
import numpy as np
import tflearn
import tensorflow as tf
import pickle
import random
import json

# Download the Punkt tokenizer for sentence splitting
nltk.download('punkt')

# Initialize the stemmer
stemmer = nltk.stem.lancaster.LancasterStemmer()

# Load the JSON data containing intents
with open("WHO.json") as json_file:                 
    intents_data = json.load(json_file)

# Attempt to load preprocessed data
try:
    with open("data.pickle", "rb") as pickle_file:
        vocabulary, labels, training_data, output_data = pickle.load(pickle_file)
except:
    # Initialize lists for processing data
    vocabulary = []
    labels = []
    documents_x = []
    documents_y = []

    # Tokenize patterns and prepare training data
    for intent in intents_data["intents"]: 
        for pattern in intent["patterns"]:
            tokenized_words = nltk.word_tokenize(pattern)
            vocabulary.extend(tokenized_words)
            documents_x.append(tokenized_words)
            documents_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    # Perform stemming on words
    vocabulary = [stemmer.stem(word.lower()) for word in vocabulary if word != "?"]         
    vocabulary = sorted(set(vocabulary))
    labels = sorted(labels)                                     

    # Create training data and output labels
    training_data = []
    output_data = []
    empty_output = [0 for _ in range(len(labels))]
    
    for index, doc in enumerate(documents_x):
        bag_of_words = []

        stemmed_words = [stemmer.stem(word) for word in doc]

        for word in vocabulary:
            bag_of_words.append(1 if word in stemmed_words else 0)

        output_row = empty_output[:]
        output_row[labels.index(documents_y[index])] = 1

        training_data.append(bag_of_words)
        output_data.append(output_row)
        
    # Convert training data and output to numpy arrays 
    training_data = np.array(training_data)     
    output_data = np.array(output_data)

    # Save the processed data for future use
    with open("data.pickle", "wb") as pickle_file:
        pickle.dump((vocabulary, labels, training_data, output_data), pickle_file)

# Building the Neural Network Model
tf.reset_default_graph()                   

model_network = tflearn.input_data(shape=[None, len(training_data[0])])
model_network = tflearn.fully_connected(model_network, 8)
model_network = tflearn.fully_connected(model_network, 8)
model_network = tflearn.fully_connected(model_network, len(output_data[0]), activation="softmax")
model_network = tflearn.regression(model_network)

# Uncomment to load a pre-trained model
# model = tflearn.DNN(model_network)
# try:                             
#     model.load("model.tflearn")
# except:

# Training and Saving the Model
model = tflearn.DNN(model_network)
model.fit(training_data, output_data, n_epoch=1000, batch_size=8, show_metric=True)     
model.save("model.tflearn")

# Function to create a bag of words representation
def create_bag_of_words(sentence, vocabulary):                             
    bag = [0 for _ in range(len(vocabulary))]

    tokenized_sentence = nltk.word_tokenize(sentence)
    stemmed_sentence = [stemmer.stem(word.lower()) for word in tokenized_sentence]

    for word in stemmed_sentence:
        for index, vocab_word in enumerate(vocabulary):
            if vocab_word == word:
                bag[index] = 1

    return np.array(bag)

# Function to handle chat interaction
def start_chat():
    print("Start talking with the bot and ask your queries about Corona-virus (type 'quit' to stop)!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        prediction_results = model.predict([create_bag_of_words(user_input, vocabulary)])[0]
        predicted_index = np.argmax(prediction_results)
        
        tag = labels[predicted_index]
        if prediction_results[predicted_index] > 0.7:
            for intent in intents_data["intents"]:
                if intent['tag'] == tag:
                    responses = intent['responses']

            print(random.choice(responses))
        else:
            print("I am sorry, but I can't understand.")

# Start the chat
start_chat()