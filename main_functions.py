import json

# A function to save a JSON document to a file

def save_json(data, filename):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file)
        print(f"File {filename} saved successfully.")

# A function to load a JSON document from a file
# python receives the data as a dictionary

def load_json(filename):
    with open(filename, 'r') as read_file:
        received_data = json.load(read_file)
        print(f"File {filename} loaded successfully.")
        return received_data