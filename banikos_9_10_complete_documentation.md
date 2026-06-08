# BanikOS 9/10 Complete Documentation

## Document Purpose

এই ডকুমেন্টটি BanikOS-এর final 9/10 product, dashboard, architecture এবং developer handoff documentation। এখানে business rules, modules, dashboards, roles, permissions, routes, audit, state machines, data entities, API grouping, release roadmap এবং critical test cases এক জায়গায় রাখা হয়েছে।

Target:

```text
Vision clarity: 9/10
Business logic: 9/10
Dashboard planning: 9/10
Developer handoff readiness: 9/10
```

---

## 1. Product Vision

BanikOS হবে একটি local-first, AI-assisted, audit-controlled business operating system। এটি retail shop, online order, wholesale, courier, finance, inventory, CRM, marketing, reseller, task management, staff control এবং AI agent-কে একটি trusted backbone থেকে পরিচালনা করবে।

BanikOS শুধু POS না, শুধু ERP না, শুধু CRM না, শুধু chatbot না। এটি হবে ব্যবসার main control backbone, যেখানে প্রতিটি sale, stock movement, payment, return, courier status, staff action, AI suggestion এবং finance impact audit log সহ সংরক্ষিত থাকবে।

### Core Principle

```text
Clean data first
Rules before AI
POS = Offline counter sale only
Courier needed from POS = Convert/forward to Online/Courier Order workflow
Delivered = Actual sale/conversion
Every important action = Audit logged
Local core data = Protected
Hosting platform = Limited sync surface
AI = Assistant, not uncontrolled owner
```

---

## 2. Most Important Business Rules

### 2.1 POS Rule

POS module শুধুমাত্র offline/counter sale-এর জন্য থাকবে।

POS sale-এর সাধারণ flow:

```text
Customer buys at counter
Payment received / due recorded
Invoice printed
Stock deducted
Cash/bank/mobile payment updated
Audit log created
```

### 2.2 POS Sale Courier Rule

যদি POS থেকে কোনো customer order courier-এ পাঠাতে হয়, তাহলে সেটি pure POS sale হিসেবে থাকবে না। সেটি online/courier order workflow-তে convert বা forward হবে।

Flow:

```text
POS counter request
Customer delivery address added
Courier required selected
System converts it to Courier Order / Online Order type
Courier risk check runs
Packing task created
Dispatch/courier booking
Delivered হলে actual sale confirmed
```

### 2.3 Delivered-Only Sale Rule

BanikOS-এ actual sale/conversion হবে শুধু delivered হলে।

```text
Order placed = Order intent
Paid = Payment received
Packed = Operational progress
Dispatched = Courier handover
Delivered = Actual sale/conversion
Cancelled = No sale
Returned = Sale reversal
Partial return = Adjusted sale value
```

এই rule finance, marketing ROAS, staff commission, reseller commission, profit report এবং courier reconciliation-এ enforce করতে হবে।

### 2.4 Finance Truth Rule

Finance dashboard-only হবে না। Finance অবশ্যই ledger-based হবে।

```text
Stock movement
Order status
Payment status
Courier COD
Return/partial return
Vendor payable
Customer receivable
Wholesale receivable
Commission payable
```

সব কিছু ledger এবং audit trail-এর সঙ্গে মিলতে হবে।

### 2.5 AI Control Rule

AI assistant হিসেবে কাজ করবে, uncontrolled decision maker হিসেবে না।

```text
AI can observe.
AI can suggest.
AI can draft.
AI can execute low-risk guarded actions.
AI cannot bypass permission, approval, audit or business rules.
```

---

## 3. User Role & Department Structure

### 3.1 Main Roles

- Owner / CEO
- Admin
- CTO / Technical Admin
- CFO / Finance Manager
- COO / Operations Manager
- CMO / Marketing Manager
- Store Manager
- POS Staff
- Sales/CRM Staff
- Telesales Staff
- Packaging Staff
- Delivery/Courier Staff
- Wholesale Manager
- Reseller Manager
- Support Agent
- AI Supervisor

### 3.2 Multi-Role Staff Rule

BanikOS small business support করবে যেখানে staff সংখ্যা কম। একজন staff একাধিক role পেতে পারে, কিন্তু প্রতিটি action active role অনুযায়ী audit log হবে।

Example:

```text
User: Rahim
Assigned roles: POS Staff, Packaging Staff, Delivery Coordinator
Current active role: POS Staff
Action: Counter sale
Audit role: POS Staff
```

### 3.3 Active Role Switcher

Multi-role staff-এর জন্য frontend-এ active role switcher থাকতে হবে।

Rule:

```text
One person can hold multiple roles.
Every action must be tied to one active role.
Sensitive actions still require approval.
```

### 3.4 Role Combination Presets

#### Small Shop Preset

```text
Owner/Admin = CEO + CFO + COO + CMO
Staff 1 = POS + Inventory + Packaging
Staff 2 = Sales/CRM + Omnichannel + Telesales
Staff 3 = Delivery/Courier + Return Handling
```

#### Medium Business Preset

```text
Owner/Admin = CEO
Manager = COO + Approval Manager
Finance Staff = CFO Assistant
Sales Staff = CRM + Telesales
Store Staff = POS + Inventory
Packing Staff = Packaging only
Delivery Staff = Courier only
Marketing Staff = CMO Assistant
```

#### Enterprise Preset

```text
Separate team for each department:
POS, Inventory, Finance, Courier, CRM, Marketing, Omnichannel, Wholesale, Reseller, AI Supervision
```

---

## 4. Dashboard Architecture

### 4.1 Dashboard Count Decision

Dashboard count নিয়ে confusion এড়াতে তিনটি level রাখা হলো।

```text
Minimum workable role dashboards = 12
Recommended frontend design surfaces = 15
Enterprise frontend surfaces = 19
```

### 4.2 Recommended Full-Cover Architecture

