import os, sys
from usgw.config import Config

def main():
    config = Config()
    print "===>", config.filename
    n = len(max(config, key=len))
    for key in config:
        print "%-*s = %s" % (n, key, config[key])
