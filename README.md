# WebHook listener for Cisco Meraki alerts  - AWS Lambda Function      
[Meraki Webhooks](https://create.meraki.io/guides/webhooks/)      

purpose: Meraki Webhooks are a powerful and lightweight new way to subscribe to alerts sent from the Meraki Cloud when something happens. They include a JSON formatted message and are sent to a unique URL where they can be processed, stored or used to trigger powerful automations.

## Usage      

this package uses the [serverless.com](https://serverless.com) framwork.    

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


