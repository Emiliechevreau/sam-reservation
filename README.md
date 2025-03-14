# SAM — Ride Booking and Management Application

SAM is a Flask web application for managing ride **bookings**, **tracking**, **cancellations**, and **billing**. It synchronizes time slots with **Google Calendar** and stores operational data in Excel workbooks.

> Portfolio version: the original application code has been preserved. The repository was cleaned up and documented to make it clearer and safer to publish on GitHub.

## Project Background

This application was developed as a fourth-year Innovation and Industry Project at ESILV. The student team worked with the City of Asnières-sur-Seine to explore how the Municipal Accompaniment Service (SAM) could modernize its transportation booking process for elderly residents.

The existing workflow relied mainly on phone calls and paper records. This created a significant administrative workload and made it difficult for municipal staff to coordinate bookings, drivers, cancellations, and billing. The project therefore aimed to turn this manual process into a simple digital workflow for staff and drivers while keeping the interface accessible to non-technical users.

The team analyzed the municipality's needs, translated them into functional requirements, and refined the solution through interviews, prototypes, regular meetings, and user feedback. Because the underlying information was confidential, the application was developed with fictitious Excel and CSV data. Google Calendar integration was added to connect reservations directly to drivers' calendars.

The result is a functional prototype and proof of concept. It demonstrates how the SAM workflow could be digitalized, but it was not designed to directly replace the municipality's existing software. The project also produced technical documentation, user documentation, presentations, and a visual poster.

## Overview

The web interface allows users to:

- authenticate before accessing the dashboard;
- search for a customer in an Excel database while tolerating input variations;
- create a booking and calculate its price based on the journey type;
- assign a ride to a driver and create the corresponding Google Calendar event;
- record rides in an Excel summary workbook;
- view quarterly billing summaries for each customer;
- search for and cancel a booking;
- apply cancellations to Google Calendar and the billing data.

## Tech Stack

| Area | Technologies |
| --- | --- |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript, Jinja |
| Data | pandas, openpyxl, Excel `.xlsx` |
| Matching | RapidFuzz |
| Integration | Google Calendar API, OAuth 2.0 |
| Runtime | Local Flask application |

## Repository Structure

```text
sam-reservation-portfolio/
├── app.py                     # Main Flask application
├── main.py                    # Google Calendar utility script
├── templates/                 # HTML and Jinja2 pages
├── images/                    # Original graphic assets
├── docs/
│   ├── ARCHITECTURE.md        # Application flows and components
│   ├── DATA_FILES.md          # Expected Excel workbook structure
│   ├── SECURITY.md            # Publication and deployment precautions
│   └── SETUP.md               # Detailed installation guide
├── credentials.example.json   # OAuth example without secrets
├── requirements.txt           # Python dependencies
├── .gitignore                 # Secrets, local data, and temporary files
├── .editorconfig              # Editor conventions
└── CONTRIBUTING.md            # Contribution guidelines
```

### Why do `app.py` and `templates/` remain at the repository root?

The application currently relies on relative paths for `credentials.json`, `token.json`, `Base_de_donnees.xlsx`, and `Récapitulatif_Courses.xlsx`, as well as Flask's standard `templates/` convention. Moving these files without changing the code could break the application, so the portfolio version keeps the existing layout.

## Quick Start After Cloning

The files in `templates/` are **Flask templates**. They are not designed to be opened directly by double-clicking the HTML files. Start the Flask server first, then open the application in a browser.

### 1. Clone the repository

```bash
git clone <GITHUB_REPOSITORY_URL>
cd sam-reservation-portfolio
```

Replace `<GITHUB_REPOSITORY_URL>` with the HTTPS or SSH URL shown under the repository's **Code** button on GitHub.

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the web application

```bash
python app.py
```

By default, Flask starts at:

```text
http://127.0.0.1:5000
```

Open this address in a browser. The home page redirects to the login screen.

**Demo credentials currently defined in the code:**

```text
Username: admin
Password: password123
```

After signing in, users can access the dashboard and navigate between the application pages.

### 5. Available pages

| Local URL | Purpose |
| --- | --- |
| `http://127.0.0.1:5000/login` | Login |
| `http://127.0.0.1:5000/` | Dashboard and home page |
| `http://127.0.0.1:5000/formulaire` | New booking |
| `http://127.0.0.1:5000/summary` | Customer summary |
| `http://127.0.0.1:5000/annulation` | Ride cancellation |

> The interface and navigation can be started after installing the Python dependencies. Some business operations also require the local Excel workbooks and Google Calendar credentials described below.

## Full Configuration

The booking, billing, and Google Calendar synchronization features require two additional components.

### Excel workbooks

The application expects these files at the repository root:

```text
Base_de_donnees.xlsx
Récapitulatif_Courses.xlsx
```

They are excluded from the portfolio version to avoid publishing personal or operational data. Their expected structure is documented in [`docs/DATA_FILES.md`](docs/DATA_FILES.md).

### Google Calendar

1. Create a project in Google Cloud Console.
2. Enable the **Google Calendar API**.
3. Create OAuth credentials for a **Desktop application**.
4. Download the OAuth JSON file.
5. Place it at the repository root with the exact name `credentials.json`.
6. Restart `python app.py` if necessary.

The first operation that requires Google Calendar starts the OAuth flow and generates a local `token.json` file. Both files are ignored by Git and must never be published.

A secret-free example is provided in `credentials.example.json`.

### Stop the server

In the terminal where Flask is running, press:

```text
Ctrl + C
```

See [`docs/SETUP.md`](docs/SETUP.md) for detailed configuration and troubleshooting information.

## Main Workflow

```text
Login
   ↓
Dashboard
   ├── New booking
   │      ↓
   │  Customer search → Price calculation → Google Calendar → Excel
   │
   ├── Customer summary
   │      ↓
   │  Read Excel database → Quarterly summary
   │
   └── Cancellation
          ↓
      Ride search → Calendar deletion → Excel update
```

## Technical Features

- Flask routes with Jinja rendering and JSON responses;
- session management for access control;
- Excel workbook reading and writing;
- name normalization and accent removal;
- fuzzy matching with `RapidFuzz`;
- Google Calendar event creation and deletion;
- quarterly billing logic;
- multiple drivers managed through separate calendars;
- platform-specific Excel file opening on Windows, macOS, and Linux.

## Security and Limitations

This application is a prototype and requires additional hardening before a production deployment:

- login credentials are currently defined in the code;
- the Flask session key is defined in the code;
- calendar identifiers are present in the code;
- data is stored in local Excel workbooks rather than a transactional database;
- OAuth secrets are designed for local use;
- the original version does not include an automated test suite.

These points are documented without changing the application code. See [`docs/SECURITY.md`](docs/SECURITY.md).

## Documentation

- [Detailed installation guide](docs/SETUP.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Data files](docs/DATA_FILES.md)
- [Security](docs/SECURITY.md)
- [Contribution guidelines](CONTRIBUTING.md)

## Portfolio Context

This repository demonstrates:

- the design of an end-to-end booking workflow;
- third-party API integration through OAuth 2.0;
- Excel data processing with Python;
- user input processing with fuzzy matching;
- development of a multi-page Flask web application;
- synchronization between a web interface, local data, and an external calendar.

## License

No license has been added automatically. Before publishing the repository, add a license that accurately reflects the project's ownership and contributors' rights.
