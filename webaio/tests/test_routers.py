from ..decorators import action
from ..viewsets import BaseViewSet
from ..routers import SimpleRouter


class TestSimpleRouter(object):

    def test_register_all_methods_viewset(self):

        # Defining viewsets to test
        class AllMethodsViewSet(BaseViewSet):

            def create(self, request):
                pass

            def list(self, request):
                pass

            def detail(self, request):
                pass

            def destroy(self, request):
                pass

            def update(self, request):
                pass

            def partial_update(self, request):
                pass

        router = SimpleRouter()
        router.register(AllMethodsViewSet, basename='all')

        assert len(router.routespatters) == len(SimpleRouter.known_actions)

    def test_register_none_methods_viewset(self):

        class NoneMethosViewset(BaseViewSet):
            pass

        router = SimpleRouter()
        router.register(NoneMethosViewset, basename='none')

        assert len(router.routespatters) == 0

    def test_register_custom_actions_viewset(self):

        class CustomActionMethosViewset(BaseViewSet):

            @action(detail=True, method='post')
            def detail_action(self):
                pass

            @action(detail=False, method='get')
            def non_detail_action(self):
                pass

        router = SimpleRouter()
        router.register(CustomActionMethosViewset, basename='custom')

        assert len(router.routespatters) == 2
