# BanikOS Frontend Core Architecture Specs Combined - 10/10

This file combines the frontend index, workspace architecture, enterprise UX specs, engineering architecture, and full dashboard prompt pack.

## Originally Combined Files

These files were merged into this standalone document and the split copies were deleted:

- banikos_frontend_10_of_10_index.md
- banikos_frontend_workspace_architecture_spec.md
- banikos_frontend_design_system_spec.md
- banikos_frontend_data_grid_spec.md
- banikos_frontend_workflow_state_ui_spec.md
- banikos_frontend_notification_system_spec.md
- banikos_frontend_approval_ux_spec.md
- banikos_frontend_ai_interaction_spec.md
- banikos_frontend_offline_sync_spec.md
- banikos_frontend_engineering_architecture.md
- banikos_frontend_responsive_behavior_spec.md
- banikos_frontend_interaction_rules_spec.md
- banikos_full_frontend_dashboard_prompt_pack_10_of_10.md

---

# Included Section: banikos_frontend_10_of_10_index.md

# BanikOS Frontend 10/10 Specification Pack

## Purpose

This pack upgrades the BanikOS frontend plan from dashboard mockups into enterprise application interface architecture.

The system still covers 31 dashboards/views, but users should not navigate 31 separate top-level destinations. The frontend must use a workspace architecture with progressive disclosure, adaptive context rails, a unified command palette, and consistent interaction rules.

## Core Navigation Decision

Use 7 core workspaces:

| Workspace | Contains |
|---|---|
| Command | Executive, Operations, Approvals, Exceptions |
| Commerce | POS, Orders, Courier, Delivery |
| Inventory | Inventory, Warehouse, Purchase |
| Finance | CFO, COD Clearing, Daily Closing |
| Customer | CRM, Telesales, Inbox, Reseller |
| Organization | HR, Tasks, SOP |
| Intelligence | AI, Analytics, Audit, System Health |

The 31 dashboards become views, tabs, boards, or deep links inside these workspaces.

## Sections In This Standalone Master File

1. Workspace Architecture Spec
2. Design System Spec
3. Data Grid Spec
4. Workflow State UI Spec
5. Notification System Spec
6. Approval UX Spec
7. AI Interaction Spec
8. Offline and Sync Spec
9. Frontend Engineering Architecture
10. Responsive Behavior Spec
11. Interaction Rules Spec
12. Full Dashboard Prompt Pack

Note: the original split source files were intentionally deleted after this combined master file was created.

## Frontend Quality Target

BanikOS frontend must be:

- beautiful but operational
- compact but readable
- workspace-based, not dashboard-sprawled
- table-first where records matter
- timeline-first where history matters
- approval-first where risk matters
- offline-aware where field work matters
- finance-truth-aware everywhere money is involved
- AI-assisted but human-controlled

## Final Architecture Principle

The UI should not ask staff to understand the full system.

It should show each user the right workspace, the right task, the right risk, and the right next action.

---

# Included Section: banikos_frontend_workspace_architecture_spec.md

# BanikOS Frontend Workspace Architecture Spec

## Problem

The full BanikOS system covers 31 dashboards. If each dashboard becomes a separate primary navigation item, the UI will become hard to learn, slow to navigate, and operationally confusing.

## Decision

Use 7 core workspaces. Dashboards become internal views, tabs, boards, drawers, or deep links inside those workspaces.

## Workspace Map

| Workspace | Primary Users | Included Views |
|---|---|---|
| Command | Owner, CEO, COO, Admin | Executive, Operations, Approval Queue, Exception Board |
| Commerce | POS Staff, Order Manager, Courier Team | POS, Online Orders, Courier Orders, Delivery |
| Inventory | Inventory Staff, Warehouse Staff, Purchase Staff | Inventory, Warehouse PWA, Purchase/Vendor |
| Finance | CFO, Owner, Store Manager | Finance/CFO, COD Clearing, Daily Closing |
| Customer | CRM, Sales, Support, Reseller Manager | CRM, Telesales, Omnichannel Inbox, Reseller |
| Organization | HR, Managers, Staff | HR, Task Manager, SOP/Learning |
| Intelligence | AI Supervisor, Analyst, Admin, CTO | AI Control, Analytics, Audit Log, System Health |

## Primary Navigation

Left sidebar should show only:

```text
Command
Commerce
Inventory
Finance
Customer
Organization
Intelligence
Admin
```

Admin may be a separate persistent area or a protected view under Command depending on role.

## Secondary Navigation

Inside each workspace, use:

- horizontal tabs for high-level views
- segmented controls for workflow modes
- saved views for table presets
- route breadcrumbs for nested records
- command palette for jumping directly to any view

Example Commerce workspace:

```text
Commerce
  POS
  Orders
  Courier
  Delivery
  Returns
```

## Workspace Landing Pages

Each workspace landing page should show:

- current workload
- blocked items
- urgent approvals
- exceptions
- recent activity
- primary action
- "continue where you left off"

## Role-Based Defaults

Each user should land in the workspace that matches active role.

Examples:

| Active Role | Default Workspace | Default View |
|---|---|---|
| POS Staff | Commerce | POS |
| Order Manager | Commerce | Orders |
| Courier Coordinator | Commerce | Courier |
| Inventory Staff | Inventory | Inventory |
| Warehouse Staff | Inventory | Warehouse PWA |
| CFO | Finance | Finance Truth |
| Store Manager | Finance | Daily Closing |
| CRM Staff | Customer | CRM |
| Support Agent | Customer | Inbox |
| AI Supervisor | Intelligence | AI Review |
| Admin | Command | Admin Control |

## Route Strategy

Use stable workspace routes:

```text
/command
/command/executive
/command/operations
/command/approvals
/command/exceptions

/commerce
/commerce/pos
/commerce/orders
/commerce/courier
/commerce/delivery

/inventory
/inventory/stock
/inventory/warehouse
/inventory/purchase

/finance
/finance/ledger
/finance/cod-clearing
/finance/daily-closing

/customer
/customer/crm
/customer/telesales
/customer/inbox
/customer/reseller

/organization
/organization/hr
/organization/tasks
/organization/sop

/intelligence
/intelligence/ai
/intelligence/analytics
/intelligence/audit
/intelligence/system-health
```

## Context Rail Modes

The right rail should adapt to workspace and user intent.

| Mode | Use In | Shows |
|---|---|---|
| Operational | Commerce, Inventory, Organization | task blockers, warnings, SLA, linked tasks |
| Financial | Finance, Commerce payment views | approval, variance, ledger impact, COD |
| Risk | Command, Courier, Inventory, AI | fraud, audit, exceptions, suspicious activity |
| Executive | Command | summary, escalations, top risks, AI brief |
| Minimal | POS, mobile, high-speed screens | only critical warnings and active role |

## Command Palette

Shortcut:

```text
Ctrl + K
```

Capabilities:

- open order by ID
- open customer by phone
- open SKU
- open tracking code
- create task
- create order
- jump workspace
- ask AI summary
- create approval request
- open daily closing
- open COD clearing

## Deep Link Policy

Every major record should have deep links:

```text
/commerce/orders/:id
/customer/customers/:id
/inventory/skus/:id
/finance/ledger/:entryId
/command/approvals/:id
/intelligence/audit/:id
```

Deep links open the correct workspace with a detail drawer or full detail view.

## Anti-Confusion Rules

- Do not expose all 31 dashboards in the primary sidebar.
- Do not duplicate the same action in unrelated workspaces unless context demands it.
- If the same record appears in multiple workspaces, keep one canonical detail drawer.
- Use role-based default views.
- Use command palette for power navigation.
- Use workspace breadcrumbs for orientation.

---

# Included Section: banikos_frontend_design_system_spec.md

# BanikOS Design System Spec

## Purpose

The design system keeps BanikOS consistent across all workspaces, dashboards, tables, drawers, modals, mobile views, approvals, audit timelines, and AI panels.

The visual direction is a premium dark enterprise command center: compact, readable, calm, precise, and operational.

## Design Principles

