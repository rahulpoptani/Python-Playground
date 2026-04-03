# Building Notification System

## Identify Roles (not classes)
1. Alert - what happened
2. Subscriber - who wants to know
3. Notification Channel - how to notify
4. Dispatcher - orchestrating sending
5. Subscription Manager - who is subscribed to what

## Step 1: Define the core abstraction
### Notification Channel
```
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass
```
**Framework Rule**: Core code depends, ONLY on this abstraction

## Step 2: Concrete Implementation (plugins, not core)
```
class EmailChannel(NotificationChannel):
    def send(self, recipient, message):
        print(f"[EMAIL] {recipient}: {message}")
```
```
class SlackChannel(NotificationChannel):
    def send(self, recipient, message):
        print(f"[SLACK] {recipient}: {message}")

```
**Note**: No Core logic changed. This is Open/Close Principle

## Step 3: Introduce Dispatcher
### Framework Orchestration Flow
```
class AlertDispatcher:
    def __init__(self, channels):
        self.channels = channels  # dict[str, NotificationChannel]

    def dispatch(self, subscribers, message):
        for sub in subscribers:
            channel = self.channels[sub.channel]
            channel.send(sub.user, message)
```
**Note**: Dispatcher doesn't know about Slack, it only knows the Contract. That's **Dependency Inversion Principle**

## Step 4: Subscription Model (framework core)
```
class Subscription:
    def __init__(self, user, channel):
        self.user = user
        self.channel = channel
```
```
class SubscriptionManager:
    def __init__(self):
        self._subscriptions = []

    def subscribe(self, subscription):
        self._subscriptions.append(subscription)

    def get_subscribers(self):
        return self._subscriptions
```

## Step 5: Registry Pattern
