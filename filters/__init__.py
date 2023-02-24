from .link import IsLink


def register_all_filters(dp):
    dp.filters_factory.bind(IsLink)