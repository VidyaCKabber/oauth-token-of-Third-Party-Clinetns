import json
import sys
import psycopg2
import requests
from UpdateTokens import PG_CONN_INFO


class CommonMethods(object):

    def __init__(self, plugin_id) -> object:
        try:
            self.conn = psycopg2.connect(**PG_CONN_INFO)
            self.cursor = self.conn.cursor()
            self.plugin_id = plugin_id
            self.headers = {}
            self.data = {}
            self.connjson = None
            self.request_url = None

        except Exception as e:
            print("I am unable to connect to the database.", e)
            sys.exit()

    def get_cdata_user_details(self):
        try:
            self.cursor.execute(
                'SELECT integration,connection_json,request_url FROM cdata_plugin_oauth_tokens WHERE plugin_id={0}'.format(
                    self.plugin_id))
            records = self.cursor.fetchall()

            for row in records:
                self.connjson = row[1]
                self.request_url = row[2]

            # get refresh token
            refresh_token = json.loads(self.connjson).get('refresh_token')

            # read user login credentials from cdata_user_details table
            self.cursor.execute(
                'SELECT username, password, oauthclientid, oauthclientsecret FROM cdata_user_details WHERE id={0}'.format(
                    self.plugin_id))
            usercreds = self.cursor.fetchall()

            user_info = {'refresh_token': refresh_token, 'usercreds': usercreds}
            return user_info

        except Exception as e:
            print(e)

    def update_access_token(self, **kwargs):
        try:
            for key, value in kwargs.items():
                if 'headers' in key:
                    self.headers.update(value)
                elif 'data' in key:
                    self.data.update(value)

            response = requests.post(self.request_url, headers=self.headers, data=self.data)
            if response.ok:
                access_token = response.json().get("access_token")
                refresh_token = response.json().get("refresh_token")
                con_json = json.loads(self.connjson)
                if access_token is not None:
                    con_json["access_token"] = access_token  # update new access_token

                if refresh_token is not None:
                    con_json["refresh_token"] = refresh_token

                data = "'{}'".format(json.dumps(con_json))
                update_cdata_plugin_oauth_tokens = 'UPDATE cdata_plugin_oauth_tokens SET connection_json={0} WHERE plugin_id={1}'.format(
                    data, self.plugin_id)
                self.cursor.execute(update_cdata_plugin_oauth_tokens)
                self.conn.commit()
                self.cursor.close()

                # Tokens updated successfully
                if self.cursor.rowcount:
                    return True
                else:
                    return False
        except:
            print(response.json())

    def clear_access_token(self):
        try:
            self.cursor.execute(
                'SELECT connection_json FROM cdata_plugin_oauth_tokens WHERE plugin_id={0}'.format(self.plugin_id))
            records = self.cursor.fetchall()

            for row in records:
                self.connjson = row[0]

            con_json = json.loads(self.connjson)

            if con_json["access_token"] is not None:
                con_json["access_token"] = None  # update new access_token

            data = "'{}'".format(json.dumps(con_json))
            update_cdata_plugin_oauth_tokens = 'UPDATE cdata_plugin_oauth_tokens SET connection_json={0} WHERE plugin_id={1}'.format(
                data, self.plugin_id)
            self.cursor.execute(update_cdata_plugin_oauth_tokens)
            self.conn.commit()
            self.cursor.close()

            # Tokens cleared successfully
            if self.cursor.rowcount:
                return True
            else:
                return False
        except Exception as e:
            print(e)
