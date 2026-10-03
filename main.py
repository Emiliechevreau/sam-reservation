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
    "chauffeur_1": "de424181d6c86685839a30b9b9c62db6de45a97323c678896394bbe92cbfbff1@group.calendar.google.com",
    "chauffeur_2": "d617dbb297331365d1ba8d59e18af95a7f70db29db08d2ffefcd0b12022636e6@group.calendar.google.com",
    "chauffeur_3": "a599d3ea5281ef706263421ede3b3f00ebf8c32cad2cd5760016d44acee16942@group.calendar.google.com",
    "chauffeur_4": "a64652188ddba34bfc5b473fe018b3c10e0e4d82155b301ed4574e7f09a2b1ea@group.calendar.google.com",
    "chauffeur_5": "4134ac1dfa30a995a19ba3f584b5fda017ccedfc8ce9eef9e1ce9291640b6916@group.calendar.google.com",
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
            creds = flow.run_local_server(port=8080)
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
