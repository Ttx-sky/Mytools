import os
import requests
import webbrowser
import subprocess
import shutil
import time
import commands

# 打包后的ipa文件路径
backupIPA = '/Users/sino/Desktop/ChinaLife-IPA'
# 应用对应蒲公英路径
openUrlPath = 'https://www.pgyer.com'
# 应用下载页
openDownLoadUrlPath = 'https://www.pgyer.com/manager/dashboard/app'
# 项目scheme
print(openUrlPath, "\n", openDownLoadUrlPath)
schemeName = 'ChinaLife_EC'

# 蒲公英账号USER_KEY、API_KEY及App_Key 需要替换成自己的蒲公英账号对应的key
USER_KEY = "44686765363b42a01a733b2e4fed82d3"
API_KEY = "44686765363b42a01a733b2e4fed82d3"
App_Key = "44686765363b42a01a733b2e4fed82d3"


# clean工程
def cleanPro():
    # 开始时间
    start = time.time()
    # 选择编译环境
    if desDv == 1:
        desDvStr = 'Release'
    else:
        desDvStr = 'Debug'
    # xcodeproj工程
    cleanProRun = 'xcodebuild clean -project %s.xcodeproj -scheme %s -configuration %s' % (
    schemeName, schemeName, desDvStr)
    # workspace工程
    # cleanProRun = 'xcodebuild clean -workspace %s.xcworkspace -scheme %s -configuration %s'%(schemeName,schemeName,desDvStr)

    print('%s' % cleanProRun)
    cleanProcessRun = subprocess.Popen(cleanProRun, shell=True)
    cleanProcessRun.wait()
    # 结束时间
    end = time.time()
    # 获取Code码
    cleanReturnCode = cleanProcessRun.returncode
    print('%s' % cleanReturnCode)
    if cleanReturnCode != 0:
        print("\n***************clean失败******耗时:%s秒***************\n" % (end - start))
    else:
        print("\n***************clean成功*********耗时:%s秒************\n" % (end - start))
        # archive
        archive()


# 编译打包流程
def archive():
    # 删除之前打包的ChinaLife-IPA文件夹
    subprocess.call(["rm", "-rf", backupIPA])
    time.sleep(1)
    # 在桌面上创建ChinaLife-IPA文件夹
    mkdir(backupIPA)
    #    subprocess.call(["mkdir","-p",backupIPA])
    time.sleep(1)
    # 开始时间
    start = time.time()
    # xcodeproj工程
    # archiveRun = 'xcodebuild archive -project %s.xcodeproj -scheme %s -archivePath ./build/%s.xcarchive'%(schemeName,schemeName,schemeName)
    archiveRun = 'xcodebuild archive -project %s.xcodeproj -scheme %s -archivePath %s/%s.xcarchive' % (
    schemeName, schemeName, backupIPA, schemeName)
    # workspace工程
    # archiveRun = 'xcodebuild archive -workspace %s.xcworkspace -scheme %s -archivePath %s/%s.xcarchive'%(schemeName,schemeName,backupIPA,schemeName)

    print('%s' % archiveRun)
    archiveProcessRun = subprocess.Popen(archiveRun, shell=True)
    archiveProcessRun.wait()
    # 结束时间
    end = time.time()
    # 获取Code码
    archiveReturnCode = archiveProcessRun.returncode
    print('%s' % archiveReturnCode)
    if archiveReturnCode != 0:
        print("\n***************archive失败******耗时:%s秒***************\n" % (end - start))
    else:
        print("\n***************archive成功*********耗时:%s秒************\n" % (end - start))
        # 导出IPA
        exportIPA()


def exportIPA():
    # 开始时间
    start = time.time()
    # iOS8.2之前打包方式
    # exportRun = 'xcodebuild -exportArchive -archivePath ./build/%s.xcarchive -exportPath ./build/%s -exportFormat ipa -exportProvisioningProfile "adhoc_coolfood'%(schemeName,schemeName)
    # iOS9
    exportRun = 'xcodebuild -exportArchive -archivePath %s/%s.xcarchive -exportPath %s %s -exportOptionsPlist ./ExportOptions.plist' % (
    backupIPA, schemeName, backupIPA, schemeName)
    print('++++++%s' % exportRun)
    exportProcessRun = subprocess.Popen(exportRun, shell=True)
    exportProcessRun.wait()

    # 结束时间
    end = time.time()
    # 获取Code码
    exportReturnCode = exportProcessRun.returncode
    if exportReturnCode != 0:
        print("\n***************导出IPA失败*********耗时:%s秒************\n" % (end - start))
    else:
        print("\n***************导出IPA成功*********耗时:%s秒************\n" % (end - start))
        # 切换到当前目录
        os.chdir(backupIPA)
        # 删除app后缀文件
        commands.getoutput('rm -rf ./*.xcarchive')
        time.sleep(1)


#        uploadIPA('%s/%s.ipa'%(backupIPA,schemeName))
#        openDownloadUrl()

# 个人打包不需要，先注释掉
# 上传蒲公英
# def uploadIPA(IPAPath):
#    if(IPAPath==''):
#        print("\n***************没有找到关联IPA包*********************\n")
#        return
#    else:
#        print("\n***************IPA包开始上传到蒲公英*********************\n")
#        url='http://www.pgyer.com/apiv1/app/upload'
#        data={
#            'uKey':USER_KEY,
#            '_api_key':API_KEY,
#            'installType':'2',
#           #下载IPA密码可以为空
#            'password':'123456',
#            'updateDescription':des
#        }
#        files={'file':open(IPAPath,'rb')}
#        r=requests.post(url,data=data,files=files)
#
# def openDownloadUrl():
#    #用非系统默认浏览器打开
#    webbrowser.open('%s%s'%(openUrlPath,App_Key),new=1,autoraise=True)
#    time.sleep(3)
#    webbrowser.open(openDownLoadUrlPath,new=1,autoraise=True)
#    print ("\n*************** IPA上传更新成功 *********************\n")

##创建backupIPA文件夹
def mkdir(backupIPA):
    isExists = os.path.exists(backupIPA)
    if not isExists:
        os.makedirs(backupIPA)
        print(backupIPA + '创建成功')
        return True
    else:
        print(backupIPA + '目录已经存在')
        return False


# if __name__ == '__main__'的意思是：
# 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__ == '__main__':
    des = input("请输入更新的日志描述:")
    desDv = input('请输入编译环境 1、Release 2、Debug:')
    # clean
    cleanPro()

