# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from connector_builder.generated.models.add_fields_all_of import AddFieldsAllOf
from connector_builder.generated.models.added_field_definition import AddedFieldDefinition
from connector_builder.generated.models.parsed_add_field_definition import ParsedAddFieldDefinition


class AddFields(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AddFields - a model defined in OpenAPI

        fields: The fields of this AddFields.
        parsed_fields: The parsed_fields of this AddFields [Optional].
    """

    fields: List[AddedFieldDefinition]
    parsed_fields: Optional[List[ParsedAddFieldDefinition]] = None

AddFields.update_forward_refs()
