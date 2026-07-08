from datetime import date, timedelta
import holidays

# Batch pattern
PATTERN = ["1357", "246"]


class BatchScheduler:

    def __init__(self):
        pass

    def generate_schedule(self, year, month, absent_dates=None):

        if absent_dates is None:
            absent_dates = []

        india_holidays = holidays.India(years=[year])

        # Number of days in month
        if month == 12:
            total_days = 31
        else:
            total_days = (date(year, month + 1, 1) - timedelta(days=1)).day

        # Original schedule
        original = []
        batch = 0

        for d in range(1, total_days + 1):

            current = date(year, month, d)

            holiday_name = ""

            is_govt = current in india_holidays

            if is_govt:
                holiday_name = india_holidays[current]

            is_absent = d in absent_dates

            original.append({
                "date": d,
                "day": current.strftime("%A"),
                "batch": PATTERN[batch % 2],
                "holiday": is_govt or is_absent,
                "holiday_name": holiday_name if is_govt else ("Absent" if is_absent else "")
            })

            # Government Holiday does NOT consume batch
            if not (is_govt or is_absent):
                batch += 1

        # Final schedule
        final = []

        batch = 0

        for item in original:

            if item["holiday"]:

                final.append({
                    "date": item["date"],
                    "day": item["day"],
                    "batch": "Holiday",
                    "status": item["holiday_name"]
                })

            else:

                final.append({
                    "date": item["date"],
                    "day": item["day"],
                    "batch": PATTERN[batch % 2],
                    "status": "Working Day"
                })

                batch += 1

        return final