- Function before decoration
- Status before description
- Tables before cards for records
- Timeline before raw logs for history
- Approval before execution for sensitive actions
- Role clarity before feature access
- Progressive disclosure before dashboard sprawl
- High contrast before subtle styling

## Color Tokens

Use semantic color tokens, not random colors.

```text
bg.app
bg.sidebar
bg.surface
bg.surface-raised
bg.input
bg.hover
bg.selected

text.primary
text.secondary
text.muted
text.inverse

border.default
border.strong
border.focus

status.success
status.warning
status.danger
status.info
status.neutral

risk.low
risk.medium
risk.high
risk.blocked

finance.debit
finance.credit
finance.variance
finance.settled

approval.pending
approval.approved
approval.rejected
approval.escalated

sync.online
sync.offline
sync.queued
sync.failed
```

## Recommended Palette

Dark base:

```text
app background: #0B0F14
sidebar: #0F1620
surface: #151C26
raised surface: #1B2430
border: #293241
primary text: #F4F7FB
secondary text: #A8B3C2
muted text: #6F7B8A
accent: #36C2A5
info: #60A5FA
warning: #FBBF24
danger: #F87171
success: #34D399
purple AI accent: #A78BFA
```

Avoid a one-note purple/blue dashboard. Use semantic accents sparingly.

## Typography

Use a modern UI sans font.

Scale:

```text
display: 28/36 semibold
page title: 22/30 semibold
section title: 16/24 semibold
body: 14/22 regular
table body: 13/20 regular
caption: 12/18 regular
micro: 11/16 medium
```

Rules:

- no negative letter spacing
- avoid oversized headings inside operational panels
- table text must remain readable at dense density
- button text must never overflow

## Spacing Tokens

```text
space.1 = 4px
space.2 = 8px
space.3 = 12px
space.4 = 16px
space.5 = 20px
space.6 = 24px
space.8 = 32px
```

Layout rhythm:

- dashboard gutters: 16px to 24px
- table row padding: 8px to 10px
- form field gap: 12px
- section gap: 20px

## Radius And Elevation

```text
radius.sm = 4px
radius.md = 6px
radius.lg = 8px
```

Cards and panels should use 6px to 8px radius. Avoid overly rounded UI.

Elevation:

- use borders more than shadows
- drawers and modals may use soft shadow
- dark UI should not rely only on shadow

## Core Components

Required system components:

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
- ConfirmDialog
- AuditTimeline
- NotificationCenter
- EmptyState
- LoadingSkeleton
- ErrorState
- OfflineBanner
- ConflictResolver
- AIInsightPanel

## Component States

Every component must support:

```text
default
hover
focus
active
disabled
loading
empty
error
offline
permission_denied
approval_required
sync_queued
sync_failed
```

## Button System

Button hierarchy:

| Type | Use |
|---|---|
| Primary | one main action per view |
| Secondary | normal action |
| Ghost/Icon | table and toolbar utilities |
| Danger | destructive action |
| Approval | shield icon, approval-required action |

Rules:

- one primary action per screen region
- dangerous actions must open confirmation
- approval actions must open approval drawer
- icon-only actions require tooltip

## Badge System

Badges must be compact and table-friendly.

Badge types:

- status
- risk
- approval
- finance
- sync
- role
- SLA
- AI

## Form System

Forms must include:

- clear labels
- inline validation
- reason fields for sensitive actions
- attachment support where evidence matters
- dirty state warning
- submit disabled until valid
- permission-aware field locking

## Motion

Use subtle motion only:

- drawer slide
- modal fade
- row expand
- status update flash
- skeleton loading

Avoid decorative animations in operational screens.

## Accessibility

Minimum requirements:

- keyboard navigation
- focus ring visible
- contrast-safe text
- tooltip for icon-only buttons
- non-color status indicators
- table row selection readable by keyboard and screen readers

## Design Review Checklist

Before approving any screen:

- Is the primary action obvious?
- Is business status visible?
- Are risks and approvals visible but not overwhelming?
- Is the table dense but readable?
- Are empty/loading/error/offline states designed?
- Does the screen respect active role and permission?
- Is finance truth visible where money is involved?
- Is the UI consistent with the design system?

---

# Included Section: banikos_frontend_data_grid_spec.md

# BanikOS Unified Data Grid Spec

## Purpose

The data grid is the heart of BanikOS. Orders, customers, SKU, ledger entries, approvals, audit logs, courier settlements, tasks, and exceptions all depend on fast, reliable, dense tables.

Every record-heavy dashboard must use the same grid architecture.

## Required Capabilities

Each grid must support:

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

## Grid Layout

Recommended structure:

```text
GridHeader
  Title
  Count
  Primary Action

GridToolbar
  Search
  Status Tabs
  Filter Button
  Saved Views
  Column Button
  Export Button

GridBody
  Sticky Header
  Pinned Columns
  Rows
  Row Actions

BulkActionBar
  Selected Count
  Allowed Bulk Actions

DetailDrawer
  Opens from row click or action
```

## Standard Columns

Use domain-specific columns plus common columns.

Common columns:

```text
select
record_id
status
risk
approval
sync
owner_or_assignee
updated_at
actions
```

## Table Density

Support:

| Density | Use |
|---|---|
| Compact | operations, finance, admin |
| Comfortable | CRM, support, task |
| Expanded | touch/tablet mode |

## Row Click Behavior

Default:

- single click selects row or opens preview depending on workspace
- double click opens detail drawer
- Enter opens detail drawer
- row actions are icon buttons with tooltips

High-speed screens like POS should avoid complex row interactions.

## Saved Views

Each grid should support saved views:

Examples:

- Orders: "Paid but not delivered"
- Courier: "COD pending over 7 days"
- Inventory: "Low stock by warehouse"
- Finance: "Unreconciled mobile wallet"
- Approvals: "Waiting for me"
- Audit: "Permission changes"

Saved view contains:

```text
name
owner
scope: private/team/company
filters
columns
sort
density
created_at
updated_at
```

## Filter Presets

Filters should be fast and business-oriented:

- status
- date range
- branch
- assignee
- risk
- approval state
- payment state
- courier provider
- sync state
- amount range
- source channel

## Bulk Action Rules

Bulk action toolbar should show only allowed actions.

Examples:

- assign staff
- change status if state machine allows
- request approval
- export selected if permitted
- mark reviewed

Rules:

- bulk destructive action requires confirmation
- bulk sensitive action requires approval
- blocked rows show reason
- partial success results show summary

## Inline Editing

Inline edit is allowed only for low-risk fields:

- assignee
- tag
- priority
- note
- due date

Inline edit is not allowed for:

- ledger amount
- payment status
- stock quantity
- permission
- order final state

Sensitive edits open drawer or approval flow.

## Export Policy

Export button must be permission-aware.

Export requires:

- permission check
- audit log
- visible scope
- optional approval for sensitive data

Export states:

```text
allowed
approval_required
permission_denied
processing
ready
failed
```

## Keyboard Shortcuts

Minimum:

```text
/ = focus search
f = open filters
v = saved views
c = columns
Enter = open row
Space = select row
Esc = close drawer
Ctrl+K = command palette
```

## Performance

Rules:

- virtualize rows above 200 records
- server-side filtering for large datasets
- keep row height stable
- preserve scroll position after drawer close
- use skeleton loading, not layout jumps
- debounce search
- cache saved views

## Grid Quality Checklist

- Can a power user operate it with keyboard?
- Can a manager save a useful view?
- Are risk, approval, audit, and sync visible?
- Are dangerous bulk actions protected?
- Does row click open useful detail?
- Does the grid stay fast with large data?

---

# Included Section: banikos_frontend_workflow_state_ui_spec.md

# BanikOS Workflow State UI Spec

## Purpose

BanikOS business rules depend on state machines. The frontend must make state visible, explain allowed actions, and prevent invalid transitions.

State is not just a backend concern. It is a core UI concept.

## Required Component

Create a reusable `WorkflowStatePanel`.

It appears in:

- order detail
- courier detail
- packing detail
- delivery detail
- payment detail
- return detail
- stock transfer detail
- approval detail

## Visual Model

Show workflow as:

```text
Current State
Allowed Next Actions
Blocked Actions
Required Approval
SLA Timer
Timeline
```

For long workflows, use a compact stepper plus detail panel.

## Order Workflow

```text
Draft
Placed
Confirmed
Stock Reserved
Packed
Dispatched
Delivered
Completed
```

Exception states:

```text
Hold
Cancelled
Failed Delivery
Partial Delivered
Returned
Lost
Damaged
Refunded
```

UI rules:

- show "Actual Sale: No" until Delivered
- show "Actual Sale: Yes" only when delivered/completed policy allows
- display blocked actions with reason
- show finance impact when moving to Delivered

## Payment Workflow

```text
Unpaid
Partial Paid
Paid
COD Pending
COD Collected by Courier
COD Settled
Refunded
Written Off
```

UI rules:

- Paid does not equal Delivered
- COD collected by courier does not equal cash received
- refund and write-off require approval

## Fulfillment Workflow

```text
Not Started
Pick Pending
Picked
Packed
Handover Ready
Handover Done
In Transit
Delivered
Exception
Returned to Origin
```

UI rules:

- packing cannot complete without item verification unless override approved
- handover requires courier/tracking or manual delivery assignment

## Inventory Workflow

Movement types:

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
```

UI rules:

- manual stock adjustment opens approval drawer
- stock count variance shows before/after
- negative stock blocked by default

## State Transition Display

Each state node should show:

```text
label
status
timestamp
actor
active_role
source_device
approval_link
SLA
notes
```

## Allowed Action Panel

For current state, show:

- primary allowed action
- secondary allowed actions
- approval-required actions
- blocked actions with reason

Example:

```text
Current: Packed
Primary: Handover to Courier
Secondary: Print Label, Edit Package Weight
Approval: Cancel Packed Order
Blocked: Mark Delivered, reason: must be dispatched first
```

## SLA Timers

Show SLA timers for:

- confirmation pending
- packing pending
- dispatch pending
- failed delivery unresolved
- COD unsettled
- approval pending
- sync failed

Timer severity:

```text
normal
warning
breached
escalated
```

## State Errors

Invalid transition error should be business-readable:

Bad:

```text
Invalid status transition.
```

Good:

```text
This order cannot be marked Delivered before it is Dispatched. Complete courier handover first.
```

## Timeline Integration

Every state change creates timeline entry:

```text
state_changed
from
to
actor
active_role
timestamp
reason
approval_ref
```

## Quality Checklist

- Is current state obvious?
- Is the next safe action obvious?
- Are blocked actions explained?
- Are approval-required transitions clear?
- Is finance impact shown where relevant?
- Is the timeline complete?

---

# Included Section: banikos_frontend_notification_system_spec.md

# BanikOS Notification System Spec

## Purpose

BanikOS needs one unified notification system. Without priority, ownership, and action rules, a large ERP-style system becomes noisy and chaotic.

## Notification Types

```text
approval
exception
finance_mismatch
failed_sync
courier_issue
stock_alert
task
mention
security
ai_review
system_health
daily_closing
```

## Priority Levels

| Priority | Meaning | Example |
|---|---|---|
| Critical | business risk now | finance sync conflict, permission breach |
| High | needs same-day action | COD overdue, failed delivery spike |
| Medium | normal operational action | task assigned, approval pending |
| Low | informational | report ready |

## Notification Center Layout

Sections:

- Waiting for me
- Critical
- Approvals
- Exceptions
- Finance
- Sync/System
- AI Review
- Mentions
- Archived

Each item shows:

```text
type
priority
title
short summary
linked record
workspace
owner
created_at
SLA/age
primary action
secondary action
```

## Delivery Channels

In-app is primary.

Optional channels:

- email
- SMS
- WhatsApp internal alert
- desktop push
- mobile push

Critical notifications may escalate by role.

## Actionable Notifications

Every notification should have a direct action:

- open approval
- open exception
- open order
- retry sync
- assign owner
- mark reviewed
- create task

Avoid notifications that only say "something happened."

## Deduplication

Group repeated events.

Example:

```text
18 orders have COD settlement delay from Steadfast.
```

Do not show 18 separate alerts unless the user expands.

## Notification Rules By Role

| Role | Should See |
|---|---|
| POS Staff | POS sync, cash session, approval result |
| Order Manager | order exceptions, confirmation queue |
| Courier Coordinator | delivery failure, COD aging, claim issue |
| Inventory Staff | stock alert, stock count, transfer |
| CFO | finance mismatch, COD clearing, refund approval |
| COO | operations exceptions, SLA breach |
| Admin | security, sync, permission, system health |
| AI Supervisor | AI blocked action, review needed |

## Read And Archive Behavior

- open item does not always mean resolved
- resolved state should come from linked workflow
- archive hides notification but keeps audit
- critical notification cannot be dismissed without reason if unresolved

## Notification Badges

Sidebar badges:

- count only actionable items
- critical count shown separately
- avoid badge overload

Top bar:

- show critical indicator
- show total waiting-for-me count

## Quality Checklist

- Is the notification actionable?
- Is priority clear?
- Is ownership clear?
- Is it grouped when repeated?
- Does it link to the right workspace and record?
- Can user resolve or assign it?

---

# Included Section: banikos_frontend_approval_ux_spec.md

# BanikOS Approval UX Spec

## Purpose

Approvals are a core safety mechanism in BanikOS. The UI must make approval-required actions clear, fast to review, and fully auditable.

## Required Components

- ApprovalBadge
- ApprovalDrawer
- ApprovalQueue
- ApprovalTimeline
- ApprovalReasonInput
- ApprovalImpactPreview

## Approval Drawer

The approval drawer is the standard review interface.

Required sections:

```text
Header
  action title
  risk level
  requester
  active role
  requested time

Impact Preview
  before/after diff
  finance impact
  stock impact
  customer impact
  permission impact

Evidence
  reason
  notes
  attachments
  linked records

Context
  audit history
  previous similar approvals
  AI summary if available

Decision
  approve
  reject
  request more info
  escalate
  mandatory decision reason
