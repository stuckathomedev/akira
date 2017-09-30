import re
import facebook
from modules.facebook.facebook_cfg import cfg

def post_on_facebook(msg):
    api = get_api(cfg)

    status_msg = msg
    status = api.put_object(parent_object='me', connection_name='feed', message=status_msg)

def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'], version="2.1")
    resp = graph.get_object('me/accounts')
    page_access_token = None
    return graph

trigger_regex = re.compile('^post (?:on|to) facebook(?: that)? (.+)$', re.IGNORECASE)

def run(matches):
    post_on_facebook(matches.groups()[0])