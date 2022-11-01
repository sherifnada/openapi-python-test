# coding: utf-8

from abc import ABC, abstractmethod
from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter
)

from openapi_python_test.generated.models.hello_world_get200_response import HelloWorldGet200Response


class DefaultApi(ABC): 
  # autogenned, contains pythonic signature of api
  @abstractmethod
  async def hello_world(self, *args, **kwargs) -> HelloWorldGet200Response:
     """ hello world """


def initialize_router(api: DefaultApi) -> APIRouter:
    router = APIRouter()
    # Directly add the method as a route implementation 
    # instead of adding via decoration (which is the current approach)
    router.add_api_route(
        "/hello_world",
        endpoint=api.hello_world,
        methods=["GET"],
        responses={
            200: {"model": HelloWorldGet200Response, "description": "Successful operation"},
        }
    )
    
    # for each endpoint, do the same thing...
    # ...
    
    # at the end just return the router
    print("HELLOOOOO")
    
    return router