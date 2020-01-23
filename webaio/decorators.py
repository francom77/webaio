def action(method='get', detail=False, **kwargs):
    """
    Mark a ViewSet method as a routable action.
    `@action`-decorated functions will be endowed with a `mapping` property,
    a `MethodMapper` that can be used to add additional method-based behaviors
    on the routed action.
    :param methods: A list of HTTP method names this action responds to.
                    Defaults to GET only.
    :param detail: Required. Determines whether this action applies to
                   instance/detail requests or collection/list requests.
    :param kwargs: Additional properties to set on the view.  This can be used
                   to override viewset-level *_classes settings, equivalent to
                   how the `@renderer_classes` etc. decorators work for function-
                   based API views.
    """
    method = method.lower()

    def decorator(func):
        func._is_custom_action = True
        func.detail = detail
        func.method = method
        func.url_path = func.__name__
        func.url_name = func.__name__.replace('_', '-')
        func.kwargs = kwargs

        return func
    return decorator
