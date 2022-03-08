# -*- coding: utf-8 -*-
'''

                            _ooOoo_
                           o8888888o
                           88" . "88
                           (| -_- |)
                            O\ = /O
                        ____/`---'\____
                      .   ' \\| |// `.
                       / \\||| : |||// \
                     / _||||| -:- |||||- \
                       | | \\\ - /// | |
                     | \_| ''\---/'' | |
                      \ .-\__ `-` ___/-. /
                   ___`. .' /--.--\ `. . __
                ."" '< `.___\_<|>_/___.' >'"".
               | | : `- \`.;`\ _ /`;.`/ - ` : | |
                 \ \ `-. \_ __\ /__ _/ .-` / /
         ======`-.____`-.___\_____/___.-`____.-'======
                            `=---='

         .............................................
                  佛祖保佑             永无BUG

@Author  : lqh
@Time    : 2022/3/8 11:28
'''
import json

import requests

def req(url,data='',method='get'):
    data = json.dumps(data)
    if method =='get':
        res = requests.get(url,data)
        if res.status_code == 200:
            res = res.text
        else:
            print('请求失败：'+str(res.status_code))
    else:
        res = requests.post(url,data)
        if res.status_code == 200:
            res.encoding='gbk'
            res = res.text
        else:
            print('请求失败：'+str(res.status_code))
    return res


res = req('https://www.galaxyautotech.com/ugc-admin/#/platform/scene-manage-ugc')
print(res)

