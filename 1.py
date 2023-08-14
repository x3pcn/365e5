import time

def focus_timer(minutes):
    # 将分钟转换为秒
    seconds = minutes * 60

    print(f"Focus timer started for {minutes} minutes.")

    # 等待指定的专注时间
    time.sleep(seconds)

    print("Focus timer ended.")

# 设置专注时间为25分钟
focus_timer(25)
