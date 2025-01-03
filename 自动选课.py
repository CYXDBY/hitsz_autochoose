import requests
import time

from datetime import datetime
from datetime import timedelta
from datetime import timezone


p_ids = ['247AK74N7ED588RPK0630B18F80A261B']    # 课程ID，在选课页面点击所想选课程所在的顶部栏后，在F12的“网络”页面弹出的数据包中
p_xkfsdm = 'xx-b-b'                             # 课程类型，也在上述数据包中，一般是拼音，如：xx-b-b表示限选，bx-b-b表示必选
xn = '2024-2025'                                # 目标课程学年
xq = '2'                                        # 目标课程学期（秋季1，春季2，夏季3）
dqxn = '2024-2025'                              # 当前学年
dqxq = '1'                                      # 当前学期（秋季1，春季2，夏季3）
wait = 1.25                                     # 抢课间隔时间（建议间隔1.25s）
startTime = '12_59_55'                          # 抢课开始时间
switch = 1                                      # 是否启用定时抢课：0是1否
cookie = '_gscu_651000777=001003220goh0010; JSESSIONID=F7F7E808FD3394F7766022588069BD84; route=2134183320579982c02bf8dff07b0881'




SHA_TZ = timezone(timedelta(hours=8), name='Asia/Shanghai')
url = 'http://jw.hitsz.edu.cn/Xsxk/addGouwuche'
headers = {
    'Host': 'jw.hitsz.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://jw.hitsz.edu.cn/Xsxk/query/1',
    'Content-Length': str(498 + len(p_xkfsdm)),
    'Origin': 'http://jw.hitsz.edu.cn',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'RoleCode': '01',
    'X-Requested-With': 'XMLHttpRequest',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }

# 生成发出的data
while switch == 0:
    # 获取当前北京时间
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ)
    timen = beijing_now.strftime('%H_%M_%S')
    print(timen)
    if timen == startTime:
        switch = 1
        break

while switch == 1:
    #发包
    try:
        for i in range(len(p_ids)):
            data = f'p_pylx=1&mxpylx=1&p_sfgldjr=0&p_sfredis=0&p_sfsyxkgwc=0&p_xktjz=rwtjzyx&p_chaxunxh=&p_gjz=&p_skjs=&p_xn={xn}&p_xq={xq}&p_xnxq={xn+xq}1&p_dqxn={dqxn}&p_dqxq={dqxq}&p_dqxnxq={dqxn+dqxq}4&p_xkfsdm={p_xkfsdm}&p_xiaoqu=&p_kkyx=&p_kclb=&p_xkxs=&p_id={p_ids[i]}&p_sfhlctkc=0&p_sfhllrlkc=0&p_kxsj_xqj=&p_kxsj_ksjc=&p_kxsj_jsjc=&p_kcdm_js=&p_kcdm_cxrw=&p_kc_gjz=&p_xzcxtjz_nj=&p_xzcxtjz_yx=&p_xzcxtjz_zy=&p_xzcxtjz_zyfx=&p_xzcxtjz_bj=&p_sfxsgwckb=1&p_skyy=&p_chaxunxkfsdm=&pageNum=1&pageSize=8'
            ret = requests.post(url = url,headers=headers, data=data, timeout=1000)
            response_json = ret.json()
            print(response_json)
            time.sleep(wait)

    except Exception as e:
        print('[Error]: ' + str(e))
