A client should not be forced to depend on interfaces it does not use

### What Does This Mean?
1. A class should not implement methods it doesn’t need.w
2. Instead of one large interface, break it into multiple smaller interfaces.
3. This ensures better maintainability and flexibility.

### Violating Interface Segregation Principle (Bad Design)
Let's say we have a Worker interface with methods for different types of employees.

```
from abc import ABC, abstractmethod

# This interface forces all subclasses to implement all methods.
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

# A full-time employee needs all methods.
class FullTimeEmployee(Worker):
    def work(self):
        return "Working full-time!"

    def eat(self):
        return "Eating lunch break!"

    def sleep(self):
        return "Sleeping at night!"

# A robot only works, but it is forced to implement eat() and sleep()
class Robot(Worker):
    def work(self):
        return "Working 24/7!"

    def eat(self):
        raise Exception("I don't eat!")    # Violates ISP

    def sleep(self):
        raise Exception("I don't sleep!")  # Violates ISP

# Test
robot = Robot()
print(robot.work())  # Works
print(robot.eat())   # Throws Exception: "I don't eat!"

```

### Problems with this Approach
1. Robot is forced to implement methods (eat(), sleep()) it doesn't need.
2. Breaks ISP because classes should not depend on unnecessary methods.
3. Every new subclass must implement all methods, even if irrelevant.

### Good Design
We break the Worker interface into smaller, more specific interfaces.

```
# Separate interfaces for different behaviors
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

# A full-time employee needs all interfaces.
class FullTimeEmployee(Workable, Eatable, Sleepable):
    def work(self):
        return "Working full-time!"

    def eat(self):
        return "Eating lunch break!"

    def sleep(self):
        return "Sleeping at night!"

# A robot only needs the Workable interface.
class Robot(Workable):
    def work(self):
        return "Working 24/7!"  # No unnecessary methods

# Test
robot = Robot()
print(robot.work())  # Works fine, no unnecessary methods!
```

### Benefits of Following ISP
1. Avoids forcing classes to implement unnecessary methods.
2. Improves maintainability and flexibility.
3. Makes the code more modular and easier to extend.

### Key Takeaways
1. Split large interfaces into smaller, specific interfaces.
2. A class should only implement the interfaces it actually needs.
3. Prevents unnecessary dependencies, making the code more scalable.