```text
1 Master Admin Control Panel
+ 1 C-Level Executive Dashboard
+ 13 Department/Module Panels
+ Shared Approval Rail
+ Shared Audit Stream
+ Role-Based Navigation
```

### 4.3 Recommended 15 Frontend Surfaces

This 15-surface plan is the Phase-1 full-cover design package. Some surfaces are intentionally merged to reduce first-build complexity.

```text
1. Master Admin Control Panel
2. C-Level Executive Dashboard with CEO/CFO/COO/CMO/CTO tabs
3. POS Panel
4. Order Management Panel
5. Courier Order Panel
6. Inventory Panel
7. Vendor Purchase Panel
8. Wholesale Panel
9. Finance Panel
10. CRM/Sales Panel
11. Telesales Panel
12. Packaging Panel
13. Delivery/Courier Panel
14. Marketing/Omnichannel Panel
15. Task/Reseller/AI Control Panel
```

Important:

```text
Marketing/Omnichannel is merged for Phase-1 only.
Task/Reseller/AI Control is merged for Phase-1 only.
Enterprise version must split them into separate workflow panels.
```

### 4.4 Future 19 Enterprise Surfaces

```text
1. Master Admin Control Panel
2. C-Level Executive Dashboard
3. POS Panel
4. Order Management Panel
5. Courier Order Panel
6. Inventory Panel
7. Vendor Purchase Panel
8. Wholesale Panel
9. Finance/CFO Panel
10. CRM/Sales Panel
11. Telesales Panel
12. Packaging Panel
13. Delivery/Courier Panel
14. COD Risk Panel
15. Marketing/CMO Panel
16. Omnichannel Inbox Panel
17. Task Manager/Internal Inbox Panel
18. Website/Landing Control Panel
19. Reseller + AI Control Panel
```

### 4.5 Route Map

Initial frontend route contract:

```text
/admin
/executive
/pos
/orders
/courier-orders
/inventory
/purchases
/wholesale
/finance
/crm
/telesales
/packaging
/delivery
/marketing-omnichannel
/control-center
```

Future enterprise route split:

```text
/cod-risk
/marketing
/inbox
/task-control
/website
/reseller-control
/ai-control
```

Route naming rule:

```text
/control-center = Phase-1 merged Task/Reseller/AI control surface.
/task-control, /reseller-control, /ai-control = enterprise split routes.
/control must not be used because it is too generic.
```

### 4.6 Shared Application Shell

Every authenticated screen should use the same shell.

```text
Left Sidebar: role-based module navigation
Top Bar: search, active role switcher, sync status, notifications, AI mode, emergency lock
Main Area: current panel
Right Rail: approval queue, risk alerts, AI alerts
Bottom/Side Stream: audit timeline where useful
```

### 4.7 Common Panel Layout

Each panel should follow the same structure:

```text
Page Header
Metric Strip
Main Work Table / Queue / Kanban
Right Context Panel
Approval/Risk Section
Audit Timeline
```

---

## 5. Core Feature Modules

## Core 1: Admin & Governance Core

Purpose: পুরো system control, permission, audit, approval এবং emergency control admin side থেকে পরিচালনা করা।

Features:

- Tenant/business setup
- Business profile setup
- Branch/shop setup
- Warehouse/location setup
- Role-based access control
- Permission templates
- Multi-role staff assignment
- Department-wise dashboard
- Owner emergency override
- Emergency lock mode
- Approval queue
- Handover mode
- System-wide audit log
- Staff action log
- AI action log
- Login/session log
- Backup and restore control
- Local-to-hosting sync control
- Security alert center

9/10 Requirement:

- Every sensitive action must require permission.
- Every important action must create audit log.
- Admin must see who did what, when, from which role, and what changed.

## Core 2: Product, Inventory & Vendor Purchase Core

Purpose: Product, stock, purchase, vendor, cost এবং inventory truth maintain করা।

Features:

- Product master catalog
- SKU/barcode
- Product category
- Product image
- Product description
- Retail price
- Wholesale price
- Manual wholesale price support
- Variant support
- Stock by warehouse/location
- Stock by rack/bin if needed
- Purchase from vendor
- Purchase invoice
- Vendor ledger
- Partial vendor payment
- Vendor due/baki tracking
- Buying cost tracking
- Moving Average Cost / FIFO cost calculation
- Damage/loss/shrinkage tracking
- Stock adjustment with approval
- Stock audit/physical count
- Low stock alert
- Packaging material BOM/cost
- Negative stock prevention

Vendor Purchase Flow:

```text
Vendor selected
Purchase invoice created
Products received into stock
Cost recorded
Vendor payable updated
Payment full/partial/due recorded
Ledger and audit log updated
```

## Core 3: POS / Offline Retail Core

Purpose: দোকানের counter sale বা offline sale পরিচালনা করা। POS হবে offline sale-only module.

Features:

- Fast counter sale
- Barcode scan
- Product search
- Cart
- Discount
- VAT/tax if applicable
- Payment method: cash, bank, bKash, Nagad, card
- Split payment
- Customer optional/required setting
- Walk-in customer mode
- Invoice print
- Thermal printer support
- Return/exchange from POS
- Partial return
- Cash drawer tracking
- EOD cash reconciliation
- Staff-wise sale tracking
- Offline local mode
- POS shift open/close
- Cash shortage/excess log
- Dynamic QR payment for exact amount
- POS-to-courier conversion

9/10 Requirement:

- POS should stay fast and simple.
- POS should not become mixed with online order complexity.
- Courier needed হলে order must move to courier workflow.
- Cash drawer and actual sale must always match.

## Core 4: Online / Manual / Social Order Core

Purpose: Website, Facebook, WhatsApp, phone call, manual admin order সব online/order lifecycle manage করা।

Features:

- Website order
- Facebook order
- WhatsApp order
- Manual order
- Phone order
- Customer profile
- Customer address book
- Payment method
- COD support
- Advance payment support
- Order status lifecycle
- Invoice generation
- Stock reservation
- Order risk check
- Order note
- Source tracking
- CRM link
- Customer timeline

