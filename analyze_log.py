import csv
from datetime import date

LOG_FILE = "mood_log.csv"

def load_moods(filename=LOG_FILE):
    """Load all mood entries from the CSV and return a list of (date, mood)."""
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            rows = [(row["date"], int(row["mood"])) for row in reader]
        return rows
    except FileNotFoundError:
        print("No mood_log.csv file found. Run mood_tracker.py first.")
        return []

def calculate_stats(entries):
    """Return total entries, average mood, highest mood, lowest mood."""
    if not entries:
        return None

    moods = [m for (_, m) in entries]
    total = len(moods)
    avg = sum(moods) / total
    highest = max(moods)
    lowest = min(moods)

    return {
        "total": total,
        "average": avg,
        "highest": highest,
        "lowest": lowest
    }

def main():
    entries = load_moods()

    if not entries:
        return

    stats = calculate_stats(entries)

    print("\n📊 Mood Log Summary")
    print("----------------------")
    print(f"Total entries: {stats['total']}")
    print(f"Average mood: {stats['average']:.2f}")
    print(f"Highest mood recorded: {stats['highest']}")
    print(f"Lowest mood recorded: {stats['lowest']}")
    print()

if __name__ == "__main__":
    main()
