from datetime import datetime


def get_week_number(date: datetime.date) -> int:
    """Week number calculation function"""

    start_date = datetime.strptime('2018-12-30', '%Y-%m-%d').date()
    week = int((date - start_date).days // 7) + 1
    return week
