# BANIKOS - 10/10 Operational OS Blueprint

## Executive Summary

BanikOS হবে একটি local-first, AI-assisted, audit-controlled business operating system। এটি retail POS, online order, courier, wholesale, reseller, inventory, warehouse, finance, CRM, marketing, staff control, task management, analytics এবং AI assistant-কে এক unified operational backbone-এ আনবে।

এই version-এর লক্ষ্য:

- business rule ambiguity কমানো
- developer handoff-ready specification তৈরি করা
- MVP scope বাস্তবসম্মত করা
- Bangladesh commerce operation support করা
- AI-কে controlled assistant হিসেবে রাখা
- finance truth, audit, approval এবং permission-কে system core করা

Final philosophy:

> Operational simplicity with enterprise intelligence.

Golden rule:

> Clean data first. Rules before AI. Delivered equals actual sale. Every important action is auditable.

---

# 1. Non-Negotiable Business Rules

## 1.1 Revenue Truth

Order placed, paid, packed, dispatched বা courier handover হলেই sale complete হবে না।

Actual sale/conversion হবে শুধু:

```text
Order Status = Delivered
Return Window Rule = passed or accepted policy state
Finance Entry = posted to ledger
```

Reports, ROAS, staff commission, reseller commission, profit, inventory valuation এবং revenue dashboard এই rule enforce করবে।

## 1.2 POS Truth

POS শুধু offline counter sale।

যদি POS customer courier delivery চায়:

```text
POS Draft
-> Courier Required
-> Convert to Online/Courier Order
-> Risk Check
-> Stock Reserve
-> Packing
-> Courier Booking
-> Dispatch
-> Delivered
-> Revenue Recognized
```

Pure POS sale কখনো courier pipeline skip করবে না।

## 1.3 Ledger Truth

Finance dashboard total নয়, ledger-based হবে।

প্রতিটি financial impact ডাবল-entry বা ledger-mapped transaction হিসেবে থাকবে:

- cash sale
- bank/mobile payment
- courier COD receivable
- courier settlement
- customer due
- wholesale receivable
- vendor payable
- refund
- return loss
- discount
- commission
- expense
- inventory adjustment impact

## 1.4 Audit Truth

Every important action must create an audit log:

- who
- active role
- branch/location
- before state
- after state
- reason
- approval reference
- source device/session
- timestamp

Audit log append-only হবে। Delete নয়, correction entry হবে।

## 1.5 Permission Truth

একজন staff একাধিক role পেতে পারে, কিন্তু প্রতিটি action active role দিয়ে execute হবে।

Example:

```text
User: Rahim
Roles: POS Staff, Inventory Staff
Active Role: POS Staff
Action: Stock adjustment
Result: Denied or approval required
```

## 1.6 AI Truth

AI suggest, summarize, draft, classify, detect risk এবং assist করতে পারবে।

AI কখনো পারবে না:

- permission bypass
- approval bypass
- direct ledger posting
- direct refund
- direct stock adjustment
- sensitive data expose
- destructive action
- unrestricted database query

AI output must be logged when it affects business decisions.

---

# 2. Final Modular Architecture

## 2.1 Module List

1. Commerce Core
2. POS Core
3. Order & Courier Core
4. Inventory & Warehouse Core
5. Purchase & Vendor Core
6. Finance & Accounting Core
7. Customer/CRM Core
8. Wholesale & Reseller Core
9. Marketing & Omnichannel Core
10. Task, SOP & Learning Core
11. Governance, Security & Audit Core
12. Analytics & BI Core
13. AI Intelligence Layer
14. Public Website/Storefront Sync Layer

## 2.2 Architecture Layers

```text
Experience Layer
  Web Dashboard
  POS Screen
  Warehouse Mobile/PWA
  Delivery/Courier Workspace
  Executive Command Center
  ChatOps/Inbox

Application Layer
  Use Cases
  Business Rules
  Workflow Engines
  Approval Engine
  Permission Engine

Domain Layer
  Orders
  Inventory
  Ledger
  Customer
  Staff
  Audit
  Events

Infrastructure Layer
  PostgreSQL
  Redis
  Queue
  Object Storage
  Search
  Notification Providers
  Courier/Payment APIs

AI Layer
  Read-only context
  Tool policy
  Approval gates
  Prompt logs
  Human review
```

