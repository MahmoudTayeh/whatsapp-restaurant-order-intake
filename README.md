# WhatsApp Restaurant Order Intake & Staff Dashboard (Starter MVP)

This project automates restaurant order intake via WhatsApp and publishes confirmed orders to a restaurant-specific staff interface.

## Project Overview

The system acts as a middleware layer between WhatsApp customers and restaurant staff operations:
- **Input:** WhatsApp customer messages (via provider webhook)
- **Processing:** Conversation flow + order building + validation + persistence
- **Output:** Order displayed in staff dashboard

## Tech Stack

- **Backend:** Django + Django REST Framework (DRF)
- **Database:** SQLite (for MVP) / PostgreSQL (recommended for production)
- **Frontend:** React + TypeScript
- **WhatsApp Integration:** Meta WhatsApp Cloud API (or equivalent)

## Core Features

- **Multi-Tenant Routing:** Identify restaurant by inbound identifier.
- **Session Management:** Maintain customer conversation state.
- **Menu Presentation:** Dynamic menu display on WhatsApp.
- **Order Building:** Cart management via chat.
- **Staff Dashboard:** Real-time order management for kitchen staff.

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install django djangorestframework django-cors-headers
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

## API Endpoints

- **Webhook:** `POST /api/chat/webhook/whatsapp/` - Receives WhatsApp messages.
- **Orders:** `GET /api/orders/` - Lists orders for the dashboard.
- **Admin:** `/admin/` - Manage restaurants, menus, and orders.
