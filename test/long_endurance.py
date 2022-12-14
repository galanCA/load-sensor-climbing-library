import sys
sys.path.insert(0,'../src')
import climbing_force_sensor

showPlot = False

# Todo:
# Make the output into a table

print("Regression test long endurance")

BW = 148 / 2.20462262185
print("Body weight", "{:.3f}".format(BW), "Kg")
leftHand = climbing_force_sensor.LongEndurance("LeftHand_4m_20mm_7_3.txt")
print("Left Hand:")
#data = leftHand.get_data()
#print("Get data", leftHand.get_data())
leftHand.get_max(BW)
leftHand.get_critical_force(BW)
leftHand.get_anaerobic_capacity(BW)
leftHand.dynamic_strength_index()
print("Get max: ", "{:.2f}".format(leftHand.max_force), "Kg" )
print("Get max percent BW: ", "{:.2f}".format(leftHand.max_force_BW), "%" )
print("Get critical force: ", "{:.2f}".format(leftHand.CF), "Kg" )
print("Get critical force %: ", "{:.2f}".format(leftHand.CF_BW), "%" )
print("Get anaerobic capacity: ", "{:.2f}".format(leftHand.anaerobic_capacity), "Kg s" )
print("Get anaerobic capacity per Kg: ", "{:.2f}".format(leftHand.anaerobic_capacity_BW), "Kg s/Kg" )
print("DSI @ 200ms per Kg: ", "{:.2f}".format(leftHand.anaerobic_capacity_BW), "%")

rightHand = climbing_force_sensor.LongEndurance("Rightarm_4m_20mm_7_3.txt")
rightHand.get_max(BW)
rightHand.get_critical_force(BW)
rightHand.get_anaerobic_capacity(BW)
rightHand.dynamic_strength_index(BW)
print("\nRight hand:")
#data = rightHand.get_data()
#print("Get data", rightHand.get_data())
print("Get max: ", "{:.2f}".format(rightHand.max_force), "Kg" )
print("Get max percent BW: ", "{:.2f}".format(rightHand.max_force_BW), "%" )
print("Get critical force: ", "{:.2f}".format(rightHand.CF), "Kg" )
print("Get critical force %: ", "{:.2f}".format(rightHand.CF_BW), "%" )
print("Get anaerobic capacity: ", "{:.2f}".format(rightHand.anaerobic_capacity), "Kg s" )
print("Get anaerobic capacity per Kg: ", "{:.2f}".format(rightHand.anaerobic_capacity_BW), "Kg s/Kg" )
print("DSI @ 200ms per Kg: ", "{:.2f}".format(leftHand.anaerobic_capacity_BW), "%")

if showPlot:
    leftHand.plot()
    rightHand.plot()