---

# 3. MVP Boundary

## 3.1 Phase 1.0 - Must Build First

Phase 1.0 only builds the operational spine:

- login, user, role, permission
- product, SKU, barcode
- inventory location and stock movement
- POS offline counter sale
- online/courier order workflow
- packing and dispatch workflow
- delivery status and return flow
- finance ledger foundation
- courier COD receivable and settlement
- audit log
- approval queue
- basic reports

## 3.2 Phase 1.1 - Stabilization

- purchase and vendor payable
- customer profile and timeline
- wholesale due ledger
- daily closing
- stock count
- exception dashboard
- basic notification
- dashboard polishing

## 3.3 Phase 2 - Growth

- CRM/telesales workspace
- marketing campaign approval
- reseller portal
- advanced BI
- public website sync
- multi-branch support

## 3.4 Phase 3 - AI Assistance

- order risk assistant
- finance anomaly assistant
- stock forecast assistant
- customer reply draft
- executive summary
- SOP assistant

## 3.5 Phase 4 - Enterprise

- API marketplace
- advanced automation
- workflow builder
- franchise/multi-company support
- predictive operations

---

# 4. Core State Machines

## 4.1 Order State

```text
draft
-> placed
-> confirmed
-> stock_reserved
-> packed
-> dispatched
-> delivered
-> completed
```

Exception states:

```text
cancelled
hold
failed_delivery
partial_delivered
returned
lost
damaged
refunded
```

Rules:

- revenue recognized only at delivered/completed
- stock deducted/reserved according to inventory policy
- cancelled before dispatch releases stock
- return creates reverse logistics and finance adjustment
- lost/damaged requires approval and courier claim

## 4.2 Payment State

```text
unpaid
partial_paid
paid
cod_pending
cod_collected_by_courier
cod_settled
refunded
written_off
```

Rules:

- paid does not equal delivered
- COD is receivable until courier settlement
- refund requires linked original transaction
- write-off requires approval

## 4.3 Fulfillment State

```text
not_started
pick_pending
picked
packed
handover_ready
handover_done
in_transit
delivered
exception
returned_to_origin
```

## 4.4 Inventory Movement Types

```text
purchase_receive
sale_reserve
sale_release
sale_deduct
return_receive
damage_writeoff
stock_transfer_out
stock_transfer_in
stock_adjustment
stock_count_correction
sample_or_gift
```

Rules:

- every movement links to a source document
- manual adjustment requires reason and approval
- negative stock disabled by default
- physical count correction creates audit and variance report

---

# 5. Permission And Approval Matrix

## 5.1 Permission Model

Permissions must be action-based:

```text
module.resource.action.scope
```

Examples:

```text
orders.order.create.own
orders.order.cancel.branch
inventory.stock.adjust.branch
finance.ledger.post.company
marketing.campaign.approve.company
ai.suggestion.execute.none
```

## 5.2 Approval Required Actions

Always approval required:

- discount above threshold
- manual stock adjustment
- refund
- COD write-off
- courier lost claim close
- vendor payment above limit
- expense above limit
- customer due write-off
- wholesale credit limit override
- marketing bulk campaign send
- AI-generated bulk action
- permission change
- audit-sensitive configuration change

## 5.3 Role Groups

```text
Owner/Admin
COO/Operations Manager
CFO/Finance Manager
POS Staff
Order Manager
Courier Coordinator
Warehouse Staff
Purchase Manager
CRM/Telesales Staff
Marketing Staff
Wholesale Manager
Reseller Manager
Delivery Staff
AI Supervisor
Auditor
```

## 5.4 Active Role Rule

Every session has:

```text
user_id
active_role_id
branch_id
device_id
permission_scope
```

Audit logs must store active_role_id, not only user_id.

---

# 6. Data Model Blueprint

## 6.1 Identity And Governance

Core tables:

