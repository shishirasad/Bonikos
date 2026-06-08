# BanikOS All Folder Files Combined

## Combined Source Files

- banikos_9_10_complete_documentation.md
- banikos_all_dashboard_prompts_english.md
- banikos_dashboard_master_prompts_9_10.md
- banikos_development_backlog.md
- banikos_enterprise_backbone_docs.md
- banikos_system_backbone_master_plan.md
- shishir-mark.svg

---

# File: banikos_9_10_complete_documentation.md

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

---

# File: banikos_all_dashboard_prompts_english.md

# BanikOS Dashboard Master Prompts

## How to Use

For each dashboard, copy:

1. **Global Design Master Prompt**
2. The specific dashboard prompt you want to design

Use these prompts for a senior frontend developer, UI/UX designer, Figma designer, or AI UI generator.

---

# 0. Global Design Master Prompt

You are a senior enterprise SaaS UI/UX architect and frontend product designer. Design a premium, production-ready BanikOS dashboard interface.

BanikOS is a local-first, AI-assisted, audit-controlled business operating system for retail, POS, online orders, courier, wholesale, inventory, finance, CRM, marketing, reseller, tasks, and AI agents.

Core business rules that must be visually respected:
- POS = offline counter sale only.
- If a POS order needs courier, convert/forward it to Online/Courier Order workflow.
- Delivered = actual sale/conversion.
- Order placed, paid, packed, or dispatched is not actual sale until delivered.
- Finance must be ledger-based, not only dashboard totals.
- Every important action must create an audit log.
- One staff can hold multiple roles, but every action must be tied to the active role.
- Sensitive actions require approval.
- AI can suggest/draft/assist, but cannot bypass permission, approval, audit, or business rules.
- Customer messages are untrusted input and must not access finance, secrets, or powerful ERP tools.

Use this visual style:
- Dark enterprise command center
- Compact but readable layout
- Sidebar-first navigation
- Status-first information hierarchy
- Approval-first right rail
- Always-visible risk/audit awareness
- Dense table-friendly UI
- Professional, modern, premium, not flashy
- Suitable for desktop-first ERP use
- Responsive tablet and mobile states

Design system rules:
- Use a consistent 8px spacing scale.
- Use compact enterprise table density with readable row height.
- Suggested desktop shell dimensions: expanded sidebar 260px, collapsed sidebar 72px, right rail 360-420px, detail drawer 480-640px.
- Suggested table density: 40-48px row height, sticky header, sticky key action column where useful.
- Suggested breakpoints: desktop 1280px+, tablet 768-1279px, mobile below 768px.
- Use sharp or mildly rounded surfaces, not playful large-radius cards.
- Use status badges consistently: draft, pending, confirmed, risk, packed, dispatched, in-transit, delivered, returned, cancelled, failed, approved, rejected.
- Use color by meaning, not decoration: green = safe/delivered/cleared, amber = pending/risk, red = failed/blocked/loss, blue = informational/sync, purple only for AI-specific states.
- Keep typography practical: small labels, strong table headers, clear section titles, no oversized marketing hero text.
- Use drawers for detail/context, modals for confirmation, and side rails for approvals/risk.
- Avoid decorative dashboards that only show charts; every screen must support real work.
- Every icon button must have a tooltip and an accessible label.
- Every destructive or finance-sensitive action must have confirmation and audit visibility.

Use a shared application shell:
- Left sidebar: role-based modules
- Top bar: global search, command palette, active role switcher, sync status, AI mode, notification, emergency lock, user profile
- Main canvas: dashboard/page content
- Right rail: approvals, risks, AI alerts, selected item context
- Audit stream: visible where relevant

Device role rules:
- Desktop = full operation, data entry, finance, inventory, reporting, reconciliation.
- Tablet = manager review, approvals, queue review, packing/delivery supervision.
- Mobile = alerts, approvals, task update, courier status, quick reply, critical summaries only.
- Do not force complex finance, inventory audit, or full report building into mobile.

Route and merge rules:
- Use `/control-center` for the Phase-1 merged Task/Reseller/AI panel.
- Do not use `/control` because it is too generic.
- Use `/reseller-control` and `/ai-control` as separate enterprise split routes.
- Marketing/Omnichannel is merged for Phase-1 only; enterprise version must split it.
- Task/Reseller/AI is merged for Phase-1 only; enterprise version must split it.

Every dashboard must include:
- Page header with title, status, primary actions
- Metric strip with key KPIs
- Main work area: table, queue, kanban, form, or chart depending on module
- Right context panel for selected item details
- Approval/risk section
- Audit timeline or latest activity
- Search, filter, sort
- Loading, empty, error, permission-denied states
- Desktop/tablet/mobile behavior
- Clear route name
- Clear role access

Output format required:

```text
1. Layout Summary
2. Route and Primary Roles
3. Desktop Wireframe Description
4. Tablet Behavior
5. Mobile Behavior
6. KPI Cards
7. Main Work Area Structure
8. Table / Queue / Kanban Columns
9. Primary Actions
10. Drawers, Modals, and Side Rails
11. Status Badge System
12. Empty / Loading / Error / Permission Denied States
13. Permission and Approval Behavior
14. Audit Log Touchpoints
15. Component List for Frontend Implementation
16. Developer Notes
17. Suggested Test Touchpoints
```

Suggested Test Touchpoints must mention:

```text
Unit-level validation for business rules shown on the screen
Integration flow that connects this screen to stock/finance/order/audit
E2E user journey for the primary workflow
Security/permission test for sensitive actions
```

Quality guardrails:
- Do not produce the same generic layout for every module.
- Make the core workflow of each module visually dominant.
- POS must be cart-first and scan-first.
- Finance must be ledger-first.
- Omnichannel must be conversation-first.
- Packaging must be scan/checklist-first.
- Courier must be tracking/COD-first.
- Admin must be risk/approval-first.
- Marketing must be campaign/event-health-first.
- Task manager must be ownership/SLA-first.
- AI Control must be approval/guardrail-first.

Dashboard-specific layout patterns:

```text
Admin = command grid + approval/risk rail + live audit stream
Executive = tabbed C-level overview + drill-down risk lists
POS = barcode/search + cart + payment + shift drawer
Orders = status pipeline + order table + customer context
Courier Orders = booking queue + tracking table + COD reconciliation
Inventory = stock table + location view + movement history
Vendor Purchase = purchase invoice flow + receive items + vendor ledger
Wholesale = bulk order table + manual pricing + receivable ledger
Finance = journal table + account ledger + reconciliation panels
CRM/Sales = lead board + customer timeline + follow-up queue
Telesales = call queue + script panel + callback scheduler
Packaging = pick list + scan/check confirmation + handover queue
Delivery/Courier = dispatch queue + status updates + claim tracking
Marketing/Omnichannel Phase-1 = campaign/event health tabs + inbox tab
Control Center Phase-1 = task tab + reseller tab + AI approval tab
COD Risk = risk queue + risk reason breakdown + override approval
Marketing Enterprise = campaign table + content calendar + event health
Inbox Enterprise = three-column inbox + thread + customer/order context
Task Enterprise = task board + internal inbox + SLA/escalation queue
Website Enterprise = publish list + sync queue + landing/page manager
Reseller Control = reseller ledger + commission + payout approval
AI Control = suggestion queue + guardrail status + agent activity log
```

---

# 1. Master Admin Control Panel — Master Prompt

## Route
`/admin`

## Primary Users
Owner, Admin

## Objective
Design the main command center of BanikOS where the owner/admin can monitor and control the whole business, approvals, risks, AI alerts, sync health, and department status from one screen.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Net profit today/month
- Delivered sales
- Pending orders
- Cash/bank/mobile balance
- Courier COD receivable
- Vendor payable
- Wholesale receivable
- Inventory value
- Low stock count
- Pending approvals
- AI alerts
- Sync health
- Courier risk count

## Required Main Sections
- Business health strip
- Master command shortcut panel
- Department/module health grid
- Right approval/risk rail
- AI alert panel
- Sync and system health widget
- Live audit stream
- Emergency lock section

## Main Table / Queue / Kanban Requirements
Module health cards instead of one large table. Each card must show module status, pending count, risk count, key metric, next action, and open module button.

## Primary Actions
- Approve/reject sensitive requests
- Jump to any module
- Trigger emergency lock
- Open audit log
- Review AI alerts
- Review sync/API failure
- Start AI handover
- Open approval queue

## Command Palette Examples
The Master Admin Control Panel must include a command palette with quick actions such as:

```text
Create order
Add product
Receive stock
Open approval queue
Run system sync
Emergency lock
Search customer
Search order
Search SKU/barcode
Open finance ledger
Open courier reconciliation
Open audit log
Open AI suggestion queue
```

## Business Rules to Enforce in UI
- Admin must see all critical risks.
- Delivered-only sales must be separated from pending/placed orders.
- Emergency lock must require confirmation.
- Every admin action must be audit logged.
- AI cannot execute sensitive action without approval.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 2. C-Level Executive Dashboard — Master Prompt

## Route
`/executive`

## Primary Users
Owner, CEO, CFO, COO, CMO, CTO, Admin

## Objective
Design one executive dashboard with tabs for CEO, CFO, COO, CMO, and CTO so C-level users can see business, finance, operations, marketing, and system health from one place.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Business health score
- Net profit
- Delivered sales
- Cash position
- Payable/receivable
- Operational backlog
- Marketing ROAS
- System health
- Pending approvals
- Urgent risks

## Required Main Sections
- CEO Overview tab
- CFO Finance View tab
- COO Operations View tab
- CMO Marketing View tab
- CTO System View tab
- Cross-department risk summary
- Executive AI summary
- Approval queue

## Main Table / Queue / Kanban Requirements
Use tabbed executive cards and drill-down tables. Each tab should have its own KPI row, status cards, and top risks list.

## Primary Actions
- Switch C-level tabs
- Open related department panel
- Approve executive-level requests
- Export executive summary
- View AI executive insight
- Open risk details

## Business Rules to Enforce in UI
- One executive dashboard first; later tabs can become separate dashboards.
- Finance numbers must be ledger-based.
- Marketing purchase/conversion must be delivered-only.
- CTO tab must show sync/webhook/security failures.
- Sensitive approvals must be visible across tabs.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 3. POS Panel — Master Prompt

## Route
`/pos`

## Primary Users
POS Staff, Store Manager, Admin

## Objective
Design a fast offline counter sale POS panel. POS must remain simple and focused on in-store sales. If courier is needed, the order must be converted to courier/online workflow.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Current shift sales
- Cash drawer expected
- Completed POS sales
- Returns today
- Discounts today
- Items sold
- Cash shortage/excess
- Held carts

## Required Main Sections
- Barcode/search input
- Product grid/list
- Cart panel
- Payment panel
- Customer optional field
- Discount control
- Invoice print area
- Shift open/close
- EOD reconciliation
- POS-to-courier conversion button

## Main Table / Queue / Kanban Requirements
Cart-first layout. Product search and barcode input must be extremely prominent. Cart lines must include item, SKU, qty, price, discount, stock warning, remove action.

## Primary Actions
- Scan/search product
- Add/remove cart item
- Apply discount with permission
- Select payment method
- Split payment
- Print invoice
- Hold cart
- Complete sale
- Return/exchange
- Open/close shift
- EOD reconcile
- Send by Courier

## Required POS Keyboard Shortcuts
The POS panel must be keyboard-friendly for fast counter sales.

```text
F2 = Focus product search / barcode input
F4 = Open payment panel
F6 = Hold current cart
F8 = Print invoice
Ctrl + Enter = Complete sale
Ctrl + Backspace = Clear selected cart item
Esc = Close drawer/modal or cancel current quick action
Alt + C = Open customer field
Alt + R = Start return/exchange flow
Alt + D = Open discount control
Alt + K = Send by Courier conversion drawer
```

Shortcut rules:
- Every shortcut must have visible tooltip support.
- Shortcuts must not trigger destructive actions without confirmation.
- Sensitive actions such as high discount or send by courier must still respect permission and approval rules.

## Business Rules to Enforce in UI
- POS = offline sale only.
- Send by Courier must convert to Online/Courier Order workflow.
- POS completed sale deducts stock and posts payment.
- Voided cart before completion has no stock/sale impact.
- High discount requires approval.
- EOD mismatch creates shortage/excess log.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.

Special required flow: Design a “Send by Courier” drawer requiring customer name, phone, address, courier/payment/COD info, risk preview, and confirmation that the POS sale is converted to Courier Order.


---

# 4. Order Management Panel — Master Prompt

## Route
`/orders`

## Primary Users
Sales/CRM Staff, Admin, COO

## Objective
Design the main order lifecycle panel for website, manual, social, phone, and non-POS orders. It must show order intent vs actual delivered sale clearly.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Total orders today
- Confirmed orders
- Payment pending
- Address incomplete
- Risk hold
- Packed
- Dispatched
- Delivered sales
- Cancelled/returned

## Required Main Sections
- Order pipeline status board
- Order list table
- Customer detail panel
- Payment/COD status
- Source tracking
- Risk score preview
- CRM linked notes
- Audit timeline

## Main Table / Queue / Kanban Requirements
Order table columns: order ID, customer, source, phone, amount, payment status, order status, risk score, assigned staff, created time, next action.

## Primary Actions
- Create manual order
- Confirm order
- Request advance
- Mark address incomplete
- Send to packing
- Cancel request
- Link to CRM
- View customer timeline
- Convert source/order status
- Add internal note

## Business Rules to Enforce in UI
- Order placed is not actual sale.
- Delivered is actual sale.
- Cancelled before delivery = no sale.
- Returned after delivery = reversal.
- Address incomplete orders cannot dispatch.
- Risk hold requires approval/override.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 5. Courier Order Panel — Master Prompt

## Route
`/courier-orders`

## Primary Users
Delivery Coordinator, COO, Admin

## Objective
Design a courier order dashboard for POS-to-courier converted orders and online courier orders, including dispatch, tracking, COD, return, lost parcel, and courier claim workflows.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Courier-ready orders
- Booked shipments
- In transit
- Delivered
- COD pending
- Returned
- Lost/claim
- Courier COD receivable
- Reconciliation mismatch