Order Status Flow:

```text
Draft
Placed
Confirmed
Packed
Dispatched
Delivered / Returned / Cancelled
```

## Core 5: Wholesale Commerce Core

Purpose: Wholesale sale, pricing, due, payment, ledger এবং reporting retail থেকে আলাদা রাখা।

Features:

- Wholesale customer profile
- Wholesale customer category
- Manual sell price per order
- Wholesale price list
- Bulk quantity order
- Wholesale invoice
- Partial payment
- Due/baki tracking
- Wholesale receivable ledger
- Wholesale return
- Wholesale profit report
- Separate wholesale dashboard
- Separate wholesale stock impact report

Separation Rule:

```text
Retail report != Wholesale report
Retail customer ledger != Wholesale customer ledger
Retail pricing != Wholesale pricing
Retail profit != Wholesale profit
```

## Core 6: CRM, Sales & Telesales Core

Purpose: Lead, customer follow-up, call, notes, upsell/cross-sell এবং sales team activity manage করা।

Features:

- CRM lead board
- Lead source tracking
- Website leads
- Facebook/WhatsApp leads
- Call log
- IP calling integration
- Follow-up schedule
- Telesales queue
- Sales script
- Objection note
- Customer interest tag
- Upsell/cross-sell suggestion
- Daily sales agent note
- Customer timeline
- Lead-to-order conversion
- Lost lead reason

Learning Data:

- Customer objection
- Successful reply
- Failed reply
- Product demand
- Price sensitivity
- Delivery concern
- Competitor mention
- Campaign/source quality

## Core 7: Packaging, Delivery & Courier Core

Purpose: Packing, dispatch, courier, return, lost parcel, courier reconciliation এবং delivery operation manage করা।

Packaging Features:

- Packaging task queue
- Assigned packing task only
- Pick list
- Product scan/check
- Pack confirmation
- Packaging material usage
- Damage/missing report
- Handover to delivery/courier

Delivery/Courier Features:

- Dispatch queue
- Courier booking
- Tracking code
- Delivery status update
- Return status
- Lost parcel alert
- Courier claim
- Fake return verification
- Courier payment reconciliation
- Courier charge calculation
- COD receivable tracking

Courier Truth:

```text
Dispatched != Delivered
Returned must trigger verification
Delivered triggers actual sale/conversion
Courier payout must match tracking code
```

## Core 8: COD Risk Management Core

Purpose: Fake order, return risk, bad customer, incomplete address এবং COD loss কমানো।

Features:

- Active Transit Protection
- Smart Advance Trigger
- Address Scoring Engine
- Geographical Risk Alerts
- Fake Order Detection
- Blacklist Engine
- Risky phone number detection
- Repeat return customer detection
- Suspicious order hold
- Advance courier charge requirement
- Admin approval for risky orders

9/10 Requirement:

- Risk score should be visible before dispatch.
- High-risk order should not go directly to courier.
- Admin must be able to override with reason.

## Core 9: Finance & CFO Core

Purpose: Business finance, cash, bank, payable, receivable, courier clearing, profit/loss, return loss, commission এবং audit-ready report manage করা।

Features:

- Cash flow
- Profit and loss
- Balance view
- Cash account
- Bank account
- Mobile banking account
- Vendor payable
- Customer receivable
- Wholesale receivable
- Courier receivable/clearing account
- Reseller commission payable
- Staff commission payable
- Expense tracking
- Packaging cost
- Return loss
- Damage loss
- Inventory shrinkage loss
- Tax/VAT-ready report
- Audit-ready transaction trail
- Voucher system
- EOD cash reconciliation
- Cash shortage/excess log
- Fiscal year closing
- Invoice numbering rule

CFO Must See:

- Which sales are delivered
- Which money is collected
- Which courier still holds COD money
- Which vendor is owed money
- Which reseller must be paid
- Which staff earned commission
- Which product is profitable after ad, courier, return and packaging cost

## Core 10: Marketing, CMO & Ads Core

Purpose: Organic marketing, paid ads, content planning, event tracking, ROAS এবং campaign performance manage করা।

Features:

- Content calendar
- Post schedule
- Post edit/delete/reschedule
- AI content generation
- Image/video/audio/script workflow
- Organic campaign planning
- Paid ad tracking
- Meta Ads integration
- Google Ads integration
- GA4/GTM integration
- TikTok Ads integration
- WhatsApp campaign center
- Bulk message approval
- Audience segment suggestion
- Campaign result analysis
- ROAS/CPA/CTR/CPC
- Delivered-sale ROAS
- Landing page performance
- Marketing task board
- Social agent supervision

Event Rule:

```text
PageView = Page viewed
ViewContent = Product viewed
AddToCart = Cart event
InitiateCheckout = Checkout started
OrderPlaced/Lead = Order submitted
Purchase = Delivered only
CancelOrder = Cancelled
ReturnOrder = Returned
PartialReturn = Adjusted value
```

## Core 11: Omnichannel & Customer Message Core

Purpose: Messenger, WhatsApp, Facebook comments, Instagram, website chat সব customer conversation এক inbox-এ manage করা।

Features:

- Channel account management
- Facebook page connection
- WhatsApp Business connection
- Instagram connection
- Website live chat
- Unified inbox
- Facebook comment-to-DM
- WhatsApp Cloud API
- Message routing
- Conversation status
- Conversation assignment
- Staff/team inbox permission
- AI reply suggestion
- AI handover
- Human takeover
- Internal note
- Customer timeline
- Product/order context panel
- Customer sentiment
- Emotion detection
- Spam/abuse filtering
- Prompt-injection sandboxing

Security Rule:

```text
Customer messages are untrusted input.
Customer-facing AI must never get direct access to ERP secrets, finance data, unrestricted database context or powerful tools.
```

## Core 12: Task Assignment & Internal Communication Core

