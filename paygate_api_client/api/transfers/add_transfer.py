from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...types import UNSET, Unset
from typing import Dict
from typing import Union
from ...models.create_transfer import CreateTransfer
from typing import cast
from ...models.transfer import Transfer



def _get_kwargs(
    *,
    client: Client,
    json_body: CreateTransfer,
    x_idempotency_key: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/transfers".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    if x_idempotency_key is not UNSET:
        headers["x-idempotency-key"] = x_idempotency_key
    if x_request_id is not UNSET:
        headers["x-request-id"] = x_request_id
    headers["x-organization"] = x_organization


    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Transfer]:
    if response.status_code == 201:
        response_201 = Transfer.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Transfer]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateTransfer,
    x_idempotency_key: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[Transfer]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,
x_idempotency_key=x_idempotency_key,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    json_body: CreateTransfer,
    x_idempotency_key: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Optional[Transfer]:
    """ Create a new transfer between a Source and a Destination. Transfers can only be modified in the pending status.
 """

    return sync_detailed(
        client=client,
json_body=json_body,
x_idempotency_key=x_idempotency_key,
x_request_id=x_request_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateTransfer,
    x_idempotency_key: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[Transfer]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,
x_idempotency_key=x_idempotency_key,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    json_body: CreateTransfer,
    x_idempotency_key: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Optional[Transfer]:
    """ Create a new transfer between a Source and a Destination. Transfers can only be modified in the pending status.
 """

    return (await asyncio_detailed(
        client=client,
json_body=json_body,
x_idempotency_key=x_idempotency_key,
x_request_id=x_request_id,
x_organization=x_organization,

    )).parsed
