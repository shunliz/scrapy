#encoding:utf-8
import scrapy
import urllib2
import uuid
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            #"https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=美女&cl=2&lm=-1&ie=utf-8&oe=utf-8st=-1&ic=0&word=美女&face=0&istype=2&nc=1&cg=girl&rn=30&pn=%d" %i for i in range(0,901,30)
            "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=刘亦菲&cl=2&lm=-1&ie=utf-8&oe=utf-8st=-1&ic=0&word=刘亦菲&face=0&istype=2&nc=1&cg=girl&rn=30&pn=390"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies={'Cookie':'BDqhfp=%E7%BE%8E%E5%A5%B3%26%260-10-1undefined%26%260%26%261; firstShowTip=1; BAIDUID=83A0F48B15C1154F5B1DD7310D97C730:FG=1; BIDUPSID=084BE203E5D6291D53ECF0A9F1F26AEB; PSTM=1488959491; BAIDUCUID=++; __cfduid=d3f04d29c87b29b109c2ada56fe03688e1493185698; BDUSS=1xaExxY21oQU9xVkdtR3lEUGFQWk5HWmFMMTZiTjBRTWVFd0piV0xxQmY5cUJaSUFBQUFBJCQAAAAAAAAAAAEAAADOZX0xenNsaTY2NTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF9peVlfaXlZQ2; cleanHistoryStatus=0; BDSFRCVID=LA8sJeC62G2x3WbA8L6zhBlhb6cghYoTH6aoLA2bbSefdke2_UEXEG0PDf8g0Ku-LgM-ogKKy2OTH9jP; H_BDCLCKID_SF=tR4JoK8KJDL3eJbGq6_a-n0eqxby26nAWGReaJ5nJDoKjqbOL45Nqf-DMx7G2IrfWPDeaCb-QpP-HJ7NM6DB-Jkq-GOKKlvPJ2C8Kl0MLPjYbb0xyn_VQxtI-UnMBMn8teOnaIT_LIFBbD-9ej-2enk_qlo0eJ3-5TIX3buQWlQrqpcNLTDKhMAn3NQH3CrxaGc35J4Ebhn0_IQJDpO1j4_ebM5bBxQ7LIjw0n3J0R7hfh5jDh3Ub6ksD-Rte43f0C7y0hvcMCocShPwMl00jTJQDN_fJ5nfb5kXWnjja-K_Hn7zen3CDbtpbtbmhU-ebC373hDEJbvmVnrk5lJIyqJQBn0jK4RJMR7ZVD_5JKtahDPr5nJbqR_EbfOtetJyaR3zBIJbWJ5TEPnjDnt2X5KFqtjxtIrLtnvTatTHKtOYqhnR2t85y6TXjaAHtTtJtb3fL-08bJcoDR0k-PnVeUJ3QlbZKxtqte7joMKy-qjsER6YMM5S-6L8y-vOWh3nWncKW-Tp5p3FfDbdht6B3J-DMRo405OT3gDO0KJcbRoDoqQqhPJvyncXXnO7q4TTfJCjoDtyJKP3fP36qR7HqtD3bqbJa46MHD7yWCvI3hO5OR5Jj6KMMp8m0J5CqIrh0CbGWnntalv_8lbO3MA--t4DDPQuXf3pWaTN3t322fOhsq0x0bQte-bQyp_LqPc4QIOMahvXtq7xOKTF05CBej3beHKJqbvKHDQKLJD8bn5ffjrnh6RAQRLyyxomtjj0Kb-DMKOpfT6tHnnth-7Dhqks-HoaLUkqKCOf3C5MWPbabfJpbhLB3q_jQttjQnoPfIkja-KE5P3bHJ7TyURBDx47yarBQTIqtRFt_DIhfbj2q5rd5tQbbtFShMntKI62aKDs2pDy-hcqEIL4QT5WDp-VLH7rtJT30DJ33DQJ5bnZDUbSj4QoXMoX-x5gK45b2KIHMM5Nyp5nhMJeb67JDMP0qtvMWCry523iXCovQpPBjxtu-n5jHjjyDaLH3J; MCITY=-233%3A; indexPageSugList=%5B%22%E7%BE%8E%E5%A5%B3%22%2C%22%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%22%2C%22%E6%B8%85%E7%BA%AF%E7%BE%8E%E5%A5%B3%22%2C%22%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87%22%5D; H_PS_PSSID=1447_21115_17001_25226_25177_20719; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; userFrom=null; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm'})

    def parse(self, response):
#         for img in response.css("imglist"):
#             img_url = img.xpath("div/a/image/@data-imgurl").extract()
#             name = uuid.UUID().get_hex()
#             urllib.urlretrieve(img_url, 'images/'+name+'.jpg')
        body = json.loads(response.body)
        imgs = body['data']
        for img in imgs:
            try:
                name = uuid.uuid4()
                #urllib.urlretrieve(img['middleURL'],'images\\'+str(name)+'.jpg') #
                binary_data = urllib2.urlopen(img['middleURL']).read()
                temp_file = open(str(name)+'.jpg', 'wb')
                temp_file.write(binary_data)
                temp_file.close()
            except Exception as e:
                print e