from functools import reduce
from settings import INSTALLED_APPS


def get_server_actions():
    modules = reduce(
            lambda value, item: value + [__import__(f'{item}.actions')],
            INSTALLED_APPS,
            [],
        )
    actions = reduce(
            lambda value, item: value + [getattr(item, 'actions', [])],
            modules,
            [],
        )
    return reduce(
            lambda value, item: value + getattr(item, 'actionnames', []),
            actions,
            []
        )

