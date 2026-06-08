# BanikOS Frontend Component Prompts - 10/10

## How To Use

প্রতিটি component/screen design করার আগে প্রথমে **Global Frontend Master Prompt** ব্যবহার করুন। এরপর যে component বানাতে চান, সেই component-এর আলাদা prompt যোগ করুন।

Target user:

- senior frontend developer
- UI/UX designer
- Figma designer
- AI UI generator
- React/Next.js dashboard builder

---

# 0. Global Frontend Master Prompt

You are a senior enterprise SaaS UI/UX architect and frontend engineer. Design a production-ready frontend for BanikOS, a local-first, AI-assisted, audit-controlled business operating system for retail POS, online orders, courier, inventory, finance, CRM, marketing, reseller, warehouse, staff operations, and AI supervision.

The interface must feel like a premium operational command center, not a marketing website. Prioritize clarity, speed, dense but readable information, reliable workflows, and role-specific actions.

Non-negotiable business rules to reflect visually:

- POS is offline counter sale only.
- If POS needs courier delivery, it must convert to Online/Courier Order workflow.
- Delivered equals actual sale/conversion.
- Paid, packed, dispatched, or courier handover is not actual sale until delivered.
- Finance is ledger-based, not dashboard-total-based.
- COD collected by courier is receivable until settled.
- Every important action creates an audit log.
- Sensitive actions require approval.
- One staff can have multiple roles, but every action must use active role.
- AI can suggest, draft, summarize, and classify, but cannot bypass permission, approval, audit, or finance rules.

Visual style:

- dark enterprise command center
- sidebar-first navigation
- compact but readable layout
- status-first hierarchy
- approval-first right rail
- audit/risk awareness always visible
- dense table-friendly UI
- modern, professional, premium, not flashy
- avoid decorative clutter
- use clear icon buttons, status chips, segmented tabs, filters, tables, drawers, modals, and command bars

Global layout:

- fixed left sidebar
- top command/search bar
- main work area
- right context rail for approval, risk, audit, AI notes
- bottom or side activity timeline when needed

Use these interaction principles:

- primary action must be obvious
- dangerous action must require confirmation and reason
- approval-required action must open approval request flow
- empty states must suggest next useful action
- loading states must preserve layout
- tables must support search, filters, status tabs, bulk actions, and row detail drawer
- mobile/PWA screens must prioritize scanning, barcode, quick action, and offline indicators

Do not create a landing page. Build the actual operational UI.

---

# 1. App Shell Component Prompt

Design the BanikOS main app shell.

Include:

- fixed left sidebar with module groups: Command, POS, Orders, Courier, Inventory, Finance, CRM, Marketing, Tasks, AI, Admin
- top bar with global search, branch selector, active role switcher, sync status, notification icon, user menu
- main content slot
- right context rail slot
- compact dark theme
- visible active module and active role
- emergency/admin alert area for critical sync, finance, or audit issues

The shell must support staff with multiple roles. The active role selector must be visually important because every action is audited against active role.

---

# 2. Sidebar Navigation Component Prompt

Design a dense enterprise sidebar for BanikOS.

Include:

- icon + label navigation
- grouped sections
- collapsed and expanded states
- unread/approval count badges
- risk indicator badges
- active route state
- role-restricted disabled items
- quick links for POS Sale, Order Board, Packing Queue, COD Clearing, Approval Queue, Audit Log

Style it as a serious operational console, not a colorful consumer app.

---

# 3. Top Command Bar Component Prompt

Design the BanikOS top command bar.

Include:

- global command search
- quick create button
- active branch selector
- active role selector
- sync/offline status
- notification center
- current date/session status
- user menu

The command search should support searching order ID, customer phone, SKU, courier tracking code, invoice, ledger entry, and task.

---

# 4. Right Context Rail Component Prompt

Design a reusable right context rail for BanikOS.

Include:

- pending approval cards
- risk alerts
- audit timeline
- AI suggestions
- related customer/order/ledger context
- quick action buttons
- collapsible sections

The rail must never hide critical approval or audit warnings. It should help users act safely without leaving the main workflow.

---

# 5. Status Chip System Prompt

Design a complete status chip/badge system for BanikOS.

Include statuses for:

- order: draft, placed, confirmed, packed, dispatched, delivered, returned, cancelled, hold
- payment: unpaid, partial, paid, COD pending, COD settled, refunded
- inventory: in stock, low stock, reserved, damaged, transfer pending
- approval: pending, approved, rejected, escalated
- risk: low, medium, high, blocked
- sync: online, offline, queued, failed

Use distinct shapes, icons, and accessible contrast. Status must be readable inside tables.

---

# 6. Data Table Component Prompt

Design a reusable BanikOS enterprise data table.

Include:

- sticky header
- compact rows
- status chips
- column visibility control
- filter bar
- search
- saved views
- bulk action toolbar
- row detail drawer
- audit indicator per row
- approval-required action indicator
- pagination and density toggle

Tables must support operational speed. Avoid oversized cards.

---

# 7. Detail Drawer Component Prompt

Design a reusable side detail drawer.

Include:

- entity summary header
- status timeline
- key facts
- linked records
- payment/ledger summary if relevant
- audit log tab
- notes tab
- attachments tab
- approval actions
- safe primary/secondary action area

The drawer should let staff resolve most tasks without opening a new page.

---

# 8. Approval Request Modal Prompt

Design the approval request modal for sensitive BanikOS actions.

Include:

- requested action summary
- business impact summary
- before/after values
- reason input
- approver selection or rule-based approver
- risk level
- required evidence/attachment
- submit for approval button
- cancel button

The modal must make it clear that the action is not executed until approved.

---

# 9. Audit Timeline Component Prompt

Design the audit timeline component.

Include:

- actor name
- active role
- action
- before/after summary
- timestamp
- source device/session
- approval reference
- reason
- filter by action type

The timeline should feel trustworthy and forensic, but still readable for business users.

---

# 10. Master Admin Control Panel Prompt

Design the BanikOS Master Admin Control Panel.

Primary users: Owner, Admin.

Main goals:

- control users, roles, permissions
- review approval rules
- monitor audit log
- manage system settings
- see sync/API failures
- enforce emergency controls

Include:

- top health summary: active staff, pending approvals, failed sync, risk alerts
- user/role management table
- permission template area
- approval rules panel
- audit log stream
- emergency lock/suspend controls with confirmation
- right rail with critical security and finance alerts

The page must feel like the control room of the whole system.

---

# 11. Executive Dashboard Prompt

Design the BanikOS C-Level Executive Dashboard.

Primary users: Owner, CEO, CFO, COO, CMO.

Include tabs:

- Overview
- Finance Truth
- Operations
- Inventory
- Courier/COD
- Marketing
- Risk/Audit

Show:

- delivered sales only as actual revenue
- pending COD receivable
- courier settlement aging
- stock risk
- return/loss rate
- pending approvals
- high-risk customers/orders
- daily cash closing status
- audit anomalies

The dashboard should prioritize business truth over vanity metrics.

---

# 12. POS Panel Prompt

Design the BanikOS POS Panel.

Primary users: POS Staff, Store Manager.

Core rules:

- POS is offline counter sale only.
- Courier delivery from POS must convert to courier order workflow.
- Discounts require permission if above threshold.
- Every sale affects inventory and ledger.

Include:

- barcode/SKU search
- cart
- customer quick lookup
- payment method selector
- discount control with permission indicator
- receipt preview
- hold sale
- cash session status
- offline mode indicator
- convert to courier order action
- right rail with active role, approval warnings, audit note

The UI must be fast enough for a real shop counter.

---

# 13. Order Management Panel Prompt

Design the BanikOS Order Management Panel.

Primary users: Order Manager, CRM Staff, COO.

Include:

- order status kanban/table toggle
- filters by source, status, payment, courier, risk, date
- customer/order quick search
- order detail drawer
- confirm order action
- stock reserve action
- payment verification
- customer contact history
- suspicious order warning
- conversion/revenue truth indicator

Show clearly that placed/paid orders are not final sales until delivered.

---

# 14. Courier Order Panel Prompt

Design the BanikOS Courier Order Panel.

Primary users: Courier Coordinator, COO, Admin.

Include:

- courier booking queue
- tracking code column
- courier provider selector
- COD amount
- courier charge
- dispatch status
- failed delivery status
- return-to-origin status
- lost/damaged claim status
- settlement status
- high-risk address/customer indicators

Include right rail:

- courier risk
- pending COD receivable
- claim reminders
- audit stream

The UI must make COD and settlement truth impossible to miss.

---

# 15. Inventory Panel Prompt

Design the BanikOS Inventory Panel.

Primary users: Inventory Staff, Store Manager, Admin.

Include:

- stock overview
- SKU table
- warehouse/location filter
- stock movement timeline
- stock reservation view
- low stock alerts
- damaged stock
- stock transfer
- stock count
- manual adjustment request flow

Manual stock adjustment must show approval-required state. Negative stock should be visually blocked unless policy allows.

---

# 16. Warehouse Mobile/PWA Panel Prompt

Design a mobile-first Warehouse/Packing PWA for BanikOS.

Primary users: Warehouse Staff, Packaging Staff.

Include:

- scan barcode action
- pick list
- packing queue
- packed confirmation
- missing item report
- damage report
- handover ready status
- offline queue indicator
- large touch-friendly buttons
- simple one-task-at-a-time flow

The mobile UI must be fast, simple, and usable in a busy warehouse.

---

# 17. Vendor Purchase Panel Prompt

