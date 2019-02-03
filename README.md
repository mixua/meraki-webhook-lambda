# Generic WebHook listener AWS Lambda Function    

## Usage      

```
$ npm install -g serverless
$ serverless install --url https://github.com/alexdebrie/meraki-webhook --name my-flask-app
$ cd my-flask-app
$ npm run setup
<answer prompts>
$ sls deploy
```

Once the deploy is complete, run `sls info` to get the endpoint:

```sh
$ sls info
Service Information
<snip>
endpoints:
  ANY - https://{some-subdomain}.execute-api.us-east-1.amazonaws.com/dev <-- Endpoint
  ANY - https://{some-subdomain}.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
```

#### Invoke via curl:     

````sh
curl --header "Content-Type: application/json" --request POST --data '{"something":"xyz","somethingelse":"xyz"}' https://{some-subdomain}.execute-api.us-east-1.amazonaws.com/dev
````


