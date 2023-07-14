# Purpose of this API is to return back the set of data (in this case movies) belonging to a specific cluster

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


