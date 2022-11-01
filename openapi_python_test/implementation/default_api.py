from openapi_python_test.generated.apis.default_api import DefaultApi
from openapi_python_test.generated.models.hello_world_get200_response import HelloWorldGet200Response

class DefaultApiImpl(DefaultApi):
    async def hello_world() -> HelloWorldGet200Response:
        return HelloWorldGet200Response(hello="world")