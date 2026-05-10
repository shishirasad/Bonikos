---
colors:
  primary: "#8b5cf6"
  background: "#0f172a"
  surface: "rgba(30, 41, 59, 0.7)"
  surface-hover: "rgba(30, 41, 59, 0.9)"
  text-primary: "#ffffff"
  text-muted: "#94a3b8"
  success: "#10b981"
  warning: "#f59e0b"
  danger: "#ef4444"
  border-glass: "rgba(255, 255, 255, 0.1)"

typography:
  font-family-base: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
  font-family-heading: "Inter, ui-sans-serif, system-ui, -apple-system, sans-serif"
  h1: "2.25rem; 700; tracking-tight; leading-tight"
  h2: "1.5rem; 600; tracking-tight; leading-snug"
  h3: "1.125rem; 600; tracking-tight; leading-snug"
  body-lg: "1.125rem; 400; leading-relaxed"
  body: "0.875rem; 400; leading-relaxed"
  label: "0.75rem; 500; uppercase; tracking-wider"

spacing:
  page-pad: "2rem"
  card-pad: "1.5rem"
  gap-xs: "0.5rem"
  gap-sm: "0.75rem"
  gap-md: "1rem"
  gap-lg: "1.5rem"
  gap-xl: "2rem"

radii:
  sm: "0.25rem"
  md: "0.375rem"
  lg: "0.5rem"
  xl: "0.75rem"
  2xl: "1rem"
  3xl: "1.5rem"
  full: "9999px"

shadows:
  sm: "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
  md: "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
  glow: "0 0 15px rgba(139, 92, 246, 0.5)"
  ambient: "0 25px 50px -12px rgba(0, 0, 0, 0.5)"
  glass: "inset 0 1px 0 0 rgba(255, 255, 255, 0.1)"

elevation:
  app-container: "ambient"
  card: "glass"
  dropdown: "md"

motion:
  duration-fast: "150ms"
  duration-normal: "200ms"
  duration-slow: "300ms"
  easing-default: "cubic-bezier(0.4, 0, 0.2, 1)"
---

# Design System: GlassERP (Premium Dark Mode SaaS)

This document outlines the design intent and visual identity for our premium multi-tenant SaaS ERP platform. The aesthetic is heavily inspired by modern "glassmorphism" running on a deep, immersive dark canvas. 

## Look and Feel

The interface is designed to evoke the feeling of a state-of-the-art command center. It is undeniably a dark-mode-first application, eschewing traditional flat designs for a layout that feels layered, deep, and highly premium.

*   **Vibe:** Futuristic, professional, high-tech, and incredibly clean. It should wow the user instantly.
*   **The Canvas:** The root background is a solid deep slate (`#0f172a`), serving as the infinite canvas for the application.
*   **The App Container:** The primary application window floats above this canvas, utilizing a very large border radius (`3xl` / 24px) and casting a deep, ambient shadow (`ambient`). 
*   **Surface Depth:** Data cards, sidebar sections, and functional panels do not use opaque colors. Instead, they utilize the `surface` token (a semi-transparent slate `rgba(30, 41, 59, 0.7)`) combined with a strong backdrop blur. This creates a frosted glass effect that allows the underlying deep background to subtly show through.

## Core Visual Signatures

### Glassmorphism
The cornerstone of this design system is the glass effect. Every floating container or card must:
1. Use the semi-transparent `surface` color.
2. Apply a heavy CSS `backdrop-filter: blur(12px)`.
3. Be framed by an ultra-thin, low-opacity white border (`border-glass`) to catch the simulated light and define the edge against the dark background.

### Neon/Glow Accents
To contrast against the dark, muted slate tones, the primary action color is a vivid Violet (`#8b5cf6`).
*   **Primary Buttons:** Use the solid primary violet color. When hovered, they should not just change color—they should emit a soft outer glow (`shadow-glow`) to signify interactivity.
*   **Active States:** Selected menu items or active tabs should feature a subtle left-border or bottom-border indicator using the primary violet.

### Typography & Contrast
The entire UI relies on the **Inter** typeface for its pristine legibility and modern geometric proportions.
*   **High Emphasis:** Page titles, primary metrics, and core data use stark white (`text-primary`).
*   **Muted Information:** Table headers, timestamps, and secondary descriptions drop back to a soft slate grey (`text-muted`). This contrast is critical to prevent the dense ERP data from overwhelming the user.

## Component Intent

### Cards
Cards are the primary structural building block. They use a `2xl` (16px) border radius to feel soft and approachable despite the high-tech styling. The inner content is heavily padded (`card-pad`) to maintain whitespace and breathability.

### Inputs and Forms
Form fields should blend into the glass aesthetic. They should have a slightly darker or more opaque background than the cards they sit on, utilizing a smaller `lg` (8px) border radius. Focus states should transition the border to the primary violet (`#8b5cf6`) smoothly over `150ms`.

### Motion
Animations should feel snappy but fluid. Micro-interactions like hovering a table row or button should use the `duration-fast` transition. Modal entrances and slide-over drawers should use `duration-normal` with the `easing-default` curve to feel deliberate and premium without slowing the user down.
