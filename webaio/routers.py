"""
Routers provide a convenient and consistent way of automatically
determining the URL conf for your API.
They are used by simply instantiating a Router class, and then registering
all the required ViewSets with that router.
For example, you might have a `routes.py` that looks something like this:
    router = routers.SimpleRouter()
    router.register(UserViewSet, basename='user')
    router.register(AccountViewSet, basename='account')
    routespatters = router.routespatters
"""
from aiohttp import web
from inspect import getmembers
from .viewsets import BaseViewSet


def _is_custom_action(attr) -> bool:
    """
    Return True if the object has _is_custom_action attribute and is True
    """
    if hasattr(attr, '_is_custom_action'):
        return attr._is_custom_action
    return False


class SimpleRouter(object):

    base_action_path = '/{basename}/'
    detail_action_path = '/{basename}/{{id}}/'
    known_actions = [
        {'action': 'create', 'http_method': web.post, 'path': base_action_path},
        {'action': 'list', 'http_method': web.get, 'path': base_action_path},
        {'action': 'detail', 'http_method': web.get, 'path': detail_action_path},
        {'action': 'destroy', 'http_method': web.delete, 'path': detail_action_path},
        {'action': 'update', 'http_method': web.put, 'path': detail_action_path},
        {'action': 'partial_update', 'http_method': web.patch, 'path': detail_action_path},
    ]

    def __init__(self):
        self.routespatters = []

    def register(self, ViewSet: BaseViewSet, basename: str):
        actions = self._get_custom_actions(ViewSet) + self.known_actions

        for action in actions:
            current_action = action.get('action')
            if hasattr(ViewSet, current_action):
                http_method = action.get('http_method')

                self.routespatters.append(
                    http_method(
                        action['path'].format(basename=basename),
                        getattr(ViewSet, current_action)
                    )
                )

    def _get_custom_actions(self, ViewSet: BaseViewSet) -> list:
        """
        Returns a list of custom actions defined in the ViewSet class
        """
        methods = [method for _, method in getmembers(ViewSet, _is_custom_action)]
        actions = []
        for method in methods:
            action_path = self.detail_action_path if method.detail else self.base_action_path
            action_path += f'{method.url_name}/'
            action = {
                'action': method.__name__,
                'http_method': getattr(web, method.method),
                'path': action_path,
            }
            actions.append(action)

        return actions
