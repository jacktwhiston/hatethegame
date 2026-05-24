import datetime

from htg import CondecoBooker


def main():
    booker = CondecoBooker()

    # Let's book the week a fortnight from now
    now = datetime.datetime.now()
    days_to_monday = (7 - now.weekday()) % 7
    monday_fortnight = now + datetime.timedelta(days=days_to_monday + 7)

    for i in range(5):
        booker.book_desk(monday_fortnight + datetime.timedelta(days=i))


if __name__ == '__main__':
    main()
