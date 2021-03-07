from decimal import Decimal


def currency(amount: str) -> Decimal:
    if not amount:
        return Decimal("0.00")

    return Decimal(amount).quantize(Decimal(".01"))