```

## Approval Triggers

Always approval-required:

- discount above threshold
- manual stock adjustment
- refund
- COD write-off
- courier lost claim close
- vendor payment above limit
- expense above limit
- customer due write-off
- wholesale credit override
- marketing bulk send
- AI-generated bulk action
- permission change
- audit-sensitive setting change

## Approval States

```text
not_required
required
requested
in_review
approved
rejected
more_info_requested
escalated
expired
cancelled
executed
```

## Approval Badge Rules

Every relevant record row should show:

- pending approval
- approved
- rejected
- escalated
- blocked by approval

Badge click opens the approval drawer.

## Decision Hierarchy

Buttons:

- Approve: primary only when all required context is present
- Reject: danger/secondary
- Request Info: secondary
- Escalate: secondary

Mandatory reason:

- required for reject
- required for risky approve
- required for override

## Diff Preview

Every approval should show before/after.

Examples:

Stock adjustment:

```text
SKU: BLK-TSHIRT-M
Before: 42
After: 32
Difference: -10
Reason: damaged stock
Finance impact: possible inventory loss
```

Refund:

```text
Order: ORD-10294
Amount: 1,250 BDT
Payment: bKash
Ledger impact: reverse sale/payment
```

Permission change:

```text
User: Rahim
Added permission: finance.refund.approve.branch
Risk: high
```

## Approval Queue

Approval Queue dashboard should support:

- waiting for me
- all pending
- by module
- by amount
- by requester
- by risk
- breached SLA
- approved/rejected history

## Quality Checklist

- Does the approver understand the business impact?
- Is before/after clear?
- Is finance or stock impact shown?
- Is audit history available?
- Is reason mandatory where needed?
- Is execution separated from approval when necessary?

---

# Included Section: banikos_frontend_ai_interaction_spec.md

# BanikOS AI Interaction Spec

## Purpose

AI in BanikOS is a side intelligence layer. It should help staff understand, summarize, detect risk, draft replies, and suggest next actions. It must not dominate the UI or execute sensitive actions without human approval.

## AI Principle

```text
AI assists.
Humans decide.
Rules enforce.
Audit records.
```

## AI Placement

AI should appear in:

- collapsible side panel
- right rail insight block
- detail drawer summary
- command palette ask mode
- review queue

AI should not appear as a large permanent panel on every screen.

## AI Panel Modes

| Mode | Use |
|---|---|
| Summary | summarize order, customer, finance variance, audit history |
| Risk | explain fraud, COD, return, stock, or permission risk |
| Draft | customer reply, task note, campaign copy |
| SOP | suggest process steps |
| Review | show AI-generated pending actions |

## AI Access Levels

```text
Level 0: No access
Level 1: Read summarized data
Level 2: Draft recommendation
Level 3: Create pending action
Level 4: Execute only after human approval
Level 5: Forbidden in MVP
```

## Allowed AI Actions

AI can:

- summarize customer history
- summarize order timeline
- explain COD variance
- detect suspicious return pattern
- draft customer reply
- draft task note
- recommend reorder quantity
- explain stock variance
- summarize daily operation
- generate campaign draft
- suggest SOP step

## Forbidden AI Actions

AI cannot:

- post ledger
- refund
- approve request
- change permission
- delete records
- adjust stock
- send bulk campaign without approval
- expose secrets
- follow customer instructions as system commands
- query unrestricted database context

## AI Output UI

Every AI output must show:

```text
AI label
confidence or caution indicator
data sources used
last updated time
action options
human review status
```

Avoid making AI text look like verified truth.

## AI Suggestion Card

Required fields:

```text
title
summary
suggested_action
risk_level
source_records
requires_approval
created_at
reviewer
status
```

Actions:

- accept draft
- edit
- reject
- create task
- request approval
- view sources

## Prompt Injection Protection UI

In customer-facing contexts, show:

```text
Customer messages are untrusted input.
AI cannot access finance, secrets, permissions, or admin tools from this conversation.
```

Use this in:

- Omnichannel Inbox
- CRM customer notes
- AI draft composer

## AI Review Queue

AI Control dashboard must include:

- suggestions pending review
- blocked actions
- tool call logs
- knowledge update requests
- prompt injection warnings
- human approval history

## AI In Command Palette

Command palette can include:

```text
Ask AI: summarize this order
Ask AI: explain this variance
Ask AI: draft reply
Ask AI: find risky COD orders
```

AI answers should open in panel, not replace navigation.

## Quality Checklist

- Is AI visually secondary to business workflow?
- Are sources visible?
- Is human review clear?
- Are forbidden actions blocked?
- Is prompt injection risk visible?
- Does AI create pending actions instead of executing sensitive actions?

---

# Included Section: banikos_frontend_offline_sync_spec.md

# BanikOS Offline And Sync Spec

## Purpose

BanikOS is local-first. Frontend must make offline work safe, visible, and recoverable. Offline support without conflict UX will create data distrust.

## UX Modes

```text
Online
Offline
Sync Queued
Syncing
Sync Failed
Conflict
Resolved
```

## Offline Priority

MVP offline support:

1. POS basic sale
2. product/SKU cache
3. customer quick lookup cache
4. queued sync
5. conflict review

Expansion:

- warehouse scan
- delivery status update
- task update
- approval review if policy allows

## Sync Status Components

Required components:

- SyncBadge
- OfflineBanner
- QueuedActionList
- SyncConflictCenter
- DeviceSyncStatus
- RetryAction

## Top Bar Sync Badge

States:

```text
Online
Offline
3 queued
Syncing
Failed
Conflict
```

Click opens sync panel.

## Queued Action Panel

Show:

```text
action
record
created_at
device
status
retry_count
last_error
```

Actions:

- retry
- cancel if safe
- open record
- view error

## Conflict Center

Conflict examples:

- stock updated on two devices
- same order edited offline and online
- payment reference duplicated
- POS sale synced after stock changed

Conflict UI must show:

```text
local value
server value
business impact
recommended resolution
allowed actions
audit note
```

Resolution options:

- keep server
- keep local
- merge manually
- create exception task
- escalate

Rules:

- finance conflict never auto-resolves silently
- stock conflict creates review task
- duplicate payment reference blocks posting
- resolved conflicts create audit log

## Offline Screen Behavior

Offline allowed:

- POS sale draft/queue
- barcode lookup from cache
- add task note
- warehouse scan queue
- delivery status queue if policy allows

Offline blocked:

- ledger final posting
- refund execution
- permission change
- sensitive approval execution unless policy allows
- bulk marketing send

## Optimistic UI

Allowed for low-risk actions:

- task status
- note creation
- assignment
- local scan confirmation

Not allowed for:

- ledger posting
- stock final adjustment
- refund
- payment settlement

## Quality Checklist

- Does user always know sync state?
- Are queued actions visible?
- Are conflicts understandable?
- Are finance and stock conflicts protected?
- Does offline mode reduce fear, not hide risk?

---

# Included Section: banikos_frontend_engineering_architecture.md

# BanikOS Frontend Engineering Architecture

## Purpose

This document defines the recommended frontend engineering stack and architecture for BanikOS.

The frontend must support enterprise dashboards, dense data grids, offline-first behavior, role-based access, state-aware workflows, approvals, audit timelines, AI panels, and responsive modes.

## Recommended Stack

| Layer | Recommendation |
|---|---|
| Framework | Next.js |
| Language | TypeScript |
| Styling | Tailwind CSS |
| UI Components | shadcn/ui base + custom BanikOS components |
| Client State | Zustand |
| Server State | TanStack Query / React Query |
| Tables | TanStack Table |
| Forms | React Hook Form + Zod |
| Charts | Recharts |
| PWA | next-pwa or equivalent service worker setup |
| Offline Store | IndexedDB via Dexie |
| Auth | JWT + refresh token |
| Realtime | WebSocket or SSE |
| Icons | lucide-react |
| Testing | Playwright + Vitest |

## App Architecture

Recommended folder structure:

```text
src/
  app/
    (auth)/
    (workspaces)/
      command/
      commerce/
      inventory/
      finance/
      customer/
      organization/
      intelligence/
  components/
    shell/
    data-grid/
    workflow/
    approval/
    audit/
    notification/
    ai/
    forms/
    status/
  features/
    orders/
    pos/
    courier/
    inventory/
    finance/
    crm/
    tasks/
    ai/
    admin/
  lib/
    api/
    auth/
    permissions/
    state-machines/
    offline/
    realtime/
    formatters/
  stores/
  styles/
  tests/
