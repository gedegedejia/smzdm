# 什么值得买精选网页爬取与推送 🛍️

## 目录

- [项目简介](#项目简介)
- [安装依赖](#安装依赖)
- [使用说明](#使用说明)
- [作者](#作者)


#### 项目简介
可以对什么值得买的精选页面编写爬虫，提取网页链接、发布时间、商品标题、商品优惠信息、商品价格、点值率、评价数量等信息。
对爬虫进行自动化部署（速度30分钟1次爬取），该程序设定过滤阈值为：点值率大于60，有优惠，且有评论，提高优惠信息的有效比例。
利用 Bark（ios） 推送平台，实现优惠信息的自动推送。

### 安装依赖
⚠️终端运行以下命令，下载所需要的库文件：
```sh
pip install -r reqiurements.txt
```

### 使用说明
- IOS 端：下载 bark 软件
- PC  端：在 transform.py 中将 BARK_API_URL 替换成自己的 api 后，运行 app.py 。

可以在 transform 的 main 函数中修改过滤阈值


# XPath 选择器

| 元素               | 节点   | XPath                                                      |
|--------------------|--------|------------------------------------------------------------|
| links              | 父节点 | `//div[@class="z-feed-content"]/h5/a/@href`                |
| time               | 子节点 | `//span[@class="time"]/text()`                             |
| title              | 子节点 | `//div[@class="title-box"]/h1[@class="title J_title"]/text()` |
| price              | 子节点 | `//span[@class="price-large"]/span/text()`                 |
| discount           | 子节点 | `//div[@class="item-subtitle"]/a/span/text()`              |
| rating_worthy_num  | 子节点 | `//span[@id="rating_worthy_num"]/text()`                   |
| rating_unworthy_num| 子节点 | `//span[@id="rating_unworthy_num"]/text()`                 |
| panelTitle         | 子节点 | `//div[@id="panelTitle"]/em/text()`                        |

### 作者
姚诗娴：yao_shi_xian@icloud.com