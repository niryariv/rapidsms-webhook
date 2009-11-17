#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

# URL to POST to when an SMS is received

target_urls = {
    '*' : 'http://qkhack.appspot.com/rapid',        # default, if no keyword is matched
    'test'  : 'http://qkhack.appspot.com/rapid1',
    'another' : 'http://qkhack.appspot.com/rapid2',
}

# to set a single URL target regardless of keyword, use:
# target_urls = { '*' : 'http://qkhack.appspot.com/rapid' }


# User agent to send with the request
user_agent = 'RapidSMS WebHook/0.1'