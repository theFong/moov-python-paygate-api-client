from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...types import UNSET, Unset
from typing import Union



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




def _build_response(*, response: httpx.Response) -> Response[None]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    transfer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
transfer_id=transfer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    transfer_id: str,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
transfer_id=transfer_id,
x_request_id=x_request_id,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(
            **kwargs
        )

    return _build_response(response=response)

