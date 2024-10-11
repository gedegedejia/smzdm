import json
from lxml import etree
import requests

def extract_data(tree, xpath_expr):
    data = tree.xpath(xpath_expr)
    return [item.strip() for item in data if item.strip()]

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.RequestException as e:
        print(f"请求失败：{e}")
        return None

def main():
    results = []
    
    try:
        with open('test.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print("文件未找到。")
        return
    
    root = etree.HTML(html_content)
    links = extract_data(root, '//div[@class="z-feed-content"]/h5/a/@href')
    
    for url in links:
        html_content = fetch_html(url)
        if html_content:
            print(f"爬取网页：{url}")
            son = etree.HTML(html_content)
            
            # 提取发布时间
            time = extract_data(son, '//span[@class="time"]/text()')
            
            # 提取商品标题
            title = extract_data(son, '//div[@class="title-box"]/h1[@class="title J_title"]/text()')
            
            # 提取商品价格
            price = extract_data(son, '//span[@class="price-large"]/span/text()')
            if isinstance(price, list) and price:
                price = ' '.join(price)
            else:
                price = "未知"
            
            # 提取商品优惠信息
            discount = extract_data(son, '//div[@class="item-subtitle"]/a/span/text()')
            if discount == "" :
                discount = "无优惠"

            # 提取点值率
            rating_worthy_num = extract_data(son, '//span[@id="rating_worthy_num"]/text()')
            rating_unworthy_num = extract_data(son, '//span[@id="rating_unworthy_num"]/text()')
            
            # 提取评价数量
            panelTitle = extract_data(son, '//div[@id="panelTitle"]/em/text()')
            comment = extract_data(son, '//div[@class="comment-main-list-item-content-comment padding-right-10"]/span/text()')
            n = int(panelTitle[0]) if panelTitle and panelTitle[0].isdigit() else 0

            # 确保评论数量与面板标题数量一致
            if n > 0:
                comment = comment[:n]
            # 创建一个字典来存储提取的信息
            result = {
                "url": url,
                "time": time[0] if time else "",
                "title": title[0] if title else "",
                "price": price,
                "discount": discount[0] if discount else "",
                "rating_worthy_num": rating_worthy_num[0] if rating_worthy_num else "",
                "rating_unworthy_num": rating_unworthy_num[0] if rating_unworthy_num else "",
                "panelTitle": panelTitle[0] if panelTitle else "",
                "comment": comment
            }
            results.append(result)
        else:
            print("无法获取网页内容。")
    
    # 将结果保存为JSON文件
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    

if __name__ == '__main__':
    main()