from marshmallow import Schema, fields, post_load

from dominoes import Domino, DominoData


class DominoSchema(Schema):
    value_one = fields.Integer()
    value_two = fields.Integer()

    @post_load
    def to_domino(self, data, **kwargs):
        return Domino(**data)


class DominoDataSchema(Schema):
    starting_value = fields.Integer()
    domino_list = fields.List(fields.Nested(DominoSchema))

    @post_load
    def to_domino_data(self, data, **kwargs):
        return DominoData(**data)
