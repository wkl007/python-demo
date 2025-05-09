class Dict(dict):
    """
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty'] # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    """

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'"Dict" object has no attribute "%s"' % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# doctest: +IGNORE_EXCEPTION_DETAIL 让 doctest 不强制匹配完整异常，只匹配类型（避免干扰）。