## Required Main Sections
- Courier booking queue
- Tracking table
- COD receivable widget
- Return/lost parcel queue
- Courier provider status
- Reconciliation status
- Right detail panel with customer/order/courier info

## Main Table / Queue / Kanban Requirements
Courier table columns: shipment ID, order ID, customer, courier provider, tracking code, COD amount, delivery status, reconciliation status, risk score, last update, next action.

## Primary Actions
- Book courier
- Print courier label
- Update tracking
- Mark dispatched
- Sync courier status
- Mark delivered/returned
- Open claim
- Upload courier sheet
- Reconcile COD
- Override with approval

## Business Rules to Enforce in UI
- Dispatched is not delivered.
- Delivered triggers actual sale/conversion.
- Returned must trigger verification.
- Courier payout must match tracking code.
- COD receivable must clear only after reconciliation.
- Duplicate webhook/status update must not duplicate posting.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 6. Inventory Panel — Master Prompt

## Route
`/inventory`

## Primary Users
Store Manager, Inventory Staff, Admin

## Objective
Design an inventory control panel for product catalog, SKU/barcode, stock by location, stock movement, low stock, damage, loss, stock audit, and negative stock prevention.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Total SKUs
- Inventory value
- Low stock count
- Out of stock
- Stock movement today
- Damage/loss count
- Pending stock adjustments
- Reserved stock

## Required Main Sections
- Product catalog table
- Stock by warehouse/location
- Low stock alerts
- Stock movement history
- Stock audit section
- Damage/loss/shrinkage section
- Stock adjustment requests

## Main Table / Queue / Kanban Requirements
Inventory table columns: SKU, product, variant, category, warehouse/location, available stock, reserved stock, cost, retail price, wholesale price, status, next action.

## Primary Actions
- Add/edit product
- Create variant
- Move stock
- Request stock adjustment
- Approve adjustment if permitted
- Start stock audit
- Mark damage/loss
- View movement history
- Generate barcode/SKU

## Business Rules to Enforce in UI
- Negative stock is blocked unless approved override exists.
- Stock adjustment requires permission and audit.
- Reserved stock must be separated from available stock.
- Inventory cost must feed finance/profit calculation.
- Stock audit discrepancy becomes shrinkage/loss.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 7. Vendor Purchase Panel — Master Prompt

## Route
`/purchases`

## Primary Users
Purchase Staff, CFO, Admin

## Objective
Design a vendor purchase dashboard for purchase invoice, product receive, cost entry, vendor payable, partial payment, vendor ledger, and due alerts.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Purchase invoices today
- Pending receiving
- Vendor payable
- Due today
- Partial payments
- Purchase value
- Items received
- Cost variance alerts

## Required Main Sections
- Vendor list
- Purchase invoice table
- Receive stock workflow
- Vendor ledger panel
- Due alert panel
- Payment request/approval section
- Cost entry form

## Main Table / Queue / Kanban Requirements
Purchase table columns: invoice no, vendor, item count, purchase value, received status, payable amount, paid amount, due date, approval status, next action.

## Primary Actions
- Create purchase invoice
- Receive products
- Add cost
- Record partial payment request
- Approve vendor payment
- View vendor ledger
- Set due date
- Export purchase report

## Business Rules to Enforce in UI
- Vendor payable updates after purchase invoice/receive.
- Product cost must connect to inventory valuation.
- Vendor payment is sensitive and needs approval.
- Partial payment must update vendor ledger.
- Every purchase/payment action must be audit logged.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 8. Wholesale Panel — Master Prompt

## Route
`/wholesale`

## Primary Users
Wholesale Manager, CFO, Admin

## Objective
Design a wholesale dashboard separate from retail, with wholesale customers, bulk order, manual price, invoice, partial payment, due/baki, receivable ledger, return, and profit report.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Wholesale sales
- Wholesale due
- Active wholesale customers
- Pending invoices
- Partial payments
- Wholesale profit
- Returned wholesale items
- Overdue receivables

## Required Main Sections
- Wholesale order creation
- Wholesale customer table
- Bulk item entry
- Manual price control
- Wholesale invoice list
- Receivable ledger
- Due/baki alert
- Wholesale return workflow

## Main Table / Queue / Kanban Requirements
Wholesale order table columns: invoice no, customer, item count, total amount, paid, due, payment status, delivery/status, profit estimate, next action.

## Primary Actions
- Create wholesale order
- Set manual wholesale price
- Apply price list
- Record partial payment
- View receivable ledger
- Create return
- Print wholesale invoice
- Export wholesale report

## Business Rules to Enforce in UI
- Retail and wholesale reports must not mix.
- Wholesale customer ledger is separate from retail customer ledger.
- Manual price override requires permission.
- Wholesale due must update receivable ledger.
- Delivered/fulfilled logic must impact profit correctly.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 9. Finance Panel — Master Prompt

## Route
`/finance`

## Primary Users
CFO, Owner, Admin

## Objective
Design a ledger-based finance panel showing cash, bank, mobile banking, payable, receivable, courier clearing, staff/reseller commission, expenses, profit/loss, vouchers, and audit-ready trail.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Cash balance
- Bank balance
- Mobile banking balance
- Vendor payable
- Customer receivable
- Wholesale receivable
- Courier clearing/COD receivable
- Net profit
- Expenses
- Pending approvals

## Required Main Sections
- Finance overview
- Chart of accounts summary
- Journal entry table
- Ledger view
- Payable/receivable panels
- Courier clearing panel
- Expense entry
- Voucher section
- Approval queue
- Audit-ready export

## Main Table / Queue / Kanban Requirements
Ledger table columns: date, journal no, account, debit, credit, entity, source module, status, approval, created by, audit link.

## Primary Actions
- Create voucher/journal request
- Approve finance adjustment
- View account ledger
- Export report
- Reconcile courier COD
- Record expense
- View payable/receivable
- Review commission payable

## Required Finance Filters, Reports, and Reconciliation Views
The Finance panel must be ledger-first and report-ready.

Required filters:

```text
Date range filter
Branch filter
Account filter
Payment method filter
Source module filter
Entity filter: vendor/customer/reseller/courier/staff
Approval status filter
Journal status filter
```

Required report views:

```text
Trial balance
Profit and loss
Cash/bank/mobile balance
Vendor payable aging
Customer receivable aging
Wholesale receivable aging
Courier clearing report
Staff commission payable
Reseller commission payable
Expense report
Return/damage/shrinkage loss report
Audit-ready journal export
```

Required reconciliation views:

```text
Cash drawer vs system cash
Bank statement vs bank ledger
Mobile banking transaction vs payment ledger
Courier COD sheet vs courier receivable
Vendor payment vs vendor payable
Customer payment vs customer receivable
```

Export requirements:

```text
Export PDF
Export Excel/CSV
Print ledger
Download audit-ready report
```

## Business Rules to Enforce in UI
- Finance must be ledger-based.
- Debit total must equal credit total.
- Order placed creates no sale revenue.
- Delivered creates sale revenue/COGS impact.
- Courier COD received clears courier receivable.
- Finance adjustment requires approval and audit.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 10. CRM/Sales Panel — Master Prompt

## Route
`/crm`

## Primary Users
Sales Staff, CRM Staff, Sales Manager

## Objective
Design a CRM/sales dashboard to manage leads, source tracking, customer timeline, follow-up, notes, objections, interest tags, upsell/cross-sell, and lead-to-order conversion.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- New leads
- Follow-ups due
- Hot leads
- Converted leads
- Lost leads
- Average response time
- Agent performance
- Source quality

## Required Main Sections
- Lead kanban board
- Lead table
- Customer timeline
- Follow-up scheduler
- Objection notes
- Sales notes
- Upsell/cross-sell suggestions
- Lead source analytics

## Main Table / Queue / Kanban Requirements
Lead table columns: lead name, phone, source, interest, stage, assigned agent, next follow-up, last contact, conversion probability, next action.

## Primary Actions
- Create lead
- Assign follow-up
- Add note
- Log objection
- Convert lead to order
- Mark lost with reason
- Schedule call
- View customer timeline

## Business Rules to Enforce in UI
- CRM notes must feed future sales learning.
- Lead source must be tracked.
- Follow-up should not be lost.
- Customer timeline must show orders, messages, calls, notes.
- Conversion to order must follow order workflow.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 11. Telesales Panel — Master Prompt

## Route
`/telesales`

## Primary Users
Telesales Staff, Sales Manager

## Objective
Design a telesales dashboard for call queue, callback schedule, call status, call script, objection note, customer history, conversion result, and daily performance.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Calls assigned today
- Calls completed
- Callbacks due
- Converted calls
- Failed calls
- No answer
- Average call duration
- Agent conversion rate

## Required Main Sections
- Call queue
- Callback calendar/list
- Call script panel
- Customer history panel
- Objection note area
- Conversion result panel
- Daily performance summary

## Main Table / Queue / Kanban Requirements
Call queue columns: customer/lead, phone, source, priority, last call, next callback, assigned agent, status, script, next action.

## Primary Actions
- Start call
- Log call outcome
- Schedule callback
- Add objection note
- Convert to order
- Mark not interested
- Assign to CRM
- View customer/order history

## Business Rules to Enforce in UI
- Every call outcome must be logged.
- Objection notes should feed learning/CRM.
- Conversion creates order but not actual sale until delivered.
- Staff performance should be measurable.
- Follow-up/callback cannot be lost.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 12. Packaging Panel — Master Prompt

## Route
`/packaging`

## Primary Users
Packaging Staff, COO

## Objective
Design a focused packaging dashboard where packaging staff only see assigned packing tasks, pick list, scan/check products, confirm pack, record packaging material usage, report damage/missing, and handover to courier/delivery.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Pending packing tasks
- Packed today
- Packing errors
- Missing items
- Damaged items
- Packaging material used
- Ready for dispatch
- SLA overdue tasks

## Required Main Sections
- Assigned task queue
- Pick list view
- Scan/check section
- Packaging material usage panel
- Damage/missing report form
- Handover confirmation
- Task audit timeline

## Main Table / Queue / Kanban Requirements
Task table columns: task ID, order ID, customer, items count, priority, SLA, assigned staff, packing status, courier required, next action.

## Primary Actions
- Start packing
- Scan product
- Confirm item checked
- Add packaging material
- Report damage/missing
- Complete packing
- Handover to delivery/courier
- Add internal note

## Business Rules to Enforce in UI
- Packaging staff should see assigned tasks only unless extra permission.
- Packed is not delivered.
- Damage/missing report must update operation and audit.
- Packaging material usage should feed cost/profit calculation.
- Product scan/check should reduce packing errors.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 13. Delivery/Courier Panel — Master Prompt

## Route
`/delivery`

## Primary Users
Delivery Staff, Courier Coordinator, COO

## Objective
Design a delivery/courier operations dashboard for dispatch queue, courier handover, tracking update, return update, lost parcel alert, claim tracking, and courier payment matching.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Pending dispatch
- Handover completed
- In transit
- Delivery failed
- Returned
- Lost/claim
- COD pending
- Payment mismatch

## Required Main Sections
- Dispatch queue
- Courier handover list
- Tracking update table
- Return/lost parcel queue
- Claim tracker
- Courier payment matching section
- Delivery staff task list

## Main Table / Queue / Kanban Requirements
Delivery table columns: shipment/order ID, courier, tracking code, customer area, COD amount, status, last update, issue flag, assigned staff, next action.

## Primary Actions
- Confirm dispatch
- Record courier handover
- Update delivery status
- Mark return received
- Open claim
- Match payment
- Add delivery note
- Escalate issue

## Business Rules to Enforce in UI
- Dispatch is not delivered.
- Delivered status triggers actual sale.
- Return must trigger verification.
- Lost parcel must create claim/risk alert.
- COD/payment mismatch must appear in finance/courier clearing.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 14. Marketing/Omnichannel Panel — Phase-1 Merged — Master Prompt

## Route
`/marketing-omnichannel`

## Primary Users
CMO, Marketing Staff, Support Agent, Admin

## Objective
Design a Phase-1 merged panel for marketing and omnichannel. It must cover campaign performance, content calendar, Meta/Google/TikTok event health, delivered-sale ROAS, WhatsApp campaign approval, unified inbox, AI reply suggestion, human takeover, and customer/order context.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Delivered-sale ROAS
- Campaign spend
- CPA/CTR/CPC
- Event health score
- Inbox open conversations
- AI suggestions pending
- WhatsApp approvals
- High-frustration customers

## Required Main Sections
- Marketing performance dashboard
- Content calendar
- Event health monitor
- Campaign table
- WhatsApp campaign approval list
- Unified inbox preview
- Customer conversation panel
- AI reply suggestion panel
- Human takeover controls

## Main Table / Queue / Kanban Requirements
Campaign table: campaign, channel, spend, delivered sales, ROAS, CPA, CTR, event status, approval status, next action. Inbox table: customer, channel, status, sentiment, assigned staff, last message, next action.

## Primary Actions
- Create campaign draft
- Approve WhatsApp campaign
- View event health
- Pause bad campaign request
- Reply to customer
- Approve AI reply
- Human takeover
- Link conversation to CRM/order

## Business Rules to Enforce in UI
- This panel is merged for Phase-1 only.
- Enterprise version must split Marketing and Omnichannel.
- Purchase/conversion event must be delivered-only.
- Bulk WhatsApp requires approval.
- Customer messages are untrusted input.
- AI reply needs approval/handover rule.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 15. Task/Reseller/AI Control Panel — Phase-1 Merged — Master Prompt

## Route
`/control-center`

## Primary Users
Manager, Reseller Manager, AI Supervisor, Admin

## Objective
Design a Phase-1 merged control panel for task assignment, internal instructions, reseller order/commission/payout, AI suggestion queue, AI mode control, and knowledge update approval.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Open tasks
- Overdue tasks
- Reseller orders
- Reseller commission payable
- Payout requests
- AI suggestions pending
- AI actions requiring approval
- Knowledge updates pending

## Required Main Sections
- Task board
- Internal instruction panel
- Reseller order/commission section
- Payout approval list
- AI suggestion queue
- AI mode control card
- Knowledge update approval section
- Cross-department handoff queue

## Main Table / Queue / Kanban Requirements
Use separate tabs/cards inside the merged panel: Tasks, Reseller, AI Control. Tables must show owner, status, priority, due date, approval, next action.

