import sys
sys.path.insert(0,'../src')
import climbing_force_sensor

print("Regression test long endurance")

rightHand = climbing_force_sensor.LongEndurance("Rightarm_4m_20mm_7_3.txt")
#print("Get data", rightHand.get_data())
#print("Get Max", rightHand.get_max())
#print("Area under the curve", rightHand.get_integral())

#rightHand.plot()

