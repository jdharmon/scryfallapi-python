# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SetList(Model):
    """SetList.

    :param data:
    :type data: list[~scryfall.models.Set]
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': '[Set]'},
    }

    def __init__(self, data=None):
        super(SetList, self).__init__()
        self.data = data