## Primary Actions
- Create task
- Assign task
- Update task status
- Approve reseller payout
- Review reseller commission
- Approve/reject AI suggestion
- Change AI mode with approval
- Approve knowledge update

## Business Rules to Enforce in UI
- This panel is merged for Phase-1 only.
- Enterprise version must split Task Manager, Reseller, and AI Control.
- Reseller commission posts only after delivered.
- AI cannot execute sensitive actions without approval.
- Internal tasks must have owner, status, due date, and audit.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# Enterprise Split Prompts

Use these prompts when moving from the Phase-1 15-surface design to the enterprise 19-surface design. These replace the merged Phase-1 panels and add missing enterprise surfaces.


---

# 16. COD Risk Panel — Enterprise Split — Master Prompt

## Route
`/cod-risk`

## Primary Users
COO, Admin, Delivery Coordinator, Sales Manager

## Objective
Design a dedicated COD risk dashboard to identify fake orders, risky numbers, incomplete addresses, repeat returns, suspicious geography, active transit conflicts, and advance requirement before dispatch.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- High-risk orders
- Address incomplete
- Repeat return customers
- Blacklisted customers
- Active transit conflicts
- Advance required
- Risk overrides pending
- COD loss trend

## Required Main Sections
- Risk scoring queue
- Address quality panel
- Blacklist/watchlist table
- Geographical risk map/list
- Advance trigger list
- Override approval queue
- Risk reason breakdown

## Main Table / Queue / Kanban Requirements
Risk table columns: order ID, customer, phone, area, amount, risk score, risk reasons, previous returns, active transit, recommended action, approval status.

## Primary Actions
- Hold order
- Require advance
- Request full address
- Blacklist request
- Approve risk override
- Release to packing
- Add risk note
- View customer history

## Business Rules to Enforce in UI
- High-risk order cannot dispatch without approval/override.
- Risk score must be visible before dispatch.
- Blacklist is sensitive and requires approval.
- Risk override must require reason and audit.
- COD risk decisions must feed order and courier workflow.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 17. Marketing/CMO Panel — Enterprise Split — Master Prompt

## Route
`/marketing`

## Primary Users
CMO, Marketing Staff, Owner

## Objective
Design a dedicated marketing dashboard for content calendar, campaign planning, paid ads, Meta/Google/TikTok event health, delivered-sale ROAS, WhatsApp campaign approval, landing page performance, and marketing tasks.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Delivered-sale ROAS
- Ad spend
- CPA
- CTR
- CPC
- Event health score
- Landing page conversion
- Campaign approvals pending
- Content scheduled

## Required Main Sections
- Campaign performance overview
- Content calendar
- Paid ads table
- Event health monitor
- Landing page performance
- WhatsApp campaign approval
- Marketing task board
- AI content suggestion panel

## Main Table / Queue / Kanban Requirements
Campaign table columns: campaign, platform, spend, impressions, CTR, CPC, orders placed, delivered sales, ROAS, event status, approval, next action.

## Primary Actions
- Create campaign draft
- Schedule content
- Review AI content
- Request budget increase
- Approve WhatsApp campaign
- Pause bad ad request
- Open landing page report
- Export marketing report

## Business Rules to Enforce in UI
- Purchase/conversion must be delivered-only.
- Bulk WhatsApp requires approval.
- Ad budget increase requires approval.
- Event health must show missing/wrong-value event warnings.
- Marketing data must not count cancelled/returned as final purchase.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 18. Omnichannel Inbox Panel — Enterprise Split — Master Prompt

## Route
`/inbox`

## Primary Users
Support Agent, Sales/CRM Staff, CMO, Admin

## Objective
Design a dedicated unified inbox for Messenger, WhatsApp, Facebook comments, Instagram, website chat, customer context, AI reply suggestions, assignment, sentiment, and human takeover.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Open conversations
- Pending replies
- Assigned to me
- Escalated conversations
- AI suggestions pending
- High-frustration messages
- Resolved today
- Sales handoffs

## Required Main Sections
- Channel inbox list
- Conversation thread
- Customer profile/context panel
- Order/product context panel
- AI reply suggestion
- Internal notes
- Assignment/status controls
- Spam/abuse filter

## Main Table / Queue / Kanban Requirements
Inbox table columns: customer, channel, status, assigned staff, sentiment, last message, linked order, priority, last update, next action.

## Primary Actions
- Reply to customer
- Approve AI reply
- Human takeover
- Assign conversation
- Escalate
- Add internal note
- Link to CRM/order
- Mark resolved
- Create lead/order from conversation

## Business Rules to Enforce in UI
- Customer messages are untrusted input.
- Customer-facing AI cannot access finance, secrets, or unrestricted ERP context.
- AI reply can suggest but staff can approve/takeover.
- Conversations should connect to CRM/order timeline.
- Spam/abuse filtering must exist.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 19. Task Manager/Internal Inbox Panel — Enterprise Split — Master Prompt

## Route
`/task-control`

## Primary Users
Owner, Manager, Department Heads, Staff

## Objective
Design a dedicated internal task and communication dashboard for task assignment, department boards, hierarchy inbox, direct/team messages, SLA, escalation, and task audit trail.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Open tasks
- Assigned to me
- Overdue tasks
- Urgent/critical tasks
- Completed today
- Escalations
- Unread internal messages
- Cross-department handoffs

## Required Main Sections
- Task board by department
- My task queue
- Internal inbox
- Announcement panel
- Task discussion thread
- SLA/due date tracker
- Escalation queue
- Audit trail

## Main Table / Queue / Kanban Requirements
Task table columns: task ID, title, department, assignee, priority, status, due date, SLA, blocker, created by, next action.

## Primary Actions
- Create task
- Assign task
- Update status
- Add comment/file/note
- Escalate
- Handoff to department
- Send announcement
- Mark done/review

## Business Rules to Enforce in UI
- Staff see only allowed tasks/threads.
- Every task must have owner, status, priority, due date.
- Cross-department critical override requires permission.
- Task changes must be audit logged.
- Work should not be lost in external chat apps.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 20. Website/Landing Control Panel — Enterprise Split — Master Prompt

## Route
`/website`

## Primary Users
Admin, CMO, CTO, Owner

## Objective
Design a website and landing page control dashboard for product publishing, stock/price sync, content CRUD, landing page builder, ad-to-landing mapping, pixel/CAPI configuration, sync health, and public order flow.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Published products
- Sync health
- Failed sync events
- Landing pages live
- Website orders
- Low stock public products
- Pixel/CAPI health
- Page conversion

## Required Main Sections
- Product publish/unpublish list
- Landing page manager
- Website order sync queue
- Price/stock sync status
- Pixel/CAPI setup panel
- Ad campaign mapping
- Failed sync/retry section
- Hosting health card

## Main Table / Queue / Kanban Requirements
Website table columns: page/product, status, stock sync, price sync, last sync, campaign mapped, pixel health, conversion, next action.

## Primary Actions
- Publish/unpublish product
- Update page content
- Create landing page
- Map product to landing page
- Map campaign to landing page
- Configure pixel/CAPI
- Retry failed sync
- Review website order

## Business Rules to Enforce in UI
- Hosting cannot directly access local database.
- Local core is source of truth for product, stock, price, finance.
- Website order creates order intent, not actual sale.
- Sync failure must be visible.
- Conflict requires admin review, not silent overwrite.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 21. Reseller Control Panel — Enterprise Split — Master Prompt

## Route
`/reseller-control`

## Primary Users
Reseller Manager, CFO, Admin, Owner

## Objective
Design a dedicated reseller control dashboard for reseller order review, available catalog visibility, reseller commission, delivery-based commission posting, failed delivery policy, reseller ledger, payout request, and CFO/admin payout approval.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be reseller ledger, commission, and payout-first. Do not mix AI agent control into this primary surface.

## Required KPI / Metric Cards
- Active resellers
- Reseller orders
- Delivered reseller orders
- Failed reseller deliveries
- Commission payable
- Payout requests
- Approved payouts
- Deducted delivery charges
- Reseller ledger mismatch alerts

## Required Main Sections
- Reseller overview
- Reseller order review table
- Reseller product/catalog visibility
- Commission ledger
- Payout approval queue
- Failed delivery deduction panel
- Reseller performance summary
- Reseller account detail drawer
- Finance/audit timeline

## Main Table / Queue / Kanban Requirements
Reseller order table columns:

```text
Reseller
Order ID
Customer
Order status
Delivered value
Commission amount
Failed delivery charge
Payout status
Ledger status
Created date
Next action
```

Commission ledger columns:

```text
Date
Reseller
Order ID
Delivered amount
Commission rule
Commission earned
Adjustment/deduction
Payable balance
Payout status
Audit link
```

## Primary Actions
- Review reseller order
- Approve/reject reseller payout
- Review commission calculation
- Apply failed delivery policy
- Adjust commission with approval
- View reseller ledger
- Export reseller statement
- Open related courier/order
- Add internal note
- Suspend reseller with approval

## Business Rules to Enforce in UI
- Reseller commission posts only after delivered status.
- Returned/cancelled order must not create commission.
- Failed delivery deduction must follow policy and audit log.
- Payout requires CFO/admin approval.
- Reseller cannot access core business finance.
- Ledger adjustment requires approval and reason.
- Every payout and commission change must be audit logged.

## Drawers / Modals / Context Panels
- Reseller profile drawer
- Reseller order detail drawer
- Commission calculation drawer
- Payout approval drawer
- Failed delivery deduction drawer
- Audit timeline drawer
- Confirmation modal for payout, suspension, and adjustment
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for reseller and payout states:

```text
active
suspended
order-placed
dispatched
delivered
returned
cancelled
commission-pending
commission-posted
payout-requested
payout-approved
payout-paid
deduction-applied
ledger-mismatch
```

## Responsive Behavior
- Desktop: full reseller ledger, payout queue, right detail drawer, and audit stream.
- Tablet: reseller summary, payout queue, order review, detail drawer.
- Mobile: payout approvals, critical reseller alerts, and quick reseller order review only.

## Acceptance Criteria
- Reseller manager can review reseller orders and commission without opening finance panel for every item.
- CFO/admin can approve payout from the same panel.
- Delivered-only commission rule is visually obvious.
- Returned/cancelled orders never show as payable commission.
- Sensitive actions create approval request and audit log.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.

---

# 22. AI Control Panel — Enterprise Split — Master Prompt

## Route
`/ai-control`

## Primary Users
AI Supervisor, Admin, Owner, CTO, Department Managers

## Objective
Design a dedicated AI control dashboard for AI agent supervision, suggestion queue, approval workflow, guarded autopilot settings, agent mode control, confidence/risk visibility, knowledge update approval, and AI action audit logs.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be AI suggestion, guardrail, approval, and agent activity-first. Do not mix reseller financial payout workflow into this surface.

## Required KPI / Metric Cards
- Active AI agents
- AI suggestions pending
- AI actions waiting approval
- Guardrail blocks
- Low-confidence suggestions
- Human takeover requests
- Knowledge updates pending
- Autopilot actions today
- Rejected AI actions
- AI audit warnings

## Required Main Sections
- AI agent status grid
- AI suggestion queue
- Approval-required AI action list
- Guardrail and risk monitor
- Agent mode control panel
- Human takeover queue
- Knowledge update approval panel
- AI action audit log
- Cloud AI usage/cost indicator
- Department-wise AI activity summary

## Main Table / Queue / Kanban Requirements
AI suggestion table columns:

```text
Suggestion ID
Agent
Department
Suggested action
Confidence
Risk level
Guardrail matched
Human approval required
Created time
Approval status
Next action
```

Agent activity table columns:

```text
Agent
Mode
Status
Last action
Success/failure
Cloud AI used
Cost indicator
Guardrail event
Last human approval
Next action
```

## Primary Actions
- Approve/reject AI suggestion
- Request revision
- Assign human takeover
- Change AI mode
- Enable/disable guarded autopilot
- View guardrail reason
- Approve knowledge update
- Reject unsafe suggestion
- Open AI action log
- Disable agent temporarily
- Export AI audit report

## AI Modes
Design visible controls for these modes:

```text
Observe = report only
Approval = draft/suggestion, admin approves
Handover = works when staff is absent
Guarded Autopilot = executes low-risk actions within strict rules
```

## Business Rules to Enforce in UI
- AI cannot perform sensitive actions without approval.
- AI mode change is sensitive and must be logged.
- Guarded autopilot must be limited to low-risk actions.
- Finance, refund, payout, price change, blacklist, ad budget, bulk campaign and knowledge mutation require approval.
- Customer-facing AI cannot access finance, secrets, or unrestricted ERP tools.
- Every AI suggestion/action must show confidence, reason, guardrail, and approval status.
- Knowledge update requires manager/admin approval.

## Drawers / Modals / Context Panels
- AI suggestion detail drawer
- Guardrail explanation drawer
- AI action audit drawer
- Agent settings drawer
- Knowledge suggestion review drawer
- Human takeover drawer
- Confirmation modal for mode change/autopilot enable/agent disable
- Permission denied state for unauthorized users

## Status Badge System
Use AI-specific badges:

```text
observe
approval-mode
handover
guarded-autopilot
pending-approval
approved
rejected
blocked-by-guardrail
low-confidence
human-takeover
knowledge-pending
unsafe
```

## Responsive Behavior
- Desktop: full suggestion queue, agent grid, guardrail monitor, and audit log.
- Tablet: approval queue, agent status, guardrail alerts, detail drawer.
- Mobile: urgent AI approvals, human takeover alerts, unsafe action warnings only.

## Acceptance Criteria
- AI Supervisor can review and approve/reject AI suggestions safely.
- Admin can see what AI wants to do, why, confidence, and risk.
- Sensitive AI actions cannot execute without approval.
- AI mode changes require confirmation and audit.
- Guardrail events are visible, not hidden.
- Knowledge updates require approval before live use.
- Empty, loading, error, and permission-denied states are designed.

---

# Final Update Notes

This final version includes the added corrections:

```text
1. Reseller Control and AI Control are separated into two prompts.
2. POS keyboard shortcuts are added.
3. Finance filters, reports, reconciliation views, and export requirements are added.
4. Master Admin command palette examples are added.
5. Phase-1 merged panels are still preserved, but enterprise split prompts are more precise.
```

