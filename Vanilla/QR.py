import requests
import time

# 一言API接口
api_url = "https://v1.hitokoto.cn/"

# 上次发送消息的时间
last_send_time = 0

# 获取一言
def get_yiyan():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data["hitokoto"]
    else:
        return "获取一言失败，请稍后再试"

# QQ机器人
while True:
    # 获取当前时间
    now = time.time()

    # 如果距离上次发送消息的时间小于5秒，则不做处理
    if now - last_send_time < 5:
        time.sleep(1)
        continue

    # 否则，等待用户输入消息
    msg = input("请输入消息：")

    # 如果用户输入“一言”，则获取一言并回复
    if msg == "一言":
        reply = get_yiyan()
        print("机器人回复：", reply)
        last_send_time = now
    else:
        print("机器人不理你...")
