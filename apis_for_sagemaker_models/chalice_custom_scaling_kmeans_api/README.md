# Purpose of this API is to take in categories that you are interested in and then call the 2 sagemaker endpoints behind the scenes and return a cluster number

config.json should look like this
```json
{
  "version": "2.0",
  "app_name": "example-app",
  "manage_iam_role": false,
  "iam_role_arn": "arn:aws:iam::XXXX:role/service-role/S3_read_access",
  "stages": {
    "dev": {
      "api_gateway_stage": "api"
    }
  }
}
```
