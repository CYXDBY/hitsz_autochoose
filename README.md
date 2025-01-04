# 项目概述
hitsz本研平台自动抢课脚本

大三了用不着这玩意抢了，顺手开源了

# 使用教程
**1.此图为需要填写的参数列表，下面展示如何填写关键参数**
![image](https://github.com/user-attachments/assets/732b92a6-f953-4e47-988b-f80c537c5741)

**2.p_ids的填写**

首先进入本研平台的选课界面
![image](https://github.com/user-attachments/assets/ebce639a-808a-419d-b755-9a08a8b77f9f)

按下F12打开开发者选项，进入网络页面
![image](https://github.com/user-attachments/assets/4a066758-38d3-4c14-872b-30d068fd45ba)

然后点击所需要课程所在的栏目，此时右边会多出一个数据包
![image](https://github.com/user-attachments/assets/b0dae0fe-b486-4462-b36b-00c6dcb33619)

打开该数据包的**预览**页面，这些就是各个课程的**p_id**了
![image](https://github.com/user-attachments/assets/313931b5-f020-4517-8dc0-33315e20e63e)

打开可以看到课程名字，注意**p_id**是**id**，而不是**kcid**
![image](https://github.com/user-attachments/assets/b72c4f87-8737-4c43-99d3-6a2060d4092b)


**3.p_xkfsdm的填写**

打开与p_id同一个数据包的另一项
![image](https://github.com/user-attachments/assets/56dad737-aba7-4164-a8cd-7bdc37327649)

下拉找到课程类型，即**p_xkfsdm**
![image](https://github.com/user-attachments/assets/ea87ce03-7c44-4949-b3e1-742ca78369ce)


**4.剩余参数**

学年学期等参数根据注释填写即可

**switch**为1时，运行脚本即开始抢课

**switch**为0时，运行脚本到指定时间时自动开始抢课（使用前需先手动校准电脑右下角的本地时间）

**注：由于学校的服务器太烂，基本上每次到选课前一两分钟都要重新刷新一次cookie，所以定时选课功能基本废了，还是要到时间手动运行**



**5.cookie参数**

抢课期间学校的垃圾服务器会把已经在线的人卡下线，此时整个系统基本是登不上去的。对于正常选课的人需要先登录上系统，加载出画面，还要艰难地进入到选课页面才能选课，基本不可能。

然而cookie在点击**登录**的时候就有，这样就能做到还没进入平台就能抢到课，以下为具体流程：

被卡掉后，一般都会处在这个界面，此时打开F12并且清空一下数据包历史
![image](https://github.com/user-attachments/assets/b18826b7-b13c-4d1a-b85e-9857eb28e019)

点击登录，随便在右侧找一个有cookie的数据包，将该cookie粘贴到脚本中即可
![image](https://github.com/user-attachments/assets/13b79306-520a-4787-a7b3-2677953d977f)

**注：如果提示jsessionid失效等错误，说明你又被踢下线了，重试拿一个新cookie即可**

