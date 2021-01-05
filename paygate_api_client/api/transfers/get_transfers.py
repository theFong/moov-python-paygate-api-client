from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response

from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import Dict
from typing import Union
import datetime
from ...models.transfers import Transfers
from ...models.transfer_status import TransferStatus
from typing import cast



def _get_kwargs(
    *,
    client: Client,
    skip: Union[Unset, int] = 0,
    count: Union[Unset, int] = 25,
    status: Union[Unset, TransferStatus] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    organization_i_ds: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Dict[str, Any]:
    url = "{}/transfers".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()

    if x_request_id is not UNSET:
        headers["x-request-id"] = x_request_id
    headers["x-organization"] = x_organization


    json_status: Union[Unset, TransferStatus] = UNSET
    if not isinstance(status, Unset):
        json_status = status

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()

    params: Dict[str, Any] = {
    }
    if skip is not UNSET:
        params["skip"] = skip
    if count is not UNSET:
        params["count"] = count
    if status is not UNSET:
        params["status"] = json_status
    if start_date is not UNSET:
        params["startDate"] = json_start_date
    if end_date is not UNSET:
        params["endDate"] = json_end_date
    if organization_i_ds is not UNSET:
        params["organizationIDs"] = organization_i_ds
    if customer_i_ds is not UNSET:
        params["customerIDs"] = customer_i_ds


    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Transfers]:
    if response.status_code == 200:
        response_200 = Transfers.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Transfers]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    skip: Union[Unset, int] = 0,
    count: Union[Unset, int] = 25,
    status: Union[Unset, TransferStatus] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    organization_i_ds: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[Transfers]:
    kwargs = _get_kwargs(
        client=client,
skip=skip,
count=count,
status=status,
start_date=start_date,
end_date=end_date,
organization_i_ds=organization_i_ds,
customer_i_ds=customer_i_ds,
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
    skip: Union[Unset, int] = 0,
    count: Union[Unset, int] = 25,
    status: Union[Unset, TransferStatus] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    organization_i_ds: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Optional[Transfers]:
    """ List all Transfers created for the given organization. """

    return sync_detailed(
        client=client,
skip=skip,
count=count,
status=status,
start_date=start_date,
end_date=end_date,
organization_i_ds=organization_i_ds,
customer_i_ds=customer_i_ds,
x_request_id=x_request_id,
x_organization=x_organization,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    skip: Union[Unset, int] = 0,
    count: Union[Unset, int] = 25,
    status: Union[Unset, TransferStatus] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    organization_i_ds: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Response[Transfers]:
    kwargs = _get_kwargs(
        client=client,
skip=skip,
count=count,
status=status,
start_date=start_date,
end_date=end_date,
organization_i_ds=organization_i_ds,
customer_i_ds=customer_i_ds,
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
    skip: Union[Unset, int] = 0,
    count: Union[Unset, int] = 25,
    status: Union[Unset, TransferStatus] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    organization_i_ds: Union[Unset, str] = UNSET,
    customer_i_ds: Union[Unset, str] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    x_organization: str,

) -> Optional[Transfers]:
    """ List all Transfers created for the given organization. """

    return (await asyncio_detailed(
        client=client,
skip=skip,
count=count,
status=status,
start_date=start_date,
end_date=end_date,
organization_i_ds=organization_i_ds,
customer_i_ds=customer_i_ds,
x_request_id=x_request_id,
x_organization=x_organization,

    )).parsed
