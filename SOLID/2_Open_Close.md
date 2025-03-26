Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

### What Does This Mean?
**Open for Extension**: You should be able to add new functionality to the system without modifying existing code.

**Closed for Modification**: Once a class is implemented and tested, you shouldn’t have to modify it to add new behavior. Instead, you should extend it.

### Why is this Important?
1. Reduces the risk of breaking existing code.
2. Makes code scalable and maintainable.
3. Encourages the use of polymorphism and abstraction.


### Example
Let's say we have a DiscountCalculator class that calculates discounts based on the customer type.
```
class DiscountCalculator:
    def get_discount(self, customer_type, price):
        if customer_type == "regular":
            return price * 0.05  # 5% discount
        elif customer_type == "vip":
            return price * 0.1  # 10% discount
        else:
            return 0  # No discount

```
**Problems**

1. If we add a new customer type ("gold"), we need to modify this class.
2. This violates OCP because the class is not closed for modification.

**We can refactor the code using polymorphism and inheritance, making it extensible.**

```
from abc import ABC, abstractmethod

# Step 1: Create an abstract class for Discount Strategy
class DiscountStrategy(ABC):
    @abstractmethod
    def get_discount(self, price):
        pass

# Step 2: Create concrete discount classes for different customers
class RegularCustomerDiscount(DiscountStrategy):
    def get_discount(self, price):
        return price * 0.05  # 5% discount

class VIPCustomerDiscount(DiscountStrategy):
    def get_discount(self, price):
        return price * 0.1  # 10% discount

# Step 3: Create a class that uses a discount strategy
class DiscountCalculator:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def calculate(self, price):
        return self.discount_strategy.get_discount(price)

# Step 4: Use the DiscountCalculator with different strategies
regular_discount = DiscountCalculator(RegularCustomerDiscount())
vip_discount = DiscountCalculator(VIPCustomerDiscount())

print(regular_discount.calculate(1000))  # Output: 50.0
print(vip_discount.calculate(1000))      # Output: 100.0
```

### Benefits
1. **Closed for modification**: The DiscountCalculator class does not change when a new discount type is added.
2. **Open for extension**: We can introduce a new discount strategy (e.g., GoldCustomerDiscount) without modifying existing code.
3. **Follows the Strategy Pattern**: The discount logic is now encapsulated in separate classes, making it more modular.

### Key Takeaways
1. Avoid modifying existing code when adding new behavior.
2. Use abstraction (via base classes or interfaces).
3. Apply polymorphism to allow new implementations without changing existing logic.
4. Helps in writing scalable, maintainable, and robust code.ss