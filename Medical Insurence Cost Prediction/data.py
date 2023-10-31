import pickle

# Load data from a .pkl file
with open('feature_pipeline.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

with open('your_model.pkl', 'rb') as file1:
    loaded_data1 = pickle.load(file1)


# Print the loaded data
print(loaded_data)
# print(loaded_data1)

