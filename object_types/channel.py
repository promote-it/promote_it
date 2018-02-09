#!/usr/bin/env python

from enum import Enum

from .promote_it_object import PromoteItObject

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
    def __init__(self,
                 id=None,
                 name=None,
                 title=None,
                 description=None,
                 submitted_by=None,
                 submitted_on=None,
                 status=Status.PENDING_APPROVAL):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.submitted_by = submitted_by
        self.submitted_on = submitted_on
        self.status = status


    @classmethod
    def de_json(cls, data):
        if not data:
            return None

        return cls(**data)
