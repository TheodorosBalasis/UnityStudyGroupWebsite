from pymongo import MongoClient
from usgw.config import Config
from usgw.util import atoi

config = Config()


def get_db():
    ''' Returns DB handle. '''
    dbuser = config['DBUSER']
    dbpass = config['DBPASS']
    dbtype = config['DBTYPE']
    dbhost = config['DBHOST']
    dbport = config['DBPORT']
    dbname = config['DBNAME']

    client = MongoClient('%s://%s:%s@%s/%s' % (
        dbtype, dbuser, dbpass, dbhost, dbname
    ), atoi(dbport))

    return client[dbname]