Design the BanikOS Vendor Purchase Panel.

Primary users: Purchase Staff, CFO, Admin.

Include:

- purchase order list
- vendor ledger summary
- receive stock flow
- cost update warning
- payable status
- payment request
- approval-required purchase/payment indicators
- product cost impact preview

The panel must connect purchase, inventory, and finance clearly.

---

# 18. Wholesale Panel Prompt

Design the BanikOS Wholesale Panel.

Primary users: Wholesale Manager, CFO, Admin.

Include:

- wholesale customer list
- price list selector
- bulk order creation
- credit limit indicator
- due ledger
- payment collection
- delivery/dispatch state
- commission if relevant
- approval for credit override

Separate retail customer ledger from wholesale customer ledger visually.

---

# 19. Finance/CFO Panel Prompt

Design the BanikOS Finance/CFO Panel.

Primary users: CFO, Owner, Admin.

Core rules:

- finance must be ledger-based
- delivered orders create actual revenue
- COD is receivable until settled
- refund/write-off requires approval

Include:

- ledger entries table
- chart of accounts summary
- cash closing
- bank/mobile wallet reconciliation
- courier COD clearing
- customer receivable
- vendor payable
- expenses
- refund queue
- daily close checklist
- audit trail

Use serious finance UI. Avoid vanity revenue cards that ignore ledger truth.

---

# 20. COD Clearing Component Prompt

Design the COD Clearing component.

Include:

- courier provider tabs
- tracking code match
- delivered parcels
- COD expected
- courier charge
- settlement received
- variance
- partial settlement
- unresolved aging
- import settlement sheet action
- approval for write-off or claim close

The component must show exactly which courier still holds COD money.

---

# 21. CRM/Sales Panel Prompt

Design the BanikOS CRM/Sales Panel.

Primary users: CRM Staff, Sales Manager.

Include:

- customer timeline
- lead board
- follow-up queue
- last order status
- return/refusal history
- call/note logging
- upsell/cross-sell suggestion
- customer risk badge
- task creation

Customer context must include order, payment, return, and support history without overwhelming the staff.

---

# 22. Telesales Panel Prompt

Design the BanikOS Telesales Panel.

Primary users: Telesales Staff, Sales Manager.

Include:

- call queue
- customer card
- script/SOP panel
- order creation shortcut
- follow-up outcome buttons
- callback scheduler
- objection/reason logging
- conversion status
- quality/audit notes

The UI must help staff complete calls quickly and consistently.

---

# 23. Packaging Panel Prompt

Design the BanikOS Packaging Panel.

Primary users: Packaging Staff, COO.

Include:

- packing queue
- order item checklist
- barcode scan verify
- packaging material usage
- weight/size input
- missing/damaged item report
- handover to courier action
- packing audit trail

The screen must reduce wrong item dispatch.

---

# 24. Delivery/Courier Panel Prompt

Design the BanikOS Delivery/Courier Panel.

Primary users: Delivery Staff, Courier Coordinator, COO.

Include:

- dispatch list
- delivery route/status
- courier handover
- failed delivery reason
- return pickup
- COD collection state
- proof of delivery attachment
- exception reporting

Mobile-friendly layout required. Make actions large and status-driven.

---

# 25. COD Risk Panel Prompt

Design the BanikOS COD Risk Panel.

Primary users: COO, Courier Coordinator, Admin.

Include:

- high-risk orders
- repeated refusal customers
- incomplete address
- high COD amount
- suspicious phone/address
- courier return rate
- recommendation: approve, hold, request advance, cancel
- approval workflow
- AI risk explanation area

Risk score must assist human decision-making, not silently block orders unless configured.

---

# 26. Marketing/CMO Panel Prompt

Design the BanikOS Marketing/CMO Panel.

Primary users: CMO, Marketing Staff.

Include:

- campaign calendar
- campaign list
- segment selector
- spend tracker
- delivered-sales-based ROAS
- content approval queue
- bulk message approval
- channel performance
- pixel/CAPI status

Marketing metrics must distinguish placed order, dispatched order, delivered order, and returned order.

---

# 27. Omnichannel Inbox Panel Prompt

Design the BanikOS Omnichannel Inbox Panel.

Primary users: Support Agent, CRM Staff, Sales Staff.

Include:

- unified inbox for Messenger, WhatsApp, Facebook comments, Instagram, website chat
- conversation list
- customer/order context panel
- reply composer
- AI reply draft with human send only
- tag/status controls
- assign to staff
- create order from conversation
- untrusted input warning for customer messages

The UI must prevent customer messages from controlling internal tools or exposing sensitive data.

---

# 28. Task Manager Panel Prompt

Design the BanikOS Task Manager/Internal Inbox Panel.

Primary users: Managers, Department Staff.

Include:

