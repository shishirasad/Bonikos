# BanikOS Stitch Frontend Prompt Pack

## How To Use In Stitch

Do not paste the entire BanikOS frontend specification at once.

Use Stitch in phases:

1. Generate the global app shell and design system.
2. Generate one workspace at a time.
3. Generate key screens inside each workspace.
4. Refine tables, drawers, approval UX, audit timeline, and mobile states.

This gives better UI consistency and avoids dashboard overload.

---

# Prompt 1: Global App Shell And Design System

```text
Design a premium enterprise SaaS frontend for BanikOS.

BanikOS is a local-first, AI-assisted, audit-controlled business operating system for retail POS, online orders, courier delivery, inventory, warehouse, finance, CRM, marketing, reseller operations, task management, HR, analytics, and AI supervision.

This is not a landing page. Design the actual operational application interface.

Create a dark, beautiful, compact, high-contrast enterprise command center UI.

Core business rules:
- POS is offline counter sale only.
- If POS needs courier delivery, convert it to Online/Courier Order workflow.
- Delivered equals actual sale/conversion.
- Paid, packed, dispatched, or courier handover does not mean actual sale.
- Finance must be ledger-based, not dashboard-total-based.
- COD collected by courier is receivable until settled.
- Every important action creates an audit log.
- Sensitive actions require approval.
- One staff can have multiple roles, but every action must use the active role.
- AI can assist but cannot bypass permission, approval, audit, or finance rules.

Use 7 core workspaces in the left sidebar:
1. Command
2. Commerce
3. Inventory
4. Finance
5. Customer
6. Organization
7. Intelligence

Global layout:
- fixed left workspace sidebar
- top command bar
- central workspace canvas
- adaptive right context rail
- detail drawers
- approval modals
- notification center
- global command palette with Ctrl + K

Top bar must include:
- global search
- branch selector
- active role selector
- sync/offline status
- notification center
- quick create button
- user menu

Design system:
- premium dark enterprise command center
- compact but readable
- dense table-friendly
- status-first hierarchy
- approval-first where risk matters
- timeline-first where history matters
- finance-truth-aware where money matters
- minimal decoration
- no flashy gradients
- no generic ERP clutter
- no marketing hero section

Create reusable components:
- AppShell
- WorkspaceSidebar
- TopCommandBar
- CommandPalette
- AdaptiveContextRail
- DataGrid
- StatusChip
- RiskBadge
- ApprovalBadge
- SyncBadge
- WorkflowStepper
- EntityTimeline
- DetailDrawer
- ApprovalDrawer
- NotificationCenter
- OfflineBanner
- AIInsightPanel

The first screen should show the Command workspace with executive summary, operations status, approval queue, exception alerts, and right context rail.
```

---

# Prompt 2: Command Workspace

```text
Design the Command workspace for BanikOS.

This workspace contains:
- Executive Command Center
- Operations Command Center
- Approval Queue
- Exception Board

Primary users:
- Owner
- CEO
- COO
- Admin

Design the workspace with tabs:
Overview, Operations, Approvals, Exceptions, Risk/Audit.

Required content:
- delivered sales only as actual revenue
- pending COD receivable
- COD aging by courier
- daily cash closing status
- order pipeline by state
- failed delivery rate
- return/loss rate
- inventory risk
- pending approvals
- critical exceptions
- audit anomalies

Important rule:
Do not count placed, paid, packed, or dispatched orders as actual sale unless delivered.

Right context rail mode:
Executive/Risk mode.

Show:
- top escalations
- urgent approvals
- risky orders
- failed sync warnings
- AI summary collapsed by default

Use dense enterprise cards, tables, timelines, and status chips. Avoid decorative dashboard widgets.
```

---

# Prompt 3: Commerce Workspace