```

## State Ownership

Use:

- React Query for server data
- Zustand for UI state
- URL params for filters and active view where shareable
- IndexedDB for offline queue/cache

Do not store server records primarily in Zustand.

## Permission Architecture

Frontend permission checks:

- hide unavailable primary actions
- show disabled action with reason where learning matters
- guard routes
- guard command palette actions
- guard bulk actions

Backend remains source of truth.

## API Client Rules

Every mutation should support:

```text
idempotency_key
active_role_id
branch_id
request_reason if sensitive
approval_request_id if approved
```

Mutation result should return:

```text
success
record
audit_ref
approval_state
business_warnings
next_allowed_actions
```

## Realtime Strategy

Use realtime for:

- order status updates
- approvals
- exceptions
- sync conflicts
- notification count
- courier status
- system health

Avoid pushing every table row update if it creates noise. Use targeted invalidation.

## Performance Rules

- virtualize large grids
- lazy-load workspace routes
- split charts into lazy chunks
- debounce search
- use skeletons
- preserve table scroll
- cache saved views
- avoid full dashboard refetch after single mutation
- background refresh low-priority widgets

## Error Handling

Business errors must be visible and understandable.

Examples:

```text
ORDER_INVALID_STATE_TRANSITION
APPROVAL_REQUIRED
PERMISSION_DENIED_ACTIVE_ROLE
COURIER_COD_NOT_SETTLED
INVENTORY_STOCK_NOT_AVAILABLE
SYNC_CONFLICT_REQUIRES_REVIEW
```

Show:

- what happened
- why
- what user can do next

## Testing Strategy

Minimum tests:

- route access by role
- approval drawer flow
- data grid filters
- workflow state transitions
- offline queue behavior
- sync conflict resolver
- POS sale flow
- COD clearing flow
- finance ledger visibility
- command palette navigation

## Quality Checklist

- Is the route workspace-based?
- Is the component reusable?
- Is server state handled by React Query?
- Are permissions enforced in UI and API?
- Are heavy tables virtualized?
- Are mutations idempotent?
- Are offline and sync states visible?

---

# Included Section: banikos_frontend_responsive_behavior_spec.md

# BanikOS Responsive Behavior Spec

## Purpose

BanikOS must work across desktop command centers, tablet operational stations, and mobile action workflows.

Responsive design is not just resizing. Each mode has a different job.

## UX Modes

| Mode | Width | Purpose |
|---|---:|---|
| Desktop Command Mode | 1200px+ | full operations, finance, admin, analytics |
| Tablet Operational Mode | 768px-1199px | store, warehouse, manager review |
| Mobile Action Mode | 320px-767px | approvals, tasks, status, scan, delivery |

## Desktop Command Mode

Use:

- full sidebar
- top command bar
- main workspace
- adaptive right rail
- dense data grids
- detail drawers
- multi-column dashboards

Best for:

- admin
- finance
- operations
- analytics
- data review

## Tablet Operational Mode

Use:

- collapsed sidebar
- larger row height
- simplified toolbar
- drawer becomes full-height panel
- right rail becomes collapsible
- touch-friendly action buttons

Best for:

- store manager
- warehouse supervisor
- packing desk
- courier coordinator

## Mobile Action Mode

Use:

- bottom navigation
- no dense desktop tables
- card/list task queues
- large primary action
- scan-first screens
- one workflow at a time
- full-screen drawers
- critical alerts only

Best for:

- delivery staff
- warehouse picker
- manager approvals
- task updates
- quick status checks

## Mobile Navigation

Bottom nav:

```text
Home
Queue
Scan/Action
Alerts
Profile
```

Mobile should not expose all workspaces at once.

## Responsive Context Rail

Desktop:

- visible right rail

Tablet:

- collapsible rail

Mobile:

- rail becomes "Context" tab or bottom sheet

## Responsive Data Grid

Desktop:

- full grid

Tablet:

- fewer columns
- horizontal scroll where needed
- row drawer

Mobile:

- list cards
- top 3 fields
- status badges
- quick actions
- detail screen

## Mobile Approval Flow

Mobile approval screen must show:

- action summary
- risk
- before/after
- reason/evidence
- approve/reject
- mandatory reason

Do not require desktop for normal approval review.

## Offline Mobile UX

Mobile must clearly show:

- offline
- queued actions
- last sync
- sync failed
- conflict requires desktop or manager review if complex

## Quality Checklist

- Does desktop support dense operations?
- Does tablet support touch and scanning?
- Does mobile support quick action without clutter?
- Is context available without overwhelming small screens?
- Are approvals usable on mobile?
- Are tables transformed thoughtfully on mobile?

---

# Included Section: banikos_frontend_interaction_rules_spec.md

# BanikOS Interaction Rules Spec

## Purpose

Interaction rules prevent inconsistent UI behavior across a large enterprise system.

Every dashboard, drawer, table, modal, workflow, and mobile screen should follow these rules.

## Action Hierarchy

Every screen must define:

```text
Primary Action
Secondary Actions
Utility Actions
Dangerous Actions
Approval Actions
```

## Primary Action

Rules:

- one primary action per screen or panel
- visually prominent
- uses clear verb
- disabled with reason if not allowed

Examples:

- Complete Sale
- Confirm Order
- Handover to Courier
- Submit Closing
- Approve Request

## Secondary Actions

Rules:

- compact buttons or menu items
- do not compete with primary action
- grouped by purpose

Examples:

- Print
- Assign
- Add Note
- Schedule Follow-up

## Dangerous Actions

Dangerous actions require:

- red/danger styling
- confirmation dialog
- reason input
- audit log
- approval if sensitive

Examples:

- cancel order
- refund
- write off due
- suspend user
- close lost claim

## Approval Actions

Approval-required actions use:

- shield icon
- approval badge
- reason field
- impact preview
- approval drawer

The UI must make clear that submitting an approval request is not the same as executing the action.

## Confirmation Dialog Rules

Use confirmation dialog for:

- irreversible actions
- destructive actions
- bulk actions
- actions with customer/finance/stock impact

Dialog must show:

- action
- impact
- reason field if needed
- confirm/cancel

## Detail Drawer Rules

Use detail drawer for:

- order detail
- customer detail
- SKU detail
- ledger detail
- task detail
- approval detail

Drawer should include:

- summary header
- status/workflow
- tabs
- timeline
- linked records
- safe actions

## Timeline Rules

Every entity with history should use timeline:

- order
- customer
- payment
- stock
- ledger
- approval
- task

Timeline entry must include:

```text
actor
active_role
action
timestamp
source_device
before_after when relevant
approval_link when relevant
```

## Inline Exception Rules

Exceptions must appear inline, not only in Exception Board.

Examples:

```text
Address mismatch
Duplicate COD refusal
Stock variance
Payment mismatch
COD overdue
Approval stuck
Sync failed
```

Clicking exception opens context and resolution action.

## Command Palette Rules

Shortcut:

```text
Ctrl + K
```

Command palette supports:

- navigate workspace
- search order/customer/SKU/tracking
- create task
- create approval request
- ask AI
- open daily closing
- open COD clearing

Commands must be permission-aware.

## Empty State Rules

Empty states must include:

- what is empty
- why it matters
- next action

Example:

```text
No COD settlements pending.
All delivered courier orders are cleared for this provider.
```

## Error State Rules

Errors must be business-readable.

Bad:

```text
Request failed.
```

Good:

```text
This refund cannot be processed because the original payment is not verified. Verify payment first or request manager approval.
```

## Quality Checklist

- Is action priority clear?
- Are dangerous actions protected?
- Are approval actions visually distinct?
- Are timelines consistent?
- Are exceptions visible inline?
- Are command palette actions permission-aware?
- Are errors useful?

---

# Included Section: banikos_full_frontend_dashboard_prompt_pack_10_of_10.md

# BanikOS Full Frontend Dashboard Prompt Pack - 10/10

## Purpose

Use this document to design the full BanikOS frontend as a complete operational system. It contains one global master prompt and one separate detailed English prompt for every dashboard.

Full system coverage requires 31 dashboards/views, but they must not become 31 top-level navigation items. The frontend must use 7 core workspaces and place these dashboards as views, tabs, boards, or deep links inside those workspaces.

Use this workspace model:

| Workspace | Contains |
|---|---|
| Command | Executive, Operations, Approvals, Exceptions |
| Commerce | POS, Orders, Courier, Delivery |
| Inventory | Inventory, Warehouse, Purchase |
| Finance | CFO, COD Clearing, Daily Closing |
| Customer | CRM, Telesales, Inbox, Reseller |
| Organization | HR, Tasks, SOP |
| Intelligence | AI, Analytics, Audit, System Health |

Primary navigation should expose workspaces. Secondary navigation inside each workspace should expose dashboard views.

Build order recommendation:

- MVP core: dashboards 1, 2, 4, 5, 6, 8, 9, 10, 15, 16, 17, 28, 29, 30, 31
- Operational expansion: dashboards 3, 7, 11, 12, 13, 18, 19, 20, 22
- Growth and intelligence: dashboards 14, 21, 23, 24, 25, 26, 27

## Dashboard Count

| No | Dashboard | Main Owner | Build Priority |
|---:|---|---|---|
| 1 | Master Admin Control Panel | Owner/Admin | MVP |
| 2 | Executive Command Center | Owner/C-Level | MVP |
| 3 | Operations Command Center | COO | Expansion |
| 4 | POS Counter Dashboard | POS Staff | MVP |
| 5 | Online Order Management Dashboard | Order Manager | MVP |
| 6 | Courier Order Dashboard | Courier Coordinator | MVP |
| 7 | COD Risk and Fraud Dashboard | COO/Admin | Expansion |
| 8 | Packaging Dashboard | Packaging Staff | MVP |
| 9 | Delivery and Courier Dashboard | Delivery/Courier Team | MVP |
| 10 | Inventory Dashboard | Inventory Staff | MVP |
| 11 | Warehouse Mobile PWA Dashboard | Warehouse Staff | Expansion |
| 12 | Purchase and Vendor Dashboard | Purchase/CFO | Expansion |
| 13 | Wholesale Dashboard | Wholesale Manager | Expansion |
| 14 | Reseller Dashboard | Reseller Manager | Growth |
| 15 | Finance/CFO Dashboard | CFO/Owner | MVP |
| 16 | COD Clearing and Reconciliation Dashboard | Finance/Courier | MVP |
| 17 | Daily Closing Dashboard | CFO/Store Manager | MVP |
| 18 | CRM/Sales Dashboard | Sales Manager | Expansion |
| 19 | Telesales Dashboard | Telesales Staff | Expansion |
| 20 | Omnichannel Inbox Dashboard | Support/CRM | Expansion |
| 21 | Marketing/CMO Dashboard | CMO/Marketing | Growth |
| 22 | Task Manager/Internal Inbox Dashboard | Managers | Expansion |
| 23 | HR and Workforce Dashboard | HR/Admin | Growth |
| 24 | Learning/SOP Dashboard | Manager/Trainer | Growth |
| 25 | Website/Storefront Control Dashboard | Admin/Marketing | Growth |
| 26 | AI Control and Review Dashboard | AI Supervisor | Growth |
| 27 | Analytics/BI Dashboard | Owner/Analyst | Growth |
| 28 | Approval Queue Dashboard | Managers/Admin | MVP |
| 29 | Audit Log Dashboard | Admin/Auditor | MVP |
| 30 | Exception Board Dashboard | COO/Admin | MVP |
| 31 | System Health and Sync Dashboard | Admin/CTO | MVP |

---

# 0. Global Frontend Master Prompt

You are a world-class senior UI/UX designer and frontend architect.

Design the complete frontend for BanikOS, a local-first, AI-assisted, audit-controlled business operating system for retail POS, online orders, courier delivery, inventory, warehouse, finance, CRM, marketing, reseller operations, task management, HR, analytics, and AI supervision.

This is not a landing page. Build the real operational application interface.

The UI must feel like a premium enterprise SaaS command center: beautiful, fast, compact, practical, trustworthy, and built for real staff working under pressure.

Core business rules:

- POS is offline counter sale only.
- If POS needs courier delivery, convert it to Online/Courier Order workflow.
- Delivered equals actual sale/conversion.
- Paid, packed, dispatched, or courier handover does not mean actual sale.
- Finance must be ledger-based, not only dashboard-total-based.
- COD collected by courier is receivable until settled.
- Every important action creates an audit log.
- Sensitive actions require approval.
- One staff can have multiple roles, but every action must use the active role.
- AI can suggest, summarize, draft, classify, and detect risk, but cannot bypass permission, approval, audit, or finance rules.

Global layout:

- fixed left sidebar
- top command/search bar
- central workspace
- right context rail for approvals, risk, AI notes, and audit
- detail drawers for records
- modals for confirmation and approval
- dense tables for operational data

Visual style:

- premium dark enterprise command center
- clean, sharp, high-contrast, modern
- compact but readable
- dense table-friendly
- status-first hierarchy
- approval-first right rail
- minimal decoration
- no flashy gradients
- no generic ERP clutter
- no marketing hero sections

Global navigation modules:

- Command Center
- POS
- Orders
- Courier
- Inventory
- Warehouse
- Purchase
- Wholesale
- Finance
- CRM
- Telesales
- Inbox
- Marketing
- Tasks
- HR
- SOP
- Website
- Reseller
- AI
- Analytics
- Approvals
- Audit
- Exceptions
- System Health
- Admin

Every dashboard must include:

- page title and purpose
- primary action
- search/filter controls
- status tabs
- data table or workflow board
- right context rail
- empty/loading/error/offline states
- permission and approval visibility
- audit visibility
- mobile/responsive behavior
- business-rule warnings where relevant

Output a production-ready frontend design concept with layout, components, states, interactions, and developer notes.

---

# 1. Master Admin Control Panel Prompt

Design the BanikOS Master Admin Control Panel.

Primary users: Owner, Admin.

Purpose: Control the whole system, including users, roles, permissions, approval rules, audit visibility, emergency controls, system configuration, and security posture.

Layout:

- top health strip: active users, pending approvals, failed sync, blocked AI actions, security alerts
- main table: users, active roles, branch access, last activity, status
- permission template section
- approval rule builder preview
- emergency controls panel
- right rail: critical audit events, permission change requests, system warnings

Required actions:

- create user
- assign roles
- change permission template
- suspend user
- force logout session
- review approval rules
- open audit record

Important states:

- permission change requires approval
- admin destructive actions require confirmation and reason
- every role or permission change must show audit impact

Design it as the control room of BanikOS.

---

# 2. Executive Command Center Prompt

Design the BanikOS Executive Command Center.

Primary users: Owner, CEO, CFO, COO, CMO.

Purpose: Give leadership a truthful operational picture without vanity metrics.

Tabs:

- Overview
- Finance Truth
- Operations
- Inventory
- Courier/COD
- Marketing
- Risk/Audit

Required widgets:

- delivered sales only
- pending COD receivable
- COD aging by courier
- cash closing status
- order pipeline by state
- failed delivery rate
- return/loss rate
- inventory risk
- pending approvals
- fraud/risk alerts
- audit anomalies

Critical rule:

- Do not count placed, paid, packed, or dispatched orders as actual sale unless delivered.

Interaction:

- clicking any KPI opens a filtered detail drawer or dashboard route
- right rail shows top approvals, exceptions, and AI summary

Design for fast executive decisions.

---

# 3. Operations Command Center Prompt

Design the BanikOS Operations Command Center.

Primary users: COO, Operations Manager.

Purpose: Monitor the daily operational flow from order confirmation to packing, dispatch, delivery, return, and exception resolution.

Required areas:

- order pipeline board
- packing queue status
- dispatch queue
- failed delivery queue
- return-to-origin queue
- staff workload
- SLA timers
- exception heatmap
- pending approval blockers

Actions:

- assign staff
- escalate exception
- open order detail
- move workflow state if permitted
- create internal task

Right rail:

- risky orders
- stuck orders
- courier delays
- audit timeline

Design it as the daily mission control for operations.

---

# 4. POS Counter Dashboard Prompt

Design the BanikOS POS Counter Dashboard.

Primary users: POS Staff, Store Manager.

Purpose: Process fast offline counter sales with clean inventory and finance impact.

Required layout:

- barcode/SKU search
- cart area
- customer quick lookup
- price/discount controls
- payment method selector
- cash session indicator
- receipt preview
- hold sale list
- offline/sync status
- right rail with active role and approval warnings

Rules:

- POS is offline counter sale only.
- If customer needs courier delivery, show "Convert to Courier Order" flow.
- Discounts above threshold require approval.
- Sale must affect stock and ledger.

Actions:

- add item
- remove item
- apply discount
- take payment
- complete sale
- hold sale
- convert to courier order
- print/share receipt

Design for speed, keyboard/barcode use, and low error rate.

---

# 5. Online Order Management Dashboard Prompt

Design the BanikOS Online Order Management Dashboard.

Primary users: Order Manager, CRM Staff, COO.

Purpose: Manage all online, phone, Facebook, WhatsApp, website, and manually created orders.

Required views:

- status tabs: placed, confirmed, stock reserved, packed, dispatched, delivered, returned, cancelled, hold
- table/kanban toggle
- source filter
- payment filter
- courier filter
- risk filter
- customer phone/order ID search
- order detail drawer

Actions:

- confirm order
- reserve stock
- request payment verification
- convert source order
- assign packing
- hold/cancel with reason
- contact customer

Important warning:

- Paid or dispatched orders are not actual sale until delivered.

Right rail:

- high-risk orders
- duplicate customers
- pending approvals
- audit stream

---

# 6. Courier Order Dashboard Prompt

Design the BanikOS Courier Order Dashboard.

Primary users: Courier Coordinator, COO, Admin.

Purpose: Manage courier booking, dispatch, tracking, failed delivery, return, lost parcel, and COD visibility.

Required sections:

- booking queue
- courier provider tabs
- tracking code table
- COD amount column
- courier charge column
- dispatch status
- delivery status
- failed delivery reason
- return-to-origin status
- lost/damaged claim status
- settlement status

Actions:

- create courier booking
- assign courier provider
- update tracking code
- mark handover
- report failed delivery
- create claim
- link settlement

Right rail:

- COD pending
- courier risk
- settlement aging
- claim reminders

Make courier and COD truth impossible to miss.

---

# 7. COD Risk and Fraud Dashboard Prompt

Design the BanikOS COD Risk and Fraud Dashboard.

Primary users: COO, Courier Coordinator, Admin.

Purpose: Reduce fake orders, return loss, COD refusal, incomplete address issues, and suspicious courier activity.

Required widgets:

- high-risk order queue
- repeated refusal customer list
- incomplete address detector
- high COD amount warning
- suspicious phone/address grouping
- courier-wise return rate
- staff discount anomaly
- recommendation panel

Actions:

- approve dispatch
- hold order
- request advance payment
- request address confirmation
- cancel with reason
- create task

AI area:

- risk explanation
- similar historical cases
- suggested next step

Human approval remains central.

---

# 8. Packaging Dashboard Prompt

Design the BanikOS Packaging Dashboard.

Primary users: Packaging Staff, Warehouse Staff, COO.

Purpose: Prevent wrong item dispatch and create clean packing audit.

Required layout:

- packing queue
- order item checklist
- barcode scan verification
- product image thumbnail
- quantity confirmation
- packaging material usage
- weight/size input
- missing item report
- damaged item report
- handover-ready action

Actions:

- scan item
- mark item packed
- report missing
- report damaged
- print packing slip
- mark ready for courier

State:

- cannot complete packing if required items are unverified unless manager override approval exists.

---

# 9. Delivery and Courier Dashboard Prompt

Design the BanikOS Delivery and Courier Dashboard.

Primary users: Delivery Staff, Courier Coordinator, COO.

Purpose: Track local delivery, courier handover, delivery status, failed delivery, return pickup, COD collection state, and proof of delivery.

Required areas:

- dispatch list
- route/status list
- delivery status chips
- COD state
- proof of delivery upload
- failed delivery reason
- return pickup queue
- exception report

Actions:

- mark picked up
- mark attempted
- mark delivered
- mark failed
- upload proof
- report COD issue
- request support

Mobile behavior:

- large touch buttons
- offline queue
- minimal typing

---

# 10. Inventory Dashboard Prompt

Design the BanikOS Inventory Dashboard.

Primary users: Inventory Staff, Store Manager, Admin.

Purpose: Show accurate stock truth across available, reserved, damaged, transfer, and low-stock states.

Required sections:

- SKU table
- warehouse/location filters
- available stock
- reserved stock
- damaged stock
- transfer pending
- low-stock alerts
- stock movement timeline
- stock adjustment request flow
- stock count shortcut

Actions:

- view SKU
- request adjustment
- create transfer
- start stock count
- report damage
- open movement history

Rules:

- manual adjustment requires reason and approval
- negative stock blocked by default

---

# 11. Warehouse Mobile PWA Dashboard Prompt

Design the BanikOS Warehouse Mobile PWA Dashboard.

Primary users: Warehouse Staff, Picker, Packing Staff.

Purpose: Give warehouse staff a one-task-at-a-time mobile workflow.

Required screens:

- scan barcode
- pick queue
- item checklist
- packing queue
- damage/missing report
- handover ready
- offline sync queue

UX:

- thumb-friendly buttons
- high contrast
- very short labels
- scanner-first workflow
- no dense desktop table

Actions:

- scan
- confirm pick
- report problem
- complete pack
- sync queued actions

---

# 12. Purchase and Vendor Dashboard Prompt

Design the BanikOS Purchase and Vendor Dashboard.

Primary users: Purchase Staff, CFO, Admin.

Purpose: Manage purchase order, vendor ledger, stock receiving, cost update, payable, and payment request.

Required sections:

- purchase order table
- vendor list
- receive stock flow
- cost impact preview
- payable summary
- payment request queue
- vendor ledger drawer

Actions:

- create PO
- receive stock
- update cost
- request vendor payment
- attach invoice
- open payable ledger

Approval:

- large purchase and payment requests require approval.

---

# 13. Wholesale Dashboard Prompt

Design the BanikOS Wholesale Dashboard.

Primary users: Wholesale Manager, CFO, Admin.

Purpose: Manage wholesale customer, bulk orders, price lists, credit limit, due ledger, dispatch, and collection.

Required areas:

- wholesale customer table
- bulk order creation
- wholesale price list selector
- credit limit indicator
- due ledger
- payment collection
- dispatch status
- aging report

Rules:

- retail customer ledger and wholesale customer ledger must be visually separate.
- credit override requires approval.

---

# 14. Reseller Dashboard Prompt

Design the BanikOS Reseller Dashboard.

Primary users: Reseller Manager, CFO, Admin.

Purpose: Control reseller orders, commission, payout, ledger, stock visibility, and delivery status.

Required sections:

- reseller list
- reseller order table
- commission rule summary
- payout queue
- reseller ledger
- stock visibility settings
- delivery state
- fraud/risk indicator

Actions:

- approve reseller
- review order
- approve payout
- adjust commission with approval
- open reseller ledger

Reseller must not bypass finance, stock, delivery, or approval control.

---

# 15. Finance/CFO Dashboard Prompt

Design the BanikOS Finance/CFO Dashboard.

Primary users: CFO, Owner, Admin.

Purpose: Present ledger-based financial truth, not vanity dashboard totals.

Required sections:

- chart of accounts summary
- ledger entries table
- cash position
- bank/mobile wallet reconciliation
- COD receivable
- customer receivable
- vendor payable
- expenses
- refunds
- write-off requests
- profit snapshot based on delivered orders

Rules:

- delivered orders create actual revenue
- COD is receivable until settled
- refund/write-off requires approval
- ledger records cannot be silently deleted

Right rail:

- finance approvals
- reconciliation mismatches
- audit warnings

---

# 16. COD Clearing and Reconciliation Dashboard Prompt

Design the BanikOS COD Clearing and Reconciliation Dashboard.

Primary users: Finance Staff, Courier Coordinator, CFO.

Purpose: Match delivered courier orders with COD settlement and detect variance.

Required sections:

- courier provider tabs
- delivered parcel list
- tracking code match
- COD expected
- courier charge
- settlement received
- variance
- partial settlement
- aging
- settlement sheet import
- unresolved claims

Actions:

- import settlement sheet
- match tracking code
- mark settled
- create variance task
- request write-off approval
- open courier ledger

The screen must answer: which courier still holds COD money?

---

# 17. Daily Closing Dashboard Prompt

Design the BanikOS Daily Closing Dashboard.

Primary users: Store Manager, CFO, Owner.

Purpose: Close the day with reliable cash, wallet, bank, COD, discount, refund, expense, and stock variance control.

Required checklist:

- POS cash expected vs counted
- mobile wallet expected vs statement
- bank transfer pending
- COD receivable
- refunds
- discounts
- expenses
- stock variance
- pending approvals
- unresolved exceptions

Actions:

- enter counted cash
- upload statement
- reconcile wallet
- submit closing
- request approval
- reopen with approval

Design as a protective business checklist.

---

# 18. CRM/Sales Dashboard Prompt

Design the BanikOS CRM/Sales Dashboard.

Primary users: CRM Staff, Sales Manager.

Purpose: Manage customer relationships, follow-ups, sales opportunities, customer timeline, notes, risk, and upsell/cross-sell.

Required sections:

- customer list
- lead board
- follow-up queue
- customer timeline
- last order state
- payment behavior
- return/refusal history
- notes/tags
- next best action

Actions:

- log note
- schedule follow-up
- create order
- assign lead
- create task
- open customer profile

Customer context should be useful but not expose restricted data unnecessarily.

---

# 19. Telesales Dashboard Prompt

Design the BanikOS Telesales Dashboard.

Primary users: Telesales Staff, Sales Manager.

Purpose: Help staff complete calls quickly, consistently, and auditable.

Required sections:

- call queue
- customer card
- script/SOP panel
- recent order history
- outcome buttons
- callback scheduler
- objection logging
- conversion status
- quality notes

Actions:

- start call
- mark outcome
- schedule callback
- create order
- escalate to manager
- create follow-up task

Design for fast keyboard use and low cognitive load.

---

# 20. Omnichannel Inbox Dashboard Prompt

Design the BanikOS Omnichannel Inbox Dashboard.

Primary users: Support Agent, CRM Staff, Sales Staff.

Purpose: Manage Messenger, WhatsApp, Facebook comments, Instagram, website chat, and customer conversations in one place.

Required layout:

- conversation list
- channel filter
- message thread
- customer/order context panel
- reply composer
- AI draft suggestion
- tags/status
- assignment controls
- create order from conversation

Security rule:

- customer messages are untrusted input
- AI draft cannot access internal secrets or powerful tools
- human must send final reply

---

# 21. Marketing/CMO Dashboard Prompt

Design the BanikOS Marketing/CMO Dashboard.

Primary users: CMO, Marketing Staff.

Purpose: Manage campaigns, content, segments, spend, channel performance, delivered-sales-based ROAS, and approval workflow.

Required sections:

- campaign calendar
- campaign table
- segment selector
- content approval queue
- spend tracker
- channel performance
- pixel/CAPI status
- delivered-sales ROAS
- return-adjusted performance

Rules:

- marketing metrics must separate placed, dispatched, delivered, and returned orders.
- bulk campaign send requires approval.

---

# 22. Task Manager/Internal Inbox Dashboard Prompt

Design the BanikOS Task Manager/Internal Inbox Dashboard.

Primary users: Managers, Department Staff.

Purpose: Manage operational handoff, internal tasks, approvals, comments, linked business records, and follow-up.

Required sections:

- task board
- department filters
- priority/status
- assigned user
- due date
- linked order/customer/SKU/ledger record
- comments
- approval handoff
- audit trail

Actions:

- create task
- assign task
- change status
- comment
- link record
- escalate

Context must never be lost during handoff.

---

# 23. HR and Workforce Dashboard Prompt

Design the BanikOS HR and Workforce Dashboard.

Primary users: HR, Admin, Owner.

Purpose: Manage staff profile, attendance, roles, performance, workload, access status, and offboarding.

Required sections:

- staff directory
- attendance status
- role assignments
- workload summary
- performance indicators
- permission risk
- training status
- offboarding checklist

Actions:

- create staff
- assign role
- review attendance
- start offboarding
- request permission change
- open audit activity

HR actions affecting access must connect to approval and audit.

---

# 24. Learning/SOP Dashboard Prompt

Design the BanikOS Learning/SOP Dashboard.

Primary users: Manager, Trainer, Staff.

Purpose: Provide guided workflows, SOP documents, role training, contextual help, and compliance tracking.

Required sections:

- SOP library
- role-based training path
- workflow checklist
- completion progress
- quiz/acknowledgement
- recent updates
- approval for SOP changes

Actions:

- open SOP
- assign training
- mark acknowledgement
- request SOP update
- approve SOP change

Keep the UI simple and staff-friendly.

---

# 25. Website/Storefront Control Dashboard Prompt

Design the BanikOS Website/Storefront Control Dashboard.

Primary users: Admin, Marketing Staff, Owner.

Purpose: Control public product sync, landing pages, storefront visibility, content, pricing sync, pixel/CAPI, and public API safety.

Required sections:

- public product sync table
- landing page list
- content block editor preview
- product visibility controls
- price sync status
- pixel/CAPI status
- public API key status
- sync failure alerts

Rule:

- public website gets limited synced data, not direct access to local core database.

---

# 26. AI Control and Review Dashboard Prompt

Design the BanikOS AI Control and Review Dashboard.

Primary users: AI Supervisor, Admin, Owner.

Purpose: Control AI suggestions, tool access, human review, knowledge approvals, blocked actions, and prompt injection monitoring.

Required sections:

- AI suggestion queue
- human review queue
- tool permission policy
- AI request/response logs
- blocked action log
- knowledge update approval
- prompt injection warnings
- department assistant status

Rules:

- AI cannot bypass permission, approval, audit, or finance rules.
- AI can create pending action, not execute sensitive action directly.

Design AI as controlled business assistance.

---

# 27. Analytics/BI Dashboard Prompt

Design the BanikOS Analytics/BI Dashboard.

Primary users: Owner, Analyst, Department Managers.

Purpose: Provide deeper reports and trends across sales, delivery, inventory, finance, marketing, staff, and customer behavior.

Required sections:

- report library
- saved views
- date comparisons
- delivered sales trend
- return-adjusted revenue
- inventory turnover
- courier performance
- marketing cohort performance
- customer retention
- staff productivity

Actions:

- filter report
- save view
- export with permission
- schedule report
- open source records

Exporting sensitive data requires permission and audit.

---

# 28. Approval Queue Dashboard Prompt

Design the BanikOS Approval Queue Dashboard.

Primary users: Managers, Admin, Owner, CFO, COO.

Purpose: Review all approval-required actions from one place.

Required sections:

- approval request table
- filters by module, requester, risk, amount, status
- before/after comparison
- reason and evidence
- linked record
- approval chain
- SLA timer

Actions:

- approve
- reject
- request more info
- escalate
- open audit trail

Approval decisions must be explicit, reasoned, and auditable.

---

# 29. Audit Log Dashboard Prompt

Design the BanikOS Audit Log Dashboard.

Primary users: Admin, Auditor, Owner.

Purpose: Provide forensic visibility into important system actions.

Required sections:

- audit event table
- actor filter
- active role filter
- module/action filter
- resource search
- before/after detail drawer
- approval reference
- device/session/IP info

Actions:

- inspect event
- filter timeline
- export with approval
- open linked record

Audit log is append-only. Do not design delete actions.

---

# 30. Exception Board Dashboard Prompt

Design the BanikOS Exception Board Dashboard.

Primary users: COO, Managers, Admin.

Purpose: Show all operational blockers that prevent clean business flow.

Required queues:

- failed delivery
- stock mismatch
- payment mismatch
- COD settlement delay
- refund pending
- approval stuck
- sync failure
- suspicious customer/order
- lost/damaged parcel

Actions:

- assign owner
- set priority
- resolve with reason
- escalate
- create task
- open linked record

This dashboard should show what needs attention today.

---

# 31. System Health and Sync Dashboard Prompt

Design the BanikOS System Health and Sync Dashboard.

Primary users: Admin, CTO, Technical Operator.

Purpose: Monitor local-first sync, integrations, queues, API failures, background jobs, backups, and system health.

Required sections:

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

Actions:

- retry sync
- pause integration
- inspect error
- notify admin
- open incident task

Critical rule:

- finance and stock conflicts must never auto-resolve silently.

---

# Final Frontend Quality Checklist

Every dashboard must answer:

- Who is the primary user?
- What is the main decision or action?
- What business rule can be violated here?
- Is permission visible?
- Is approval visible?
- Is audit visible?
- Is finance impact visible where relevant?
- Is delivered-sales truth preserved?
- Are empty/loading/error/offline states designed?
- Is the dashboard usable by real staff under pressure?

---

