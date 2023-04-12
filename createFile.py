
from fileinput import filename
import os,sys,time,datetime,json
from datetime import datetime



strFile=time.strftime('%Y-%m-%d %H:%M:%S %A', time.localtime())
print(strFile)
strSp = strFile.split()[0].split('-')

print(strSp)


weekNum=datetime.now().weekday()
print(weekNum)

week_day_dict = [
    '星期一',
    '星期二',
    '星期三',
    '星期四',
    '星期五',
    '星期六',
    '星期天'
]

zh_week=week_day_dict[weekNum]
print(zh_week)

# 如果没有则创建配置文件
file_name = 'config.json'
js_val = dict()


if os.path.exists(file_name):
    with open(file_name, 'r') as fr:
        js_val = json.loads(fr.read())
    pass
else:
    js_val['suf_name'] = 'txt' # 默认后缀为txt
    with open(file_name, 'w') as fw:
        fw.write(json.dumps(js_val))
        # json.dump(js_val, fw)


fileName = strSp[1] + '-' + strSp[2] + '-' + zh_week + '.' + js_val['suf_name']

print(fileName)
file=open(fileName, 'w')
file.close()



