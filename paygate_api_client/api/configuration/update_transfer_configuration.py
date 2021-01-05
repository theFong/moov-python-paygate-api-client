from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...types import UNSET, Unset
from typing import Dict
from typing import Union
from typing import cast
from ...models.organization_configuration import OrganizationConfiguration



def _get_kwargs(
    *,
    client: Client,
    json_body: OrganizationConfiguration,
    x_organization: Union[Unset, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/configuration/transfers".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    if x_organization is not UNSET:
        headers["x-organization"] = x_organization


    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[OrganizationConfiguration]:
    if response.status_code == 200:
        response_200 = OrganizationConfiguration.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[OrganizationConfiguration]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: OrganizationConfiguration,
    x_organization: Union[Unset, str] = UNSET,

) -> Response[OrganizationConfiguration]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,
x_organization=x_organization,

    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    json_body: OrganizationConfiguration,
    x_organization: Union[Unset, str] = UNSET,

) -> Optional[OrganizationConfiguration]:
    """ Update the config for the provided organization. """

    return sync_detailed(
        client=client,
json_body=json_body,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    json_body: OrganizationConfiguration,
    x_organization: Union[Unset, str] = UNSET,

) -> Response[OrganizationConfiguration]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,
x_organization=x_organization,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    json_body: OrganizationConfiguration,
    x_organization: Union[Unset, str] = UNSET,

) -> Optional[OrganizationConfiguration]:
    """ Update the config for the provided organization. """

    return (await asyncio_detailed(
        client=client,
json_body=json_body,
x_organization=x_organization,

    )).parsed
