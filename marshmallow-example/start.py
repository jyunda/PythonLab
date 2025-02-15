from __future__ import annotations

from datetime import date
from pprint import pprint

from marshmallow import Schema, fields


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


if __name__ == "__main__":
    bowie = {"name": "David Bowie"}
    album = {"artist": bowie, "title": "Hunky Dory", "release_date": date(1971, 12, 17)}

    schema = AlbumSchema()
    result = schema.dump(album)
    pprint(result, indent=2)
    # { 'artist': {'name': 'David Bowie'},
    #   'release_date': '1971-12-17',
    #   'title': 'Hunky Dory'}