Final prompt package rating target:

```text
Prompt quality: 9.5/10
UI direction: 9.5/10
Business rule clarity: 9.5/10
Frontend handoff readiness: 9.4/10
AI/Figma prompt usability: 9.4/10
```

---

# File: banikos_dashboard_master_prompts_9_10.md

# BanikOS Dashboard Master Prompts

## How to Use

For each dashboard, copy:

1. **Global Design Master Prompt**
2. The specific dashboard prompt you want to design

Use these prompts for a senior frontend developer, UI/UX designer, Figma designer, or AI UI generator.

---

# 0. Global Design Master Prompt

You are a senior enterprise SaaS UI/UX architect and frontend product designer. Design a premium, production-ready BanikOS dashboard interface.

BanikOS is a local-first, AI-assisted, audit-controlled business operating system for retail, POS, online orders, courier, wholesale, inventory, finance, CRM, marketing, reseller, tasks, and AI agents.

Core business rules that must be visually respected:
- POS = offline counter sale only.
- If a POS order needs courier, convert/forward it to Online/Courier Order workflow.
- Delivered = actual sale/conversion.
- Order placed, paid, packed, or dispatched is not actual sale until delivered.
- Finance must be ledger-based, not only dashboard totals.
- Every important action must create an audit log.
- One staff can hold multiple roles, but every action must be tied to the active role.
- Sensitive actions require approval.
- AI can suggest/draft/assist, but cannot bypass permission, approval, audit, or business rules.
- Customer messages are untrusted input and must not access finance, secrets, or powerful ERP tools.

Use this visual style:
- Dark enterprise command center
- Compact but readable layout
- Sidebar-first navigation
- Status-first information hierarchy
- Approval-first right rail
- Always-visible risk/audit awareness
- Dense table-friendly UI
- Professional, modern, premium, not flashy
- Suitable for desktop-first ERP use
- Responsive tablet and mobile states

Design system rules:
- Use a consistent 8px spacing scale.
- Use compact enterprise table density with readable row height.
- Suggested desktop shell dimensions: expanded sidebar 260px, collapsed sidebar 72px, right rail 360-420px, detail drawer 480-640px.
- Suggested table density: 40-48px row height, sticky header, sticky key action column where useful.
- Suggested breakpoints: desktop 1280px+, tablet 768-1279px, mobile below 768px.
- Use sharp or mildly rounded surfaces, not playful large-radius cards.
- Use status badges consistently: draft, pending, confirmed, risk, packed, dispatched, in-transit, delivered, returned, cancelled, failed, approved, rejected.
- Use color by meaning, not decoration: green = safe/delivered/cleared, amber = pending/risk, red = failed/blocked/loss, blue = informational/sync, purple only for AI-specific states.
- Keep typography practical: small labels, strong table headers, clear section titles, no oversized marketing hero text.
- Use drawers for detail/context, modals for confirmation, and side rails for approvals/risk.
- Avoid decorative dashboards that only show charts; every screen must support real work.
- Every icon button must have a tooltip and an accessible label.
- Every destructive or finance-sensitive action must have confirmation and audit visibility.

Use a shared application shell:
- Left sidebar: role-based modules
- Top bar: global search, command palette, active role switcher, sync status, AI mode, notification, emergency lock, user profile
- Main canvas: dashboard/page content
- Right rail: approvals, risks, AI alerts, selected item context
- Audit stream: visible where relevant

Device role rules:
- Desktop = full operation, data entry, finance, inventory, reporting, reconciliation.
- Tablet = manager review, approvals, queue review, packing/delivery supervision.
- Mobile = alerts, approvals, task update, courier status, quick reply, critical summaries only.
- Do not force complex finance, inventory audit, or full report building into mobile.

Route and merge rules:
- Use `/control-center` for the Phase-1 merged Task/Reseller/AI panel.
- Do not use `/control` because it is too generic.
- Use `/reseller-control` and `/ai-control` as separate enterprise split routes.
- Marketing/Omnichannel is merged for Phase-1 only; enterprise version must split it.
- Task/Reseller/AI is merged for Phase-1 only; enterprise version must split it.

Every dashboard must include:
- Page header with title, status, primary actions
- Metric strip with key KPIs
- Main work area: table, queue, kanban, form, or chart depending on module
- Right context panel for selected item details
- Approval/risk section
- Audit timeline or latest activity
- Search, filter, sort
- Loading, empty, error, permission-denied states
- Desktop/tablet/mobile behavior
- Clear route name
- Clear role access

Output format required:

```text
1. Layout Summary
2. Route and Primary Roles
3. Desktop Wireframe Description
4. Tablet Behavior
5. Mobile Behavior
6. KPI Cards
7. Main Work Area Structure
8. Table / Queue / Kanban Columns
9. Primary Actions
10. Drawers, Modals, and Side Rails
11. Status Badge System
12. Empty / Loading / Error / Permission Denied States
13. Permission and Approval Behavior
14. Audit Log Touchpoints
15. Component List for Frontend Implementation
16. Developer Notes
17. Suggested Test Touchpoints
```

Suggested Test Touchpoints must mention:

```text
Unit-level validation for business rules shown on the screen
Integration flow that connects this screen to stock/finance/order/audit
E2E user journey for the primary workflow
Security/permission test for sensitive actions
```

Quality guardrails:
- Do not produce the same generic layout for every module.
- Make the core workflow of each module visually dominant.
- POS must be cart-first and scan-first.
- Finance must be ledger-first.
- Omnichannel must be conversation-first.
- Packaging must be scan/checklist-first.
- Courier must be tracking/COD-first.
- Admin must be risk/approval-first.
- Marketing must be campaign/event-health-first.
- Task manager must be ownership/SLA-first.
- AI Control must be approval/guardrail-first.

Dashboard-specific layout patterns:

```text
Admin = command grid + approval/risk rail + live audit stream
Executive = tabbed C-level overview + drill-down risk lists
POS = barcode/search + cart + payment + shift drawer
Orders = status pipeline + order table + customer context
Courier Orders = booking queue + tracking table + COD reconciliation
Inventory = stock table + location view + movement history
Vendor Purchase = purchase invoice flow + receive items + vendor ledger
Wholesale = bulk order table + manual pricing + receivable ledger
Finance = journal table + account ledger + reconciliation panels
CRM/Sales = lead board + customer timeline + follow-up queue
Telesales = call queue + script panel + callback scheduler
Packaging = pick list + scan/check confirmation + handover queue
Delivery/Courier = dispatch queue + status updates + claim tracking
Marketing/Omnichannel Phase-1 = campaign/event health tabs + inbox tab
Control Center Phase-1 = task tab + reseller tab + AI approval tab
COD Risk = risk queue + risk reason breakdown + override approval
Marketing Enterprise = campaign table + content calendar + event health
Inbox Enterprise = three-column inbox + thread + customer/order context
Task Enterprise = task board + internal inbox + SLA/escalation queue
Website Enterprise = publish list + sync queue + landing/page manager
Reseller Control = reseller ledger + commission + payout approval
AI Control = suggestion queue + guardrail status + agent activity log
```

---

# 1. Master Admin Control Panel — Master Prompt

## Route
`/admin`

## Primary Users
Owner, Admin

## Objective
Design the main command center of BanikOS where the owner/admin can monitor and control the whole business, approvals, risks, AI alerts, sync health, and department status from one screen.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Net profit today/month
- Delivered sales
- Pending orders
- Cash/bank/mobile balance
- Courier COD receivable
- Vendor payable
- Wholesale receivable
- Inventory value
- Low stock count
- Pending approvals
- AI alerts
- Sync health
- Courier risk count

## Required Main Sections
- Business health strip
- Master command shortcut panel
- Department/module health grid
- Right approval/risk rail
- AI alert panel
- Sync and system health widget
- Live audit stream
- Emergency lock section

## Main Table / Queue / Kanban Requirements
Module health cards instead of one large table. Each card must show module status, pending count, risk count, key metric, next action, and open module button.

## Primary Actions
- Approve/reject sensitive requests
- Jump to any module
- Trigger emergency lock
- Open audit log
- Review AI alerts
- Review sync/API failure
- Start AI handover
- Open approval queue

## Business Rules to Enforce in UI
- Admin must see all critical risks.
- Delivered-only sales must be separated from pending/placed orders.
- Emergency lock must require confirmation.
- Every admin action must be audit logged.
- AI cannot execute sensitive action without approval.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 2. C-Level Executive Dashboard — Master Prompt

## Route
`/executive`

## Primary Users
Owner, CEO, CFO, COO, CMO, CTO, Admin

## Objective
Design one executive dashboard with tabs for CEO, CFO, COO, CMO, and CTO so C-level users can see business, finance, operations, marketing, and system health from one place.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Business health score
- Net profit
- Delivered sales
- Cash position
- Payable/receivable
- Operational backlog
- Marketing ROAS
- System health
- Pending approvals
- Urgent risks

## Required Main Sections
- CEO Overview tab
- CFO Finance View tab
- COO Operations View tab
- CMO Marketing View tab
- CTO System View tab
- Cross-department risk summary
- Executive AI summary
- Approval queue

## Main Table / Queue / Kanban Requirements
Use tabbed executive cards and drill-down tables. Each tab should have its own KPI row, status cards, and top risks list.

## Primary Actions
- Switch C-level tabs
- Open related department panel
- Approve executive-level requests
- Export executive summary
- View AI executive insight
- Open risk details

## Business Rules to Enforce in UI
- One executive dashboard first; later tabs can become separate dashboards.
- Finance numbers must be ledger-based.
- Marketing purchase/conversion must be delivered-only.
- CTO tab must show sync/webhook/security failures.
- Sensitive approvals must be visible across tabs.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 3. POS Panel — Master Prompt

## Route
`/pos`

## Primary Users
POS Staff, Store Manager, Admin

## Objective
Design a fast offline counter sale POS panel. POS must remain simple and focused on in-store sales. If courier is needed, the order must be converted to courier/online workflow.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Current shift sales
- Cash drawer expected
- Completed POS sales
- Returns today
- Discounts today
- Items sold
- Cash shortage/excess
- Held carts

## Required Main Sections
- Barcode/search input
- Product grid/list
- Cart panel
- Payment panel
- Customer optional field
- Discount control
- Invoice print area
- Shift open/close
- EOD reconciliation
- POS-to-courier conversion button

## Main Table / Queue / Kanban Requirements
Cart-first layout. Product search and barcode input must be extremely prominent. Cart lines must include item, SKU, qty, price, discount, stock warning, remove action.

## Primary Actions
- Scan/search product
- Add/remove cart item
- Apply discount with permission
- Select payment method
- Split payment
- Print invoice
- Hold cart
- Complete sale
- Return/exchange
- Open/close shift
- EOD reconcile
- Send by Courier

## Business Rules to Enforce in UI
- POS = offline sale only.
- Send by Courier must convert to Online/Courier Order workflow.
- POS completed sale deducts stock and posts payment.
- Voided cart before completion has no stock/sale impact.
- High discount requires approval.
- EOD mismatch creates shortage/excess log.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.

Special required flow: Design a “Send by Courier” drawer requiring customer name, phone, address, courier/payment/COD info, risk preview, and confirmation that the POS sale is converted to Courier Order.


---

# 4. Order Management Panel — Master Prompt

## Route
`/orders`

## Primary Users
Sales/CRM Staff, Admin, COO

## Objective
Design the main order lifecycle panel for website, manual, social, phone, and non-POS orders. It must show order intent vs actual delivered sale clearly.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Total orders today
- Confirmed orders
- Payment pending
- Address incomplete
- Risk hold
- Packed
- Dispatched
- Delivered sales
- Cancelled/returned

## Required Main Sections
- Order pipeline status board
- Order list table
- Customer detail panel
- Payment/COD status
- Source tracking
- Risk score preview
- CRM linked notes
- Audit timeline

## Main Table / Queue / Kanban Requirements
Order table columns: order ID, customer, source, phone, amount, payment status, order status, risk score, assigned staff, created time, next action.

## Primary Actions
- Create manual order
- Confirm order
- Request advance
- Mark address incomplete
- Send to packing
- Cancel request
- Link to CRM
- View customer timeline
- Convert source/order status
- Add internal note

## Business Rules to Enforce in UI
- Order placed is not actual sale.
- Delivered is actual sale.
- Cancelled before delivery = no sale.
- Returned after delivery = reversal.
- Address incomplete orders cannot dispatch.
- Risk hold requires approval/override.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 5. Courier Order Panel — Master Prompt

## Route
`/courier-orders`

## Primary Users
Delivery Coordinator, COO, Admin

## Objective
Design a courier order dashboard for POS-to-courier converted orders and online courier orders, including dispatch, tracking, COD, return, lost parcel, and courier claim workflows.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Courier-ready orders
- Booked shipments
- In transit
- Delivered
- COD pending
- Returned
- Lost/claim
- Courier COD receivable
- Reconciliation mismatch

## Required Main Sections
- Courier booking queue
- Tracking table
- COD receivable widget
- Return/lost parcel queue
- Courier provider status
- Reconciliation status
- Right detail panel with customer/order/courier info

## Main Table / Queue / Kanban Requirements
Courier table columns: shipment ID, order ID, customer, courier provider, tracking code, COD amount, delivery status, reconciliation status, risk score, last update, next action.

## Primary Actions
- Book courier
- Print courier label
- Update tracking
- Mark dispatched
- Sync courier status
- Mark delivered/returned
- Open claim
- Upload courier sheet
- Reconcile COD
- Override with approval

## Business Rules to Enforce in UI
- Dispatched is not delivered.
- Delivered triggers actual sale/conversion.
- Returned must trigger verification.
- Courier payout must match tracking code.
- COD receivable must clear only after reconciliation.
- Duplicate webhook/status update must not duplicate posting.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 6. Inventory Panel — Master Prompt

## Route
`/inventory`

## Primary Users
Store Manager, Inventory Staff, Admin

## Objective
Design an inventory control panel for product catalog, SKU/barcode, stock by location, stock movement, low stock, damage, loss, stock audit, and negative stock prevention.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Total SKUs
- Inventory value
- Low stock count
- Out of stock
- Stock movement today
- Damage/loss count
- Pending stock adjustments
- Reserved stock

