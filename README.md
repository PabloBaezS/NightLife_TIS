# Nightlife

![Logo Nightlife](https://github.com/user-attachments/assets/5797db7a-3cc3-419f-914d-2b5d1a416ab5)

**Nightlife** is a mobile-first application designed to streamline the booking and purchasing experience in nightclubs across Medellín. The app allows users to reserve tables, buy tickets, and access exclusive club offers. Nightlife also includes an admin interface for nightclub owners to manage their offerings.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## Project Overview

**Nightlife** is a project aimed at simplifying the nightlife experience in Medellín. Users can browse, reserve tables, buy tickets, and manage their nightclub experiences directly from their mobile devices. Club administrators can update reservations, manage bookings, and customize offerings in real-time through a robust admin interface.

This project is part of a larger initiative for improving user interaction with businesses using a modern, mobile-friendly web interface backed by Django.

### Key Stakeholders

- **Users**: Individuals looking to reserve tables, buy tickets, and access other services at nightclubs.
- **Club Administrators**: Nightclub owners who will use the admin section to manage reservations, update availability, and monitor user activities.

### Scope

The app will offer the following:
- Reservation of tables and other nightclub services.
- Purchase of tickets for events or special offers.
- A comprehensive admin interface for nightclubs to manage their services.
- Mobile-first user interface to provide a seamless experience.

---

## Features

- **User Section**:
  - Browse nightclubs and available services.
  - Reserve tables, tickets, and exclusive packages.
  - View past and upcoming reservations.
  
- **Admin Section**:
  - Manage club services, availability, and pricing.
  - View and process user reservations.
  - Generate reports on bookings and sales.
  
- **Interesting Functionalities**:
  - Search for available services by date and club name.
  - Generate PDF invoices for reservations and ticket purchases.
  - View top 3 most reserved clubs or services.
  - Track reservation status and receive push notifications for updates.

---

## Technologies

The following technologies will be used to build Nightlife:

- **Django 4.2.16**: Backend framework
- **SQLite3**: Default database for development
- **HTML/CSS**: For basic templating and styling
- **Bootstrap**: For responsive design
- **JavaScript**: For dynamic content loading and user interactivity
- **Django REST Framework**: API for mobile app functionality (optional)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PabloBaezS/NightLife_TIS.git
   ```

2. Navigate to the project directory:

   ```bash
   cd NightLife_TIS
   ```

3. Set up a virtual environment and install dependencies:

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the app via `http://127.0.0.1:8000/`.

---

## Usage

- **User Interface**: Accessible via the root route (`/`), where users can browse available nightclubs and make reservations.
- **Admin Interface**: Access the admin panel at `/admin/` to manage bookings, update services, and view sales.

## License

This project is licensed by the creators.
