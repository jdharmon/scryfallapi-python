# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class Layouts(Enum):

    normal = "normal"
    split = "split"
    flip = "flip"
    transform = "transform"
    meld = "meld"
    leveler = "leveler"
    saga = "saga"
    planar = "planar"
    scheme = "scheme"
    vanguard = "vanguard"
    token = "token"
    double_faced_token = "double_faced_token"
    emblem = "emblem"
    augment = "augment"
    host = "host"


class Colors(Enum):

    w = "W"
    u = "U"
    b = "B"
    r = "R"
    g = "G"


class LegalStatus(Enum):

    legal = "legal"
    not_legal = "not_legal"
    restricted = "restricted"
    banned = "banned"


class Rarity(Enum):

    common = "common"
    uncommon = "uncommon"
    rare = "rare"
    mythic = "mythic"


class BorderColors(Enum):

    black = "black"
    borderless = "borderless"
    gold = "gold"
    silver = "silver"
    white = "white"


class SetTypes(Enum):

    core = "core"
    expansion = "expansion"
    masters = "masters"
    masterpiece = "masterpiece"
    from_the_vault = "from_the_vault"
    spellbook = "spellbook"
    premium_deck = "premium_deck"
    duel_deck = "duel_deck"
    commander = "commander"
    planechase = "planechase"
    conspiracy = "conspiracy"
    archenemy = "archenemy"
    vanguard = "vanguard"
    funny = "funny"
    starter = "starter"
    box = "box"
    promo = "promo"
    token = "token"
    memorabilia = "memorabilia"
    treasure_chest = "treasure_chest"


class UniqueStrategy(Enum):

    cards = "cards"
    art = "art"
    prints = "prints"


class SortOrder(Enum):

    name = "name"
    set = "set"
    released = "released"
    rarity = "rarity"
    color = "color"
    usd = "usd"
    tix = "tix"
    eur = "eur"
    cmc = "cmc"
    power = "power"
    toughness = "toughness"
    edhrec = "edhrec"
    artist = "artist"


class SortDirection(Enum):

    auto = "auto"
    asc = "asc"
    desc = "desc"