## Required Main Sections
- Product catalog table
- Stock by warehouse/location
- Low stock alerts
- Stock movement history
- Stock audit section
- Damage/loss/shrinkage section
- Stock adjustment requests

## Main Table / Queue / Kanban Requirements
Inventory table columns: SKU, product, variant, category, warehouse/location, available stock, reserved stock, cost, retail price, wholesale price, status, next action.

## Primary Actions
- Add/edit product
- Create variant
- Move stock
- Request stock adjustment
- Approve adjustment if permitted
- Start stock audit
- Mark damage/loss
- View movement history
- Generate barcode/SKU

## Business Rules to Enforce in UI
- Negative stock is blocked unless approved override exists.
- Stock adjustment requires permission and audit.
- Reserved stock must be separated from available stock.
- Inventory cost must feed finance/profit calculation.
- Stock audit discrepancy becomes shrinkage/loss.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 7. Vendor Purchase Panel — Master Prompt

## Route
`/purchases`

## Primary Users
Purchase Staff, CFO, Admin

## Objective
Design a vendor purchase dashboard for purchase invoice, product receive, cost entry, vendor payable, partial payment, vendor ledger, and due alerts.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Purchase invoices today
- Pending receiving
- Vendor payable
- Due today
- Partial payments
- Purchase value
- Items received
- Cost variance alerts

## Required Main Sections
- Vendor list
- Purchase invoice table
- Receive stock workflow
- Vendor ledger panel
- Due alert panel
- Payment request/approval section
- Cost entry form

## Main Table / Queue / Kanban Requirements
Purchase table columns: invoice no, vendor, item count, purchase value, received status, payable amount, paid amount, due date, approval status, next action.

## Primary Actions
- Create purchase invoice
- Receive products
- Add cost
- Record partial payment request
- Approve vendor payment
- View vendor ledger
- Set due date
- Export purchase report

## Business Rules to Enforce in UI
- Vendor payable updates after purchase invoice/receive.
- Product cost must connect to inventory valuation.
- Vendor payment is sensitive and needs approval.
- Partial payment must update vendor ledger.
- Every purchase/payment action must be audit logged.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 8. Wholesale Panel — Master Prompt

## Route
`/wholesale`

## Primary Users
Wholesale Manager, CFO, Admin

## Objective
Design a wholesale dashboard separate from retail, with wholesale customers, bulk order, manual price, invoice, partial payment, due/baki, receivable ledger, return, and profit report.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Wholesale sales
- Wholesale due
- Active wholesale customers
- Pending invoices
- Partial payments
- Wholesale profit
- Returned wholesale items
- Overdue receivables

## Required Main Sections
- Wholesale order creation
- Wholesale customer table
- Bulk item entry
- Manual price control
- Wholesale invoice list
- Receivable ledger
- Due/baki alert
- Wholesale return workflow

## Main Table / Queue / Kanban Requirements
Wholesale order table columns: invoice no, customer, item count, total amount, paid, due, payment status, delivery/status, profit estimate, next action.

## Primary Actions
- Create wholesale order
- Set manual wholesale price
- Apply price list
- Record partial payment
- View receivable ledger
- Create return
- Print wholesale invoice
- Export wholesale report

## Business Rules to Enforce in UI
- Retail and wholesale reports must not mix.
- Wholesale customer ledger is separate from retail customer ledger.
- Manual price override requires permission.
- Wholesale due must update receivable ledger.
- Delivered/fulfilled logic must impact profit correctly.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 9. Finance Panel — Master Prompt

## Route
`/finance`

## Primary Users
CFO, Owner, Admin

## Objective
Design a ledger-based finance panel showing cash, bank, mobile banking, payable, receivable, courier clearing, staff/reseller commission, expenses, profit/loss, vouchers, and audit-ready trail.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Cash balance
- Bank balance
- Mobile banking balance
- Vendor payable
- Customer receivable
- Wholesale receivable
- Courier clearing/COD receivable
- Net profit
- Expenses
- Pending approvals

## Required Main Sections
- Finance overview
- Chart of accounts summary
- Journal entry table
- Ledger view
- Payable/receivable panels
- Courier clearing panel
- Expense entry
- Voucher section
- Approval queue
- Audit-ready export

## Main Table / Queue / Kanban Requirements
Ledger table columns: date, journal no, account, debit, credit, entity, source module, status, approval, created by, audit link.

## Primary Actions
- Create voucher/journal request
- Approve finance adjustment
- View account ledger
- Export report
- Reconcile courier COD
- Record expense
- View payable/receivable
- Review commission payable

## Business Rules to Enforce in UI
- Finance must be ledger-based.
- Debit total must equal credit total.
- Order placed creates no sale revenue.
- Delivered creates sale revenue/COGS impact.
- Courier COD received clears courier receivable.
- Finance adjustment requires approval and audit.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 10. CRM/Sales Panel — Master Prompt

## Route
`/crm`

## Primary Users
Sales Staff, CRM Staff, Sales Manager

## Objective
Design a CRM/sales dashboard to manage leads, source tracking, customer timeline, follow-up, notes, objections, interest tags, upsell/cross-sell, and lead-to-order conversion.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- New leads
- Follow-ups due
- Hot leads
- Converted leads
- Lost leads
- Average response time
- Agent performance
- Source quality

## Required Main Sections
- Lead kanban board
- Lead table
- Customer timeline
- Follow-up scheduler
- Objection notes
- Sales notes
- Upsell/cross-sell suggestions
- Lead source analytics

## Main Table / Queue / Kanban Requirements
Lead table columns: lead name, phone, source, interest, stage, assigned agent, next follow-up, last contact, conversion probability, next action.

## Primary Actions
- Create lead
- Assign follow-up
- Add note
- Log objection
- Convert lead to order
- Mark lost with reason
- Schedule call
- View customer timeline

## Business Rules to Enforce in UI
- CRM notes must feed future sales learning.
- Lead source must be tracked.
- Follow-up should not be lost.
- Customer timeline must show orders, messages, calls, notes.
- Conversion to order must follow order workflow.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 11. Telesales Panel — Master Prompt

## Route
`/telesales`

## Primary Users
Telesales Staff, Sales Manager

## Objective
Design a telesales dashboard for call queue, callback schedule, call status, call script, objection note, customer history, conversion result, and daily performance.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Calls assigned today
- Calls completed
- Callbacks due
- Converted calls
- Failed calls
- No answer
- Average call duration
- Agent conversion rate

## Required Main Sections
- Call queue
- Callback calendar/list
- Call script panel
- Customer history panel
- Objection note area
- Conversion result panel
- Daily performance summary

## Main Table / Queue / Kanban Requirements
Call queue columns: customer/lead, phone, source, priority, last call, next callback, assigned agent, status, script, next action.

## Primary Actions
- Start call
- Log call outcome
- Schedule callback
- Add objection note
- Convert to order
- Mark not interested
- Assign to CRM
- View customer/order history

## Business Rules to Enforce in UI
- Every call outcome must be logged.
- Objection notes should feed learning/CRM.
- Conversion creates order but not actual sale until delivered.
- Staff performance should be measurable.
- Follow-up/callback cannot be lost.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 12. Packaging Panel — Master Prompt

## Route
`/packaging`

## Primary Users
Packaging Staff, COO

## Objective
Design a focused packaging dashboard where packaging staff only see assigned packing tasks, pick list, scan/check products, confirm pack, record packaging material usage, report damage/missing, and handover to courier/delivery.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Pending packing tasks
- Packed today
- Packing errors
- Missing items
- Damaged items
- Packaging material used
- Ready for dispatch
- SLA overdue tasks

## Required Main Sections
- Assigned task queue
- Pick list view
- Scan/check section
- Packaging material usage panel
- Damage/missing report form
- Handover confirmation
- Task audit timeline

## Main Table / Queue / Kanban Requirements
Task table columns: task ID, order ID, customer, items count, priority, SLA, assigned staff, packing status, courier required, next action.

## Primary Actions
- Start packing
- Scan product
- Confirm item checked
- Add packaging material
- Report damage/missing
- Complete packing
- Handover to delivery/courier
- Add internal note

## Business Rules to Enforce in UI
- Packaging staff should see assigned tasks only unless extra permission.
- Packed is not delivered.
- Damage/missing report must update operation and audit.
- Packaging material usage should feed cost/profit calculation.
- Product scan/check should reduce packing errors.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 13. Delivery/Courier Panel — Master Prompt

## Route
`/delivery`

## Primary Users
Delivery Staff, Courier Coordinator, COO

## Objective
Design a delivery/courier operations dashboard for dispatch queue, courier handover, tracking update, return update, lost parcel alert, claim tracking, and courier payment matching.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Pending dispatch
- Handover completed
- In transit
- Delivery failed
- Returned
- Lost/claim
- COD pending
- Payment mismatch

## Required Main Sections
- Dispatch queue
- Courier handover list
- Tracking update table
- Return/lost parcel queue
- Claim tracker
- Courier payment matching section
- Delivery staff task list

## Main Table / Queue / Kanban Requirements
Delivery table columns: shipment/order ID, courier, tracking code, customer area, COD amount, status, last update, issue flag, assigned staff, next action.

## Primary Actions
- Confirm dispatch
- Record courier handover
- Update delivery status
- Mark return received
- Open claim
- Match payment
- Add delivery note
- Escalate issue

## Business Rules to Enforce in UI
- Dispatch is not delivered.
- Delivered status triggers actual sale.
- Return must trigger verification.
- Lost parcel must create claim/risk alert.
- COD/payment mismatch must appear in finance/courier clearing.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 14. Marketing/Omnichannel Panel — Phase-1 Merged — Master Prompt

## Route
`/marketing-omnichannel`

## Primary Users
CMO, Marketing Staff, Support Agent, Admin

## Objective
Design a Phase-1 merged panel for marketing and omnichannel. It must cover campaign performance, content calendar, Meta/Google/TikTok event health, delivered-sale ROAS, WhatsApp campaign approval, unified inbox, AI reply suggestion, human takeover, and customer/order context.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Delivered-sale ROAS
- Campaign spend
- CPA/CTR/CPC
- Event health score
- Inbox open conversations
- AI suggestions pending
- WhatsApp approvals
- High-frustration customers

## Required Main Sections
- Marketing performance dashboard
- Content calendar
- Event health monitor
- Campaign table
- WhatsApp campaign approval list
- Unified inbox preview
- Customer conversation panel
- AI reply suggestion panel
- Human takeover controls

## Main Table / Queue / Kanban Requirements
Campaign table: campaign, channel, spend, delivered sales, ROAS, CPA, CTR, event status, approval status, next action. Inbox table: customer, channel, status, sentiment, assigned staff, last message, next action.

## Primary Actions
- Create campaign draft
- Approve WhatsApp campaign
- View event health
- Pause bad campaign request
- Reply to customer
- Approve AI reply
- Human takeover
- Link conversation to CRM/order

## Business Rules to Enforce in UI
- This panel is merged for Phase-1 only.
- Enterprise version must split Marketing and Omnichannel.
- Purchase/conversion event must be delivered-only.
- Bulk WhatsApp requires approval.
- Customer messages are untrusted input.
- AI reply needs approval/handover rule.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 15. Task/Reseller/AI Control Panel — Phase-1 Merged — Master Prompt

## Route
`/control-center`

## Primary Users
Manager, Reseller Manager, AI Supervisor, Admin

## Objective
Design a Phase-1 merged control panel for task assignment, internal instructions, reseller order/commission/payout, AI suggestion queue, AI mode control, and knowledge update approval.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Open tasks
- Overdue tasks
- Reseller orders
- Reseller commission payable
- Payout requests
- AI suggestions pending
- AI actions requiring approval
- Knowledge updates pending

## Required Main Sections
- Task board
- Internal instruction panel
- Reseller order/commission section
- Payout approval list
- AI suggestion queue
- AI mode control card
- Knowledge update approval section
- Cross-department handoff queue

## Main Table / Queue / Kanban Requirements
Use separate tabs/cards inside the merged panel: Tasks, Reseller, AI Control. Tables must show owner, status, priority, due date, approval, next action.

## Primary Actions
- Create task
- Assign task
- Update task status
- Approve reseller payout
- Review reseller commission
- Approve/reject AI suggestion
- Change AI mode with approval
- Approve knowledge update

## Business Rules to Enforce in UI
- This panel is merged for Phase-1 only.
- Enterprise version must split Task Manager, Reseller, and AI Control.
- Reseller commission posts only after delivered.
- AI cannot execute sensitive actions without approval.
- Internal tasks must have owner, status, due date, and audit.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# Enterprise Split Prompts

Use these prompts when moving from the Phase-1 15-surface design to the enterprise 19-surface design. These replace the merged Phase-1 panels and add missing enterprise surfaces.


---

# 16. COD Risk Panel — Enterprise Split — Master Prompt

## Route
`/cod-risk`

## Primary Users
COO, Admin, Delivery Coordinator, Sales Manager

## Objective
Design a dedicated COD risk dashboard to identify fake orders, risky numbers, incomplete addresses, repeat returns, suspicious geography, active transit conflicts, and advance requirement before dispatch.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- High-risk orders
- Address incomplete
- Repeat return customers
- Blacklisted customers
- Active transit conflicts
- Advance required
- Risk overrides pending
- COD loss trend

## Required Main Sections
- Risk scoring queue
- Address quality panel
- Blacklist/watchlist table
- Geographical risk map/list
- Advance trigger list
- Override approval queue
- Risk reason breakdown

## Main Table / Queue / Kanban Requirements
Risk table columns: order ID, customer, phone, area, amount, risk score, risk reasons, previous returns, active transit, recommended action, approval status.

## Primary Actions
- Hold order
- Require advance
- Request full address
- Blacklist request
- Approve risk override
- Release to packing
- Add risk note
- View customer history

## Business Rules to Enforce in UI
- High-risk order cannot dispatch without approval/override.
- Risk score must be visible before dispatch.
- Blacklist is sensitive and requires approval.
- Risk override must require reason and audit.
- COD risk decisions must feed order and courier workflow.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 17. Marketing/CMO Panel — Enterprise Split — Master Prompt

