from django.utils.timesince import timesince as django_timesince

def custom_timesince(value, now=None, custom_minutes='минут', custom_hours='часов'):
    timesince = django_timesince(value, now=now)
    timesince = timesince.replace(
        'minutes', custom_minutes
    )
    return timesince
