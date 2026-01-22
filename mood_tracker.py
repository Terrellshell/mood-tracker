# mood tracker v1.1 - test
# Triggering GitHub Desktop change detection
# test changes
"""
Mood Tracker v2.0
Collects a daily mood rating (1–5), logs it to a CSV file,
and reports a 7-day average with a helpful message.
"""

import csv
from datetime import date, timedelta

LOG_FILE = "mood_log.csv"


def ensure_log_file(filename=LOG_FILE):
    """Create the CSV file with headers if it doesn't exist."""
    try:
        with open(filename, "r"):
            pass
    except FileNotFoundError:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "mood"])


def log_mood(mood, filename=LOG_FILE):
    """Append today's mood to the log file."""
    today = date.today().isoformat()
    ensure_log_file(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, mood])


def read_recent_moods(days=7, filename=LOG_FILE):
    """Return a list of mood values from the last `days` days."""
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        return []

    cutoff = date.today() - timedelta(days=days)
    recent = []

    for row in rows:
        row_date = date.fromisoformat(row["date"])
        if row_date >= cutoff:
            recent.append(int(row["mood"]))

    return recent


def calculate_average(moods):
    """Return the average mood or None if no data."""
    if not moods:
        return None
    return sum(moods) / len(moods)


def get_message(average_mood):
    """Return a message based on the user's recent mood trend."""
    if average_mood is None:
        return "No data yet. Today is Mood Day Zero."
    if average_mood < 2:
        return "Rough stretch. Be gentle with yourself."
    if average_mood < 3.5:
        return "Holding steady. Small wins still count."
    return "Trend is up. Keep riding that wave."


def main():
    """Main program loop: get mood, log it, report stats."""
    raw = input("Enter today's mood (1–5): ")

    try:
        mood = int(raw)
        if not 1 <= mood <= 5:
            raise ValueError
    except ValueError:
        print("Please enter a number between 1 and 5.")
        return

    log_mood(mood)
    recent = read_recent_moods()
    avg = calculate_average(recent)

    print()
    if avg is not None:
        print(f"Your {len(recent)}-day average mood is: {avg:.2f}")
    else:
        print("No recent mood data to average yet.")

    print(get_message(avg))


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