## Route
`/marketing`

## Primary Users
CMO, Marketing Staff, Owner

## Objective
Design a dedicated marketing dashboard for content calendar, campaign planning, paid ads, Meta/Google/TikTok event health, delivered-sale ROAS, WhatsApp campaign approval, landing page performance, and marketing tasks.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Delivered-sale ROAS
- Ad spend
- CPA
- CTR
- CPC
- Event health score
- Landing page conversion
- Campaign approvals pending
- Content scheduled

## Required Main Sections
- Campaign performance overview
- Content calendar
- Paid ads table
- Event health monitor
- Landing page performance
- WhatsApp campaign approval
- Marketing task board
- AI content suggestion panel

## Main Table / Queue / Kanban Requirements
Campaign table columns: campaign, platform, spend, impressions, CTR, CPC, orders placed, delivered sales, ROAS, event status, approval, next action.

## Primary Actions
- Create campaign draft
- Schedule content
- Review AI content
- Request budget increase
- Approve WhatsApp campaign
- Pause bad ad request
- Open landing page report
- Export marketing report

## Business Rules to Enforce in UI
- Purchase/conversion must be delivered-only.
- Bulk WhatsApp requires approval.
- Ad budget increase requires approval.
- Event health must show missing/wrong-value event warnings.
- Marketing data must not count cancelled/returned as final purchase.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 18. Omnichannel Inbox Panel — Enterprise Split — Master Prompt

## Route
`/inbox`

## Primary Users
Support Agent, Sales/CRM Staff, CMO, Admin

## Objective
Design a dedicated unified inbox for Messenger, WhatsApp, Facebook comments, Instagram, website chat, customer context, AI reply suggestions, assignment, sentiment, and human takeover.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Open conversations
- Pending replies
- Assigned to me
- Escalated conversations
- AI suggestions pending
- High-frustration messages
- Resolved today
- Sales handoffs

## Required Main Sections
- Channel inbox list
- Conversation thread
- Customer profile/context panel
- Order/product context panel
- AI reply suggestion
- Internal notes
- Assignment/status controls
- Spam/abuse filter

## Main Table / Queue / Kanban Requirements
Inbox table columns: customer, channel, status, assigned staff, sentiment, last message, linked order, priority, last update, next action.

## Primary Actions
- Reply to customer
- Approve AI reply
- Human takeover
- Assign conversation
- Escalate
- Add internal note
- Link to CRM/order
- Mark resolved
- Create lead/order from conversation

## Business Rules to Enforce in UI
- Customer messages are untrusted input.
- Customer-facing AI cannot access finance, secrets, or unrestricted ERP context.
- AI reply can suggest but staff can approve/takeover.
- Conversations should connect to CRM/order timeline.
- Spam/abuse filtering must exist.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 19. Task Manager/Internal Inbox Panel — Enterprise Split — Master Prompt

## Route
`/task-control`

## Primary Users
Owner, Manager, Department Heads, Staff

## Objective
Design a dedicated internal task and communication dashboard for task assignment, department boards, hierarchy inbox, direct/team messages, SLA, escalation, and task audit trail.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Open tasks
- Assigned to me
- Overdue tasks
- Urgent/critical tasks
- Completed today
- Escalations
- Unread internal messages
- Cross-department handoffs

## Required Main Sections
- Task board by department
- My task queue
- Internal inbox
- Announcement panel
- Task discussion thread
- SLA/due date tracker
- Escalation queue
- Audit trail

## Main Table / Queue / Kanban Requirements
Task table columns: task ID, title, department, assignee, priority, status, due date, SLA, blocker, created by, next action.

## Primary Actions
- Create task
- Assign task
- Update status
- Add comment/file/note
- Escalate
- Handoff to department
- Send announcement
- Mark done/review

## Business Rules to Enforce in UI
- Staff see only allowed tasks/threads.
- Every task must have owner, status, priority, due date.
- Cross-department critical override requires permission.
- Task changes must be audit logged.
- Work should not be lost in external chat apps.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 20. Website/Landing Control Panel — Enterprise Split — Master Prompt

## Route
`/website`

## Primary Users
Admin, CMO, CTO, Owner

## Objective
Design a website and landing page control dashboard for product publishing, stock/price sync, content CRUD, landing page builder, ad-to-landing mapping, pixel/CAPI configuration, sync health, and public order flow.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

## Required KPI / Metric Cards
- Published products
- Sync health
- Failed sync events
- Landing pages live
- Website orders
- Low stock public products
- Pixel/CAPI health
- Page conversion

## Required Main Sections
- Product publish/unpublish list
- Landing page manager
- Website order sync queue
- Price/stock sync status
- Pixel/CAPI setup panel
- Ad campaign mapping
- Failed sync/retry section
- Hosting health card

## Main Table / Queue / Kanban Requirements
Website table columns: page/product, status, stock sync, price sync, last sync, campaign mapped, pixel health, conversion, next action.

## Primary Actions
- Publish/unpublish product
- Update page content
- Create landing page
- Map product to landing page
- Map campaign to landing page
- Configure pixel/CAPI
- Retry failed sync
- Review website order

## Business Rules to Enforce in UI
- Hosting cannot directly access local database.
- Local core is source of truth for product, stock, price, finance.
- Website order creates order intent, not actual sale.
- Sync failure must be visible.
- Conflict requires admin review, not silent overwrite.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.




---

# 21. Reseller Control + AI Control Panels — Enterprise Split — Master Prompt

## Routes
`/reseller-control`

`/ai-control`

## Primary Users
Reseller Manager, AI Supervisor, CFO, Admin

## Objective
Design two dedicated enterprise control surfaces: one for reseller orders/commission/payout and one for AI agent supervision. If the implementation still needs one screen temporarily, use two clear tabs, but keep the routes and responsibilities separate in the design.

## Design Instruction
Use the Global Design Master Prompt. Create a premium dark enterprise command-center dashboard for this module. The screen must be practical for real business operation, not just decorative.

Layout rule: `/reseller-control` must be reseller ledger and payout-first. `/ai-control` must be AI suggestion, guardrail, approval, and agent log-first. Do not merge reseller financial payout decisions with AI mode controls in the same primary table.

## Required KPI / Metric Cards
- Reseller orders
- Delivered reseller orders
- Commission payable
- Payout requests
- Failed deliveries
- AI suggestions pending
- AI actions waiting approval
- AI mode status
- Knowledge updates pending

## Required Main Sections
- Reseller catalog/order review
- Reseller commission ledger
- Payout approval queue
- Failed delivery deduction panel
- AI suggestion queue
- AI mode control
- Agent activity log
- Knowledge approval panel

## Main Table / Queue / Kanban Requirements
Reseller table columns: reseller, order ID, status, delivered value, commission, payout status, failed charge, next action. AI table columns: agent, suggestion, confidence, risk, approval status, action type, next action.

## Primary Actions
- Approve/reject payout
- Review commission
- Apply failed delivery policy
- Approve/reject AI suggestion
- Change AI mode
- Review agent log
- Approve knowledge update
- Disable guarded autopilot

## Business Rules to Enforce in UI
- Reseller commission posts only after delivered.
- Payout requires CFO/admin approval.
- AI cannot perform sensitive actions without approval.
- AI mode change is sensitive and must be logged.
- Knowledge update requires manager/admin approval.

## Drawers / Modals / Context Panels
- Detail drawer for selected row/item
- Approval drawer for sensitive actions
- Audit timeline drawer
- Notes/internal comments drawer where relevant
- Confirmation modal for risky actions
- Permission denied state for unauthorized users

## Status Badge System
Use clear status badges for all workflow states. Badges must visually separate safe, warning, danger, pending, approved, rejected, delivered, returned, and failed states.

## Responsive Behavior
- Desktop: full dashboard with sidebar, right rail, data table, and audit stream.
- Tablet: compressed sidebar, priority metrics, right context as drawer.
- Mobile: alerts, approvals, selected queue actions, and critical summaries only.

## Acceptance Criteria
- The dashboard can be used by the primary role without opening another module for normal work.
- Sensitive actions generate approval request.
- Every important action has audit visibility.
- Search/filter/sort exists.
- Empty, loading, error, and permission-denied states are designed.
- The design follows BanikOS rules and does not mix unrelated workflows.

---

# File: banikos_development_backlog.md

# BanikOS: Development Backlog & Remaining Tasks 📋

Status: Completed and synchronized with the BanikOS enterprise documentation set.

This document is now the completed implementation record for the BanikOS Enterprise Vision based on the master strategy guide. All listed modules are completed.

---

## 1. COD Risk Management & Logistics 🚚 (Phase 2)
*Focus: Reducing return rates and identifying risky orders before dispatch.*

- [x] **Active Transit Protection (ATP):** 
  - *Logic:* Auto-hold new orders if the customer has a previous order currently in transit (prevents duplicate fake orders).
- [x] **Smart Advance Trigger:** 
  - *Logic:* Identify high-value orders or high-risk geographic areas and automatically require courier charge in advance.
- [x] **Address Scoring Engine:** 
  - *Logic:* Detect incomplete addresses (e.g., just "Dhaka" or "Mirpur") and trigger an alert/SMS asking the customer for a full address.
- [x] **Geographical Risk Alerts:** 
  - *Logic:* Warn the admin if an order is placed from a known problematic delivery zone.
- [x] **Fake Order & Blacklist Engine:**
  - *Logic:* Auto-detect suspicious numbers or customers who previously returned 2+ COD orders, and block them or enforce full advance payment.

---

## 2. Real-Life Operations & Finance 🔄 (Phase 2 & 4)
*Focus: Handling day-to-day edge cases in retail and e-commerce.*

- [x] **Partial Return & Exchange Workflow:**
  - *Logic:* Seamless UI/backend logic to handle cases where a customer keeps 2 items, returns 1, and exchanges 1 for a different size. Automatically updates invoices and inventory without manual journal entries.
- [x] **Courier Payment Reconciliation (Clearing Account):**
  - *Logic:* Uploading Steadfast/Pathao payment sheets to auto-match which parcel's cash was received and auto-deduct the courier charges.
- [x] **Vendor Ledger & Baki (Credit) Management:**
  - *Logic:* Track partial wholesale payments and due dates. Auto-alert when it's time to pay the supplier.
- [x] **End-of-Day (EOD) Drawer Reconciliation:**
  - *Logic:* Staff must input physical cash in the drawer at closing time. If it doesn't match the system's "Cash" account, it logs a "Cash Shortage" (Staff Fraud Prevention).
- [x] **Dynamic QR Payment Integration:**
  - *Logic:* Generate automated bKash/Nagad QR codes on the POS/Invoice matching the exact due amount to prevent typing errors by customers.
- [x] **Staff Commission System:**
  - *Logic:* Calculate and credit commission to sales staff automatically when an order status changes to "Delivered".

---

## 3. Loss Management & Analytics 📉 (Phase 4)
*Focus: Identifying leaks in revenue and inventory.*

- [x] **Moving Average Cost (MAC) / FIFO Calculation:**
  - *Logic:* Accurately calculate profit even if the wholesale buying price of a product fluctuates over time.
- [x] **Hidden Costs (Packaging BOM):**
  - *Logic:* Automatically deduct the cost of polybags, premium boxes, and tape when an order is packed, to show true net margin.
- [x] **Transit Damage Tracking:**
  - *Logic:* Specific workflow to mark items as damaged in transit, updating the loss account without affecting regular COGS.
- [x] **Return Reason Analytics:**
  - *Logic:* Dashboard panel visualizing *why* items are returned (e.g., Size Issue, Late Delivery) to improve product quality.
- [x] **Inventory Shrinkage (Stock Audit):**
  - *Logic:* Module to perform physical stock counts and automatically adjust system stock, logging the discrepancy as shrinkage loss.

---

## 4. Advanced AI & Workflow Automation 🤖 (Phase 3 & 4)
*Focus: Complete automation and state-of-the-art AI integration.*

- [x] **Multimodal AI (Image/Voice Processing):**
  - *Logic:* Allow the Omnichannel Support Agent to read payment screenshots sent by customers and verify amounts, or transcribe voice notes into text.
- [x] **Sentiment Analysis Alerts:**
  - *Logic:* AI reads incoming messages/leads. If a customer is highly frustrated, it bypasses the bot and sends an urgent notification to a human manager.
- [x] **Loyalty & Retention Engine:**
  - *Logic:* Automatically award "Loyalty Points" per purchase. Customers can redeem points for discounts.
- [x] **Rule-Based Workflow Engine (IFTTT):**
  - *Logic:* A generic UI where admins can set rules: *IF [Event] THEN [Action]*. (e.g., IF order='Shipped' THEN Send_WhatsApp_Message).
- [x] **Cart Reservation Engine (Anti-Overselling):**
  - *Logic:* If a customer adds the last item to their online cart, or a POS staff opens it, lock the stock for 15 minutes to prevent double-selling.

---

## ✅ Mission Accomplished
All core enterprise features for BanikOS have been implemented. The system is now a robust, data-driven, and AI-powered ERP platform ready for enterprise-scale operations.

---

# File: banikos_enterprise_backbone_docs.md

# BanikOS: The Technical Backbone for Data-Driven Applications

This document serves as the comprehensive technical guide for using BanikOS as a headless ERP/Backbone to power a data-driven public website or e-commerce storefront.

---

## 1. High-Level Architecture (The Backbone Concept)

BanikOS is designed as a **Headless ERP**. This means the backend (FastAPI) manages all the complex data logic, while any frontend (Svelte Dashboard, Next.js Storefront, or Mobile App) can consume its data via secure REST APIs.

### The Ecosystem Flow
1.  **Data Source (BanikOS):** Centralized repository for Products, Inventory, Customers, and Finances.
2.  **API Layer:** Secure endpoints for external consumption.
3.  **Data-Driven Website (Frontend):** A fast, SEO-optimized website that pulls real-time data from the Backbone.
4.  **Action Layer:** When a customer orders on the website, it hits the Backbone's OMS (Order Management System).

---

## 2. API Reference (Backbone Consumption)

To build a data-driven website, the following API modules are utilized:

### A. Product & Inventory (The Catalog)
- **Endpoint:** `/api/inventory/products`
- **Utility:** Fetch product list, pricing, images, and stock availability.
- **Data-Driven Feature:** The website automatically hides products that are out of stock in the ERP or updates prices in real-time during sales.

