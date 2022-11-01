# coding: utf-8

from abc import ABC, abstractmethod
from typing import Callable  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter
)

from openapi_python_test.generated.models.hello_world_get200_response import HelloWorldGet200Response
import inspect

class DefaultApi(ABC): 
  @abstractmethod
  async def hello_world(self, *args, **kwargs) -> HelloWorldGet200Response:
     """ hello world """


def _assert_signature_is_set(method: Callable) -> None:
    """
    APIRouter().add_api_route expects the input method to have a signature. It gets signatures
    by running inspect.signature(method) under the hood. 

    In the case that an instance method does not declare "self" as an input parameter (due to developer error 
    for example), then the call to inspect.signature() fails. 

    This method is sort of a workaround. It tells the developer how to fix the problem if it's detected.
    """
    try:
        inspect.signature(method)
    except ValueError as e:
        # Based on empirical observation, the call to inspect fails with a ValueError
        # with exactly one argument: "invalid method signature"
        if e.args and len(e.args) == 1 and e.args[0] == "invalid method signature":
            # I couldn't figure out how to setattr on a "method" object to populate the signature. For now just kick
            # it back to the developer and tell them to set the "self" variable
            raise Exception(f"Method {method.__name__} in class {type(method.__self__).__name__} must declare the variable 'self'. ")
        else:
            raise


def initialize_router(api: DefaultApi) -> APIRouter:
    router = APIRouter()
    
    _assert_signature_is_set(api.hello_world)
    router.add_api_route(
        "/hello_world",
        endpoint=api.hello_world,
        methods=["GET"],
        responses={
            200: {"model": HelloWorldGet200Response, "description": "Successful operation"},
        },
        tags=["default"]
    )
    
    return router