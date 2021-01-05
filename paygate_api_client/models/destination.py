from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset




@attr.s(auto_attribs=True)
class Destination:
    """ Customer that is receiving a Transfer """
    customer_id: str
    account_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        customer_id =  self.customer_id
        account_id =  self.account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "customerID": customer_id,
            "accountID": account_id,
        })

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "Destination":
        d = src_dict.copy()
        customer_id = d.pop("customerID")

        account_id = d.pop("accountID")

        destination = Destination(
            customer_id=customer_id,
            account_id=account_id,
        )

        destination.additional_properties = d
        return destination

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