### B. Order Management (The Checkout)
- **Endpoint:** `/api/oms/orders`
- **Utility:** Submit customer orders directly into the ERP.
- **Backbone Logic:** The ERP automatically handles VAT, shipping calculations, and inventory deduction upon order receipt.

### C. CRM & Customer Identity
- **Endpoint:** `/api/crm/leads`
- **Utility:** Sync website signups and inquiries.
- **Data-Driven Feature:** Customer behavior on the website (e.g., viewing a specific category) is logged in the ERP for targeted marketing.

---

## 3. Social Media Automation (Omnichannel Layer)

The recently added **Facebook Comment-to-DM** system acts as an entry point for customers into the data-driven ecosystem.

### Workflow:
1.  **Trigger:** User comments on a Facebook post.
2.  **Backbone Action:** `facebook_router.py` detects the comment and matches it with a `SocialAutomationRule`.
3.  **Response:** An automated DM is sent containing a **Direct Link** to the data-driven website.
4.  **Tracking:** The Backbone tracks how many DMs were sent and how many converted into sales on the website.

---

## 4. Website Implementation Strategy

For a high-performance, data-driven website, we recommend the following stack:

| Component | Technology | Why? |
| :--- | :--- | :--- |
| **Framework** | Next.js (React) | Excellent SEO and Server-Side Rendering (SSR) for product pages. |
| **Styling** | Tailwind CSS | Rapid UI development with premium aesthetics. |
| **State Management** | React Query / SWR | Efficiently caching data from the BanikOS Backbone. |
| **Deployment** | Vercel / Docker | Seamless scaling and fast global delivery. |

---

## 5. Security & Multi-Tenancy

As a backbone for a SaaS platform, security is built-in:
- **API Key Scoping:** Public websites use a "Public Key" with restricted permissions (Read-only for products, Write-only for orders).
- **Tenant Isolation:** The Backbone ensures that a website for *Brand A* can never access data from *Brand B*.
- **Rate Limiting:** Protects the ERP from bot attacks on the public-facing storefront.

---

## 6. Future Roadmap: The Data Intelligence Layer

- **Dynamic Pricing Engine:** Change website prices based on stock levels or time of day (managed by BanikOS).
- **Personalized Storefront:** The website layout changes based on the customer's previous order history stored in the Backbone.
- **Real-time Stock Alerts:** Notify website visitors when a product they viewed is "Low in Stock" (triggering FOMO).

---

> [!IMPORTANT]
> The BanikOS Backbone is the **Single Source of Truth (SSOT)**. No data should be duplicated; the website always reflects what is currently in the ERP.

---

# File: banikos_system_backbone_master_plan.md

# BanikOS System Backbone Master Plan

Status: Master planning document for consolidating the complete BanikOS business, AI, ERP, marketing, wholesale, retail, reseller, and operations architecture.

## 1. Core Vision

BanikOS is a local-first, AI-assisted business operating system for commerce businesses. It must run daily operations even when the owner is absent, while keeping every action controlled by roles, permissions, audit logs, business rules, and clean data.

The system is not only a POS, ERP, CRM, ad tool, or AI chatbot. It is the backbone where retail, wholesale, online orders, courier, finance, marketing, staff work, reseller sales, and AI agents operate from one trusted source of truth.

Core principle:

```text
Clean data first
Rules before AI
Delivered = actual sale
Every action = audit logged
Local core data = protected
Hosting platform = limited sync surface
```

## 2. Build Priority

Admin-end work must be completed first. Customer-facing websites, reseller panels, and AI autopilot should depend on a stable admin backbone.

Recommended order:

1. Role, permission, audit log, and admin shell.
2. Product, inventory, vendor, purchase, and stock truth.
3. Retail POS and order lifecycle.
4. Wholesale sales, pricing, accounts, and separate reporting.
5. CRM, sales, telesales, customer follow-up, and IP calling.
6. Task assignment, task manager, and internal hierarchy inbox.
7. Packaging, delivery, courier, return, and cancellation workflows.
8. Finance dashboard, ledgers, payable, receivable, reseller commission.
9. Omnichannel inbox and social automation.
10. Marketing dashboard, content calendar, Meta/Google/TikTok/WhatsApp integrations.
11. AI agents with approval mode.
12. Guarded AI autopilot.
13. Website, landing page, and reseller platform public expansion.

## 3. Core-Wise System Division

### Core 1: Admin & Governance Core

Purpose:
Control the full system from the admin side before exposing external workflows.

Must include:

- Tenant/business setup.
- Role-based access control.
- Multi-role staff assignment.
- Permission templates.
- Department dashboards.
- System-wide audit log.
- AI action log.
- Staff action log.
- Approval queue.
- Handover mode.
- Owner emergency override.
- Backup and restore controls.
- Local-to-hosting sync control.

Important rule:

One staff member may hold multiple roles, but each action must be logged with the active role used for that action.

### Core 2: Product, Inventory & Vendor Purchase Core

Purpose:
Maintain product, stock, purchase, supplier, and cost truth.

Must include:

- Product master catalog.
- SKU/barcode.
- Retail price.
- Wholesale price rules.
- Manual wholesale sell price support.
- Product images and descriptions.
- Stock by warehouse/location.
- Purchase from vendor.
- Vendor ledger.
- Purchase invoice.
- Partial vendor payment.
- Vendor due tracking.
- Buying cost, moving average cost, or FIFO.
- Damage/loss/shrinkage tracking.
- Packaging material BOM/cost.

Vendor purchase flow:

```text
Vendor selected
↓
Purchase invoice created
↓
Products received into stock
↓
Cost recorded
↓
Vendor payable updated
↓
Payment made partially or fully
↓
Ledger and audit log updated
```

### Core 3: Retail Commerce Core

Purpose:
Handle normal retail/POS/e-commerce sales.

Must include:

- POS sale.
- Website order.
- Facebook/WhatsApp/manual order.
- Customer profile.
- Discount.
- Payment method.
- COD support.
- Invoice.
- Retail stock deduction.
- Return/exchange.
- Partial return.
- Delivered-only sale confirmation.

Retail sale truth:

```text
Order placed = order intent
Paid = payment received
Delivered = actual sale
Cancelled = no sale
Returned = sale reversal
Partial return = adjusted sale value
```

### Core 4: Wholesale Commerce Core

Purpose:
Keep wholesale completely separate from retail in sales, pricing, reporting, customer management, and accounting.

Must include:

- Wholesale customer profile.
- Manual sell price per order.
- Wholesale price list.
- Bulk quantity order.
- Wholesale invoice.
- Wholesale due/baki.
- Partial payment.
- Wholesale receivable ledger.
- Wholesale return.
- Wholesale profit report.
- Separate wholesale dashboard.
- Separate wholesale stock impact report.

Wholesale and retail separation:

```text
Retail sales report != Wholesale sales report
Retail customer ledger != Wholesale customer ledger
Retail pricing != Wholesale pricing
Retail profit report != Wholesale profit report
```

Shared data:

- Product master.
- Inventory stock.
- Purchase cost.
- Vendor cost.

Separated data:

- Customer type.
- Invoice type.
- Pricing logic.
- Receivable ledger.
- Sales report.
- Profit report.
- Commission logic if needed.

Wholesale sale flow:

```text
Wholesale customer selected
↓
Products added in bulk
↓
Manual or rule-based wholesale price set
↓
Invoice created
↓
Payment full/partial/due
↓
Stock deducted
↓
Wholesale receivable updated
↓
Profit and audit log updated
```

### Core 5: CRM, Sales & Telesales Core

Purpose:
Manage leads, calls, follow-up, upsell, cross-sell, and staff notes.

Must include:

- CRM lead board.
- Website leads.
- Facebook/WhatsApp leads.
- IP calling from CRM.
- Call log.
- Follow-up schedule.
- Telesales queue.
- Sales script.
- Objection note.
- Upsell/cross-sell suggestion.
- Daily sales agent notes.
- Marketing insight notes.

Sales agent learning data:

- Customer objection.
- Successful reply.
- Failed reply.
- Product demand.
- Price sensitivity.
- Delivery concern.
- Competitor mention.
- Campaign/source quality.

These notes must feed the Learning Agent and CMO dashboard after filtering and approval.

### Core 6: Packaging, Delivery & Courier Core

Purpose:
Separate operational execution from sales and marketing.

Packaging panel:

- Assigned packing task only.
- Pick list.
- Scan product.
- Pack confirmation.
- Packaging material usage.
- Damage/missing report.
- Handover to delivery/courier.

Delivery/courier panel:

- Dispatch queue.
- Courier booking.
- Tracking code.
- Delivery status.
- Return status.
- Courier claim.
- Lost parcel alert.
- Fake return verification.
- Courier payment reconciliation.

Courier truth:

```text
Dispatched != Delivered
Returned must trigger verification
Delivered triggers actual sale/conversion
Courier payout must match tracking code
```

### Core 7: Finance & CFO Core

Purpose:
Provide corporate-level finance visibility for a finance graduate/CFO.

Must include:

- Cash flow.
- Profit and loss.
- Balance view.
- Vendor payable.
- Customer receivable.
- Wholesale receivable.
- Retail receivable if applicable.
- Courier receivable/clearing account.
- Reseller commission payable.
- Staff commission.
- Expense tracking.
- Packaging cost.
- Return loss.
- Damage loss.
- Inventory shrinkage.
- Tax/VAT-ready reporting where applicable.
- Audit-ready transaction trail.

CFO must be able to see:

- Which sales are delivered.
- Which money is collected.
- Which courier still holds COD money.
- Which vendor is owed money.
- Which reseller must be paid.
- Which staff earned commission.
- Which product is profitable after ad, courier, return, and packaging cost.

### Core 8: Marketing, CMO & Ads Core

Purpose:
Give the CMO a complete organic, paid, content, and campaign command center.

Must include:

- Content calendar.
- Post schedule.
- Post edit/delete/reschedule.
- AI content generation.
- Image/video/audio/script generation workflow.
- Organic campaign planning.
- Paid ad tracking.
- Meta Ads Manager integration.
- Google Ads, GA4, and GTM integration.
- TikTok Ads, TikTok Pixel, and Events API integration.
- Multi-platform event health monitor.
- Ad set/campaign suggestions.
- ROAS/CPA/CTR/CPC.
- Delivered-sale ROAS.
- Landing page performance.
- WhatsApp campaign center.
- Bulk message approval.
- Audience segment suggestions.
- Marketing task board.
- Social agent supervision.

Paid platform event rule:

```text
PageView = page viewed
ViewContent = product viewed
AddToCart = cart event
InitiateCheckout = checkout started
OrderPlaced/Lead = order submitted
Purchase = delivered only
CancelOrder = cancelled
ReturnOrder = returned
PartialReturn = adjusted value
```

Event health must be tracked for:

- Meta Pixel and Conversions API.
- Google Ads conversions.
- GA4 events.
- Google Tag Manager containers.
- TikTok Pixel.
- TikTok Events API.
- Event deduplication.
- Server-side event delivery.
- Missing event warnings.
- Wrong-value event warnings.
- Delivered-only purchase validation.

### Core 9: Omnichannel Platform & Customer Message Core

Purpose:
Provide a full omnichannel platform for Messenger, WhatsApp, Facebook comments, Instagram, website chat, and future channels. This core must safely centralize customer conversations, channel accounts, routing, AI handover, staff takeover, and conversation outcome tracking.

Must include:

- Channel account management.
- Facebook page connection.
- WhatsApp business number connection.
- Instagram account connection where applicable.
- Website live chat connection.
- Unified omnichannel inbox.
- Facebook comment-to-DM.
- WhatsApp Cloud API.
- Message routing rules.
- Conversation status: open, pending, assigned, resolved, escalated.
- Conversation assignment.
- Staff/team inbox permissions.
- AI reply suggestion.
- AI handover when staff absent.
- Human takeover.
- Internal notes.
- Customer timeline.
- Product/order context panel.
- Customer sentiment.
- Emotion detection.
- Page-wise personality.
- Conversation save.
- Message outcome tracking.
- Sales handoff to CRM.
- Marketing handoff to campaign/audience segments.
- Spam and abuse filtering.
- Prompt-injection sandboxing.

Important security rule:

Customer messages are untrusted input. They must never get direct access to core ERP tools, secrets, finance data, or unrestricted database context.

Why it exists:

The omnichannel platform is the front line of customer demand. It must allow staff and AI agents to reply from one place, but it must also protect the ERP core from unsafe customer input. It connects CMO marketing, COO sales operations, CRM follow-up, and AI learning without mixing unsafe chat data into finance, inventory, or admin control.

### Core 10: AI Agent Core

Purpose:
Use AI as department-wise assistant/manager, not as uncontrolled owner of business logic.

Recommended logical agents:

1. Orchestrator Agent.
2. Omnichannel/Customer Agent.
3. Marketing/Ads Agent.
4. Operations Agent.
5. Finance Control Agent.
6. Learning/Knowledge Agent.

Cost-saving deployment:

```text
Service 1: Orchestrator + Customer + Learning
Service 2: Operations + Marketing + Finance
```

Agent modes:

- Observe: report only.
- Approval: create suggestion/draft, wait for admin approval.
- Handover: work when staff is absent.
- Guarded autopilot: execute low-risk actions within limits.

AI must call powerful cloud AI only for:

- Complex ad strategy.
- Creative campaign planning.
- Deep business analysis.
- Difficult content generation.
- Long report reasoning.

Local/rule-based systems should handle:

- Routing.
- FAQ retrieval.
- Stock checks.
- Order status.
- Simple sentiment.
- Scheduled alerts.
- Guardrail checks.

### Core 11: Learning & Knowledge Core

Purpose:
Let agents improve from staff behavior and customer outcomes without corrupting live behavior.

Learning sources:

- Customer chats.
- Human reply corrections.
- Sales agent notes.
- Delivered orders.
- Cancelled orders.
- Returned orders.
- Successful campaigns.
- Failed campaigns.
- Customer objections.

Initial learning rule:

```text
AI creates learning suggestion
↓
Admin/manager approves
↓
FAQ/personality/template/rule updates
```