```text
users
roles
permissions
role_permissions
user_roles
sessions
approval_requests
approval_steps
audit_logs
system_settings
```

## 6.2 Commerce

```text
customers
customer_addresses
products
product_variants
skus
price_lists
orders
order_items
order_status_history
payments
refunds
delivery_jobs
courier_bookings
courier_events
returns
return_items
```

## 6.3 Inventory

```text
warehouses
stock_locations
inventory_balances
inventory_movements
stock_reservations
stock_counts
stock_count_lines
transfers
transfer_items
damage_reports
```

## 6.4 Finance

```text
chart_of_accounts
ledger_entries
ledger_lines
cash_sessions
bank_accounts
mobile_wallet_accounts
customer_ledgers
vendor_ledgers
courier_ledgers
expense_categories
expenses
settlements
settlement_lines
commissions
```

## 6.5 CRM, Marketing, Task

```text
customer_timeline_events
leads
lead_activities
segments
campaigns
campaign_approvals
inbox_threads
inbox_messages
tasks
task_comments
sop_documents
training_progress
```

## 6.6 AI

```text
ai_requests
ai_responses
ai_tool_calls
ai_policy_decisions
ai_human_reviews
ai_knowledge_items
ai_knowledge_approvals
```

## 6.7 Required Common Columns

Business tables should include:

```text
id
company_id
branch_id
created_at
created_by
updated_at
updated_by
deleted_at
version
status
metadata_json
```

Critical tables must also include:

```text
approved_by
approved_at
audit_ref
source_type
source_id
```

---

# 7. API Contract Blueprint

## 7.1 API Grouping

```text
/auth
/users
/roles
/permissions
/products
/inventory
/pos
/orders
/courier
/returns
/finance
/customers
/crm
/marketing
/tasks
/approvals
/audit
/reports
/ai
/sync
```

## 7.2 API Rules

- all write APIs check permission
- sensitive APIs create approval request or require approval token
- all important writes create audit log
- all state changes go through state machine service
- API response includes clear business error codes
- no direct table mutation from UI
- idempotency key required for payments, ledger, order creation, courier booking

## 7.3 Example Business Error Codes

```text
ORDER_INVALID_STATE_TRANSITION
ORDER_DELIVERY_REQUIRED_CONVERT_TO_COURIER
FINANCE_LEDGER_POSTING_REQUIRED
INVENTORY_STOCK_NOT_AVAILABLE
INVENTORY_ADJUSTMENT_APPROVAL_REQUIRED
PERMISSION_DENIED_ACTIVE_ROLE
APPROVAL_REQUIRED
AI_TOOL_NOT_ALLOWED
COURIER_COD_NOT_SETTLED
RETURN_POLICY_BLOCKED
```

---

# 8. Event Model

## 8.1 Important Events

```text
order.placed
order.confirmed
order.stock_reserved
order.packed
order.dispatched
order.delivered
order.returned
payment.received
payment.refunded
inventory.movement_created
stock.adjustment_requested
stock.adjustment_approved
ledger.entry_posted
courier.booking_created
courier.cod_collected
courier.cod_settled
approval.requested
approval.approved
approval.rejected
ai.suggestion_created
ai.action_reviewed
audit.log_created
```

## 8.2 Event Rules

- events are append-only
- events carry actor, active role, source, timestamp
- events can trigger notifications, reports, projections and AI summaries
- failed event processing goes to retry queue
- finance events must be idempotent

---

# 9. Bangladesh-Specific Operations

## 9.1 Courier And COD

Must support:

- Pathao/Steadfast/RedX/Paperfly/manual courier
- COD receivable
- partial settlement
- courier charge
- return charge
- lost parcel claim
- tracking code matching
- settlement sheet import
- courier-wise aging report

Rules:

- courier payout must match tracking code
- COD collected by courier is not cash received until settled
- lost parcel close requires claim status and approval

## 9.2 Payments

Must support:

- cash
- bKash
- Nagad
- Rocket
- bank transfer
- card/POS machine
- COD
- partial payment
- advance payment

Rules:

- payment source required
- transaction reference required for mobile/bank
- duplicate reference blocked or flagged
- refund must link to original payment

