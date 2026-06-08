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
