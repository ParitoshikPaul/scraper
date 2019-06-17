# Scraper
A scraper is an Application Programming Interface (API) used to extract content from a website or a number of websites.

## Goals: 
To create a scrapper in which we'll select one of the top 5 eCommerce sites and provide a basic input string eg:
"IPhone 7" and website to scrape from eg: "Amazon". This should return the details of all the products from Amazon.

## Main challenge: 
There will be thousands of products and HTML for each product we need to parse and get the data out of it. So our scraper should be efficient enough to scrape all the data at-least 50,000 Products.

### Getting Started:
You will need a GitHub Personal Auth Token to make requests to the GitHub API. This should be set in your environment or shell rc file with the name GITHUB_API_TOKEN:

$ export GITHUB_API_TOKEN=XYZ

$ echo "export GITHUB_API_TOKEN=XYZ" >> ~/.bashrc

Additionally, to perform the labor hours estimation, you will need to install cloc into your environment. This is typically done with a Package Manager such as npm or homebrew.

You will also need a config.json file to coordinate the platforms you will connect to and scrape data from. Once you have your config file, you are ready to install and run the scraper!

### Install Scraper
$ pip install -e .

### Run Scraper with your config file ``config.json``
$ scraper --config config.json

# Few Web Scraping frameworks and libraries are:

1. Scrapy – The complete framework
2. Urllib
3. Python Requests
4. Selenium
5. Beautifulsoup
6. LXML

## 1. Scrapy – The complete web scraping framework
Scrapy is a web scraping framework written in Python which takes care of everything from downloading HTML if  web pages to storing them in the form you want. For those of you who are familiar with Django, Scrapy is a lot similar to it. The requests we make on Scrapy are scheduled and processed asynchronously. This is because it is built on top of Twisted, an asynchronous framework.

### Pros:
1. CPU usage is a lot lesser
2. Consumes lesser memory
3. Extremely efficient in comparison
4. The well-designed architecture offers you both robustness and flexibility.
5. You can easily develop custom middle-ware or pipeline to add custom functionalities.

### Cons:
1. Overkill for simple jobs
2. Might be difficult to install.
3. The learning curve is quite steep.
4. Not very beginner-friendly, since it is a full-fledged framework

### Installation:
To install Scrapy using conda run:

conda install –c conda–forge scrapy

Alternatively, if you are more familiar with the installation from PyPI, you can install using pip as :

pip install Scrapy

## 2. Urllib
It is a package with several modules for working with URLs (Uniform Resource Locators). It also offers a slightly more complex interface for handling common situations – like basic authentication, encoding, cookies, proxies and so on. These are provided by objects called handlers and openers.

urllib.request for opening and reading URLs
urllib.error containing the exceptions raised by urllib.request
urllib.parse for parsing URLs
urllib.robotparser for parsing robots.txt files

### Pros:
1. Included in python standard library
2. It defines functions and classes to help with URL actions (basic and digest authentication, redirections, cookies, etc

### Cons:
1. Unlike Requests, while using urllib you will need to use the method urllib.encode() to encode the parameters before passing them
2. Complicated when compared to Python Requests

### Installation:
Urllib is already included with your python installation, you don’t need to install it.

## 3. Requests – HTTP for humans
Requests is the perfect example how beautiful an API can be with the right level of abstraction. It’s allows you to send organic, grass-fed requests, without the need for manual labor.

### Pros:
1. Easier and shorter codes than Urllib.
2. Thread-safe.
3. Multipart File Uploads & Connection Timeouts
4. Elegant Key/Value Cookies & Sessions with Cookie Persistence
5. Automatic Decompression
6. Basic/Digest Authentication
7. Browser-style SSL Verification
8. Keep-Alive & Connection Pooling
9. Good Documentation
10. No need to manually add query strings to your URLs
11. Supports the entire restful API, i.e., all its methods – PUT, GET, DELETE, POST.

### Cons:
1. If your web page has javascript hiding or loading content, then requests might not be the way to go.

### Installation:
You can install requests using conda as :

conda install -c anaconda requests

and pip using:

pip install requests

## 4. Selenium – The automator
Selenium is a tool automates browsers based on Java. But you can access it via the Python Package Selenium.  Though primarily used as a tool for writing automated tests for web applications, it has come to some heavy use for pages that have javascript on them.

### Pros:
1. Beginner friendly
2. You get real browser to see whats going on ( unless you are on a headless mode )
3. Mimics human behavior while browsing, including clicks, selection, filling text box, scroll etc.
4. Renders a full webpage and shows HTML rendered via XHR or Javascript

### Cons:
1. Very slow
2. Heavy memory use
3. High CPU usage.

### Installation:
To install this package with conda run:

conda install -c conda-forge selenium 

Using pip, you can install by running the below on your terminal

pip install selenium

# The Parsers
a. Beautiful Soup
b. LXML

A parser is simply a program that can extract data from HTML and XML documents. They parse the structure into memory and felicitates the use selectors (either CSS or XPath) to easily extract the data. The advantage here is that parsers can automatically correct “bad” HTML (unclosed tags, badly quoted attributes, invalid HTML etc) and allow us to get the data we need. The disadvantage is that it requires more processor work in most cases, but as ever it’s a trade-off and tends to be a worthwhile one.

## 5. BS4
Beautiful Soup (BS4) is a parsing library that can use different parsers. As we already know, the content we are parsing might belong to various encodings. BS4 automatically detects it. BS4 creates a parse tree which helps you navigate a parsed document easily and find what you need.

### Pros:
1. Easier to write a bs4 snippet than lxml.
2. Small learning curve, easy to learn.
3. Quite robust.
4. Handles malformed markup well.
5. Excellent support for encoding detection

### Cons:
1. If the default parser chosen for you is incorrect, they may incorrectly parse results without warnings, which can lead to disastrous results.
2. Projects built using bs4 might not be flexible in terms of extensibility.
3. You need import multiprocessing  to make it run quicker

### Installation:
To install this package with conda run:

conda install -c anaconda beautifulsoup4 

Using pip, you can install using

pip install beautifulsoup4

## 6. LXML
Lxml is a high-performance, production-quality HTML and XML parsing library.

### Pros:
1. It is the best performing parser. As shown here
2. Most feature rich python library for the same.

### Cons:
1. Official documentation isn’t that friendly, so beginners are better off starting somewhere else.

### Installation:
With conda run, you can install using,
To install this package with conda run:

conda install -c anaconda lxml 

You can install using lxml directly using pip,

sudo apt-get install python3-lxml
