from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from typing import Dict
from typing import cast
from ...models.create_micro_deposits import CreateMicroDeposits
from ...models.micro_deposits import MicroDeposits



def _get_kwargs(
    *,
    client: Client,
    json_body: CreateMicroDeposits,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/micro-deposits".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    headers["x-organization"] = x_organization


    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[MicroDeposits]:
    if response.status_code == 200:
        response_200 = MicroDeposits.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[MicroDeposits]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateMicroDeposits,
    x_organization: str,

) -> Response[MicroDeposits]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,
x_organization=x_organization,

    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    json_body: CreateMicroDeposits,
    x_organization: str,

) -> Optional[MicroDeposits]:
    """ Start micro-deposits for a Destination to validate. """

    return sync_detailed(
        client=client,
json_body=json_body,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateMicroDeposits,
    x_organization: str,

) -> Response[MicroDeposits]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,
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
    json_body: CreateMicroDeposits,
    x_organization: str,

) -> Optional[MicroDeposits]:
    """ Start micro-deposits for a Destination to validate. """

    return (await asyncio_detailed(
        client=client,
json_body=json_body,
x_organization=x_organization,

    )).parsed
