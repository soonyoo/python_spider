# CrawlSpiders爬虫
## 1.1 创建CrawlSpiders爬虫
### 1.1.1 创建crawlspiders爬虫项目与创建普通爬虫项目相同

```python
scrapy startproject 项目名称
```

### 1.1.2 通过下面的命令可以快速创建 CrawlSpider模板 的代码：

 `scrapy genspider -t crawl [爬虫名字] [域名]`

## 1.2 LinkExtractors链接提取器（萃取器）
> 使用 LinkExtractors 可以不用程序员自己提取想要的URL，然后发送请求。这些工作都可以交给LinkExtractors，他会在所有的爬的页面中找到满足规则的url,实现自动的爬取。以下对LinkExtractors类做一个简单的介绍：

`class scrapy.linkextractors.LinkExtractor`
- LinkExtractors 的目的很简单: 提取链接｡
- 每个LinkExtractor有唯一的公共方法是 extract_links()，它接收一个 Response 对象，并返回一个 scrapy.link.Link 对象。
- LinkExtractors要实例化一次，并且 extract_links 方法会根据不同的 response 调用多次提取链接｡

```python
class scrapy.linkextractors.LinkExtractor(
    allow = (),
    deny = (),
    allow_domains = (),
    deny_domains = (),
    deny_extensions = None,
    restrict_xpaths = (),
    tags = ('a','area'),
    attrs = ('href'),
    canonicalize = True,
    unique = True,
    process_value = None
)
```
> 主要参数：

- allow：满足括号中“正则表达式”的URL会被提取，如果为空，则全部匹配。
- deny：满足括号中“正则表达式”的URL一定不提取（优先级高于allow）。
- allow_domains：会被提取的链接的domains。
- deny_domains：一定不会被提取链接的domains。
- restrict_xpaths：使用xpath表达式，和allow共同作用过滤链接。
## 1.3 Rule规则类
定义爬虫规则类。以下对这个类做一个简单的介绍：
> 1.CrawlSpider使用rules来决定爬虫的爬取规则，并将匹配后的url请求提交给引擎。所以在正常情况下，CrawlSpider不需要单独手动返回请求了。

>2.在rules中包含一个或多个Rule对象，每个Rule对爬取网站的动作定义了某种特定操作，比如提取当前相应内容里的特定链接，是否对提取的链接跟进爬取，对提交的请求设置回调函数等。

>3.如果多个rule匹配了相同的链接，则根据规则在本集合中被定义的顺序，第一个会被使用。

```python
class scrapy.spiders.Rule(
        link_extractor,
        callback = None,
        cb_kwargs = None,
        follow = None,
        process_links = None,
        process_request = None
)
```
- link_extractor：是一个LinkExtractor对象，用于定义需要提取的链接。
- callback： 从link_extractor中每获取到链接时，参数所指定的值作为回调函数，该回调函数接受一个response作为其第一个参数。
> 注意：当编写爬虫规则时，避免使用parse作为回调函数。由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了 parse方法，crawl spider将会运行失败。

- follow：是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果callback为None，follow 默认设置为True ，否则默认为False。
- process_links：指定该spider中哪个的函数将会被调用，从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。
- process_request：指定该spider中哪个的函数将会被调用， 该规则提取到每个request时都会调用该函数。 (用来过滤request)
## 实例：微信小程序教程
### 1.创建爬虫项目
`scrapy startproject wxapp`
### 2.创建爬虫
>进入wxapp目录后，运行以下命令，创建爬虫

`scrapy genspider -t crawl wxapp "wxapp-union.com" `
### 3.CrawlSpider
>需要使用LinkExtractor和Rule。这两个东西决定爬虫的具体走向。
1. allow设置规则的方法：要能够限制在我们想要的url上面。不要跟其他的url产生相同的正则表达式好即可。
2. 什么情况下使用fllow:如果在爬取页面的时候，需要奖满足当前条件的url再进行跟进，那么就设置为True.否则设置为false.
3. 什么情况下该指定callback:如果想要获取url对应页面中的数据，那么就需要指定一个callback


