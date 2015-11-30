# -*- encoding: utf-8 -*-
import json

from client import Client
from nomore_mine import token


if __name__ == "__main__":
    try:
        client = Client()
        client.init(token)
        # url1='/api/macro/getChinaDataGDP.csv?field=&indicID=M010000002&indicName=&beginDate=&endDate='
        url1='/api/subject/getSocialDataXQByDate.json?field=&statisticsDate=20151126'
        # url1 = '/api/market/getTickRTSnapshot.json?securityID=600226.XSHG'
        # url1 = '/api/market/getTickRTSnapshot.json?securityID=000001.XSHG,000001.XSHE&field=lastPrice,shortNM,dataDate,dataTime'
        code, result = client.getData(url1)
        result = json.loads(result)
        result = result['data']
        result = sorted(result, key=lambda i: i['postPercent'], reverse=True)
        if code==200:
            print(' 股票代码   用户发帖数量   占的比例')
            for i in result[:10]:
                print('%s        %d        %f' % (i['ticker'],  i['postNum'], i['postPercent']))
            # print result
        else:
            print code
            print result
        # url2='/api/subject/getThemesContent.csv?field=&themeID=&themeName=&isMain=1&themeSource='
        # code, result = client.getData(url2)
        # if(code==200):
        #     file_object = open('thefile.csv', 'w')
        #     file_object.write(result)
        #     file_object.close( )
        # else:
        #     print code
        #     print result
    except Exception, e:
        #traceback.print_exc()
        raise e