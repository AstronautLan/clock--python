import time

def concentration_timer(duration_in_minutes):
    duration_in_seconds = duration_in_minutes * 60
    print(f"专注时钟启动，时长: {duration_in_minutes} 分钟")

    time.sleep(duration_in_seconds)

    print("专注时钟结束，时间到！")

# 设置专注时长为25分钟
concentration_timer(25)