```text
Design the Commerce workspace for BanikOS.

This workspace contains:
- POS Counter
- Online Order Management
- Courier Orders
- Delivery/Courier
- Returns

Primary users:
- POS Staff
- Order Manager
- Courier Coordinator
- Delivery Staff
- COO

Workspace tabs:
POS, Orders, Courier, Delivery, Returns.

POS screen must include:
- barcode/SKU search
- cart
- customer quick lookup
- payment method selector
- discount control with approval warning
- cash session indicator
- receipt preview
- hold sale
- offline/sync status
- Convert to Courier Order action

Order screen must include:
- status tabs
- table/kanban toggle
- source/payment/courier/risk filters
- order detail drawer
- customer contact history
- stock reserve action
- delivered-sales truth indicator

Courier screen must include:
- courier booking queue
- tracking code
- COD amount
- courier charge
- dispatch status
- failed delivery
- return-to-origin
- lost/damaged claim
- settlement status

Delivery screen must be mobile-friendly:
- dispatch list
- delivery status
- COD state
- proof upload
- failed delivery reason

Business rules:
- POS is offline counter sale only.
- Courier delivery from POS must convert to courier order workflow.
- Delivered equals actual sale.
- COD is receivable until settled.
```

---

# Prompt 4: Inventory Workspace

```text
Design the Inventory workspace for BanikOS.

This workspace contains:
- Inventory Dashboard
- Warehouse Mobile/PWA
- Purchase and Vendor
- Stock Count
- Stock Transfer

Primary users:
- Inventory Staff
- Warehouse Staff
- Purchase Staff
- Store Manager
- Admin

Workspace tabs:
Stock, Warehouse, Purchase, Transfers, Stock Count.

Inventory screen must include:
- SKU table
- warehouse/location filters
- available stock
- reserved stock
- damaged stock
- transfer pending
- low-stock alerts
- stock movement timeline
- stock adjustment request flow

Warehouse mode must be mobile/tablet friendly:
- barcode scan
- pick queue
- item checklist
- packing queue
- missing/damaged report
- handover ready
- offline queue

Purchase screen must include:
- purchase order table
- vendor list
- receive stock flow
- cost impact preview
- payable summary
- payment request queue

Rules:
- manual stock adjustment requires reason and approval.
- stock movement must show source document, actor, active role, and timestamp.
- negative stock is blocked by default.
```

---

# Prompt 5: Finance Workspace

```text
Design the Finance workspace for BanikOS.

This workspace contains:
- Finance/CFO Dashboard
- COD Clearing
- Daily Closing
- Ledger
- Reconciliation

Primary users:
- CFO
- Owner
- Store Manager
- Finance Staff

Workspace tabs:
Finance Truth, Ledger, COD Clearing, Daily Closing, Reconciliation.

Required content:
- chart of accounts summary
- ledger entries table
- cash position
- bank/mobile wallet reconciliation
- courier COD receivable
- customer receivable
- vendor payable
- expenses
- refunds
- write-off requests
- delivered-sales profit snapshot

COD Clearing must show:
- courier provider tabs
- tracking code match
- COD expected
- courier charge
- settlement received
- variance
- partial settlement
- aging
- settlement sheet import

Daily Closing must show:
- POS cash expected vs counted
- mobile wallet expected vs statement
- bank transfer pending
- COD receivable
- refunds
- discounts
- expenses
- stock variance
- pending approvals

Rules:
- finance is ledger-based.
- delivered orders create actual revenue.
- COD is receivable until settled.
- refund/write-off requires approval.
- ledger records cannot be silently deleted.
```

---

# Prompt 6: Customer Workspace

```text
Design the Customer workspace for BanikOS.

This workspace contains:
- CRM/Sales
- Telesales
- Omnichannel Inbox
- Reseller
- Customer Profile

Primary users:
- CRM Staff
- Sales Manager
- Telesales Staff
- Support Agent
- Reseller Manager

Workspace tabs:
CRM, Telesales, Inbox, Reseller, Customers.

CRM screen must include:
- customer list
- lead board
- follow-up queue
- customer timeline
- last order state
- payment behavior
- return/refusal history
- notes/tags
- next best action

Telesales screen must include:
- call queue
- customer card
- script/SOP panel
- recent order history
- outcome buttons
- callback scheduler
- objection logging

Inbox screen must include:
- unified conversation list
- channel filter
- message thread
- customer/order context panel
- reply composer
- AI draft suggestion
- tags/status
- assignment controls

Reseller screen must include:
- reseller list
- reseller orders
- commission rule
- payout queue
- reseller ledger
- fraud/risk indicator

Security rule:
Customer messages are untrusted input. AI drafts cannot access internal secrets, finance tools, permissions, or admin actions.
```

