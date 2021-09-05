# Overview

This folder contains codebase for updating the data third-party plugins access token through stored refresh_token.We have to refresh tokens when it get expired and update with new tokens.There must to be some scheduler to watch this periodically. To achieve it, We use CRON, which is time-based job scheduling daemon found in Unix-like operating systems.Cron executed automatically for a set time period in the background and update the access token which is stored in json format on POSTGRES server.
- The update_plugins.py accepts command line arguments to run intended tasks on set time and date.Later we use stored access tokens to perform authentication and authorization for cdata third-party plugins.
- A POST request will make to the service’s token endpoint with grant_type=refresh_token.
- Implemented this feature for Salesforce, Hubspot, google analytics and Xero plugins.

# Postgre SQL Tables
cdata_plugin_oauth_tokens
  -----
  | plugin_id | integration | connection_json  |   request_url |
  |:---------|:---------------------|:---------------|:--------- |
  | 1  | Salesforce  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://login.salesforce.com/services/oauth2/token |
  | 2  | Hubspot  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://api.hubapi.com/oauth/v1/token |
  | 3  | Google_Analytics  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://www.googleapis.com/oauth2/v4/token |
  | 4  | Xero  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://identity.xero.com/connect/token |
  | 5  | MailChimp  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} |  |
  | 6  | Validate_Bigquery  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://accounts.google.com/o/oauth2/token |
  | 7 | Run_Bigquery  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://accounts.google.com/o/oauth2/token |
 
 cdata_plugin_oauth_tokens
  -----
  | plugin_id | integration | connection_json  |   request_url |
  |:---------|:---------------------|:---------------|:--------- |
  | 1  | Salesforce  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://login.salesforce.com/services/oauth2/token |
  | 2  | Hubspot  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://api.hubapi.com/oauth/v1/token |
  | 3  | Google_Analytics  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://www.googleapis.com/oauth2/v4/token |
  | 4  | Xero  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://identity.xero.com/connect/token |
  | 5  | MailChimp  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} |  |
  | 6  | Validate_Bigquery  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://accounts.google.com/o/oauth2/token |
  | 7 | Run_Bigquery  | {'access_token':your_access_token, 'refresh_token': your_refresh_token} | https://accounts.google.com/o/oauth2/token |

# Scripts

Support to update and clear the access_token based on command line argument.

1. List integrated plugins
   - Command line argument "--list" passed to update_plugins.py to list all supportive plugins.
   - update_plugins.py --list

2. Update access tokens
   - Command line argument "--update <api_name>" passed to update_plugins.py to update / replace existing access token by requesting authorization server using  refresh token of the plugin.
   - update_plugins.py --update <api_name>

3. Clear access token
   - Command line argument "--clear <api_name>" passed to update_plugins.py to clear saved access tokens of the plugin.
   - update_plugins.py --clear <api_name>


# Cron Job

- Access Tokens of the plugin should be updated periodically as it expires within a specific time period. To active this, we use Cron software utility is a time-based job scheduler in Unix-like operating systems.
- Cron allows Linux users to run scripts at a given time and date. After successful execution, connection json data edited in the script and updated to Postgresql server and job logs are written into schedular.log file.
- If in case any failure, then also failure logs are written into the schedular.log file with failed time.

  Token expiration time for each plugins 
  -----
  | Integration | Expiration Time (Every)          | Cron Job  |
  |:---------|:---------------------|:---------------|
  | Xero  | 30 minutes  | */30 * * * *   username   /usr/bin/python3 <update_tokens.py file path> --update xero >> <scheduler.log file path> 2>&1 |
  | Google Analytics    | 30 minutes  | */30 * * * *   username   /usr/bin/python3 <update_tokens.py file path> --update google_analytics >> <scheduler.log file path> 2>&1           |
  | Saleforce   | 2 hours | 0 */2 * * *   username   /usr/bin/python3 <update_tokens.py file path> --update salesforce >> <scheduler.log file path> 2>&1|
  | Hubspot   | 6 hours  | * 0 */6 * * *   username   /usr/bin/python3 <update_tokens.py file path> --update hubspot >> <scheduler.log file path> 2>&1           |

  
  
