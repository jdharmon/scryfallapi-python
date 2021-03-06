# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CardSymbol(Model):
    """CardSymbol.

    :param symbol:
    :type symbol: str
    :param loose_variant:
    :type loose_variant: str
    :param english:
    :type english: str
    :param transposable:
    :type transposable: bool
    :param represents_mana:
    :type represents_mana: bool
    :param cmc:
    :type cmc: float
    :param appears_in_mana_costs:
    :type appears_in_mana_costs: bool
    :param funny:
    :type funny: bool
    :param colors: Possible values include: 'W', 'U', 'B', 'R', 'G'
    :type colors: str or ~scryfall.models.Colors
    """

    _attribute_map = {
        'symbol': {'key': 'symbol', 'type': 'str'},
        'loose_variant': {'key': 'loose_variant', 'type': 'str'},
        'english': {'key': 'english', 'type': 'str'},
        'transposable': {'key': 'transposable', 'type': 'bool'},
        'represents_mana': {'key': 'represents_mana', 'type': 'bool'},
        'cmc': {'key': 'cmc', 'type': 'float'},
        'appears_in_mana_costs': {'key': 'appears_in_mana_costs', 'type': 'bool'},
        'funny': {'key': 'funny', 'type': 'bool'},
        'colors': {'key': 'colors', 'type': 'Colors'},
    }

    def __init__(self, symbol=None, loose_variant=None, english=None, transposable=None, represents_mana=None, cmc=None, appears_in_mana_costs=None, funny=None, colors=None):
        super(CardSymbol, self).__init__()
        self.symbol = symbol
        self.loose_variant = loose_variant
        self.english = english
        self.transposable = transposable
        self.represents_mana = represents_mana
        self.cmc = cmc
        self.appears_in_mana_costs = appears_in_mana_costs
        self.funny = funny
        self.colors = colors
