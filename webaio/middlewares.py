from aiohttp import web
from .exceptions import APIException


@web.middleware
async def api_exception_handler(request, handler):

    try:
        response = await handler(request)
        return response
    except APIException as exception:
        response = web.json_response(
            {'detail': exception.detail},
            status=exception.status_code
        )
        return response