Purpose: Team task, department work, internal instruction, approval, handoff এবং follow-up এক জায়গায় রাখা।

Features:

- Task assignment
- Task manager dashboard
- Department task board
- Staff task queue
- Team-wise internal inbox
- Role/hierarchy-based communication
- Manager-to-team announcement
- Direct staff message
- Threaded task discussion
- Task status: new, assigned, in progress, blocked, review, done
- Priority: normal, urgent, critical
- Due date and SLA
- File/note attachment
- Voice/call note attachment
- Escalation to manager
- Cross-department handoff
- AI task suggestion
- AI task summarization
- Task audit trail

## Core 13: Website, Landing Page & Hosting Core

Purpose: BanikOS data থেকে public website, landing page এবং storefront চালানো, কিন্তু local core database expose না করা।

Features:

- Product publish/unpublish
- Price sync
- Stock sync
- Content CRUD
- Landing page builder
- Niche-based landing templates
- Product-to-landing-page mapping
- Landing page to ad campaign mapping
- Pixel/CAPI configuration
- Website order to OMS
- Public API with scoped key
- Hosting cache
- Secure sync bridge
- Signed event communication
- Sync queue
- Failed sync retry

Local-First Rule:

```text
Local BanikOS Core = Main truth
Hosting Platform = Public website and limited cache
Secure Sync Bridge = Controlled communication
```

## Core 14: Reseller Platform Core

Purpose: Reseller যেন product sell করতে পারে, কিন্তু delivery, stock, commission, payout BanikOS control করবে।

Features:

- Reseller login
- Available product catalog
- Reseller commission display
- Reseller order submission
- Delivery handled by business
- Limited courier tracking access
- Delivered order adds commission
- Failed delivery deducts delivery charge if policy applies
- CFO payout approval
- Reseller ledger
- Reseller payout history

Reseller Flow:

```text
Reseller selects product
Commission shown
Reseller submits order
Business packages and dispatches
Delivered = Commission added
Returned/cancelled = No commission or policy deduction
CFO approves payout
```

## Core 15: AI Agent Core

Purpose: AIকে department-wise assistant হিসেবে ব্যবহার করা, কিন্তু uncontrolled business decision maker বানানো না।

Agents:

- Orchestrator Agent
- Customer/Omnichannel Agent
- Marketing/Ads Agent
- Operations Agent
- Finance Control Agent
- Learning/Knowledge Agent

AI Modes:

```text
Observe = Report only
Approval = Draft/suggestion, admin approves
Handover = Works when staff is absent
Guarded Autopilot = Executes low-risk actions within rules
```

Approval-Required AI Actions:

- Product price change
- Refund
- Order cancel
- Customer blacklist
- Vendor payment
- Reseller payout
- Ad budget increase
- Bulk WhatsApp campaign
- Finance adjustment
- High-value discount

## Core 16: Learning & Knowledge Core

Purpose: Customer chat, staff reply, order result, campaign result থেকে system learning তৈরি করা, কিন্তু approval ছাড়া live behavior change না করা।

Features:

- FAQ knowledge base
- Reply template library
- Staff correction tracking
- Successful reply tracking
- Failed reply tracking
- Customer objection library
- Product demand insight
- Campaign learning
- AI learning suggestion
- Admin approval for knowledge update

Learning Rule:

```text
AI creates learning suggestion
Manager/admin reviews
Approved knowledge updates
Future AI/staff uses it
```

---

## 6. Panel Specifications

### 6.1 Master Admin Control Panel

Primary users: Owner, Admin.

Must include:

- Full business health
- Net profit today/month
- Delivered sales
- Pending orders
- Cash/bank/mobile balance
- Courier COD receivable
- Vendor payable
- Wholesale receivable
- Inventory value
- Low stock
- Pending approvals
- AI alerts
- Courier risks
- Sync health
- Audit stream
- Emergency lock
- Module shortcut cards
- Department status cards

Primary actions:

- Approve/reject sensitive actions
- Jump to any module
- Trigger emergency lock
- Review audit log
- Review sync/API failure

### 6.2 C-Level Executive Dashboard

Tabs:

- CEO Overview
- CFO Finance View
- COO Operations View
- CMO Marketing View
- CTO System View

Rule:

```text
Build one executive dashboard first.
Later each tab can become a separate dashboard if needed.
```

### 6.3 POS Panel

Primary users: POS Staff, Store Manager.

Must support:

- Fast product search/barcode scan
- Cart
- Discount with permission
- Cash/bank/bKash/Nagad/card payment
- Split payment
- Invoice print
- Return/exchange
- Shift open/close
- Cash drawer
- EOD cash reconciliation
- POS-to-courier conversion

### 6.4 Order Management Panel

Primary users: Sales/CRM Staff, Admin, COO.

Must support:

- Website/manual/social/phone order
- Order status lifecycle
- Customer profile and address
- Payment method
- COD/advance payment
- Order source tracking
- CRM link
- Risk score preview

### 6.5 Courier Order Panel

Primary users: Delivery Coordinator, COO, Admin.

Must support:

- POS-to-courier converted orders
- Courier booking
- Tracking code
- COD risk result
- Dispatch status
- Delivery status sync
- Returned/lost parcel handling
- Courier claim
- COD receivable tracking

### 6.6 Inventory Panel

Primary users: Store Manager, Inventory Staff, Admin.

Must support:

- Product catalog
- SKU/barcode
- Variant
- Stock by location
- Stock movement history
- Low stock alert
- Stock audit
- Damage/loss/shrinkage
- Negative stock prevention

### 6.7 Vendor Purchase Panel

Primary users: Purchase Staff, CFO, Admin.

Must support:

- Vendor profile
- Purchase invoice
- Product receive
- Cost entry
- Vendor payable
- Partial payment
- Vendor ledger
- Due alert

### 6.8 Wholesale Panel

Primary users: Wholesale Manager, CFO, Admin.

Must support:

