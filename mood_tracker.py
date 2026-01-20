# test changes
import csv
from datetime import date, timedelta

LOG_FILE = "mood_log.csv"

def log_mood(mood, filename=LOG_FILE):
    """Append today's mood to the log file."""
    today = date.today().isoformat()

    # Ensure file exists with header
    try:
        with open(filename, "r") as file:
            pass
    except FileNotFoundError:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "mood"])

    # Append today's entry
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, mood])

def read_recent_moods(filename=LOG_FILE, days=7):
    """Read moods from the last `days` days and return as a list of ints."""
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

def get_message(average_mood):
    if average_mood is None:
        return "No data yet. Today is Mood Day Zero."
    if average_mood < 2:
        return "Rough stretch. Be gentle with yourself."
    elif average_mood < 3.5:
        return "Holding steady. Small wins still count."
    else:
        return "Trend is up. Keep riding that wave."

def main():
    raw = input("Enter today's mood (1-5): ")
    try:
        mood = int(raw)
        if mood < 1 or mood > 5:
            raise ValueError
    except ValueError:
        print("Please enter a number between 1 and 5.")
        return

    log_mood(mood)
    recent = read_recent_moods()
    if recent:
        avg = sum(recent) / len(recent)
    else:
        avg = None

    print()
    if avg is not None:
        print(f"Your {len(recent)}-day average mood is: {avg:.2f}")
    else:
        print("No recent mood data to average yet.")
    print(get_message(avg))

if __name__ == "__main__":
    main()
