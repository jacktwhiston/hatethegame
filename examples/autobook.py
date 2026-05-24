import datetime
import zoneinfo
from htg import CondecoBooker


def main():
    booker = CondecoBooker()
    aest = zoneinfo.ZoneInfo("Australia/Brisbane")

    # Let's book the week a fortnight from now
    today = datetime.datetime.now(tz=aest).date()
    days_until_monday = (7 - today.weekday()) % 7 or 7
    target_monday = today + datetime.timedelta(days=days_until_monday + 7)
    
    for i in range(5):
        booker.book_desk(datetime.datetime.combine(target_monday + datetime.timedelta(days=i), datetime.time()))


if __name__ == '__main__':
    main()
