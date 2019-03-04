#模拟登陆人人网
1. 想要发送post请求，那么推荐使用`scrapy.FormRequest`方法。可以方便的指定表单数据。
2. 如果想在爬虫一开始的时候就发送post请求，那么应该重写`start_requests`方法。在这个方法中，发送post请求。
3. 代码实现
```shell
$ scrapy startproject renren_login
$ cd renren_login
$ scrapy genspider renren "renren.com"
```
> python 爬虫部分

```python
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {'email': '18688280440', 'password': '*****'}
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self,response):
        url = "http://www.renren.com/969741257/profile"
        request = scrapy.Request(url, callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open('dh.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)

```