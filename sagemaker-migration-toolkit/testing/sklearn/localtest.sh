#!/usr/bin/env bash
ENDPOINT_NAME=SAGEMAKER-ENDPOINT
aws sagemaker-runtime invoke-endpoint \
	--endpoint-name ${ENDPOINT_NAME} \
	--body '{"startYear":[2015], "runtimeMinutes":[150],"Thriller":[1],"Music":[0],"Documentary":[0],
                    "Film-Noir":[0],"War":[0],"History":[0],"Animation":[0],"Biography":[0],
                    "Horror":[0],"Adventure":[0],"Sport":[0],"Musical":[0],
                    "Mystery":[0],"Action":[0],"Comedy":[0],"Sci-Fi":[1],
                    "Crime":[0],"Romance":[0],"Fantasy":[0],"Western":[0],
                    "Drama":[0],"Family":[0],
                    "averageRating":[7],"numVotes":[50]}' \
	--content-type 'application/json' \
	prediction_response.json
