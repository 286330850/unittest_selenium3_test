# unittest_selenium3_test
基于python的unittest单元测试，加入selenium3可实现web测试自动化。
## selenium3
selenium3需要geckodriver，手工下载geckodirver，然后保存在独立的路径，启动dirver时指定该路径：
```
self.driver = webdriver.Firefox(firefox_profile='D:/ff_profile',executable_path='D:/geckodriver.exe')
```
其中firefox_profile是firefox的profile所在路径。使用selenium启动firefox每次都会新建一个profile，导致有些配置无法生效，最好定制一个profile，然后每次启动的时候指定该profile。