- task board
- department filters
- priority/status
- assigned user
- due date
- linked order/customer/stock/ledger record
- comments
- approval handoff
- audit trail

The panel must support operational handoff without losing context.

---

# 29. Website/Landing Control Panel Prompt

Design the BanikOS Website/Storefront Control Panel.

Primary users: Admin, Marketing Staff, Owner.

Include:

- public product sync
- landing page list
- content blocks
- product visibility
- pricing sync status
- pixel/CAPI configuration
- public API key status
- sync failure alerts

The UI must make clear that public website gets limited synced data, not direct access to local core database.

---

# 30. Reseller Panel Prompt

Design the BanikOS Reseller Panel.

Primary users: Reseller Manager, Admin, CFO.

Include:

- reseller list
- reseller order list
- commission rule
- payout queue
- payout approval
- reseller ledger
- stock visibility rules
- delivery status
- fraud/risk indicator

The reseller must not bypass finance, stock, delivery, or approval control.

---

# 31. AI Control Panel Prompt

Design the BanikOS AI Control Panel.

Primary users: AI Supervisor, Admin, Owner.

Include:

- AI suggestion queue
- tool permission policy
- AI request/response logs
- human review queue
- knowledge update approval
- prompt injection warnings
- department-wise AI assistants
- blocked action log

Make AI feel useful but controlled. Human approval must be visually central.

---

# 32. Customer Profile Component Prompt

Design the customer profile component.

Include:

- identity and contact details
- address quality
- order history
- payment behavior
- return/refusal history
- support conversations
- notes
- tags/segments
- risk score
- privacy restrictions based on role

The component should help staff decide safely without exposing unnecessary sensitive data.

---

# 33. Order Detail Component Prompt

Design the order detail component.

Include:

- order summary
- customer summary
- item list
- order state timeline
- payment state
- fulfillment state
- courier/tracking
- stock reservation
- ledger impact preview
- audit log
- approval actions
- return/refund actions

Show prominently whether the order is counted as actual sale or not.

---

# 34. Product/SKU Detail Component Prompt

Design the product/SKU detail component.

Include:

- product images
- SKU/barcode
- variant info
- current stock by location
- reserved stock
- cost and price
- recent movement
- low stock threshold
- vendor info
- audit log

Stock truth must be clear: available, reserved, damaged, transfer pending.

---

# 35. Stock Movement Timeline Prompt

Design the stock movement timeline.

Include:

- movement type
- quantity in/out
- source document
- warehouse/location
- actor and active role
- approval reference
- timestamp
- balance after movement

The component must explain why stock changed.

---

# 36. Ledger Entry Detail Component Prompt

Design the ledger entry detail component.

Include:

- journal entry header
- debit/credit lines
- linked order/payment/refund/settlement
- posting status
- actor
- approval reference
- audit log
- reversal/correction action

The UI must never allow silent deletion of ledger records.

---

# 37. Daily Closing Component Prompt

Design the daily closing component.

Include:

- POS cash expected vs counted
- mobile wallet expected vs statement
- bank transfer pending
- COD receivable
- refunds
- discounts
- expenses
- stock variance
- pending approvals
- close day action

Closing must feel like a checklist that protects the business.

---

# 38. Exception Board Prompt

Design the BanikOS Exception Board.

Include:

- failed deliveries
- stock mismatch
- payment mismatch
- COD settlement delay
- refund pending
- approval stuck
- sync failure
- suspicious customer/order
- assigned owner
- SLA timer
- resolution workflow

This board should show what is blocking clean operations.

---

# 39. Notification Center Prompt

Design the BanikOS notification center.

Include:

- approval requests
- risk alerts
- task mentions
- finance mismatch
- stock alerts
- courier updates
- sync failure
- AI review needed

Notifications must be actionable and grouped by business urgency.

---

# 40. Empty, Loading, Error State Prompt

Design reusable empty/loading/error states for BanikOS.

Include:

- skeleton loading for tables and dashboards
- empty state with next action
- permission denied state
- approval required state
- offline queued state
- sync failed state
- business rule blocked state

The states should educate the user through clear operational language, not generic messages.

---

# 41. Mobile Bottom Navigation Prompt

Design a mobile/PWA bottom navigation for BanikOS warehouse, delivery, and POS-lite workflows.

Include:

- Scan
- Queue
- Tasks
- Alerts
- Profile/Role

Keep it thumb-friendly, high contrast, and optimized for fast operational movement.

---

# 42. Final Component Quality Checklist

Every frontend component must answer:

- Who is the primary user?
- What decision/action does this screen help them complete?
- What business rule can be violated here?
- Is permission visible?
- Is approval visible?
- Is audit visible?
- Is finance impact visible if relevant?
- Is delivered-sales truth preserved?
- Is the empty/error/offline state designed?
- Can a non-technical staff member use it under pressure?