- Wholesale customer
- Manual sell price
- Bulk order
- Wholesale invoice
- Partial payment
- Due/baki
- Wholesale receivable ledger
- Wholesale return
- Wholesale profit report

### 6.9 Finance Panel

Primary users: CFO, Owner, Admin.

Must support:

- Cash account
- Bank account
- Mobile banking account
- Vendor payable
- Customer receivable
- Wholesale receivable
- Courier clearing account
- Staff commission payable
- Reseller commission payable
- Expenses
- Profit/loss
- Voucher
- Audit-ready transaction trail

### 6.10 CRM/Sales Panel

Primary users: Sales Staff, CRM Staff, Sales Manager.

Must support:

- Lead board
- Lead source
- Customer timeline
- Follow-up
- Notes
- Objection reason
- Interest tag
- Upsell/cross-sell suggestion
- Lead-to-order conversion
- Lost lead reason

### 6.11 Telesales Panel

Primary users: Telesales Staff, Sales Manager.

Must support:

- Call queue
- Callback schedule
- Call status
- Call script
- Objection note
- Customer history
- Conversion result
- Daily performance

### 6.12 Packaging Panel

Primary users: Packaging Staff, COO.

Must support:

- Assigned packing task queue
- Pick list
- Product scan/check
- Pack confirmation
- Packaging material usage
- Damage/missing report
- Handover to courier/delivery

### 6.13 Delivery/Courier Panel

Primary users: Delivery Staff, Courier Coordinator, COO.

Must support:

- Dispatch queue
- Courier handover
- Tracking update
- Return update
- Lost parcel alert
- Claim tracking
- Courier payment matching

### 6.14 Marketing/Omnichannel Panel

Primary users: CMO, Marketing Staff, Support Agent.

Phase-1 rule:

```text
This panel is merged for Phase-1 only.
Enterprise version must split it into Marketing Panel and Omnichannel Inbox Panel.
```

Must support:

- Campaign performance
- Content calendar
- Meta/Google/TikTok event health
- Delivered-sale ROAS
- WhatsApp campaign approval
- Unified inbox
- Facebook/WhatsApp/Instagram/website chat
- AI reply suggestion
- Human takeover
- Customer/order context panel

### 6.15 Task/Reseller/AI Control Panel

Primary users: Manager, Reseller Manager, AI Supervisor, Admin.

Phase-1 rule:

```text
This panel is merged for Phase-1 only.
Enterprise version must split it into Task Manager Panel, Reseller Panel and AI Control Panel.
```

Must support:

- Task assignment
- Department task board
- Internal instruction
- SLA/due date
- Reseller order review
- Reseller commission
- Payout approval
- AI suggestion queue
- AI mode control
- Knowledge update approval

---

## 7. Permission Matrix

Use this as initial permission planning. Actual implementation should store permissions as granular actions.

```text
Role                  Admin Executive POS Orders Courier Inventory Purchase Wholesale Finance CRM Telesales Packaging Delivery Marketing Inbox Task Reseller AI
Owner/CEO             A     A         V   A      A       A         A        A         A       V   V         V         V        V         V     A    A        A
Admin                 A     V         A   A      A       A         A        A         A       A   A         A         A        A         A     A    A        A
CTO                   V     V         -   -      -       -         -        -         -       -   -         -         -        -         -     -    -        A
CFO                   V     A         -   V      V       V         A        A         A       -   -         -         -        -         -     V    A        V
COO                   V     A         V   A      A       V         V        V         V       V   V         A         A        -         -     A    V        V
CMO                   V     A         -   V      -       -         -        -         -       V   V         -         -        A         A     V    -        V
Store Manager         -     -         A   V      V       A         V        -         V       -   -         A         V        -         -     V    -        -
POS Staff             -     -         A   C      C       V         -        -         -       -   -         -         -        -         -     -    -        -
Sales/CRM Staff       -     -         -   C      V       V         -        -         -       A   V         -         -        V         V     V    -        -
Telesales Staff       -     -         -   C      V       -         -        -         -       V   A         -         -        -         V     V    -        -
Packaging Staff       -     -         -   V      V       V         -        -         -       -   -         A         V        -         -     V    -        -
Delivery Staff        -     -         -   V      A       -         -        -         -       -   -         V         A        -         -     V    -        -
Wholesale Manager     -     -         -   -      V       V         -        A         V       V   V         -         -        -         -     V    -        -
Reseller Manager      -     -         -   V      V       V         -        -         V       -   -         -         -        -         -     V    A        -
Support Agent         -     -         -   V      V       V         -        -         -       V   V         -         -        -         A     V    -        V
AI Supervisor         -     V         -   V      V       V         -        -         V       V   V         V         V        V         V     V    V        A
```

Legend:

```text
A = full access / approve where permitted
C = create or operate within assigned workflow
V = view or limited action
- = no access by default
```

Sensitive actions must require approval even if a user has broad module access.

### 7.1 Action-Based Permission Contract

The matrix above is only an overview. Real implementation must use granular action permissions.

Examples:

```text
pos.sale.view
pos.sale.create
pos.sale.void
pos.discount.apply
pos.discount.high_value.apply
pos.shift.open
pos.shift.close
pos.eod.reconcile

order.view
order.create
order.status.update
order.cancel.request
order.cancel.approve
order.convert_from_pos
order.risk_hold.override

inventory.stock.view
inventory.stock.move
inventory.stock.adjust.request
inventory.stock.adjust.approve
inventory.negative_stock.override

purchase.invoice.create
purchase.payment.request
vendor.ledger.view
vendor.payment.approve

finance.ledger.view
finance.journal.create
finance.journal.approve
finance.payment.approve
finance.report.export

wholesale.order.create
wholesale.price.override
wholesale.ledger.view

crm.lead.create
crm.followup.assign
telesales.call.log

packaging.task.assign
packaging.task.complete
delivery.status.update
courier.booking.create
courier.reconciliation.approve

marketing.campaign.create
marketing.bulk_message.request
omnichannel.inbox.reply
omnichannel.ai_reply.approve

task.create
task.assign
reseller.payout.request
reseller.payout.approve
ai.mode.change
ai.suggestion.approve
```

