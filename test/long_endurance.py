import sys
from turtle import right
sys.path.insert(0,'../src')
import climbing_force_sensor

print("Regression test long endurance")

BW = 148 / 2.20462262185
print(BW)
rightHand = climbing_force_sensor.LongEndurance("LeftHand_4m_20mm_7_3.txt")
#rightHand = climbing_force_sensor.LongEndurance("Rightarm_4m_20mm_7_3.txt")
#data = rightHand.get_data()
#print("Get data", rightHand.get_data())
print("Get Max", rightHand.get_max(BW))
print("Get critical force: ", rightHand.get_critical_force(BW))
print("Get anarobic capacity: ", rightHand.get_anaerobic_capacity(BW))

#rightHand.plot()

