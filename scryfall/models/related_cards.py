# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RelatedCards(Model):
    """RelatedCards.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param uri:
    :type uri: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, uri=None):
        super(RelatedCards, self).__init__()
        self.id = id
        self.name = name
        self.uri = uri
