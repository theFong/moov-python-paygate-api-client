from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...models.micro_deposits import MicroDeposits
from typing import Dict
from typing import cast



def _get_kwargs(
    *,
    client: Client,
    account_id: str,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/accounts/{accountID}/micro-deposits".format(
        client.base_url,accountID=account_id)

    headers: Dict[str, Any] = client.get_headers()

    headers["x-organization"] = x_organization


    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
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
    account_id: str,
    x_organization: str,

) -> Response[MicroDeposits]:
    kwargs = _get_kwargs(
        client=client,
account_id=account_id,
x_organization=x_organization,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    account_id: str,
    x_organization: str,

) -> Optional[MicroDeposits]:
    """ Retrieve the micro-deposits information for a specific accountID """

    return sync_detailed(
        client=client,
account_id=account_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    account_id: str,
    x_organization: str,

) -> Response[MicroDeposits]:
    kwargs = _get_kwargs(
        client=client,
account_id=account_id,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    account_id: str,
    x_organization: str,

) -> Optional[MicroDeposits]:
    """ Retrieve the micro-deposits information for a specific accountID """

    return (await asyncio_detailed(
        client=client,
account_id=account_id,
x_organization=x_organization,

    )).parsed
