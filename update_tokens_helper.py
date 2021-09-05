from UpdateTokens import PLUGINS
from time import strftime, gmtime
from main import CommonMethods


class UpdateTokensHelper:

    def update_salesforce_access_token(self):
        # salesforce_id = 1
        try :
            plugin_id = PLUGINS.get("salesforce")
            salesforce = CommonMethods(plugin_id)
            refresh_token = salesforce.get_cdata_user_details().get('refresh_token')
            usercreds = salesforce.get_cdata_user_details().get('usercreds')

            for row in usercreds:
                username = row[0]
                password = row[1]
                oauthclientid = row[2]
                oauthclientsecret = row[3]

            params = {
                "grant_type": "refresh_token",
                "client_id": oauthclientid,  # Consumer Key
                "client_secret": oauthclientsecret,  # Consumer Secret
                "username": username,  # The email you use to login
                "password": password,  # Concat your password and your security token
                "refresh_token": refresh_token
            }

            result = salesforce.update_access_token(data=params)

            if result:
                timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                print("Salesforce Tokens Updated Successfully,{0}".format(timenow))
            else:
                print(
                    "Unable to update Salesforce access_token. Please check the scheduler.log file to figure out the issue",
                    result)
        except Exception as e :
            print("Unable to update Salesforce access_token. Please check the scheduler.log file to figure out the issue",e)

    def update_google_analytics_access_token(self):
        # google analytics id set to 3 in cdata_plugin_oauth_tokens table
        # google_analytics_id = 3
        try :
            plugin_id = PLUGINS.get("google_analytics")
            google_analytics = CommonMethods(plugin_id)
            refresh_token = google_analytics.get_cdata_user_details().get('refresh_token')
            usercreds = google_analytics.get_cdata_user_details().get('usercreds')

            for row in usercreds:
                oauthclientid = row[2]
                oauthclientsecret = row[3]

            params = {
                'grant_type': 'refresh_token',
                'client_id': oauthclientid,
                'client_secret': oauthclientsecret,
                'refresh_token': refresh_token
            }

            result = google_analytics.update_access_token(data=params)

            if result:
                timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                print("Google Analytics Tokens Updated Successfully,{0}".format(timenow))
            else:
                print(
                    "Unable to update Google_Analytics access_token. Please check the scheduler.log file to figure out the issue",
                    result)
        except Exception as e:
            print(
                "Unable to update Google_Analytics access_token. Please check the scheduler.log file to figure out the issue",
                e)

    def update_hubspot_access_token(self):
        # hubspot id set to 2 in cdata_plugin_oauth_tokens table
        # hubspot_id = 2
        try:
            plugin_id = PLUGINS.get("hubspot")
            hubspot = CommonMethods(plugin_id)
            refresh_token = hubspot.get_cdata_user_details().get('refresh_token')
            usercreds = hubspot.get_cdata_user_details().get('usercreds')

            for row in usercreds:
                oauthclientid = row[2]
                oauthclientsecret = row[3]

            params = {
                'client_id': oauthclientid,
                'client_secret': oauthclientsecret,
                'grant_type': 'refresh_token',
                'redirect_uri': 'https://redirect.Your_Website.io/redirect/oauth2',
                'refresh_token': refresh_token
            }

            result = hubspot.update_access_token(data=params)
            if result:
                timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                print("Hubspot Tokens Updated Successfully,{0}".format(timenow))
            else:
                print("Unable to update Hubspot access_token. Please check the scheduler.log file to figure out the issue",
                      result)
        except Exception as e:
            print(
                "Unable to update Hubspot access_token. Please check the scheduler.log file to figure out the issue",
                e)

    def update_xero_access_token(self):
        # xero id set to 4 in cdata_plugin_oauth_tokens table
        # xero_id = 3
        try:
            plugin_id = PLUGINS.get("xero")
            xero = CommonMethods(plugin_id)
            refresh_token = xero.get_cdata_user_details().get('refresh_token')
            usercreds = xero.get_cdata_user_details().get('usercreds')
            for row in usercreds:
                oauthclientid = row[2]
                oauthclientsecret = row[3]

            headers = {'Content-Type': 'application/x-www-form-urlencoded'}

            params = {
                'grant_type': 'refresh_token',
                'client_id': oauthclientid,
                'client_secret': oauthclientsecret,
                'refresh_token': refresh_token
            }

            result = xero.update_access_token(headers=headers, data=params)

            if result:
                timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                print("Xero's Tokens Updated Successfully {0}".format(timenow))
            else:
                print("Unable to update Xero access_token. Please check the scheduler.log file to figure out the issue",
                      result)
        except Exception as e:
            print(
                "Unable to update Xero's access_token. Please check the scheduler.log file to figure out the issue",
                e)

    def get_plugin_list(self):
        print("We support below third-party plugins :- \n")
        for plugin in PLUGINS.keys():
            print(plugin)

    def update_bigquery_access_token(self):
        # google bigquey id set to 6 in cdata_plugin_oauth_tokens table
        # google_bigquery_id = 6
        try:
            plugin_id = PLUGINS.get("google_bigquery")
            google_analytics = CommonMethods(plugin_id)
            refresh_token = google_analytics.get_cdata_user_details().get('refresh_token')
            usercreds = google_analytics.get_cdata_user_details().get('usercreds')

            for row in usercreds:
                oauthclientid = row[2]
                oauthclientsecret = row[3]

            params = {
                'grant_type': 'refresh_token',
                'client_id': oauthclientid,
                'client_secret': oauthclientsecret,
                'refresh_token': refresh_token
            }

            result = google_analytics.update_access_token(data=params)

            if result:
                timenow = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                print("Google Bigquery Tokens Updated Successfully,{0}".format(timenow))
            else:
                print(
                    "Unable to update Google Bigquery access_token. Please check the scheduler.log file to figure out the issue",
                    result)
        except Exception as e:
            print(
                "Unable to update Google Bigquery access_token. Please check the scheduler.log file to figure out the issue",
                e)

    FUNCTION_MAP = {
        'salesforce': update_salesforce_access_token,
        'hubspot': update_hubspot_access_token,
        'google_analytics': update_google_analytics_access_token,
        'xero': update_xero_access_token,
        'bigquery': update_bigquery_access_token
    }
