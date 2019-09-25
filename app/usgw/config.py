from os import path
from sys import prefix
from collections import Mapping

class Config(Mapping):
    def __init__(self) -> None:
        self._dict = dict()
        self._find_configfile()
        self._load()

    def __getitem__(self, key) -> str:
        return self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self) -> int:
        return len(self._dict)

    def _load(self) -> None:
        '''Load the config file.'''
        with open(self._filename, 'r') as f:
            for line in f:
                if '#' in line:
                    line, comment = line.split('#', 1)
                if '=' in line:
                    key, val = map(lambda s: s.strip() , line.split('=', 1))
                else:
                    key, val = (line.strip(), '')
                if len(key):
                    self._dict[key] = val
        f.close()

    def _find_configfile(self):
        self._filename = path.join(prefix, 'etc', 'usgw.conf')

    def __repr__(self) -> str:
        return repr(self._dict)

    @property
    def filename(self) -> str:
        return self._filename
