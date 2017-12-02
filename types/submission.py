#!/usr/bin/env python

from types.promote_it_object import PromoteItObject

class Submission(PromoteItObject):

    def __init__(self):
        self.user
        self.time


    @classmethod
    def de_json(cls, data):
        if not data:
            return None

        return cls(**data)