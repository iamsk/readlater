#-*- coding: utf-8 -*-
__author__ = 'iamsk'
__email__ = 'iamsk.info@gmail.com'

import configs

def _export():
    """
    导出 readitlater
    """
    import readitlater
    api = readitlater.API(configs.RIL_APIKEY, configs.RIL_USERNAME, configs.RIL_PASSWORD)
    items = api.get()
    list = items['list']
    l = []
    for k, v in list.items():
        #state: 0=unread, 1=read
        l.append((v['url'], v['state']))
    print len(l)
    return l

def rdd_delete_bookmarks():
    """
    清空 readability
    """
    import readability
    token = readability.xauth(configs.RDD_APIKEY, configs.RDD_SECRET, configs.RDD_USERNAME, configs.RDD_PASSWORD)
    rdd = readability.oauth(configs.RDD_APIKEY, configs.RDD_SECRET, token=token)
    list = rdd.get_bookmarks()
    count = 0
    for bm in list:
        resource = 'bookmarks/%s' % bm.id
        rdd._delete_resource(resource)
        count += 1
        print count
    print 'delete count: ', count


def _import(list):
    """
    导入 readablility
    """
    import readability
    token = readability.xauth(configs.RDD_APIKEY, configs.RDD_SECRET, configs.RDD_USERNAME, configs.RDD_PASSWORD)
    rdd = readability.oauth(configs.RDD_APIKEY, configs.RDD_SECRET, token=token)
    count = 0
    for url, state in list:
        try:
            rdd.add_bookmark(url, archive=int(state))
            count += 1
            print count
        except Exception, e:
            if e.message:
                print url, state
                print e.message
    print 'add count: ', count

def run():
#    rdd_delete_bookmarks() # dangerous op, this will empty your readablility's data, to be carefully
    l = _export()
    _import(l)

if __name__ == '__main__':
    run()
