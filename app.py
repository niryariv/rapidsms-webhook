import rapidsms
import config

import urllib, urllib2


class App (rapidsms.app.App):
    def _get_target_url(self, message):
        urls = config.target_urls
        words = message.text.split()
        
        if urls.has_key('*'):
            default = urls['*']
        else:
            default = False

        if len(words) == 0 or not urls.has_key(words[0]):
            return default
        else:
            return urls[words[0]]
        
        
    def handle (self, message):        
        values = {
            'from' : message.connection.identity,
            'text' : message.text
        }
        
        url = self._get_target_url(message)
        if url is False:
            return False
            
        headers = { 'User-Agent' : config.user_agent }

        data = urllib.urlencode(values)
        req = urllib2.Request(url, data, headers) # when 'data' variable is included, urllib2 sends a POST request

        self.debug ("POST %s?%s" % (url, data))

        try:
            response = urllib2.urlopen(req)
            response_text = response.read().strip()
                        
        except urllib2.HTTPError, e:
            self.debug ("HTTP Error: %s" % e.code)
            return False
        
        if len(response_text) > 0:
            self.debug ("Received: %s" % response_text)
            message.respond(response_text)
            
        return True
