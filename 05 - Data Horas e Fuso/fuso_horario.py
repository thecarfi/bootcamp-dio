from datetime import datetime, timedelta, timezone

import pytz

data = datetime.now(pytz.timezone("America/Cuiaba"))


data2 = datetime.now(timezone(timedelta(hours=1)))

print(data)
print(data2)