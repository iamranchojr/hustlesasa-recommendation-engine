from .base_model import BaseModel


class OrderItem(BaseModel):
    product_id: int
    quantity: int
    order_id: int
    price: float

    @property
    def total_cost(self) -> float:
        return self.price * self.quantity


class Order(BaseModel):
    user_id: int
    items: list[OrderItem]

    @property
    def total_cost(self) -> float:
        total = 0
        for item in self.items:
            total += item.total_cost

        return total
