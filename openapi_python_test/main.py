from fastapi import FastAPI

from openapi_python_test.generated.apis.default_api import initialize_router
from openapi_python_test.implementation.default_api import DefaultApiImpl

app = FastAPI(
    title="my API",
    description=" API ",
    version="1.0.0",
)

app.include_router(initialize_router(DefaultApiImpl()))
