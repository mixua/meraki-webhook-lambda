# Meraki alert listener Fn()     
[Meraki Webhooks](https://create.meraki.io/guides/webhooks/)      

**What is this?:** An AWS Lambda to listen for [Cisco Meraki](https://meraki.cisco.com) alert webhooks.

**Purpose:** Meraki Webhooks are a powerful and lightweight new way to subscribe to alerts sent from the Meraki Cloud when something happens. They include a JSON formatted message and are sent to a unique URL where they can be processed, stored or used to trigger powerful automations.

**What happens with inbound alerts?:**   
Alerts are written the the log group for the Lambda function. Further processing can then be performed on the log group by other event management tooling.

**Purpose:** Meraki Webhooks are a powerful and lightweight new way to subscribe to alerts sent from the Meraki Cloud when something happens. They include a JSON formatted message and are sent to a unique URL where they can be processed, stored or used to trigger powerful automations.  

## Usage      

this package uses the [serverless.com](https://serverless.com) framework.    

```
$ npm install -g serverless
$ serverless install --url https://github.com/alexdebrie/meraki-webhook --name meraki-webhook
$ cd {this project's folder}
$ npm run setup
<answer prompts>

? What Python version?
> python3.6
? Do you have Docker installed? Recommended, but not required. (Y/n)
> Y
? Do you want to set up a custom domain? e.g. api.mycompany.com? Requires a do
main in Route53. (y/N)
N

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


