import datetime as dt
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Dictionnaire des chauffeurs avec leurs identifiants de calendrier
chauffeurs_calendars = {
    "chauffeur_1": "b304705d464df259f4ac5386ca60a84e80369f4c5addcec12cc9a17ee6b69017@group.calendar.google.com",
    "chauffeur_2": "dacdd5c9691cddf8feeef9b4897752b788f838ed4918982f65df8c250c61cace@group.calendar.google.com",
    "chauffeur_3": "1d37cc0687ce0462b489b0ef31dd4cc0a9dd01cfcda5dd0a4f816b5705265b2b@group.calendar.google.com",
    "chauffeur_4": "1845cd7fba2e73d44394bab7a0d9c7c036fff9e8ee855783d44625aae74a65e5@group.calendar.google.com",
    "chauffeur_5": "a73d79a42fdcdfa87c248b94d1052c78955ece9a5d59a3f25709ef8ad82a3bd3@group.calendar.google.com",
}

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        # Récupérer les événements pour chaque chauffeur
        now = dt.datetime.now().isoformat() + "Z"  # 'Z' indique UTC
        for chauffeur, calendar_id in chauffeurs_calendars.items():
            print(f"\nPlanning pour {chauffeur}:")
            events_result = service.events().list(
                calendarId=calendar_id,
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            ).execute()

            events = events_result.get("items", [])

            if not events:
                print("  Aucun événement trouvé.")
                continue

            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                print(f"  {start} - {event.get('summary', 'Sans titre')}")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
