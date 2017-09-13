#!/usr/bin/env python2
#-*-encoding:utf-8-*-

import os,sys
import linecache
import json
import config as config
from collections import OrderedDict

dirStr = "20"   #根目录文件夹匹配前两个字符

#检查主板串号RC
def Checkm2LogInfo_MBSN(dir):
    DirName2 = dir[-14:]     #2级目录名字

    DirNameList4 = ListDir(dir+r'\apr')
    DirName4 = DirNameList4[0] #4级目录名字

    m2Dir = dir + r'\m2'
    LogNameList = ListDir(m2Dir)
    LogDir = m2Dir + "\\"+ LogNameList[0]
    MBSN = GetM2LogMBSN(LogDir)
    MBSN = MBSN[-15:-1]

    if DirName2 == DirName4 == MBSN:
        ChenkFlg = True
    else:
        ChenkFlg = False

    Outdata = {'ChenkFlg': ChenkFlg,'DirName2':DirName2,'DirName4':DirName4,'MBSN':MBSN}
    Outjson = json.dumps(Outdata)
    return Outjson

#检查机器串号RC
def Checkm2LogInfo_TBSN(dir):
    tabletSN = GetSn(dir)
    tabletSN = tabletSN[:-1]

    m2Dir = dir + r'\m2'
    LogNameList = ListDir(m2Dir)
    LogDir = m2Dir + "\\" + LogNameList[0]
    SN = GetM2LogSN(LogDir)
    SN = SN[3:-1]

    LogNameSN = LogNameList[0][:-4]

    if tabletSN == SN == LogNameSN:
        ChenkFlg = True
    else:
        ChenkFlg = False

    Outdata = {'ChenkFlg': ChenkFlg,'tabletSN':tabletSN,'SN':SN,'LogNameSN':LogNameSN}
    Outjson = json.dumps(Outdata)
    return Outjson

#检查realsenseSN RC   //保留
def Checkm2LogInfo_RSSN(dir):
    ChenkFlg = True
    Outdata = {'ChenkFlg': ChenkFlg}
    Outjson = json.dumps(Outdata)
    return Outjson

#检查build.image 号码C
def Checkm2LogInfo_BUIM(dir):
    m2Dir = dir + r'\m2'
    LogNameList = ListDir(m2Dir)
    LogDir = m2Dir + "\\" + LogNameList[0]
    BUIM = GetM2LogBUIM(LogDir)
    BUIM = BUIM[:-1]

    if BUIM == config.BUILD:
        ChenkFlg = True
    else:
        ChenkFlg = False

    Outdata = {'ChenkFlg': ChenkFlg,'BUIM':BUIM,'config.BUILD':config.BUILD}
    Outjson = json.dumps(Outdata)
    return Outjson

#检查build.image 号码C
def Checkm2LogInfo_BUFP(dir):
    m2Dir = dir + r'\m2'
    LogNameList = ListDir(m2Dir)
    LogDir = m2Dir + "\\" + LogNameList[0]
    BUFP = GetM2LogBUFP(LogDir)
    BUFP = BUFP[:-1]

    if BUFP == config.BUFP:
        ChenkFlg = True
    else:
        ChenkFlg = False

    Outdata = {'ChenkFlg': ChenkFlg,'BUFP':BUFP,'config.BUFP':config.BUFP}
    Outjson = json.dumps(Outdata)
    return Outjson

#获取ecs主板测试时间
def Checkm2LogInfo_m2_test_time(dir):
    m2Dir = dir + r'\m2'
    LogNameList = ListDir(m2Dir)
    LogDir = m2Dir + "\\" + LogNameList[0]
    test_time = Getm2TestTime(LogDir)
    test_time = test_time[8:-10]
    return test_time

