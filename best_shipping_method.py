def cost_of_ground_shipping(weight):
  if (weight == 2) and (weight < 2):
    price = 1.50
    flat = 20.00
    cost = (weight * price) + flat
    return cost
  elif (weight > 2) and (weight <= 6):
    price = 3.00
    flat = 20.00
    cost = (weight * price) + flat
    return cost
  elif (weight > 6) and (weight <= 10):
    price = 4.00
    flat = 20.00
    cost = (weight * price) + flat
    return cost
  else:
      price = 4.75
      flat = 20.00
      cost = (weight*price) + flat
      return cost

total_cost = cost_of_ground_shipping(4.8)
print(total_cost)

cost_of_premium_shipping = 125.00

def cost_of_drone_shipping(weight):
  if (weight <= 2):
    price = 4.50
    flat = 0.00
    cost = (weight * price) + flat
    return cost
  elif (weight > 2) and  (weight <= 6):
    price = 9.00
    flat = 0.00
    cost = (weight * price) + flat
    return cost
  elif (weight > 6) and (weight <= 10):
    price = 12.00
    flat = 0.00
    cost = (weight * price) + flat
    return cost
  else:
      price = 14.25
      flat = 0.00
      cost = (weight*price) + flat
      return cost
total_cost_of_drone_shipping = cost_of_drone_shipping(4.8)

print(total_cost_of_drone_shipping)

def comparing_shipping_methods(weight):
  ground = cost_of_ground_shipping(weight)
  drone = cost_of_drone_shipping(weight)
  premium = cost_of_premium_shipping
  if (ground < drone) and (ground < premium) :
    print("The cheapest shipping method is ground shipping")
  elif (drone < ground) and (drone < premium) :
      print("The cheapest shipping method is drone shipping")
  else:
    print("the cheapest shipping method is premimum shipping")

comparing_shipping_methods(41.5)
comparing_shipping_methods(4.8)