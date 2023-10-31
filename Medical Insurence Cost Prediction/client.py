# import requests
# import pickle
# import pandas as pd

# # Load the feature engineering pipeline using pickle
# with open('feature_pipeline.pkl', 'rb') as pipeline_file:
#     feature_engineering_pipeline = pickle.load(pipeline_file)

# column_transformer = feature_engineering_pipeline.named_steps['preprocessor']
# feature_names = column_transformer.get_feature_names_out()
# print("Expected feature names:", feature_names)


# # Check the expected feature names
# # column_transformer = feature_engineering_pipeline.named_steps['preprocessor']
# # feature_names = column_transformer.get_feature_names_out()
# # # print("Expected feature names:", feature_names)
# # print("Expected feature names:", feature_engineering_pipeline.named_steps['preprocessor'].transformers_[0][1].named_steps['num'].get_feature_names())
# # print("Expected feature names:", feature_engineering_pipeline.named_steps['preprocessor'].transformers_[1][1].named_steps['cat'].named_steps['onehot'].get_feature_names(input_data.columns[3:]))
# # print("Expected feature names:", feature_engineering_pipeline.named_steps['preprocessor'].transformers_[2][1].named_steps['interaction'].get_feature_names())

# # Print the steps of your pipeline
# # for name, transformer, column_names in feature_engineering_pipeline.named_steps['preprocessor'].transformers_:
# #     print(name)
# #     print(transformer)
# #     print(column_names)



# # Now, create your input data dictionary with the correct feature names
# input_data = {
#     'num__age': 30,
#     'num__bmi': 22.7,
#     'num__children': 0,
#     'cat__sex_female': 0,  # Correct the column name
#     'cat__smoker_yes': 1,
#     'cat__region_southwest': 1,
#     'interaction__age': 30 * 22.7,
#     'interaction__bmi': 22.7 ** 2,
#     'interaction__age bmi': 30 * 22.7,
# }



# # Convert the input data dictionary into a DataFrame
# input_df = pd.DataFrame([input_data])
# print("Columns in input data:", input_df.columns)

# # Make sure to preprocess the input data using the feature engineering pipeline
# preprocessed_input_data = feature_engineering_pipeline.transform(input_df)

# # Convert the NumPy array to a Python list
# preprocessed_input_data = preprocessed_input_data.tolist()

# response = requests.post('http://127.0.0.1:5000/predict', json=preprocessed_input_data[0])
# print(response.json())



import requests
import pickle
import pandas as pd

# Load the feature engineering pipeline using pickle
with open('feature_pipeline.pkl', 'rb') as pipeline_file:
    feature_engineering_pipeline = pickle.load(pipeline_file)

# Create your input data dictionary with the correct feature names
input_data = {
    'num__age': 30,
    'num__bmi': 22.7,
    'num__children': 0,
    'cat__sex_male': 0,
    'cat__smoker_yes': 1,
    'cat__region_southwest': 1,
    'interaction__age': 30 * 22.7,
    'interaction__bmi': 22.7 ** 2,
    'interaction__age bmi': 30 * 22.7,
}

input_df = pd.DataFrame([input_data])
print(input_df.columns)

expected_order = ['num__age', 'num__bmi', 'num__children', 'cat__sex_male', ...]

# Get the actual column order from your DataFrame
actual_order = input_df.columns.tolist()

# Check if the actual order matches the expected order
if expected_order == actual_order:
    print("Column order matches the expected order.")
else:
    print("Column order does not match the expected order.")
# Convert the input data dictionary into a DataFrame
# input_df = pd.DataFrame([input_data])

# Make sure to preprocess the input data using the feature engineering pipeline
preprocessed_input_data = feature_engineering_pipeline.transform(input_df)

# Convert the NumPy array to a Python list
preprocessed_input_data = preprocessed_input_data.tolist()

# Send a POST request to your server
response = requests.post('http://127.0.0.1:5000/predict', json=preprocessed_input_data[0])
print(response.json())