#ecs主板测试结果
def Checkm2LogInfo_m2_test_result(dir):
    m2Dir = dir + r'\m2'
    LogNameList = ListDir(m2Dir)
    LogDir = m2Dir + "\\" + LogNameList[0]

    brightness_test = Get_brightness_test_Result(LogDir)
    brightness_test = brightness_test[-5:-1]

    scan_sn = Get_scan_sn_Result(LogDir)
    scan_sn = scan_sn[-5:-1]

    ring_test = Get_ring_test_Result(LogDir)
    ring_test = ring_test[-5:-1]

    charge_test = Get_charge_test_Result(LogDir)
    charge_test = charge_test[-5:-1]

    J2xxHyperTerm_test = Get_J2xxHyperTerm_test_Result(LogDir)
    J2xxHyperTerm_test = J2xxHyperTerm_test[-5:-1]

    BmmCompass_test = Get_BmmCompass_test_Result(LogDir)
    BmmCompass_test = BmmCompass_test[-5:-1]

    gps_test = Get_gps_test_Result(LogDir)
    gps_test = gps_test[-5:-1]

    mic_test = Get_mic_test_Result(LogDir)
    mic_test = mic_test[-5:-1]

    fpga_mic_test = Get_fpga_mic_test_Result(LogDir)
    fpga_mic_test = fpga_mic_test[-5:-1]

    bt_wifi_test = Get_bt_wifi_test_Result(LogDir)
    bt_wifi_test = bt_wifi_test[-5:-1]

    touch_draw = Get_touch_draw_Result(LogDir)
    touch_draw = touch_draw[-5:-1]

    camera_supported_size = Get_camera_supported_size_Result(LogDir)
    camera_supported_size = camera_supported_size[-5:-1]

    accel_test = Get_accel_test_Result(LogDir)
    accel_test = accel_test[-5:-1]

    vga_camere = Get_vga_camere_Result(LogDir)
    vga_camere = vga_camere[-5:-1]

    lcd_test = Get_lcd_test_Result(LogDir)
    lcd_test = lcd_test[-5:-1]

    otg_test = Get_otg_test_Result(LogDir)
    otg_test = otg_test[-5:-1]

    version_info = Get_version_info_Result(LogDir)
    version_info = version_info[-5:-1]

    thermal_test = Get_thermal_test_Result(LogDir)
    thermal_test = thermal_test[-5:-1]

    main_camera = Get_main_camera_Result(LogDir)
    main_camera = main_camera[-6:-2]

    if brightness_test == scan_sn == ring_test == charge_test == J2xxHyperTerm_test == BmmCompass_test \
        == gps_test == mic_test == fpga_mic_test == bt_wifi_test == touch_draw == camera_supported_size \
        == accel_test == vga_camere == lcd_test == otg_test == version_info == thermal_test == main_camera == "pass":
        ChenkFlg = True
    else:
        ChenkFlg = False

    Outdata = {'ChenkFlg': ChenkFlg, 'brightness_test': brightness_test,'scan_sn':scan_sn,'ring_test':ring_test,
               'charge_test':charge_test,'J2xxHyperTerm_test':J2xxHyperTerm_test,'BmmCompass_test':BmmCompass_test,
               'gps_test':gps_test,'mic_test':mic_test,'fpga_mic_test':fpga_mic_test,'bt_wifi_test':bt_wifi_test,
               'touch_draw':touch_draw,'camera_supported_size':camera_supported_size,'accel_test':accel_test,'vga_camere':vga_camere,
               'lcd_test':lcd_test,'otg_test':otg_test,'version_info':version_info,'thermal_test':thermal_test,'main_camera':main_camera}
    Outjson = json.dumps(Outdata)
    return Outjson

#----------------------------------------------------------------------------------
#获取MBSN号
def GetM2LogMBSN(dir):
    return linecache.getline(dir, 4)

#获取SN号
def GetSn(dir):
    return  linecache.getline(dir+r'\tablet.sn', 1)

#获取LOG SN号
def GetM2LogSN(dir):
    return linecache.getline(dir, 3)

#获取BUIM 版本号
def GetM2LogBUIM(dir):
    return linecache.getline(dir, 19)

#获取BUIM 版本号
def GetM2LogBUFP(dir):
    return linecache.getline(dir, 20)

#获取ecs主板测试时间
def Getm2TestTime(dir):
    return linecache.getline(dir, 9)

#获取主板测试结果
#brightness_test
def Get_brightness_test_Result(dir):
    return linecache.getline(dir, 39)
#scan_sn
def Get_scan_sn_Result(dir):
    return linecache.getline(dir, 40)
#ring_test
def Get_ring_test_Result(dir):
    return linecache.getline(dir, 41)
#change_test
def Get_charge_test_Result(dir):
    return linecache.getline(dir, 42)
#J2xxHyperTerm_test
def Get_J2xxHyperTerm_test_Result(dir):
    return linecache.getline(dir, 43)
#BmmCompass_test
def Get_BmmCompass_test_Result(dir):
    return linecache.getline(dir, 44)
#gps_test
def Get_gps_test_Result(dir):
    return linecache.getline(dir, 45)
#mic_test
def Get_mic_test_Result(dir):
    return linecache.getline(dir, 46)
#fpga_mic_test
def Get_fpga_mic_test_Result(dir):
    return linecache.getline(dir, 47)