Implementation rule:

```text
Role -> Permission Group -> Action Permission
User -> Multiple Roles -> Active Role -> Allowed Action
Sensitive Action -> Approval Request -> Audit Log
```

---

## 8. Approval-Required Actions

```text
refund.create
finance.adjust
vendor.payment.create
reseller.payout.approve
product.price.change
discount.high_value.apply
customer.blacklist.add
order.cancel_after_dispatch
stock.adjust
negative_stock.override
ai.autopilot.enable
bulk_whatsapp.send
ad_budget.increase
knowledge.update.approve
sync.config.change
emergency_lock.disable
```

---

## 9. State Machines

### 9.1 POS Sale State

```text
Draft Cart
Payment Pending
Paid / Due Recorded
Completed
Returned
Partially Returned
Exchanged
Voided
```

POS event/accounting impacts:

```text
On POS Completed -> stock deducted
On POS Completed -> payment posted
On POS Completed -> invoice generated/printed
On POS Returned -> stock and finance adjusted
On POS Voided before completion -> no stock or sale impact
```

### 9.2 POS-To-Courier Conversion State

```text
POS Cart
Courier Requested
Customer Address Required
Converted To Courier Order
Risk Checked
Packing Task Created
Dispatched
Delivered / Returned / Cancelled
```

### 9.3 Online Order State

```text
Draft
Placed
Payment Pending
Advance Required
Address Incomplete
Customer Confirm Pending
Confirmed
Risk Hold
Packed
Packing Failed
Courier Booking Failed
Dispatched
In Transit
Delivered
Delivery Failed
Return Requested
Return Received
Returned
Cancelled
Partial Return
Refund Pending
Refunded
```

Rules:

```text
Delivered = actual sale.
Cancelled before delivery = no sale.
Returned after delivery = sale reversal.
Partial return = adjusted sale value.
```

### 9.4 Courier Reconciliation State

```text
Booked
Dispatched
In Transit
Delivered
COD Pending
Courier Sheet Uploaded
Matched
Cleared
Mismatch / Claim
```

### 9.5 Finance Posting Rule

```text
Order placed -> no sale ledger posting
Advance paid -> payment liability/advance record
Delivered -> sale revenue + COGS + receivable/cash impact
Returned -> reversal/adjustment
Courier COD received -> courier clearing reduced
Commission -> payable created after delivered status
```

### 9.6 Double-Entry Journal Examples

Developers must model finance with journal entries and journal lines, not only dashboard totals.

Delivered COD order:

```text
Dr Courier Receivable
Cr Sales Revenue
```

COGS for delivered order:

```text
Dr Cost of Goods Sold
Cr Inventory
```

Courier COD received after courier settlement:

```text
Dr Cash/Bank
Dr Courier Charge Expense
Cr Courier Receivable
```

Return after delivery:

```text
Dr Sales Return
Cr Customer/Courier Receivable

Dr Inventory
Cr Cost of Goods Sold
```

Advance payment received before delivery:

```text
Dr Cash/Bank/Mobile Banking
Cr Customer Advance Liability
```

Delivered order with prior advance:

```text
Dr Customer Advance Liability
Dr Customer/Courier Receivable if balance remains
Cr Sales Revenue
```

Finance implementation rule:

```text
Every financial impact must create balanced journal lines.
Debit total must equal credit total.
Ledger reports must be derived from journal entries.
```

---

## 10. Audit Log Requirements

Every important action must record:

- Actor type: human, AI, system rule
- Actor ID
- Active role
- Business/tenant
- Action name
- Entity type
- Entity ID
- Data used
- Before state
- After state
- Approval status
- Reason
- External API called
- IP/device/session
- Timestamp
- Result

AI logs must also record:

- Agent name
- Agent mode
- Confidence
- Guardrail matched
- Cloud AI used or not
- Human approval required or not

### Audit Event Taxonomy

```text
auth.login
auth.logout
rbac.role.assigned
rbac.permission.changed
staff.active_role.changed
product.created
product.price.changed
inventory.stock_moved
inventory.stock_adjusted
inventory.negative_stock_override
purchase.invoice_created
vendor.payment_created
pos.sale_completed
pos.return_created
pos.shift_opened
pos.shift_closed
pos.eod_reconciled
order.created
order.confirmed
order.risk_hold_applied
order.cancelled
order.delivered
order.returned
order.partial_returned
order.converted_from_pos
packaging.task_created
packaging.task_completed
courier.booking_created
courier.status_synced
courier.cod_reconciled
finance.ledger_posted
finance.adjustment_requested
finance.adjustment_approved
crm.lead_created
crm.followup_scheduled
telesales.call_logged
marketing.campaign_created
marketing.event_health_failed
omnichannel.message_received
omnichannel.ai_reply_suggested
task.created
task.completed
reseller.order_created
reseller.commission_posted
reseller.payout_approved
ai.suggestion_created
ai.action_requested
ai.action_approved
ai.action_rejected
sync.event_sent
sync.event_failed
security.alert_created
```

---

## 11. Security Requirements

- Local-first database protection
- Hosting limited access
- Signed sync events
- Webhook signature verification
- Tenant isolation
- Role-based permission
- Session expiry
- Safe uploads
- Immutable audit logs
- Customer message sandboxing
- No direct tool access from customer-facing AI
- Secrets never exposed to agents unless scoped
- API key scoping
- Rate limiting
- Approval control for sensitive actions
- Audit trail for security-sensitive changes

---

## 12. Integration Requirements

### Courier

- Steadfast/Pathao/other courier support
- Booking API
- Tracking sync
- COD reconciliation
- Manual fallback

### Payment

- bKash
- Nagad
- Bank
- Card/POS terminal
- Dynamic QR
- Manual verification with approval

### Marketing

