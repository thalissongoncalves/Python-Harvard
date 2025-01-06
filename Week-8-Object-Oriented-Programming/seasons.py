from datetime import date, datetime
import inflect
import sys

class Birth:
    _inflect_engine = inflect.engine()

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __sub__(self, other):
        date_self = datetime(self.year, self.month, self.day)
        date_other = datetime(other.year, other.month, other.day)
        delta = date_self - date_other
        return abs(delta.days * 1440)

    def __str__(self):
        minutes = self.count_minutes_since_birth()
        p = self._inflect_engine
        words = p.number_to_words(minutes, andword="")
        return f"{words.capitalize()} {p.plural('minute', minutes)}"

    def count_minutes_since_birth(self):
        today = Birth.today()
        return today - self

    @classmethod
    def today(cls):
        now = date.today()
        return cls(now.year, now.month, now.day)

    @classmethod
    def get(cls, birth):
        try:
            year, month, day = map(int, birth.split('-'))
            datetime(year, month, day)
            if datetime(year, month, day) > datetime.now():
                sys.exit("Invalid date")
            return cls(year, month, day)
        except (ValueError, TypeError):
            sys.exit("Invalid date")

def main():
    try:
        birth_date = input("Date of Birth: ")
        birth = Birth.get(birth_date)
        print(birth)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()