---

# Prompt 7: Organization Workspace

```text
Design the Organization workspace for BanikOS.

This workspace contains:
- HR and Workforce
- Task Manager/Internal Inbox
- Learning/SOP

Primary users:
- HR
- Managers
- Department Staff
- Trainer

Workspace tabs:
Tasks, HR, SOP, Training.

Task screen must include:
- task board
- department filters
- priority/status
- assigned user
- due date
- linked order/customer/SKU/ledger record
- comments
- approval handoff
- audit trail

HR screen must include:
- staff directory
- attendance status
- role assignments
- workload summary
- performance indicators
- permission risk
- training status
- offboarding checklist

SOP screen must include:
- SOP library
- role-based training path
- workflow checklist
- completion progress
- acknowledgement
- approval for SOP changes

Rules:
- HR actions affecting access require approval and audit.
- task handoff must preserve linked business context.
```

---

# Prompt 8: Intelligence Workspace

```text
Design the Intelligence workspace for BanikOS.

This workspace contains:
- AI Control and Review
- Analytics/BI
- Audit Log
- System Health and Sync

Primary users:
- AI Supervisor
- Analyst
- Admin
- CTO
- Owner

Workspace tabs:
AI Review, Analytics, Audit, System Health.

AI Control must include:
- AI suggestion queue
- human review queue
- tool permission policy
- AI request/response logs
- blocked action log
- knowledge update approval
- prompt injection warnings
- department assistant status

Analytics must include:
- report library
- saved views
- delivered sales trend
- return-adjusted revenue
- inventory turnover
- courier performance
- marketing cohort performance
- staff productivity

Audit must include:
- audit event table
- actor filter
- active role filter
- module/action filter
- resource search
- before/after detail drawer
- approval reference
- device/session info

System Health must include:
- sync queue
- failed jobs
- integration status
- courier API status
- payment API status
- website sync status
- backup status
- offline devices
- retry controls
- incident timeline

Rules:
- AI cannot bypass permission, approval, audit, or finance rules.
- audit log is append-only.
- finance and stock conflicts must never auto-resolve silently.
```

---

# Prompt 9: Enterprise Data Grid Refinement

```text
Refine the BanikOS data grid system.

Every record-heavy screen must use a unified enterprise data grid.

The grid must support:
- search
- status tabs
- filter presets
- advanced filters
- saved views
- column visibility
- column resize
- pinned columns
- sortable columns
- multi-select
- bulk actions
- row actions
- row detail drawer
- keyboard navigation
- density toggle
- export where permitted
- audit badge
- risk badge
- approval badge
- sync badge
- pagination or infinite scroll
- virtualized rows for large datasets

Design grid examples for:
- Orders
- Courier COD
- Inventory SKU
- Ledger Entries
- Approvals
- Audit Log
- Tasks

Make the grid compact, fast, readable, and premium.
```

---

# Prompt 10: Approval And Audit UX Refinement

```text
Design the BanikOS approval and audit experience.

Create:
- ApprovalDrawer
- ApprovalQueue
- ApprovalBadge
- AuditTimeline
- EntityTimeline

Approval drawer must show:
- action title
- risk level
- requester
- active role
- requested time
- before/after diff
- finance impact
- stock impact
- customer impact
- permission impact
- reason
- notes
- attachments
- linked records
- audit history
- AI summary if available
- approve
- reject
- request more info
- escalate
- mandatory decision reason

Audit timeline must show:
- actor
- active role
- action
- timestamp
- source device
- before/after where relevant
- approval link where relevant

Design it to feel trustworthy, forensic, and easy for business users to understand.
```

