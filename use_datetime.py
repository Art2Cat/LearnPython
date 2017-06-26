#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
now + timedelta(days=2, hours=4)
# %a %b %y are three-letter abbreviation of week, month and year
# %A %B %Y are full-letter of week, month and year
# #d %H %M represent for day hour and minute
print(now.strftime('%a, %b %d %y %H:%M'))

sh_utc_8 = timezone(timedelta(hours=8))
utc8 = now.replace(tzinfo=sh_utc_8)

print('Shanghai time: %s' % utc8)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))

print('Tokyo time: %s' % tokyo_dt)

london_utc_1 = timezone(timedelta(hours=1))

# covert tokyo_dt to london_dt
london_dt = tokyo_dt.astimezone(london_utc_1)

print('London time: %s' % london_dt)
