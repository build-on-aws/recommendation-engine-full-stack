import joblib
import os
import json
import pandas as pd

"""
Deserialize fitted model
"""
def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model

"""
input_fn
    request_body: The body of the request sent to the model.
    request_content_type: (string) specifies the format/variable type of the request
"""
def input_fn(request_body, request_content_type):
    if request_content_type == 'application/json':
        request_body = json.loads(request_body)
        
        # Normalize the json_dict to create a dataframe
        json_dict_df = pd.DataFrame(request_body)
        print(json_dict_df)
        return json_dict_df
    else:
        raise ValueError("This model only supports application/json input")

"""
predict_fn
    input_data: returned array from input_fn above
    model (sklearn model) returned model loaded from model_fn above
"""
def predict_fn(input_data, model):
    print("In predict function")
    print(input_data)
    return model.transform(input_data).astype('float32')

"""
output_fn
    prediction: the returned value from predict_fn above
    content_type: the content type the endpoint expects to be returned. Ex: JSON, string

"""

def output_fn(prediction, content_type):

    # convert numpy array to list
    print("In output_fn")
    print(prediction)
   
    json_dict_df_from_model = prediction.tolist()
    
    # convert list to json
    json_response = json.dumps(json_dict_df_from_model)
    respJSON = {'Output': json_response}
    return respJSON