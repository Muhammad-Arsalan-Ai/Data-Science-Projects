# from flask import Flask, request, jsonify
# import numpy as np
# import pickle   

# app = Flask(__name__)

# # Load the pre-trained model using pickle
# with open('your_model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

# # Load the feature engineering pipeline using pickle
# with open('feature_pipeline.pkl', 'rb') as pipeline_file:
#     feature_engineering_pipeline = pickle.load(pipeline_file)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get input data as JSON
#         input_data = request.get_json()

#         # Perform feature engineering using the loaded pipeline
#         X = feature_engineering_pipeline.transform(np.array([input_data]))

#         # Make a prediction
#         prediction = model.predict(X)

#         return jsonify({'prediction': float(prediction[0])})

#     except Exception as e:
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the pre-trained model using pickle
with open('your_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the feature engineering pipeline using pickle
with open('feature_pipeline.pkl', 'rb') as pipeline_file:
    feature_engineering_pipeline = pickle.load(pipeline_file)
    print(pipeline_file)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data as JSON
        input_data = request.get_json()

        # Perform feature engineering using the loaded pipeline
        X = feature_engineering_pipeline.transform(np.array([input_data]))

        # Make a prediction
        prediction = model.predict(X)

        return jsonify({'prediction': float(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')  # Define a route for the root URL
def root():
    return 'Welcome to the Medical Insurance Cost Prediction API'

if __name__ == '__main__':
    app.run(debug=True)
