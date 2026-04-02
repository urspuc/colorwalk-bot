import json
import os
import random
import requests
from datetime import datetime

with open("colors.json", "r", encoding="utf-8") as f:
    colors = json.load(f)

color = random.choice(colors)
webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
thread_id = os.environ["DISCORD_THREAD_ID"]

message = f"🎨 今天的 ColorWalk 颜色是：**{color}**"

response = requests.post(
    webhook_url,
    params={"thread_id": thread_id},
    json={"content": message}
)

print(f"发送：{color}，状态码：{response.status_code}")
