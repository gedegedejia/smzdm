import requests
import json
from urllib.parse import quote

# Bark推送API的device_key
device_key ='自己的device_key'
ICON_URL = 'https://www.iyunying.org/wp-content/uploads/2018/03/yunying-1520024936.jpeg'

# 从output.json读取数据
def read_json_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# 通过Bark推送通知
def send_bark_notification(title: str, body: str, url: str):    
    # 拼接完整的Bark推送URL
    send_url = f"https://api.day.app/{device_key}/{title}/{body} ?url={url}&icon={ICON_URL}"
    response = requests.get(send_url)
    print(send_url)
    # 检查请求结果
    if response.status_code == 200:
        print("推送成功！")
    else:
        print(f"推送失败，状态码：{response.status_code}")

# 主函数
def main():
    # 读取output.json中的内容
    json_data = read_json_file("output.json")
    
    # 假设json_data是一个列表，取第一个元素
    if isinstance(json_data, list) and len(json_data) > 0:
        for item in json_data :
            title = "什么值得买好价"
            rating_unworthy_num = int(item.get('rating_unworthy_num'))
            rating_worthy_num = int(item.get('rating_worthy_num'))
            discount = item.get('discount')
            panelTitle =int(item.get('panelTitle'))
            #要求有评论且有优惠信息
            if discount!='' and panelTitle>0:
                body = f"物品：{item.get('title', '无内容')}\n价格：{item.get('price', '无价格')}\n优惠：{item.get('discount', '无优惠')}"
                url = item.get('url')
                # 发送推送通知
                print("发送推送")
                send_bark_notification(title, body, url)
    else:
        print("output.json的格式不正确或内容为空")

if __name__ == "__main__":
    main()