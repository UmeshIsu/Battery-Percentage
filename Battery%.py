import psutil
from plyer import notification
import time

def convert_seconds_to_hm(sec):
    if sec == psutil.POWER_TIME_UNLIMITED:
        return None, None
    elif sec == psutil.POWER_TIME_UNKNOWN:
        return "Unknown", "Unknown"
    
    sec_value = sec % (24 * 3600)
    hour_value = sec_value // 3600
    sec_value %= 3600
    min_value = sec_value // 60
    return hour_value, min_value

while True:
    try:
        battery = psutil.sensors_battery()
        if battery is not None:
            h, m = convert_seconds_to_hm(battery.secsleft)
            if h is not None:
                message = f'{h}Hr {m}Min {battery.percent}% remaining'
            else:
                message = f'{battery.percent}% remaining, time left unknown'

            notification.notify(
                title="Battery Percentage",
                message=message,
                timeout=10
            )
        else:
            notification.notify(
                title="Battery Percentage",
                message="Battery status not available",
                timeout=10
            )
    except Exception as e:
        notification.notify(
            title="Battery Percentage",
            message=f"An error occurred: {e}",
            timeout=10
        )
    
    # For testing, use a shorter interval, e.g., 60 seconds
    time.sleep(60)