- Meta Pixel/CAPI
- Google Ads
- GA4
- GTM
- TikTok Pixel/Event API
- WhatsApp Cloud API

### Integration Health

- Token expiry alert
- Webhook failure log
- Retry queue
- Manual fallback
- CTO dashboard status

### Local-First Sync Contract

Because BanikOS is local-first, sync must be designed as a reliable event system.

Required sync fields:

```text
sync_event_id
event_type
entity_type
entity_id
tenant_id
event_version
payload_hash
idempotency_key
source_system
target_system
created_at
last_synced_at
retry_count
sync_status
failed_reason
conflict_status
manual_retry_allowed
```

Required sync patterns:

```text
Outbox pattern for local-to-hosting events
Inbox/idempotency table for received webhooks
Signed event payloads
Webhook signature verification
Retry with retry count and backoff
Duplicate event protection with idempotency key
Event versioning for schema changes
Manual retry action from CTO/Admin dashboard
Visible failed sync reason
```

Conflict resolution rule:

```text
Local BanikOS Core is the source of truth for product, stock, price and finance.
Hosting platform can create public orders/leads but cannot overwrite local core truth.
Courier/payment webhooks update external status only after signature and idempotency checks.
If conflict occurs, mark as Conflict and require admin review instead of silently overwriting data.
```

---

## 13. Core Data Entities

Minimum entities for implementation planning:

```text
Tenant
Branch
Warehouse
User
Role
Permission
UserRole
ApprovalRequest
AuditLog
Product
ProductVariant
ProductCategory
Unit
TaxRule
InventoryBalance
InventoryMovement
StockReservation
Vendor
PurchaseInvoice
VendorLedgerEntry
Customer
CustomerAddress
Order
OrderItem
OrderStatusHistory
Payment
PaymentMethod
PaymentTransaction
Refund
POSShift
CashDrawerEntry
ReturnRequest
CourierProvider
CourierChargeRule
CourierShipment
CourierReconciliation
FinanceAccount
ChartOfAccount
JournalEntry
JournalEntryLine
LedgerEntry
WholesaleCustomer
WholesaleInvoice
CRMLead
FollowUp
CallLog
PackagingTask
MarketingCampaign
OmnichannelConversation
Task
Reseller
ResellerCommission
CommissionPolicy
DiscountPolicy
AIAgentLog
KnowledgeSuggestion
SyncEvent
WebhookEvent
IdempotencyKey
Notification
DeviceSession
```

---

## 14. Backend API Grouping

Suggested API groups:

Canonical order route decision:

```text
Use /api/orders for the core BanikOS ERP.
Use /api/oms/orders only if OMS becomes a separate service later.
Do not mix both names in the same implementation.
```

```text
/api/auth
/api/admin
/api/rbac
/api/audit
/api/products
/api/inventory
/api/purchases
/api/pos
/api/orders
/api/payments
/api/refunds
/api/courier
/api/finance
/api/wholesale
/api/crm
/api/telesales
/api/packaging
/api/delivery
/api/marketing
/api/omnichannel
/api/tasks
/api/resellers
/api/ai
/api/sync
/api/webhooks
/api/reports
```

---

## 15. Frontend Acceptance Criteria

For each of the 15 surfaces:

- User can access it only with proper role/permission.
- Active role is visible.
- Primary table/queue is searchable and filterable.
- Key metrics are visible at the top.
- Important row actions require confirmation or approval.
- Sensitive actions create approval request.
- Every important action creates audit log.
- Loading, empty, error and permission-denied states exist.
- Mobile/tablet/desktop layout remains usable.
- The surface has a clear path back to Master Admin or assigned module.

### 15.1 UI Design Deliverables

Senior developer/designer deliverables must include:

```text
Wireframe for all 15 surfaces
High-fidelity UI for all 15 surfaces
Responsive desktop/tablet/mobile states
Shared component library
Table component
Filter/search/sort component
Form component
Status badge system
Approval drawer
Risk alert drawer
Audit timeline
Right context panel
Empty/loading/error states
Permission denied screen
Print invoice design
Thermal invoice design
EOD cash reconciliation screen
Role switcher component
Notification/toast system
```

### 15.2 Device Role Rules

Full ERP operation should not be forced into mobile. Device responsibilities should be clear.

```text
Desktop = full operation, data entry, finance, inventory, reporting
Tablet = manager review, approval, packing/delivery queue review
Mobile = alerts, approval, task update, courier status, quick reply
```

Mobile must be usable, but desktop remains the primary surface for complex ERP work.

---

## 16. Critical Test Cases

These tests decide whether the system is truly 9/10-ready.

```text
1. POS sale deducts stock, records payment, prints invoice, creates audit log.
2. POS courier request converts to courier order and does not count as pure POS sale.
3. Online order placed does not appear as actual sale.
4. Delivered order creates sale/profit/commission effects.
5. Returned order reverses or adjusts sale value.
6. Partial return adjusts stock, revenue and profit.
7. Negative stock is blocked unless approved override exists.
8. Vendor partial payment updates vendor ledger correctly.
9. Courier COD sheet matches tracking code and clears receivable.
10. High-risk COD order cannot dispatch without approval.
11. Multi-role staff action is logged with active role.
12. AI suggestion cannot execute sensitive action without approval.
13. Customer-facing AI cannot access finance/secrets/unrestricted tools.
14. Marketing purchase event fires only after delivered.
15. Sync failure appears in admin/CTO dashboard.
16. Wholesale due does not mix with retail customer ledger.
17. Reseller commission is posted only after delivered status.
18. EOD cash mismatch creates shortage/excess log.
19. Stock adjustment requires permission and audit.
20. Emergency lock prevents unsafe system actions.
```

### 16.1 Test Type Breakdown

Unit tests:

```text
Stock cannot go negative without approved override.
Permission checker blocks unauthorized action.
Journal entry debit and credit totals must match.
Order status transition rules are valid.
Risk score flags high-risk COD order.
Discount policy detects high-value discount.
```

