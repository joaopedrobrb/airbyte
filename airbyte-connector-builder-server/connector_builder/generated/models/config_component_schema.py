# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from connector_builder.generated.models.check_stream import CheckStream
from connector_builder.generated.models.declarative_stream import DeclarativeStream


class ConfigComponentSchema(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ConfigComponentSchema - a model defined in OpenAPI

        version: The version of this ConfigComponentSchema.
        check: The check of this ConfigComponentSchema.
        streams: The streams of this ConfigComponentSchema.
    """

    version: str
    check: CheckStream
    streams: List[DeclarativeStream]

ConfigComponentSchema.update_forward_refs()
