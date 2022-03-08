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
@Time    : 2022/2/15 17:04
'''
class RunYaml():

    def __init__(self, read_result2):
        self.read_result2 = read_result2

    def get_interface(self):
        print("这是读取yaml结果" )
        print(self.read_result2)

test1 = {"login_data":"hhh"}
# RunYaml(test1).get_interface()
a= RunYaml(test1)
a.get_interface()