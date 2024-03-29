from collections import defaultdict
datas = defaultdict(list)

with open("C:\\Users\\kkdh8\\Desktop\\MODBUS.csv", encoding='utf8') as f:
    tmp = None
    for idx, x in enumerate(f):
        if x[0] == "/":
            tmp = x
            datas[tmp] = []
        else:
            datas[tmp].append(x)
print(datas)

'''
defaultdict(list,
            {'// PGC5000::AT-9202_SO2411046-040::/\n': ['AT-9202_SO2411046-040. MasterScopeRollup ,1,10001,\n',
              'AT-9202_SO2411046-040.ALARMS.POWER Fail,1,1002,\n',
              'AT-9202_SO2411046-040.ALARMS.Network Comm Failure,1,10003,\n',
              'AT-9202_SO2411046-040.ALARMS.Purge Fail MC,1,10004,\n',
              'AT-9202_SO2411046-040.ALARMS.Comm Failure Oven1,1,10005,\n',
              'AT-9202_SO2411046-040.ALARMS.Comm Failure Oven2,1,10006,\n',
              'AT-9202_SO2411046-040.ALARMS.Comm Failure Oven3,1,10007,\n',
              'AT-9202_SO2411046-040.ALARMS.Comm Failure Oven4,1,10008,\n'],
             '// PGC5000Oven::2411046-040::/\n': ['AT-9202_SO2411046-040.2411046-040.ALARMS.Software Error,1,10009,\n',
              'AT-9202_SO2411046-040.2411046-040.ALARMS.DTC Failure,1,10010,\n',
              'AT-9202_SO2411046-040.2411046-040.ALARMS.EPC Failure,1,10011,\n',
              'AT-9202_SO2411046-040.2411046-040.ALARMS.DET Failure,1,10012,\n',
              'AT-9202_SO2411046-040.2411046-040.ALARMS.Purge Fail Oven,1,10013,\n',
              'AT-9202_SO2411046-040.2411046-040.ALARMS.CAN Comm Failure,1,10014,\n',
              'AT-9202_SO2411046-040.2411046-040.ALARMS.Extended I/O Fault,1,10015,\n'],
             '// PGC5000Schedule::SCHD_2411046-040::/\n': ['AT-9202_SO2411046-040.SCHD_2411046-040.Idle,1,10016,\n',
              'AT-9202_SO2411046-040.SCHD_2411046-040.Calibrating,1,10017,\n',
              'AT-9202_SO2411046-040.SCHD_2411046-040.Validating,1,10018,\n',
              'AT-9202_SO2411046-040.SCHD_2411046-040.Maintenance,1,10019,\n'],
             '// PGC5000Stream::Stream 1::/\n': ['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.SampleTime,1,30001,TIMESTAMP3,\n',
              'AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.StreamValid,1,10020,\n',
              'AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.NewDataReady,1,1,2,\n',
              'AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.Oneline,1,10021,\n',
              'AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.OnlineRequest,1,2,\n',
              'AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.REQUEST_Analysis Name,1,3,\n'],
             '// PGC5000Component::HYDROGEN HIGH_ST1::/\n': ['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.HYDROGEN\n',
              'HIGH_ST1.Concentration,1,30004,SCALED0-9999,0,100,\n'],
             '// PGC5000Component::HYDROGEN LOW_ST1::/\n': ['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.HYDROGEN\n',
              'LOW_ST1.Concentration,1,30005,SCALED0-9999,0,10,']})
              
정상으로 읽어온다.
'''




with open("C:\\Users\\kkdh8\\Desktop\\MODBUS.csv", encoding='utf8') as f:
    tmp = None
    for idx, x in enumerate(f):
        if x[0] == "/":
            tmp = x
            datas[tmp] = []
        else:
            datas[tmp].append(list(x.split(","))) # 이렇게 수정하면,
