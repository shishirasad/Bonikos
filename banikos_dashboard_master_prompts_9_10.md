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
