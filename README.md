# Meraki alert listener Fn()     
[Meraki Webhooks](https://create.meraki.io/guides/webhooks/)      

An AWS Lambda to listen for [Cisco Meraki](https://meraki.cisco.com) alert webhooks.

purpose: Meraki Webhooks are a powerful and lightweight new way to subscribe to alerts sent from the Meraki Cloud when something happens. They include a JSON formatted message and are sent to a unique URL where they can be processed, stored or used to trigger powerful automations.

## Usage      

this package uses the [serverless.com](https://serverless.com) framework.    

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

#### Quick test: Invoke via curl:     

````sh
curl --header "Content-Type: application/json" --request POST --data '{"hello":"world","organizationId":"999999"}' https://{some-subdomain}.execute-api.us-east-1.amazonaws.com/dev
````

#### Postman Examples:    
https://documenter.getpostman.com/view/897512/RWaLwTY4 


