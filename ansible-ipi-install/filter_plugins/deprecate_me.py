# -*- coding: utf-8 -*-
from ansible.utils.display import Display


class FilterModule(object):
    def filters(self):
        return {"deprecate_me": self.warn_filter}

    @staticmethod
    def warn_filter(message, **kwargs):
        Display().deprecated(message)
        return message
