#!/usr/bin/env python

from enum import Enum

from types.promote_it_object import PromoteItObject


class Status(Enum):
    PENDING_APPROVAL = 1
    LIVE = 2
    REJECTED = 3
    BANNED = 4


    @classmethod
    def de_json(cls, data):
        if not data:
            return None

        return cls(**data)


class Channel(PromoteItObject):
    def __init__(self, id, name, title, description, submission, status):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.submission = submission
        self.status = status


    @classmethod
    def de_json(cls, data):
        if not data:
            return None

        return cls(**data)
