# WhatsApp Restaurant Order Intake & Staff Dashboard (Starter MVP)

This project automates restaurant order intake via WhatsApp and publishes confirmed orders to a restaurant-specific staff interface.

## Project Overview

The system acts as a middleware layer between WhatsApp customers and restaurant staff operations:
- **Input:** WhatsApp customer messages (via provider webhook)
- **Processing:** Conversation flow + order building + validation + persistence
- **Output:** Order displayed in staff dashboard

## Tech Stack

- **Backend:** Django + Django REST Framework (DRF)
- **Database:** PostgreSQL (recommended)
- **Frontend:** React (for Staff Dashboard)
- **WhatsApp Integration:** Meta WhatsApp Cloud API (or equivalent)

## Core Features

- **Multi-Tenant Routing:** Identify restaurant by inbound identifier.
- **Session Management:** Maintain customer conversation state.
- **Menu Presentation:** Dynamic menu display on WhatsApp.
- **Order Building:** Cart management via chat.
- **Staff Dashboard:** Real-time order management for kitchen staff.

## Getting Started

(Instructions for setup will be added as implementation progresses)
