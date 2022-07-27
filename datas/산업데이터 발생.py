
import json
from collections import OrderedDict
import datetime

file_data = OrderedDict()

# with open('temp.json', 'w', encoding='utf-8') as make_file:
#     file_data["TITLE"] = "ANALYZER TAGS"
#
#     file_data["analyzers"] = dict()
#
#     cnt = 1
#     for i in range(1, 489):
#         if len(str(cnt)) == 1:
#             house_tag = "0" + str(cnt) + "AH"
#         else:
#             house_tag = str(cnt) + "AH"
#
#         if len(str(i)) == 1:
#             file_data["analyzers"]["house"] = house_tag
#             file_data["analyzers"]["analyzer"] = house_tag[:2] + "-AT-00" + str(i)
#             json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
#         elif len(str(i)) == 2:
#             file_data["analyzers"]["house"] = house_tag
#             file_data["analyzers"]["analyzer"] = house_tag[:2] + "-AT-0" + str(i)
#             json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
#         else:
#             file_data["analyzers"]["house"] = house_tag
#             file_data["analyzers"]["analyzer"] = house_tag[:2] + "-AT-" + str(i)
#             json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
#         if i % 10 == 0:
#             cnt += 1
# json파일로 analyzer_tag, house_tag 만들기
###################################################################################################


analyzer_tags = []
house_tags = []

with open('temp.json', 'r', encoding='utf-8') as read_file:
    json_data = json.load(read_file)

    for k in range(len(json_data['FILE'])):
        analyzer_tags.append(json_data['FILE'][k]['analyzers']['analyzer'])  # analyzer 태그만 가져올 수 있다.
        house_tags.append(json_data['FILE'][k]['analyzers']['house'])  # house 태그만 가져올 수 있다.

###################################################################################################

import time
import random

status = ["Normal", "Validation", "Maintenance", "Breakdown", "analyzerFault", "LowFlowAlarm", "gcCommonAlarm"]

tmp = [0 for _ in range(len(analyzer_tags))]
for k in range(42, 56):
    tmp[k] = 3

for j in range(400, 412):
    tmp[j] = 4

cnt = 0
with open(str(datetime.datetime.now())[:10] + "-data-log", "w", encoding='utf-8') as file:
    for hour in range(8): # 8시간
        for min in range(60):
            for sec in range(60):
                for idx, tag in enumerate(zip(analyzer_tags, house_tags)):
                    value = (random.choices([0, 1, 2, 3, 4, 5, 6], [96, 2.95, 0.26, 0.025, 0.13, 0.13, 0.1]))[0]
                    file.write(
                        str(datetime.datetime.now())[:10] + "," + str(datetime.datetime.now())[11:19] + "," + tag[1] + "," + tag[0] + "," + status[tmp[idx]] + "," +
                        str(random.random()*10) + "," + str(random.random()*10) + "," + str(random.random()*10) + "," + str(random.random()*10) + "," + str(random.random()*10)+ "\n")

                time.sleep(1) # 1초에 한 번씩 기록되게
                cnt += 1
            print(str(datetime.datetime.now())[:19], cnt) # 1분에 한 번씩 확인용