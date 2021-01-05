from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...types import UNSET, Unset
from typing import Dict
from typing import Union
from typing import cast
from ...models.transfer import Transfer



def _get_kwargs(
    *,
    client: Client,
    transfer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/transfers/{transferID}".format(
        client.base_url,transferID=transfer_id)

    headers: Dict[str, Any] = client.get_headers()

    if x_request_id is not UNSET:
        headers["x-request-id"] = x_request_id
    headers["x-organization"] = x_organization


    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[
    Transfer,
    None
]]:
    if response.status_code == 200:
        response_200 = Transfer.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = None

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[
    Transfer,
    None
]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    transfer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[Union[
    Transfer,
    None
]]:
    kwargs = _get_kwargs(
        client=client,
transfer_id=transfer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    transfer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Optional[Union[
    Transfer,
    None
]]:
    """ Get a Transfer object for the supplied organization """

    return sync_detailed(
        client=client,
transfer_id=transfer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    transfer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[Union[
    Transfer,
    None
]]:
    kwargs = _get_kwargs(
        client=client,
transfer_id=transfer_id,
x_request_id=x_request_id,
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
    transfer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Optional[Union[
    Transfer,
    None
]]:
    """ Get a Transfer object for the supplied organization """

    return (await asyncio_detailed(
        client=client,
transfer_id=transfer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )).parsed
