from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from ..models.destination import Destination
from typing import Dict
from typing import cast



@attr.s(auto_attribs=True)
class CreateMicroDeposits:
    """  """
    destination: Destination
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        destination = self.destination.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "destination": destination,
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "CreateMicroDeposits":
        d = src_dict.copy()
        destination = Destination.from_dict(d.pop("destination"))


        create_micro_deposits = CreateMicroDeposits(
            destination=destination,
        )

        create_micro_deposits.additional_properties = d
        return create_micro_deposits

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
