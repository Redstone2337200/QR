# QR
Store QQ robot source code films

## About this QQRobot
The early QQ robot still has a lot of functions to be completed, and it will be updated later, although it is not ready to be updated.

### Contact information
>QQ：3356168312 <br>
WeChat：RTX-Redstone2337200


### About Versions
0.0.0.0.0.1 Alpha Beta version.

### Code
```python
import requests
import time

# Call the interface.
api_url = "https://v1.hitokoto.cn/"

# Gets the last send time.
last_send_time = 0

# Get a random word.
def get_yiyan():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data["hitokoto"]
    else:
        return "Failed to get. Please try again later."

# QQ Robot
while True:
    # Gets the current time.
    now = time.time()

    # If the last sending time is less than 5 seconds, it will not be executed.
    if now - last_send_time < 5:
        time.sleep(1)
        continue

    # Otherwise, wait for the user to send information.
    msg = input("Please enter information：")

    # If the user triggers the keyword, execute.
    if msg == "Yi Yan":
        reply = get_yiyan()
        print("Robot reply：", reply)
        last_send_time = now
    else:
        print("The robot doesn't seem to want to talk to you...")
```

### html
```hypertext markup language
<!DOCTYPE html>
<html>
<head>
	<title>随机一言</title>
</head>
<body>
	<h1>随机一言</h1>
	<p id="hitokoto"></p>

	<script>
		// 一言的API接口
		var url = "https://v1.hitokoto.cn/";

		// 发送HTTP请求，获取一言内容
		fetch(url)
			.then(response => response.json())
			.then(data => {
				// 输出一言内容
				document.getElementById("hitokoto").innerText = data.hitokoto;
			})
			.catch(error => console.error(error));
	</script>
</body>
</html>
```

### More Information
`
There is no more information. <br>
But all developers can add new code.
`
