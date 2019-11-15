import enum
from typing import Tuple

import sqlalchemy as s

EN = 'english'


class Weight(enum.Enum):
    """TS Rank weight as an Enum."""
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'


def match(column: s.Column, search: str, lang=EN):
    """Query that matches a TSVECTOR column with unsafe search words.

    See `websearch_to_tsquery <https://www.postgresql.org/docs/11/
    textsearch-controls.html#TEXTSEARCH-PARSING-QUERIES>`_ for more info.
    """
    return column.op('@@')(s.func.websearch_to_tsquery(lang, search))


def rank(column: s.Column, search: str, lang=EN):
    """Query that ranks a TSVECTOR column with unsafe search words.

    See `websearch_to_tsquery <https://www.postgresql.org/docs/11/
    textsearch-controls.html#TEXTSEARCH-PARSING-QUERIES>`_ for more info.
    """
    return s.func.ts_rank(column, s.func.websearch_to_tsquery(lang, search))


def _vectorize(col: s.Column, weight: Weight = Weight.D, lang=EN):
    return s.func.setweight(s.func.to_tsvector(lang, s.func.coalesce(col, '')), weight.name)


def vectorize(*cols_with_weights: Tuple[s.Column, Weight], lang=EN):
    """Produces a query that takes one ore more columns and their
    respective weights, and generates one big TSVECTOR.

    This method takes care of ``null`` column values.
    """
    first, rest = cols_with_weights[0], cols_with_weights[1:]
    tokens = _vectorize(*first, lang=lang)
    for unit in rest:
        tokens = tokens.concat(_vectorize(*unit, lang=lang))
    return tokens