## 9.3 Return And Fraud Controls

Must detect:

- repeat return customer
- fake address
- high COD refusal
- courier mismatch
- staff discount abuse
- unusual stock adjustment
- finance settlement gap

Risk score should assist, not auto-block unless configured.

---

# 10. Dashboard And UX Mapping

## 10.1 Global UX Rules

- sidebar-first navigation
- role-specific workspace
- right rail for approval/risk/audit
- dense table-friendly UI
- mobile-first for warehouse/delivery
- no overloaded dashboard for junior staff
- executive gets summary, staff gets actions

## 10.2 Core Screens

Admin:

- user/role/permission
- approval rules
- audit stream
- system settings

Operations:

- order board
- courier board
- exception board
- packing queue
- daily operation summary

Inventory:

- stock dashboard
- stock movement
- stock count
- transfer
- damage/write-off

Finance:

- ledger
- cash closing
- courier COD clearing
- expense
- receivable/payable
- profit report

CRM:

- customer timeline
- telesales queue
- lead board
- inbox

AI:

- AI suggestions
- AI review queue
- tool permission policy
- knowledge approvals

---

# 11. Finance Design

## 11.1 Chart Of Accounts Starter

```text
Assets
  Cash
  Bank
  Mobile Wallet
  Courier COD Receivable
  Customer Receivable
  Inventory Asset

Liabilities
  Vendor Payable
  Customer Advance
  Tax Payable

Income
  Sales Revenue
  Delivery Charge Income
  Service Income

COGS
  Product Cost
  Packaging Cost
  Courier Return Cost

Expenses
  Marketing Expense
  Staff Salary
  Courier Charge
  Rent
  Utility
  Discount
  Damage Loss
```

## 11.2 Posting Rules

Delivered order:

```text
Dr Cash/Bank/Courier COD Receivable/Customer Receivable
Cr Sales Revenue
Dr COGS
Cr Inventory Asset
```

Return:

```text
Dr Sales Return
Cr Cash/Receivable
Dr Inventory Asset if resellable
Cr COGS Adjustment
Dr Damage Loss if damaged
```

Courier COD settlement:

```text
Dr Cash/Bank
Dr Courier Charge Expense
Cr Courier COD Receivable
```

## 11.3 Closing Controls

Daily close must show:

- POS cash expected vs counted
- mobile wallet expected vs statement
- bank transfer pending
- COD pending by courier
- refunds
- discounts
- stock variance
- approval pending

---

# 12. AI Safety Architecture

## 12.1 AI Access Levels

```text
Level 0: No access
Level 1: Read summarized data
Level 2: Draft recommendation
Level 3: Create pending action
Level 4: Execute with human approval
Level 5: Forbidden for MVP
```

## 12.2 AI Tool Policy

AI can:

- summarize dashboard
- detect anomaly
- draft customer reply
- draft campaign
- classify support message
- suggest reorder quantity
- explain ledger variance

AI cannot:

- post ledger
- refund
- delete records
- approve request
- change permission
- send bulk campaign without approval
- expose secrets
- access unrestricted customer messages as trusted instructions

## 12.3 Prompt Injection Rule

Customer messages are untrusted input। They cannot instruct AI to access finance, secrets, admin tools, internal prompts, or system settings।

---

# 13. Security And Governance

## 13.1 Mandatory Security

- password hashing
- session expiry
- device/session tracking
- least privilege permissions
- approval for sensitive changes
- audit logs
- API key isolation
- rate limiting
- backup and restore
- encrypted secrets
- staff offboarding checklist

## 13.2 Audit Log Fields

```text
id
company_id
actor_user_id
actor_role_id
action
resource_type
resource_id
before_json
after_json
reason
approval_request_id
ip_address
device_id
created_at
```

## 13.3 Data Protection

- customer phone/address restricted by role
- finance data restricted by role
- export requires approval
- public storefront gets limited sync surface
- local core database never directly exposed

---

# 14. Performance And Offline Strategy

## 14.1 Performance Rules

