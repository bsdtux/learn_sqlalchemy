import datetime as dt
import typing as ty
from decimal import Decimal


def currency(amount: str) -> ty.Optional[Decimal]:
    try:
        return Decimal(strip_amount_puncuation(amount)).quantize(Decimal(".01"))
    except ValueError:
        print("Invalid price format. Please use the following format: (9.99)")
        return


def sanitize_date(dt_str: str) -> dt.datetime.date:
    try:
        return dt.datetime.strptime(dt_str, "%B %d, %Y").date()
    except ValueError:
        print("Invalid Dateformat: Please use the following format: (October 25, 2017)")
        return


def strip_amount_puncuation(amount: str) -> str:
    return amount.replace("$", "").replace("₵", "")
