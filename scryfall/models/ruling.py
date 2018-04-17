# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Ruling(Model):
    """Ruling.

    :param source:
    :type source: str
    :param published_at:
    :type published_at: date
    :param comment:
    :type comment: str
    """

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
        'published_at': {'key': 'published_at', 'type': 'date'},
        'comment': {'key': 'comment', 'type': 'str'},
    }

    def __init__(self, source=None, published_at=None, comment=None):
        super(Ruling, self).__init__()
        self.source = source
        self.published_at = published_at
        self.comment = comment
