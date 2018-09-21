import os
import sys
from collections import Mapping
from usgw.util import trim


class Config(Mapping):
    def __init__(self):
        self._dict = dict()
        self._find_configfile()
        self._load()

    def __getitem__(self, key):
        return self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def _load(self):
        with open(self._filename, 'r') as f:
            for line in f:
                if '#' in line:
                    line, comment = line.split('#', 1)
                if '=' in line:
                    key, val = map(trim, line.split('=', 1))
                else:
                    key, val = (trim(line), '')
                if len(key):
                    self._dict[key] = val
        f.close()

    def _find_configfile(self):
        self._filename = os.path.join(sys.prefix, 'etc', 'usgw.conf')

    def __repr__(self):
        return repr(self._dict)

    @property
    def filename(self):
        return self._filename
