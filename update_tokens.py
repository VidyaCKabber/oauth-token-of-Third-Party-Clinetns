import argparse
import sys
from UpdateTokens import PLUGINS
from main import CommonMethods
from update_tokens_helper import UpdateTokensHelper


class update_tokens:

    def __init__(self):
        self.res = UpdateTokensHelper()
        self.FUNCTION_MAP = self.res.FUNCTION_MAP

    def get_set_args(self):
        parser = argparse.ArgumentParser(description="cdata plugins")
        parser.add_argument("--clear", nargs='?') # --clear <plugin_name> -> clears the stored access_token
        parser.add_argument("--update", nargs='?') # --update <plugin_name> -> update the access_token of the plugins using stored refresh_token
        parser.add_argument("--list", nargs='?') # --list all supportive third-party plugins
        parser.parse_known_args(['--list', '--clear', '--update']) # valid cmd arguments

        if "--list" in sys.argv:
            self.res.get_plugin_list()

        elif "--update" in sys.argv:
            args = parser.parse_args()
            if args.update in self.FUNCTION_MAP.keys():
                UpdateAccessToken = self.FUNCTION_MAP[args.update]
                UpdateAccessToken(self)
            else:
                print("Invalid or we do not support {0} third-party plugin".format(args.update))

        elif "--clear" in sys.argv:
            args = parser.parse_args()
            if args.clear in PLUGINS.keys():
                try:
                    plugin_id = PLUGINS[args.clear]
                    res = CommonMethods(plugin_id)
                    result = res.clear_access_token()
                    if result:
                        print("{0}'s Tokens cleared Successfully".format(args.clear))
                    else:
                        print("Unable to clear {0} access token".format(args.clear))
                except Exception as e:
                    print("Unable to clear {0} access token because {1}".format(args.clear,e))
            else:
                print("Invalid Argument Passed")
        else:
            print("Invalid Argument Passed")


obj = update_tokens()
obj.get_set_args()