Integration tests:

```text
Delivered order posts sales journal, COGS and commission payable.
POS completed sale deducts stock, posts payment and creates audit log.
Courier COD reconciliation clears courier receivable.
Vendor partial payment updates payable ledger.
Partial return adjusts stock, revenue, COGS and customer/courier receivable.
AI approval flow creates suggestion, approval request and audit log.
```

E2E tests:

```text
POS sale -> invoice -> stock deduct -> EOD cash reconciliation.
Website order -> COD risk -> packing -> dispatch -> delivered -> finance posting.
POS courier request -> converted courier order -> delivered -> sale confirmed.
Wholesale order -> partial payment -> due ledger -> payment clearing.
Omnichannel lead -> CRM follow-up -> order creation -> delivered sale.
Reseller order -> dispatch -> delivered -> commission -> payout approval.
```

Security tests:

```text
Customer message cannot access finance or secrets through AI.
Webhook with invalid signature is rejected.
Duplicate webhook with same idempotency key does not duplicate posting.
User cannot perform action outside active role permission.
Sensitive action requires approval even for multi-role staff.
```

### 16.2 Implementation Status Vocabulary

Do not label planned features as completed unless they are implemented, tested and production-ready.

Use these statuses:

```text
Planned / Required
Designed
In Development
Implemented
Tested
Production Ready
```

Documentation rule:

```text
This document is a planning and developer handoff document.
It must not imply that all modules are already completed.
```

---

## 17. Suggested Release Roadmap

Ledger design must start in Release 1 even if the full CFO dashboard comes later.

```text
Release 1 = ledger foundation
Release 2 = POS posting
Release 3 = courier/COD posting
Release 4 = full CFO dashboard and finance reporting
```

### Release 1: Admin + Data Foundation

- Login
- Role and permission
- Active role switcher
- Audit log
- Chart of accounts
- Journal entry and journal entry line model
- Basic ledger foundation
- Payment method model
- Business setup
- Staff setup
- Product catalog
- Inventory
- Vendor purchase
- Vendor ledger

### Release 2: POS + Offline Retail

- POS sale
- Invoice
- Payment
- Return/exchange
- EOD cash
- Cash drawer
- POS-to-courier conversion
- POS sale ledger posting
- POS return/exchange finance posting

### Release 3: Online Order + Courier

- Manual/website/social order
- Order lifecycle
- Packing
- Dispatch
- Courier tracking
- COD risk
- Courier reconciliation
- Courier receivable posting
- COD settlement posting
- Return/partial return posting

### Release 4: Wholesale + Finance

- Wholesale customer
- Wholesale pricing
- Wholesale invoice
- Due/baki
- Receivable ledger
- Profit/loss
- CFO dashboard
- Full finance reports
- Journal approval workflow

### Release 5: CRM + Task + Omnichannel

- CRM lead board
- Follow-up
- Call log
- Unified inbox
- Task assignment
- Internal communication

### Release 6: Website + Landing + Marketing

- Product sync
- Stock sync
- Website order
- Landing page
- Pixel/CAPI
- Ads dashboard
- Delivered-sale ROAS

### Release 7: Reseller + AI

- Reseller panel
- Reseller commission
- Payout approval
- AI suggestion mode
- AI handover
- Guarded autopilot for low-risk tasks

---

## 18. 9/10 Checklist

To reach and maintain 9/10, BanikOS must have:

- Clear POS/offline and online/courier separation
- Delivered-only actual sale rule
- Retail and wholesale separation
- Strong inventory and cost calculation
- Vendor ledger and payable
- Customer/wholesale receivable
- Courier clearing account
- EOD cash reconciliation
- Return/exchange/partial return workflow
- COD risk scoring
- Role-permission-audit system
- Finance ledger, not only dashboard
- Admin approval for sensitive actions
- AI guardrail and approval mode
- Secure local-first sync bridge
- Website API with scoped key
- Integration monitoring and fallback
- Role-based dashboards
- Live audit stream
- Clean responsive UI
- Proper test cases for every module
- Developer-ready route map
- Action-level permission catalog
- State machines
- Audit event taxonomy
- Double-entry journal examples
- Complete finance entities
- Local-first sync contract
- UI deliverables
- Device role rules
- Unit/integration/E2E/security test breakdown
- API grouping
- Frontend acceptance criteria

---

## 19. Execution Risk

Execution risk remains medium to high because the product has many modules and strict cross-module rules.

Highest-risk areas:

- Ledger-based finance correctness
- Inventory and cost calculation correctness
- Delivered-only sale enforcement across all reports
- Courier reconciliation and COD receivable accuracy
- Local-first sync bridge security
- Role-based permission and immutable audit log
- AI guardrails and approval workflow
- POS speed while supporting conversion to courier workflow

Risk control:

- Build release by release.
- Test business rules before UI polish.
- Keep audit and permission system in Release 1.
- Never delay ledger design until the end.
- Treat delivered-only sale as a global invariant.

---

## 20. Developer Handoff Summary

Give the senior developer these requirements:

```text
Build 15 frontend surfaces first.
Treat Marketing/Omnichannel and Task/Reseller/AI as Phase-1 merged surfaces only.
Use /control-center for the merged control route, not /control.
Use one shared app shell.
Use active role switcher everywhere.
Use delivered-only sale as a hard business rule.
Use ledger-based finance.
Start chart of accounts, journal entries and ledger foundation in Release 1.
Use approval flow for sensitive actions.
Use audit log for every important action.
Keep POS offline-sale focused.
Convert POS courier requests into courier/online orders.
Design backend around explicit state machines and audit events.
Use action-level permissions, not only role-level access.
Use outbox, idempotency key and conflict handling for local-first sync.
```

Final principle:

```text
POS stays offline.
Courier order follows courier/online workflow.
Delivered is the only actual sale.
Finance must match stock, order, courier and payment.
AI must follow rules and approvals.
Every important action must be traceable.
```
