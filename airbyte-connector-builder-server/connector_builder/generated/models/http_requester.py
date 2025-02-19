# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from connector_builder.generated.models.any_of_composite_error_handler_default_error_handler import AnyOfCompositeErrorHandlerDefaultErrorHandler
from connector_builder.generated.models.any_of_interpolated_stringstring import AnyOfInterpolatedStringstring
from connector_builder.generated.models.any_of_no_auth_declarative_oauth2_authenticator_api_key_authenticator_bearer_authenticator_basic_http_authenticator import AnyOfNoAuthDeclarativeOauth2AuthenticatorApiKeyAuthenticatorBearerAuthenticatorBasicHttpAuthenticator
from connector_builder.generated.models.any_ofstringstring import AnyOfstringstring
from connector_builder.generated.models.http_requester_all_of import HttpRequesterAllOf
from connector_builder.generated.models.interpolated_request_options_provider import InterpolatedRequestOptionsProvider
from connector_builder.generated.models.requester import Requester


class HttpRequester(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    HttpRequester - a model defined in OpenAPI

        name: The name of this HttpRequester.
        url_base: The url_base of this HttpRequester.
        path: The path of this HttpRequester.
        config: The config of this HttpRequester.
        http_method: The http_method of this HttpRequester [Optional].
        request_options_provider: The request_options_provider of this HttpRequester [Optional].
        authenticator: The authenticator of this HttpRequester [Optional].
        error_handler: The error_handler of this HttpRequester [Optional].
    """

    name: str
    url_base: AnyOfInterpolatedStringstring
    path: AnyOfInterpolatedStringstring
    config: Dict[str, Any]
    http_method: Optional[AnyOfstringstring] = None
    request_options_provider: Optional[InterpolatedRequestOptionsProvider] = None
    authenticator: Optional[AnyOfNoAuthDeclarativeOauth2AuthenticatorApiKeyAuthenticatorBearerAuthenticatorBasicHttpAuthenticator] = None
    error_handler: Optional[AnyOfCompositeErrorHandlerDefaultErrorHandler] = None

HttpRequester.update_forward_refs()
