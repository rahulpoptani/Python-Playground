High-level modules should not depend on low-level modules. Both should depend on abstractions

Abstractions should not depend on details. Details should depend on abstractions

### What Does This Mean?
1. High-level modules (business logic) should not directly depend on low-level modules (implementation details).
2. Both should depend on abstractions (interfaces or abstract classes).
3. This makes the system loosely coupled and easier to maintain.

### Violating Dependency Inversion Principle (Bad Design)
Let's say we have a EmailService that sends emails, and a Notification class that depends on it.

```
class EmailService:
    def send_email(self, message):
        return f"Sending email: {message}"

# High-level module directly depends on low-level module
class Notification:
    def __init__(self):
        self.email_service = EmailService()            # X. Direct dependency

    def send_notification(self, message):
        return self.email_service.send_email(message)  # X. Hardcoded dependency

# Test
notifier = Notification()
print(notifier.send_notification("Hello, User!"))
```

### Problems with this Approach
1. **Tightly Coupled**: Notification is tightly coupled with EmailService. If we change EmailService or add SMSService, we need to modify Notification.
2. **Not Flexible**: If we want to switch from email to SMS or push notifications, we have to modify the Notification class.
3. **Violates DIP**: The high-level Notification module depends directly on a low-level module (EmailService), instead of an abstraction.

### Good Design
To fix this, we introduce an abstraction (MessageService), and both Notification and EmailService depend on it.

```
from abc import ABC, abstractmethod

# Step 1: Create an abstract class for Message Service
class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Step 2: Implement EmailService based on the abstraction
class EmailService(MessageService):
    def send(self, message):
        return f"Sending email: {message}"

# Step 3: Implement SMSService as another option
class SMSService(MessageService):
    def send(self, message):
        return f"Sending SMS: {message}"

# Step 4: Notification class now depends on abstraction, not a concrete implementation
class Notification:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service      # No direct dependency on EmailService

    def send_notification(self, message):
        return self.message_service.send(message)  # Works with any MessageService

# Step 5: Use different services without modifying Notification class
email_notifier = Notification(EmailService())
sms_notifier = Notification(SMSService())

print(email_notifier.send_notification("Hello via Email!"))  # Works with email
print(sms_notifier.send_notification("Hello via SMS!"))      # Works with SMS
```

### Benefits of Following DIP
1. Loosely Coupled Code: Notification doesn’t directly depend on EmailService or SMSService.
2. Easily Extensible: We can add PushNotificationService without modifying Notification.
3. Improved Maintainability: We can change the implementation details (e.g., switch email providers) without breaking high-level logic.

### Key Takeaways
1. High-level modules should depend on abstractions, not concrete implementations.
2. Interfaces or abstract classes should be used to define dependencies.
3. Improves flexibility, maintainability, and scalability.