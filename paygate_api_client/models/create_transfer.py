from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from typing import cast
from ..models.destination import Destination
from typing import Union
from ..models.amount import Amount
from ..types import UNSET, Unset
from ..models.source import Source



@attr.s(auto_attribs=True)
class CreateTransfer:
    """ These fields are used to initiate a Transfer between two Customer objects and their Accounts.
 """
    amount: Amount
    source: Source
    destination: Destination
    description: str
    same_day: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount.to_dict()

        source = self.source.to_dict()

        destination = self.destination.to_dict()

        description =  self.description
        same_day =  self.same_day

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "amount": amount,
            "source": source,
            "destination": destination,
            "description": description,
        })
        if same_day is not UNSET:
            field_dict["sameDay"] = same_day

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CreateTransfer":
        d = src_dict.copy()
        amount = Amount.from_dict(d.pop("amount"))


        source = Source.from_dict(d.pop("source"))


        destination = Destination.from_dict(d.pop("destination"))


        description = d.pop("description")

        same_day = d.pop("sameDay", UNSET)

        create_transfer = CreateTransfer(
            amount=amount,
            source=source,
            destination=destination,
            description=description,
            same_day=same_day,
        )

        create_transfer.additional_properties = d
        return create_transfer

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