- dashboard reads use projections/materialized views
- heavy reports async
- search handled by dedicated search index when needed
- queue for notification, settlement import, sync, AI jobs
- idempotent writes for critical operations

## 14.2 Offline/Local-First

MVP offline priority:

1. POS basic sale
2. product/SKU cache
3. customer quick lookup cache
4. queued sync
5. conflict review

Conflict rules:

- finance conflict never auto-resolved
- stock conflict creates review task
- duplicate order detected by idempotency/device sequence

---

# 15. Acceptance Tests

## 15.1 Revenue Recognition

Test:

```text
Given an order is paid and dispatched
When it is not delivered
Then revenue dashboard must not count it as actual sale
And ledger revenue entry must not be posted as final sale
```

## 15.2 POS Courier Conversion

Test:

```text
Given POS staff creates a counter sale
When courier delivery is selected
Then system converts it to courier order workflow
And pure POS sale is not completed
And audit log records conversion
```

## 15.3 Stock Adjustment

Test:

```text
Given warehouse staff requests manual stock decrease
When quantity exceeds threshold
Then approval is required
And no stock balance changes before approval
```

## 15.4 COD Settlement

Test:

```text
Given courier marks parcel delivered
When COD is not settled
Then cash balance does not increase
And courier COD receivable remains open
```

## 15.5 AI Permission

Test:

```text
Given AI drafts a refund recommendation
When user asks AI to execute refund
Then AI creates approval request only
And refund is not posted without authorized human approval
```

## 15.6 Active Role

Test:

```text
Given user has POS and Inventory roles
When active role is POS
And user attempts stock adjustment
Then system denies or requests role switch plus permission check
And audit log records active role
```

---

# 16. Definition Of Done

## 16.1 Feature Done

A feature is done only when:

- business rule documented
- permission checked
- audit log created where needed
- approval flow added where needed
- API contract stable
- UI empty/loading/error states exist
- test cases pass
- reporting impact considered
- finance impact considered
- rollback/correction path exists

## 16.2 MVP Done

MVP is done when:

- staff can sell, pack, dispatch, deliver and return orders
- stock is trustworthy
- finance can reconcile cash, mobile payment and COD
- owner can see real sales, pending COD, inventory risk and exceptions
- sensitive actions require approval
- audit trail explains what happened
- system is usable by non-technical staff

---

# 17. Implementation Roadmap

## 17.1 Sprint Group 1 - Foundation

- auth
- company/branch
- user/role/permission
- audit log
- approval engine
- product/SKU

## 17.2 Sprint Group 2 - Sales And Inventory

- POS
- online/courier order
- stock reservation
- inventory movement
- packing queue
- dispatch

## 17.3 Sprint Group 3 - Finance Truth

- chart of accounts
- ledger posting
- payment
- refund
- COD receivable
- courier settlement
- daily closing

## 17.4 Sprint Group 4 - Exceptions And Reports

- return
- failed delivery
- lost/damaged
- stock count
- exception board
- owner dashboard

## 17.5 Sprint Group 5 - CRM And Growth

- customer timeline
- telesales
- inbox
- campaign approval
- reseller/wholesale

## 17.6 Sprint Group 6 - AI Assistance

- AI read-only summary
- anomaly detection
- reply draft
- risk suggestion
- AI audit/review

---

# 18. Final 10/10 Checklist

## Product

- clear MVP boundary
- no overbuild
- role-specific UX
- Bangladesh-ready workflow
- exception-tolerant operations

## Engineering

- modular architecture
- explicit state machines
- event-driven side effects
- idempotent critical writes
- schema blueprint
- API grouping

## Finance

- delivered equals sale
- ledger-based truth
- COD clearing
- daily close
- audit-ready reports

## Governance

- active role permission
- approval engine
- append-only audit
- sensitive data protection
- AI safety gates

## QA

- acceptance tests
- business rule tests
- permission tests
- finance tests
- exception tests

---

# 19. Final Verdict

This is now a 10/10 blueprint if used as the control document for execution.

The most important discipline:

> Build the operational spine first. Stabilize it. Then expand.

BanikOS should not become a feature pile। It should become the trusted operating backbone of the business।

