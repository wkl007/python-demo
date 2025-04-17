import re
from datetime import datetime, timezone, timedelta

# 获取当前日期和时间
now = datetime.now()
print(now, type(now), now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

# 获取指定日期和时间
dt = datetime(2025, 4, 19, 12, 20)
print(dt)

# 时间戳
print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t), datetime.fromtimestamp(t, tz=timezone.utc))

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))

# datetime 加减
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
now + timedelta(days=2, hours=12)

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print(dt)

# 时区转换
utc_dt = datetime.now(timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    # 解析 datetime 字符串
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    # 解析时区字符串，形如 UTC+7:00 或 UTC-09:00
    match = re.match(r'^UTC([+-])(\d+):(\d+)$', tz_str)
    if not match:
        raise ValueError('Invalid timezone format')

    sign, hours, minutes = match.groups()
    offset = timedelta(hours=int(hours), minutes=int(minutes))
    if sign == '-':
        offset = -offset

    # 设置时区
    tz = timezone(offset)

    # 转换为带时区的 datetime
    dt_with_tz = dt.replace(tzinfo=tz)

    # 转换为 timestamp（UTC 时间）
    return dt_with_tz.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
