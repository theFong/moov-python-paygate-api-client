from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from dateutil.parser import isoparse
from typing import Union
import datetime
from ..types import UNSET, Unset
from typing import Optional
from typing import cast, List
from typing import cast
from ..models.destination import Destination
from ..models.transfer_status import TransferStatus
from ..models.amount import Amount



@attr.s(auto_attribs=True)
class MicroDeposits:
    """  """
    micro_deposit_id: str
    transfer_i_ds: List[str]
    destination: Destination
    amounts: List[Amount]
    status: TransferStatus
    created: datetime.datetime
    processed_at: Union[Unset, Optional[datetime.datetime]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        micro_deposit_id =  self.micro_deposit_id
        transfer_i_ds = self.transfer_i_ds




        destination = self.destination.to_dict()

        amounts = []
        for amounts_item_data in self.amounts:
            amounts_item = amounts_item_data.to_dict()

            amounts.append(amounts_item)




        status = self.status.value

        created = self.created.isoformat()

        processed_at: Union[Unset, str] = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat() if self.processed_at else None


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "microDepositID": micro_deposit_id,
            "transferIDs": transfer_i_ds,
            "destination": destination,
            "amounts": amounts,
            "status": status,
            "created": created,
        })
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "MicroDeposits":
        d = src_dict.copy()
        micro_deposit_id = d.pop("microDepositID")

        transfer_i_ds = cast(List[str], d.pop("transferIDs"))


        destination = Destination.from_dict(d.pop("destination"))


        amounts = []
        _amounts = d.pop("amounts")
        for amounts_item_data in (_amounts):
            amounts_item = Amount.from_dict(amounts_item_data)

            amounts.append(amounts_item)


        status = TransferStatus(d.pop("status"))


        created = isoparse(d.pop("created"))


        processed_at = None
        _processed_at = d.pop("processedAt", UNSET)
        if _processed_at is not None:
            processed_at = isoparse(cast(str, _processed_at))


        micro_deposits = MicroDeposits(
            micro_deposit_id=micro_deposit_id,
            transfer_i_ds=transfer_i_ds,
            destination=destination,
            amounts=amounts,
            status=status,
            created=created,
            processed_at=processed_at,
        )

        micro_deposits.additional_properties = d
        return micro_deposits

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
