from chalice import Chalice

app = Chalice(app_name='sagemaker-apigateway-lambda-chalice')

@app.lambda_function()
def boto3_import(event, context):
    import boto3
    return {'boto3': boto3.__file__}


@app.lambda_function()
def pandas_import(event, context):
    import pandas
    return {'pandas': pandas.__file__}
    
def np2csv(arr):
    import io
    import numpy as np
    csv = io.BytesIO()
    np.savetxt(csv, arr, delimiter=",", fmt="%g")
    return csv.getvalue().decode().rstrip()
    
    
@app.route('/', methods=['POST'], content_types=['application/json'], cors=True)
def handle_data():
    import pandas
    import boto3
    import json
    import numpy as np
    sagemaker = boto3.client('sagemaker-runtime')
    # Get the json from the request
    # input_json = app.current_request.json_body['input']
    # result = {'input': input_json}
    # result = {"startYear":[2015], "runtimeMinutes":[150], "Drama":[0], "Film-Noir":[0],"Fantasy":[0],"Animation":[0],
    #                 "Family":[0],"Documentary":[0],"War":[0],"Sport":[0],"Music":[0],"Western":[0],"Biography":[0],"Adventure":[1],
    #                 "News":[0],"History":[0],"Mystery":[0],"Sci-Fi":[1],"Action":[1],"Crime":[1],"Musical":[0],"Romance":[0],
    #                 "Comedy":[1],"Horror":[0],"Thriller":[1],"averageRating":[7],"numVotes":[50]}
                    
    request_data = app.current_request.json_body
    # converted_data = {}
    # for key, value in request_data.items():
    #     converted_data[key] = [int(value)]
    converted_data = {
        'startYear': [int(request_data.get('startYear', '0'))],
        'runtimeMinutes': [int(request_data.get('runtimeMinutes', '0'))],
        'Thriller': [int(request_data.get('Thriller', '0'))],
        'Music': [int(request_data.get('Music', '0'))],
        'Documentary': [int(request_data.get('Documentary', '0'))],
        'Film-Noir': [int(request_data.get('Film-Noir', '0'))],
        'War': [int(request_data.get('War', '0'))],
        'History': [int(request_data.get('History', '0'))],
        'Animation': [int(request_data.get('Animation', '0'))],
        'Biography': [int(request_data.get('Biography', '0'))],
        'Horror': [int(request_data.get('Horror', '0'))],
        'Adventure': [int(request_data.get('Adventure', '0'))],
        'Sport': [int(request_data.get('Sport', '0'))],
        'Musical': [int(request_data.get('Musical', '0'))],
        'Mystery': [int(request_data.get('Mystery', '0'))],
        'Action': [int(request_data.get('Action', '0'))],
        'Comedy': [int(request_data.get('Comedy', '0'))],
        'Sci-Fi': [int(request_data.get('Sci-Fi', '0'))],
        'Crime': [int(request_data.get('Crime', '0'))],
        'Romance': [int(request_data.get('Romance', '0'))],
        'Fantasy': [int(request_data.get('Fantasy', '0'))],
        'Western': [int(request_data.get('Western', '0'))],
        'Drama': [int(request_data.get('Drama', '0'))],
        'Family': [int(request_data.get('Family', '0'))],
        'averageRating': [int(request_data.get('averageRating', '0'))],
        'numVotes': [int(request_data.get('numVotes', '0'))]
    }
    print("Current converted_data")
    print(converted_data)
    result = json.dumps(converted_data).encode('utf-8')
    print("Data is :: ")
    print(result)
    # Send everything to the Sagemaker endpoint
    res = sagemaker.invoke_endpoint(
        EndpointName='sm-endpoint-sklearn-xxxxxx',
        Body=result,
        ContentType='application/json',
        Accept='application/json'
    )
    print(res)

    # Get the response body
    response_body = res['Body'].read().decode('utf-8')
    string_array = json.loads(response_body)["Output"]
    np_array = np.fromstring(string_array.replace("[", "").replace("]", ""), sep=",")
    
    arr_2d = np.reshape(np_array, (1, len(np_array)))
    payload = np2csv(arr_2d.astype('float32'))
    responsekmeans = sagemaker.invoke_endpoint(EndpointName="kmeans-xxxxxx", ContentType="text/csv", Body=payload)
    resultkmeans = json.loads(responsekmeans["Body"].read().decode())
    
    return resultkmeans['predictions'][0]['closest_cluster']

