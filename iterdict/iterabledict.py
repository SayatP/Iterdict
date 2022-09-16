class IterDict(dict):
    def __init__(self, *args, **kw):
        self._data = super(IterDict, self).__init__(*args, **kw)
        self._itemlist = list(super(IterDict, self).keys())
        self._cursor = 0

    def __setitem__(self, key, value):
        self._itemlist.append(key)
        super(self._data, self).__setitem__(key, value)

    def __next__(self):
        if self._cursor == len(self._itemlist):
            raise StopIteration
        result = self._itemlist[self._cursor]
        self._cursor += 1
        return result