'''
defaultdict(list,
            {'// PGC5000::AT-9202_SO2411046-040::/\n': [['AT-9202_SO2411046-040. MasterScopeRollup ',
               '1',
               '10001',
               '\n'],
              ['AT-9202_SO2411046-040.ALARMS.POWER Fail', '1', '1002', '\n'],
              ['AT-9202_SO2411046-040.ALARMS.Network Comm Failure',
               '1',
               '10003',
               '\n'],
              ['AT-9202_SO2411046-040.ALARMS.Purge Fail MC',
               '1',
               '10004',
               '\n'],
              ['AT-9202_SO2411046-040.ALARMS.Comm Failure Oven1',
               '1',
               '10005',
               '\n'],
              ['AT-9202_SO2411046-040.ALARMS.Comm Failure Oven2',
               '1',
               '10006',
               '\n'],
              ['AT-9202_SO2411046-040.ALARMS.Comm Failure Oven3',
               '1',
               '10007',
               '\n'],
              ['AT-9202_SO2411046-040.ALARMS.Comm Failure Oven4',
               '1',
               '10008',
               '\n']],
             '// PGC5000Oven::2411046-040::/\n': [['AT-9202_SO2411046-040.2411046-040.ALARMS.Software Error',
               '1',
               '10009',
               '\n'],
              ['AT-9202_SO2411046-040.2411046-040.ALARMS.DTC Failure',
               '1',
               '10010',
               '\n'],
              ['AT-9202_SO2411046-040.2411046-040.ALARMS.EPC Failure',
               '1',
               '10011',
               '\n'],
              ['AT-9202_SO2411046-040.2411046-040.ALARMS.DET Failure',
               '1',
               '10012',
               '\n'],
              ['AT-9202_SO2411046-040.2411046-040.ALARMS.Purge Fail Oven',
               '1',
               '10013',
               '\n'],
              ['AT-9202_SO2411046-040.2411046-040.ALARMS.CAN Comm Failure',
               '1',
               '10014',
               '\n'],
              ['AT-9202_SO2411046-040.2411046-040.ALARMS.Extended I/O Fault',
               '1',
               '10015',
               '\n']],
             '// PGC5000Schedule::SCHD_2411046-040::/\n': [['AT-9202_SO2411046-040.SCHD_2411046-040.Idle',
               '1',
               '10016',
               '\n'],
              ['AT-9202_SO2411046-040.SCHD_2411046-040.Calibrating',
               '1',
               '10017',
               '\n'],
              ['AT-9202_SO2411046-040.SCHD_2411046-040.Validating',
               '1',
               '10018',
               '\n'],
              ['AT-9202_SO2411046-040.SCHD_2411046-040.Maintenance',
               '1',
               '10019',
               '\n']],
             '// PGC5000Stream::Stream 1::/\n': [['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.SampleTime',
               '1',
               '30001',
               'TIMESTAMP3',
               '\n'],
              ['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.StreamValid',
               '1',
               '10020',
               '\n'],
              ['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.NewDataReady',
               '1',
               '1',
               '2',
               '\n'],
              ['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.Oneline',
               '1',
               '10021',
               '\n'],
              ['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.OnlineRequest',
               '1',
               '2',
               '\n'],
              ['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.REQUEST_Analysis Name',
               '1',
               '3',
               '\n']],
             '// PGC5000Component::HYDROGEN HIGH_ST1::/\n': [['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.HYDROGEN\n'],
              ['HIGH_ST1.Concentration',
               '1',
               '30004',
               'SCALED0-9999',
               '0',
               '100',
               '\n']],
             '// PGC5000Component::HYDROGEN LOW_ST1::/\n': [['AT-9202_SO2411046-040.SCHD_2411046-040.Stream 1.HYDROGEN\n'],
              ['LOW_ST1.Concentration',
               '1',
               '30005',
               'SCALED0-9999',
               '0',
               '10',
               '']]})
이렇게 데이터 가져온다.               
'''