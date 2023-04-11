Weight = 1.5

#Ground Shipping

if Weight <= 2:
  cost_ground = 1.5 * Weight + 20.00
elif Weight <= 6:
  cost_ground = 3.0 * Weight + 20.00
elif Weight <= 10:
  cost_ground = 4.0 * Weight + 20.00
elif Weight > 10:
  cost_ground = 4.75 * Weight + 20.00
else:
  print("Error")

print("Ground Shipping Cost $", cost_ground)
#Ground Shipping Premium

cost_ground_premium = 125.00

print("Cost Ground Premium $", cost_ground_premium )


#Drone Shipping

if Weight <= 2:
  cost_drone = 4.50 * Weight
elif Weight <= 6:
  cost_drone = 9.0 * Weight
elif Weight <= 10:
  cost_drone = 12.0 * Weight
elif Weight > 10:
  cost_drone = 14.25 * Weight
else:
  print("Error")

print("Drone Shipping Cost $", cost_drone)