from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from dateutil.parser import isoparse
from typing import Union
import datetime
from ..types import UNSET, Unset
from ..models.source import Source
from ..models.return_code import ReturnCode
from typing import Optional
from typing import cast
from ..models.destination import Destination
from typing import cast, List
from ..models.transfer_status import TransferStatus
from ..models.amount import Amount



@attr.s(auto_attribs=True)
class Transfer:
    """  """
    transfer_id: str
    amount: Amount
    source: Source
    destination: Destination
    description: str
    status: TransferStatus
    created: datetime.datetime
    trace_numbers: List[str]
    same_day: bool = False
    return_code: Union[Optional[ReturnCode], Unset] = UNSET
    processed_at: Union[Unset, Optional[datetime.datetime]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        transfer_id =  self.transfer_id
        amount = self.amount.to_dict()

        source = self.source.to_dict()

        destination = self.destination.to_dict()

        description =  self.description
        status = self.status.value

        same_day =  self.same_day
        created = self.created.isoformat()

        trace_numbers = self.trace_numbers




        return_code: Union[None, Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.return_code, Unset):
            return_code = self.return_code.to_dict() if self.return_code else None

        processed_at: Union[Unset, str] = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat() if self.processed_at else None


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "transferID": transfer_id,
            "amount": amount,
            "source": source,
            "destination": destination,
            "description": description,
            "status": status,
            "sameDay": same_day,
            "created": created,
            "traceNumbers": trace_numbers,
        })
        if return_code is not UNSET:
            field_dict["returnCode"] = return_code
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Transfer":
        d = src_dict.copy()
        transfer_id = d.pop("transferID")

        amount = Amount.from_dict(d.pop("amount"))


        source = Source.from_dict(d.pop("source"))


        destination = Destination.from_dict(d.pop("destination"))


        description = d.pop("description")

        status = TransferStatus(d.pop("status"))


        same_day = d.pop("sameDay")

        created = isoparse(d.pop("created"))


        trace_numbers = cast(List[str], d.pop("traceNumbers"))


        return_code = None
        _return_code = d.pop("returnCode", UNSET)
        if _return_code is not None and not isinstance(_return_code,  Unset):
            return_code = ReturnCode.from_dict(cast(Dict[str, Any], _return_code))


        processed_at = None
        _processed_at = d.pop("processedAt", UNSET)
        if _processed_at is not None:
            processed_at = isoparse(cast(str, _processed_at))


        transfer = Transfer(
            transfer_id=transfer_id,
            amount=amount,
            source=source,
            destination=destination,
            description=description,
            status=status,
            same_day=same_day,
            created=created,
            trace_numbers=trace_numbers,
            return_code=return_code,
            processed_at=processed_at,
        )

        transfer.additional_properties = d
        return transfer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