#bt_wifi_test
def Get_bt_wifi_test_Result(dir):
    return linecache.getline(dir, 48)
#touch_draw
def Get_touch_draw_Result(dir):
    return linecache.getline(dir, 49)
#camera_supported_size
def Get_camera_supported_size_Result(dir):
    return linecache.getline(dir, 50)
#accel_test
def Get_accel_test_Result(dir):
    return linecache.getline(dir, 51)
#vga_camere
def Get_vga_camere_Result(dir):
    return linecache.getline(dir, 52)
#lcd_test
def Get_lcd_test_Result(dir):
    return linecache.getline(dir, 53)
#otg_test
def Get_otg_test_Result(dir):
    return linecache.getline(dir, 54)
#version_info
def Get_version_info_Result(dir):
    return linecache.getline(dir, 55)
#thermal_test
def Get_thermal_test_Result(dir):
    return linecache.getline(dir, 56)
#main_camera
def Get_main_camera_Result(dir):
    return linecache.getline(dir, 57)
#-----------------------------------------------------------------------------------
#列出指定路径下的所有文件及文件夹
def ListDir(dir):
    list = os.listdir(dir)
    return list

#找出目标文件夹
def IsNeedDir(list):
    OutList = []
    for dir in list:
        if os.path.isdir(dir):
            if dir[0:2] == dirStr:
                OutList.append(dir)
    return OutList

# 遍历指定目录，显示目录下的所有文件名，并保存路径。
def eachFile(pwd,filepath,AllDirList):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        AllDirList.append(pwd+"\\"+filepath+'\\'+allDir)

# 遍历多个目录，显示目录下的所有文件名
def eachAllDir(pwd,list,AllDirList):
    for dir in list:
        eachFile(pwd,dir,AllDirList)

#获取当前路径
def GetPwd():
    return os.getcwd()


#------------------------run-------------------------------------------
def MainLogoAnalysis():
    num = 0

    pwd = GetPwd()
    # 获取当前路径下的所有文件
    DirList = ListDir(pwd)
    # 提取需要分析的根目录
    NeedDir = IsNeedDir(DirList)
    # 提取所有待分析的文件夹的路径
    AllDirList = []  # 所有数据目录集合
    eachAllDir(pwd,NeedDir, AllDirList)

    AllDatadic = OrderedDict()   #保存所有结果的字典

    for DirList in AllDirList:
        #001
        MBSNjson = Checkm2LogInfo_MBSN(DirList)    #检查主板串号RC 并返回结果
        #print "MBSNjson:  " + MBSNjson
        #002
        TBSNjson = Checkm2LogInfo_TBSN(DirList)    #检查机器串号RC 并返回结果
        #print "TBSNjson:  " + TBSNjson
        #003
        RSSNjson = Checkm2LogInfo_RSSN(DirList)  #检查realsenseSN RC 并返回结果
        #print "RSSNjson:  " + RSSNjson
        #004
        BUIMjson = Checkm2LogInfo_BUIM(DirList)  #检查build.image 号码C
        #print "BUIMjson:  " + BUIMjson
        #005
        BUFPjson =  Checkm2LogInfo_BUFP(DirList)  #检查build 的指纹
        #print "BUFPjson:  " + BUFPjson
        #006
        ecs_log_pull_time = AllDirList[0][:-15]              #获取日志上传时间
        ecs_log_pull_time = ecs_log_pull_time[-8:]
        #print "ecs_log_pull_time:  " + ecs_log_pull_time
        #007
        m2_test_time = Checkm2LogInfo_m2_test_time(DirList) #ecs主板测试时间
        #print "m2_test_time:  " + m2_test_time

        m2_test_resultjson = Checkm2LogInfo_m2_test_result(DirList) #ecs主板测试结果
        #print "m2_test_resultjson:  " + m2_test_resultjson

        num = num +1    #key++
        Data = {'MBSNjson':json.loads(MBSNjson),'TBSNjson':json.loads(TBSNjson),'RSSNjson':json.loads(RSSNjson),'BUIMjson':json.loads(BUIMjson),
                      'BUFPjson':json.loads(BUFPjson),'ecs_log_pull_time':ecs_log_pull_time,'m2_test_time':m2_test_time,'m2_test_resultjson':json.loads(m2_test_resultjson)}

        AllDatadic[num] = Data  #转化为dict 方便append

    OutputJson = json.dumps(AllDatadic)
    return OutputJson


#主函数
if __name__ == "__main__":
    Result = MainLogoAnalysis()
    #print Result
    file_object = open('Result.json', 'w')
    file_object.write(Result)
    file_object.close()
