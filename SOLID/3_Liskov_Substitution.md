Subtypes must be substitutable for their base types without altering the correctness of the program.

Subclass should not change the expected behaviour of parent class

This means that if **class B** is a subclass of **class A**, then objects of **type A** should be replaceable with objects of **type B** without breaking the functionality.

this principle is about making your subclasses behave like their base classes without breaking anyone’s expectations when they call the same methods.

### Violating Liskov Substitution Principle (Bad Design)
Some birds can fly, but some cannot (e.g., penguins).

```
class Bird:
    def fly(self):
        return "I can fly!"
    
class Sparrow(Bird):
    pass  # Sparrow can fly, so it works fine.

class Penguin(Bird):
    def fly(self):  
        raise Exception("I cannot fly!")  # Violating Liskov Substitution Principle

# Test
def make_bird_fly(bird: Bird):
    print(bird.fly())

sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  #  Works fine → Output: "I can fly!"
make_bird_fly(penguin)  #  Breaks → Raises Exception: "I cannot fly!"

```

### Problems with this Approach:
1. Penguin is not a proper substitute for Bird since it throws an exception.
2. Clients using Bird expect all birds to fly, but that assumption is incorrect.
3. Breaks LSP: If a subclass changes expected behavior (like fly() raising an exception), it’s violating LSP.

### Good Design
To fix this, we should separate the behavior of flying birds from non-flying birds.

```
from abc import ABC, abstractmethod

# Base class for all birds
class Bird(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # All birds make sound

# Separate class for flying birds
class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"

# Separate class for non-flying birds
class NonFlyingBird(Bird):
    def walk(self):
        return "I can walk!"

# Implement specific birds
class Sparrow(FlyingBird):
    def make_sound(self):
        return "Chirp chirp!"

class Penguin(NonFlyingBird):
    def make_sound(self):
        return "Honk honk!"

# Test
sparrow = Sparrow()
penguin = Penguin()

print(sparrow.fly())   #  Works fine → "I can fly!"
print(penguin.walk())  #  Works fine → "I can walk!"
```

### Benefits of Following LSP
1. **Proper Inheritance**: Penguin no longer has a fly() method, so it doesn't violate expectations.
2. **No Unexpected Behavior**: make_bird_fly() will not break since we don't expect all birds to fly.
3. **Better Code Maintainability**: We can extend new types of birds (e.g., Ostrich, Parrot) without modifying the base class.

### Key Takeaways
1. Subtypes should behave as their base types without breaking assumptions.
2. Avoid forcing subclasses to implement irrelevant methods (like fly() for a Penguin).
3. Use abstraction and separate behaviors when needed.