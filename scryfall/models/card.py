# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Card(Model):
    """Card.

    :param id:
    :type id: str
    :param oracle_id:
    :type oracle_id: str
    :param multiverse_ids:
    :type multiverse_ids: list[int]
    :param mtgo_id:
    :type mtgo_id: int
    :param arena_id:
    :type arena_id: int
    :param mtgo_foil_id:
    :type mtgo_foil_id: int
    :param uri:
    :type uri: str
    :param scryfall_uri:
    :type scryfall_uri: str
    :param prints_search_uri:
    :type prints_search_uri: str
    :param rulings_uri:
    :type rulings_uri: str
    :param name:
    :type name: str
    :param layout: Possible values include: 'normal', 'split', 'flip',
     'transform', 'meld', 'leveler', 'saga', 'planar', 'scheme', 'vanguard',
     'token', 'double_faced_token', 'emblem', 'augment', 'host'
    :type layout: str or ~scryfall.models.Layouts
    :param cmc:
    :type cmc: float
    :param type_line:
    :type type_line: str
    :param oracle_text:
    :type oracle_text: str
    :param mana_cost:
    :type mana_cost: str
    :param power:
    :type power: str
    :param toughness:
    :type toughness: str
    :param loyalty:
    :type loyalty: str
    :param life_modifier:
    :type life_modifier: str
    :param hand_modifier:
    :type hand_modifier: str
    :param colors:
    :type colors: list[str or ~scryfall.models.Colors]
    :param color_indicator:
    :type color_indicator: list[str or ~scryfall.models.Colors]
    :param color_identity:
    :type color_identity: list[str or ~scryfall.models.Colors]
    :param all_parts:
    :type all_parts: list[~scryfall.models.RelatedCards]
    :param card_faces:
    :type card_faces: list[~scryfall.models.CardFace]
    :param legalities:
    :type legalities: ~scryfall.models.Legality
    :param reserved:
    :type reserved: bool
    :param edhrec_rank:
    :type edhrec_rank: int
    :param set:
    :type set: str
    :param set_name:
    :type set_name: str
    :param collector_number:
    :type collector_number: str
    :param set_search_uri:
    :type set_search_uri: str
    :param scryfall_set_uri:
    :type scryfall_set_uri: str
    :param image_uris:
    :type image_uris: ~scryfall.models.ImageUri
    :param highres_image:
    :type highres_image: bool
    :param reprint:
    :type reprint: bool
    :param digital:
    :type digital: bool
    :param rarity: Possible values include: 'common', 'uncommon', 'rare',
     'mythic'
    :type rarity: str or ~scryfall.models.Rarity
    :param flavor_text:
    :type flavor_text: str
    :param artist:
    :type artist: str
    :param illustration_id:
    :type illustration_id: str
    :param frame:
    :type frame: str
    :param full_art:
    :type full_art: bool
    :param watermark:
    :type watermark: str
    :param border_color: Possible values include: 'black', 'borderless',
     'gold', 'silver', 'white'
    :type border_color: str or ~scryfall.models.BorderColors
    :param story_spotlight_number:
    :type story_spotlight_number: int
    :param story_spotlight_uri:
    :type story_spotlight_uri: str
    :param timeshifted:
    :type timeshifted: bool
    :param colorshifted:
    :type colorshifted: bool
    :param futureshifted:
    :type futureshifted: bool
    :param purchase_uris:
    :type purchase_uris: dict[str, str]
    :param related_uris:
    :type related_uris: dict[str, str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'oracle_id': {'key': 'oracle_id', 'type': 'str'},
        'multiverse_ids': {'key': 'multiverse_ids', 'type': '[int]'},
        'mtgo_id': {'key': 'mtgo_id', 'type': 'int'},
        'arena_id': {'key': 'arena_id', 'type': 'int'},
        'mtgo_foil_id': {'key': 'mtgo_foil_id', 'type': 'int'},
        'uri': {'key': 'uri', 'type': 'str'},
        'scryfall_uri': {'key': 'scryfall_uri', 'type': 'str'},
        'prints_search_uri': {'key': 'prints_search_uri', 'type': 'str'},
        'rulings_uri': {'key': 'rulings_uri', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'layout': {'key': 'layout', 'type': 'Layouts'},
        'cmc': {'key': 'cmc', 'type': 'float'},
        'type_line': {'key': 'type_line', 'type': 'str'},
        'oracle_text': {'key': 'oracle_text', 'type': 'str'},
        'mana_cost': {'key': 'mana_cost', 'type': 'str'},
        'power': {'key': 'power', 'type': 'str'},
        'toughness': {'key': 'toughness', 'type': 'str'},
        'loyalty': {'key': 'loyalty', 'type': 'str'},
        'life_modifier': {'key': 'life_modifier', 'type': 'str'},
        'hand_modifier': {'key': 'hand_modifier', 'type': 'str'},
        'colors': {'key': 'colors', 'type': '[Colors]'},
        'color_indicator': {'key': 'color_indicator', 'type': '[Colors]'},
        'color_identity': {'key': 'color_identity', 'type': '[Colors]'},
        'all_parts': {'key': 'all_parts', 'type': '[RelatedCards]'},
        'card_faces': {'key': 'card_faces', 'type': '[CardFace]'},
        'legalities': {'key': 'legalities', 'type': 'Legality'},
        'reserved': {'key': 'reserved', 'type': 'bool'},
        'edhrec_rank': {'key': 'edhrec_rank', 'type': 'int'},
        'set': {'key': 'set', 'type': 'str'},
        'set_name': {'key': 'set_name', 'type': 'str'},
        'collector_number': {'key': 'collector_number', 'type': 'str'},
        'set_search_uri': {'key': 'set_search_uri', 'type': 'str'},
        'scryfall_set_uri': {'key': 'scryfall_set_uri', 'type': 'str'},
        'image_uris': {'key': 'image_uris', 'type': 'ImageUri'},
        'highres_image': {'key': 'highres_image', 'type': 'bool'},
        'reprint': {'key': 'reprint', 'type': 'bool'},
        'digital': {'key': 'digital', 'type': 'bool'},
        'rarity': {'key': 'rarity', 'type': 'Rarity'},
        'flavor_text': {'key': 'flavor_text', 'type': 'str'},
        'artist': {'key': 'artist', 'type': 'str'},
        'illustration_id': {'key': 'illustration_id', 'type': 'str'},
        'frame': {'key': 'frame', 'type': 'str'},
        'full_art': {'key': 'full_art', 'type': 'bool'},
        'watermark': {'key': 'watermark', 'type': 'str'},
        'border_color': {'key': 'border_color', 'type': 'BorderColors'},
        'story_spotlight_number': {'key': 'story_spotlight_number', 'type': 'int'},
        'story_spotlight_uri': {'key': 'story_spotlight_uri', 'type': 'str'},
        'timeshifted': {'key': 'timeshifted', 'type': 'bool'},
        'colorshifted': {'key': 'colorshifted', 'type': 'bool'},
        'futureshifted': {'key': 'futureshifted', 'type': 'bool'},
        'purchase_uris': {'key': 'purchase_uris', 'type': '{str}'},
        'related_uris': {'key': 'related_uris', 'type': '{str}'},
    }

    def __init__(self, id=None, oracle_id=None, multiverse_ids=None, mtgo_id=None, arena_id=None, mtgo_foil_id=None, uri=None, scryfall_uri=None, prints_search_uri=None, rulings_uri=None, name=None, layout=None, cmc=None, type_line=None, oracle_text=None, mana_cost=None, power=None, toughness=None, loyalty=None, life_modifier=None, hand_modifier=None, colors=None, color_indicator=None, color_identity=None, all_parts=None, card_faces=None, legalities=None, reserved=None, edhrec_rank=None, set=None, set_name=None, collector_number=None, set_search_uri=None, scryfall_set_uri=None, image_uris=None, highres_image=None, reprint=None, digital=None, rarity=None, flavor_text=None, artist=None, illustration_id=None, frame=None, full_art=None, watermark=None, border_color=None, story_spotlight_number=None, story_spotlight_uri=None, timeshifted=None, colorshifted=None, futureshifted=None, purchase_uris=None, related_uris=None):
        super(Card, self).__init__()
        self.id = id
        self.oracle_id = oracle_id
        self.multiverse_ids = multiverse_ids
        self.mtgo_id = mtgo_id
        self.arena_id = arena_id
        self.mtgo_foil_id = mtgo_foil_id
        self.uri = uri
        self.scryfall_uri = scryfall_uri
        self.prints_search_uri = prints_search_uri
        self.rulings_uri = rulings_uri
        self.name = name
        self.layout = layout
        self.cmc = cmc
        self.type_line = type_line
        self.oracle_text = oracle_text
        self.mana_cost = mana_cost
        self.power = power
        self.toughness = toughness
        self.loyalty = loyalty
        self.life_modifier = life_modifier
        self.hand_modifier = hand_modifier
        self.colors = colors
        self.color_indicator = color_indicator
        self.color_identity = color_identity
        self.all_parts = all_parts
        self.card_faces = card_faces
        self.legalities = legalities
        self.reserved = reserved
        self.edhrec_rank = edhrec_rank
        self.set = set
        self.set_name = set_name
        self.collector_number = collector_number
        self.set_search_uri = set_search_uri
        self.scryfall_set_uri = scryfall_set_uri
        self.image_uris = image_uris
        self.highres_image = highres_image
        self.reprint = reprint
        self.digital = digital
        self.rarity = rarity
        self.flavor_text = flavor_text
        self.artist = artist
        self.illustration_id = illustration_id
        self.frame = frame
        self.full_art = full_art
        self.watermark = watermark
        self.border_color = border_color
        self.story_spotlight_number = story_spotlight_number
        self.story_spotlight_uri = story_spotlight_uri
        self.timeshifted = timeshifted
        self.colorshifted = colorshifted
        self.futureshifted = futureshifted
        self.purchase_uris = purchase_uris
        self.related_uris = related_uris
