address = "192.168.58.2"
port = "COM8"  # 读或者写端口
baudrate = 19200  # 波特率
timeout = 0.50  # 读超时设置

beeperDuration = 333
beeperfreq = 1555

FT_trigger = False#力控被触发标志
sensor_num = 1  # 力传感器编号
selection = [0, 0, 1, 0, 0, 0]
# 碰撞检测力和力矩，检测范围（force_torque-min_threshold,force_torque+max_threshold）
force_torque = [0.0, 0.0, -12.0, 0.0, 0.0, 0.0]
gain = [0.0001, 0.0, 0.0005, 0.0, 0.0, 0.0]  # 最大阈值
adj_sign = 1  # 自适应启停状态，0-关闭，1-开启
ilc_sign = 0  # ILC 控制启停状态，0-停止，1-训练，2-实操
max_dis = 500.0  # 最大调整距离
max_ang = 0.0  # 最大调整角度
# 表面定位参数
rcs = 1  # 参考坐标系，0-工具坐标系，1-基坐标系
direction = 2  # 移动方向，1-正方向，2-负方向
axis = 3  # 移动轴，1-X,2-Y,3-Z
lin_v = 15.0  # 探索直线速度，单位 mm/s
lin_a = 15.0  # 探索直线加速度，单位 mm/s^2
disMax = 100.0  # 最大探索距离，单位 mm
force_goal = 3.0  # 动作终止力阈值，单位 N
#碰撞守护
actFlag = 1 #开启标志，0-关闭碰撞守护，1-开启碰撞守护
is_select = [0,0,1,0,0,0] #六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
force_guard = [0.0,0.0,0.0,0.0,0.0,0.0] #碰撞检测力和力矩，检测范围（force_torque-min_threshold,force_torque+max_threshold）
max_threshold = [0.0,0.0,35.0,0.0,0.0,0.0] #最大阈值
min_threshold = [0.0,0.0,25.0,0.0,0.0,0.0] #最小阈值

istest = True
j0 =[[-82.9147973391089, -99.24004583075495, -92.87798286664604, -83.9551264696782, 90.99573116491337, -32.79690884127475],
     [-91.35795366646039, -105.6460541073638, -87.0258595683787, -81.0767085009282, 92.3410668703589, -32.7962561881188],
     [-98.21059425278466, -102.314694848391, -92.9530379795792, -75.5067489170792, 92.4313505569307, -32.79821414758663],
     [-91.59269125154702, -98.78928005105197, -96.45147644647275, -74.7740369740099, 93.06572942450495, -32.8247553759282]]
p0 = [[-32.2376480102539, -553.4932861328125, 318.3493041992187, 175.424118041992, 4.119261741638183, -140.3353576660156],
      [-111.9942169189453, -592.76025390625, 308.2303161621093, 178.1111907958984, 3.995391368865967,-148.7042083740234],
      [-178.493209838867, -552.515869140625, 301.926300048828, -179.3338623046875, 2.46322178840637, -155.4144897460937],
      [-111.8463058471679, -545.124267578125, 308.2901611328125, -178.3494720458984, 2.583897590637207, -148.7311096191406]]