# Designing an Service

## How an application evolve to a framework
```
Level 0: Script / Toy class
Level 1: MVP class (works, ugly, coupled)
Level 2: SOLID refactor (roles emerge)
Level 3: Extensible framework core
Level 4: Plugins, lifecycle, contracts
Level 5: Production-grade concerns
```

## Important Question to answer:
1. What stays stable, and what changes over time?

Example: Alerting System

**Changes Frequently**
1. Notification Channels (Slack, PagerDuty, etc)
2. Message Format
3. Delivery Rules

**Stays Stable**
1. Alert Lifecycle
2. Subscription Logic
3. Dispatch Flow

**Framework Core** -> Stable
**Channels** -> Extensions


## What are the Red flags in Level 1 (MVP)?
1. One class does too much
2. Behavior is hard-coded
3. No clear abstraction boundaries
4. Impossible to extend without editing existing code

This violates:
1. SRP (Single Responsibility)
2. OCP (Open/Closed)

## Level 1 -> Level 2
### Introduce Abstraction (SOLID)
1. Create Interfaces
2. Create concrete Implementations

Note: Frameworks depends on **abstractions**, applications depends on **implementations**

## Level 2 -> Level 3
Framework Core Pattern
```
core/
  ├── interfaces.py
  ├── base.py
  ├── registry.py
  ├── exceptions.py
plugins/
  ├── file.py
  ├── s3.py
```

## Level 3 -> Level 4
1. Inversion of control: Framework calls user code, not the other way around.
2. Lifecycle Hooks
3. Configuration Driven Behaviour
4. Plugin auto-discovery
5. Backward Compatibility

## Level 4 -> Level 5
1. Observability (logs, metrics, tracing) 
2. Clear failure modes
3. Explicit contracts