No unapproved live behavior mutation in the first stage.

### Core 12: Website, Landing Page & Hosting Core

Purpose:
Run public website and landing pages from BanikOS without exposing the local core.

Local-first model:

```text
Local BanikOS Core = main truth
Hosting Platform = public website and limited cache
Secure Sync Bridge = signed controlled communication
```

Website controls:

- Product publish/unpublish.
- Price update.
- Stock update.
- Content CRUD.
- Landing page builder.
- Niche-based landing templates.
- Custom design upload.
- Product-to-landing-page mapping.
- Landing page to ad campaign mapping.
- Pixel/CAPI configuration per page/brand.

Hosting must not have direct database access to local core. It should only communicate through signed events, scoped APIs, and sync queues.

### Core 13: Reseller Platform Core

Purpose:
Allow resellers to sell available products while delivery, stock, commission, and payout remain controlled by BanikOS.

Must include:

- Reseller login.
- Available product catalog.
- Reseller commission display.
- Reseller order submission.
- Delivery handled by the business.
- Courier tracking access with limited permission.
- Delivered order adds commission balance.
- Failed delivery deducts delivery charge according to policy.
- CFO payout approval.
- Reseller ledger.
- Reseller payout history.

Reseller flow:

```text
Reseller selects product
↓
Commission shown
↓
Reseller submits order
↓
Business packages and dispatches
↓
Delivered = commission added
↓
Returned/cancelled = no commission or delivery charge deduction
↓
CFO approves payout
```

### Core 14: Task Assignment, Manager & Internal Communication Core

Purpose:
Create a hierarchy-based internal work management and communication platform so teams can assign, track, discuss, approve, and complete work without relying on external chat apps.

Must include:

- Task assignment.
- Task manager dashboard.
- Department task boards.
- Staff task queue.
- Team-wise internal inbox.
- Role and hierarchy-based communication.
- Manager-to-team announcement.
- Direct staff message.
- Threaded task discussion.
- Task status: new, assigned, in progress, blocked, review, done.
- Priority: normal, urgent, critical.
- Due date and SLA.
- File/note attachment.
- Voice note or call note attachment where needed.
- Escalation to manager.
- Cross-department handoff.
- AI task suggestion.
- AI task summarization.
- Task audit trail.

Hierarchy rules:

```text
CEO/Admin can message and assign across all teams
Department heads can assign within their department
Managers can assign to their team members
Staff can update assigned tasks and reply inside allowed threads
Packaging staff only sees packaging tasks unless extra role is assigned
Delivery staff only sees delivery tasks unless extra role is assigned
```

Why it exists:

Operational work needs a controlled internal communication layer. Sales, packaging, delivery, finance, marketing, and support should not lose work inside informal chats. Every task, instruction, escalation, and completion must be tied to roles, permissions, and audit logs.

## 4. C-Level Dashboards

### CEO / Owner Dashboard

- Full business health.
- Sales, profit, cash, stock, courier, ad spend.
- Department bottlenecks.
- AI executive summary.
- Owner approval queue.
- Emergency override.
- Business running status when owner absent.

### CTO Dashboard

- System health.
- Error logs.
- Webhook failures.
- API failures.
- Sync failures.
- Agent failures.
- Security alerts.
- Suspicious action.
- Backup status.
- Performance bottlenecks.
- Backdoor/risk checklist.

### CFO Dashboard

- Corporate finance view.
- Ledger reports.
- Cash and bank.
- Vendor payable.
- Wholesale receivable.
- Courier clearing.
- Reseller commission payable.
- Staff commission.
- Profit/loss.
- Return/damage/shrinkage loss.
- Audit-ready export.

### CMO Dashboard

- Organic and paid marketing.
- Content calendar.
- AI content creation.
- Ad manager integration.
- Meta, Google, and TikTok event health.
- Campaign result.
- Delivered-sale ROAS.
- WhatsApp campaign.
- Social agent supervision.
- Marketing task and suggestion board.

### COO Dashboard

- Sales operations.
- CRM queue.
- Packaging queue.
- Delivery queue.
- Return/cancel queue.
- Task assignment and escalation.
- Internal team communication.
- Staff workload.
- Role merging controls.
- Operational bottleneck alerts.

## 5. Department Panels

- Admin Panel: all system setup and controls.
- Omnichannel Panel: inbox, replies, handover, sentiment.
- Sales/CRM Panel: leads, IP calls, follow-up, notes.
- Telesales Panel: call queue, callbacks, scripts.
- Packaging Panel: task-only packing workflow.
- Delivery/Courier Panel: dispatch, tracking, return, claims.
- Marketing Panel: content, ads, WhatsApp, campaigns.
- Finance Panel: ledgers, payments, approvals.
- Wholesale Panel: wholesale orders, due, manual pricing.
- Reseller Panel: catalog, order, commission, payout.
- Task Manager Panel: assignments, internal inbox, escalations, team communication.

## 6. Permission & Approval Rules

Low-risk actions AI/staff may perform with role permission:

- FAQ reply.
- Product availability reply.
- Order status reply.
- Follow-up reminder.
- Sentiment tag.
- Packing task update.
- Courier status check.
- Learning suggestion creation.
- Internal team message.
- Same-team task assignment within role permission.

Approval-required actions:

- Bulk WhatsApp campaign.
- Ad budget increase.
- New campaign publish.
- Product price change.
- Refund.
- Order cancel.
- Customer blacklist.
- Reseller payout.
- Vendor payment.
- High-value discount.
- Finance adjustment.
- Cross-department critical task override.

Guarded autopilot can be allowed for:

- Bad ad pause within rules.
- Low stock ad scaling stop.
- Suspicious order hold.
- After-hours customer reply.
- Follow-up scheduling.
- Lost parcel alert.

## 7. Audit Log Requirements

Every important action must record:

- Actor type: human, AI agent, system rule.
- Actor ID.
- Active role.
- Tenant/business.
- Action name.
- Data used.
- Before state.
- After state.
- Approval status.
- Reason.
- External API called.
- Timestamp.
- Result.

AI action logs must additionally record:

- Agent name.
- Agent mode.
- Confidence.
- Guardrail matched.
- Cloud AI used or not.
- Human approval required or not.

## 8. Security Backbone

Required controls:

- Local-first database protection.
- Hosting platform limited access.
- Signed sync events.
- Webhook signature verification.
- Tenant isolation.
- Role-based permissions.
- Session expiry.
- Safe uploads.
- Immutable audit logs.
- Customer message sandboxing.
- MCP/data gateway filtering.
- No direct tool access from customer-facing AI.
- Secrets never exposed to agents unless scoped and required.

## 9. Data Backbone

Single source of truth:

- Product master.
- Inventory.
- Vendor purchase.
- Retail sales.
- Wholesale sales.
- Orders.
- Delivery status.
- Payments.
- Returns.
- Customer history.
- Ad attribution.
- Platform event health.
- Task assignments.
- Internal communication threads.
- Staff actions.
- AI actions.
- Reseller commission.

Critical data rule:

Delivered order is the only actual sale/conversion. Cancelled, returned, and partial-return states must correct marketing, finance, commission, and profit reports.

## 10. Admin Control Centre UX Blueprint

Purpose:
The Admin Control Centre is the master command room for BanikOS. It is not a simple dashboard. It must expose business control, system control, AI governance, approvals, audit evidence, sync health, and emergency controls from one place.

Design direction:

- Dark enterprise command center.
- Compact, dense, and readable.
- Sidebar-first navigation.
- Status-first information hierarchy.
- Approval-first right rail.
- Audit stream always visible.
- Technical data should use monospaced typography.
- Emergency/risk states must be visually obvious.
- No marketing-style hero layout.

Recommended layout:

```text
Left Sidebar
  Core modules and system controls

Top Bar
  Global search, AI mode, sync status, notifications, emergency lock, admin profile

Main Canvas
  Business health, master command panel, module health cards, operational summaries

Right Rail
  Approval queue, AI alerts, urgent risks, handover requests

Bottom Stream
  Live audit log and system event feed
```

### 10.1 Left Sidebar Modules

Must include:

- Business.
- Staff.
- Roles & Permissions.
- AI Agents.
- Inventory.
- Vendor Purchase.
- Retail Sales.
- Wholesale.
- CRM.
- Omnichannel.
- Task Manager.
- Internal Inbox.
- Packaging.
- Delivery/Courier.
- Finance.
- Marketing.
- Ad Platform Events.
- Web & Landing Pages.
- Reseller.
- Sync Bridge.
- Security.
- Audit.
- Logs.
- Support.

Why it exists:
The sidebar is the admin's system map. A senior developer should treat every sidebar item as a real module route with its own permissions, states, and audit coverage.

### 10.2 Top Bar Controls

Must include:

- Global system search.
- Command palette.
- Emergency lock.
- Local core status.
- Hosting sync status.
- Active AI mode.
- Notification center.
- Internal inbox unread count.
- Current admin and active role.

Why it exists:
The admin must be able to search, stop, lock, sync, and inspect the system without leaving the current screen.

### 10.3 Business Health Strip

Must include:

- Net profit today.
- Delivered sales.
- Pending orders.
- Inventory value.
- Low stock count.
- Pending approvals.
- Active AI agents.
- Sync health.
- Courier risk count.
- Cash/COD receivable.

Why it exists:
The first row must answer: is the business healthy right now, and where is attention needed?

### 10.4 Master Command Panel

Must include quick actions:

- Add product.
- Create vendor purchase.
- Receive stock.
- Create retail order.
- Create wholesale order.
- Add customer/lead.
- Assign staff task.
- Send team announcement.
- Start AI handover.
- Publish/sync website.
- Create landing page.
- Launch WhatsApp campaign draft.
- Open approval queue.
- Run system sync.
- Emergency lock.

Why it exists:
The command panel is the admin's shortcut layer for high-frequency control actions. These actions must open real drawers/forms, not static buttons.

### 10.5 Module Health Grid

Must include module cards for:

- Retail sales.
- Wholesale sales.
- Inventory status.
- Vendor payable.
- CRM and leads.
- Omnichannel inbox.
- Task manager and internal inbox.
- Packaging queue.
- Delivery/courier queue.
- Finance status.
- Marketing performance.
- Ad platform event health.
- Website/landing page sync.
- Reseller orders and payout.

Each card should show:

- Current status.
- Pending count.
- Risk count.
- Key metric.
- Next action.
- Open module button.

Why it exists:
The admin should see department status at a glance and drill down only where needed.

### 10.6 Right Rail: Approval, AI & Risk

Must include:

- Approval queue.
- AI alerts.
- AI confidence and reason.
- Handover requests.
- Security overrides.
- Budget requests.
- Vendor payment requests.
- Reseller payout requests.
- Bulk campaign approval.
- Urgent risks.

Why it exists:
Risky decisions should not be buried inside department pages. The right rail keeps approval and danger visible at all times.

### 10.7 Live Audit Stream

Must include:

- Staff actions.
- AI actions.
- Rule engine actions.
- External API calls.
- Sync events.
- Failed actions.
- Security alerts.
- Finance-sensitive changes.

Why it exists:
Admin Control Centre must provide evidence, not only metrics. If something changes in the business, the admin should see who or what changed it.

### 10.8 Admin Control Centre Must Not Miss

The current reference design already covers the correct visual direction, but the full BanikOS admin redesign must also include:

- Wholesale as a first-class module, separate from retail.
- Vendor purchase and payable.
- Omnichannel platform, not only CRM.
- Task assignment and manager.
- Team-wise internal inbox with hierarchy-based communication.
- Packaging and delivery/courier panels.
- Local core and hosting sync bridge.
- Website and landing page control.
- Reseller platform control.
- Role/permission matrix.
- AI data access control.
- Delivered-only conversion truth.
- Meta, Google, and TikTok event health.
- Finance audit and payout approvals.

### 10.9 Developer Implementation Notes

- Build this as a real responsive admin surface, not a static mockup.
- Every card and command should map to a module route or drawer.
- Use reusable components for metric cards, command buttons, module cards, approval items, risk items, and audit rows.
- Keep colors and typography aligned with the command-center design system.
- Tables and dense lists should remain readable on laptop screens.
- Mobile/tablet view should show critical status and approvals first.
- Emergency lock must be a real guarded flow with confirmation.
- Every admin action must call the audit logging path.
- AI controls must never bypass permission checks.

## 11. Success Conditions

BanikOS will be successful if:

- Admin-end foundation is completed first.
- Retail and wholesale are fully separated in pricing, accounts, and reports.
- Vendor purchase and payable are accurate.
- Delivered-only sales truth is enforced.
- Every department has the right panel.
- Staff can hold multiple roles without losing audit clarity.
- AI works through permissions and guardrails.
- Marketing receives true conversion data.
- Finance can audit every taka.
- Hosting cannot expose local core data.
- Owner absence does not stop operations.

---

# File: shishir-mark.svg

```svg
<svg width="256" height="256" viewBox="0 0 256 256" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="256" height="256" rx="56" fill="#EFF6FF"/>
  <rect x="44" y="84" width="168" height="116" rx="24" fill="#3B82F6"/>
  <path d="M60 110C60 103.373 65.3726 98 72 98H184C190.627 98 196 103.373 196 110V182H60V110Z" fill="#60A5FA"/>
  <path d="M38 104.32C38 99.3808 40.8661 94.8894 45.3508 92.8115L118.352 58.9912C124.523 56.131 131.477 56.131 137.648 58.9912L210.649 92.8115C215.134 94.8894 218 99.3808 218 104.32C218 108.562 214.562 112 210.32 112H45.68C41.4385 112 38 108.562 38 104.32Z" fill="#1D4ED8"/>
  <rect x="74" y="130" width="36" height="52" rx="10" fill="white"/>
  <rect x="124" y="130" width="58" height="16" rx="8" fill="#DBEAFE"/>
  <rect x="124" y="156" width="44" height="12" rx="6" fill="#BFDBFE"/>
  <circle cx="92" cy="155" r="8" fill="#93C5FD"/>
  <path d="M74 86H182" stroke="white" stroke-width="8" stroke-linecap="round"/>
  <path d="M84 188H172" stroke="#1E3A8A" stroke-width="10" stroke-linecap="round"/>
</svg>
```

---

