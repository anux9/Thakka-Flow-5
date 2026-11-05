# دالة تحسب حالة المركبة بعد ثانية واحدة
def step(altitude, velocity, fuel, thrust):
    new_velocity = velocity - 1.62 + (thrust * 0.5)
    new_altitude = altitude - new_velocity
    new_fuel = fuel - thrust

    return new_altitude, new_velocity, new_fuel


# بداية الهبوط اليدوي
altitude = 1000
velocity = 0
fuel = 200
time = 0

print("Manual Landing")

while altitude > 0:
    print("Altitude:", round(altitude, 2))
    print("Velocity:", round(velocity, 2))
    print("Fuel:", round(fuel, 2))

    # التأكد من أن قيمة الدفع صحيحة
    while True:
        try:
            thrust = float(input("Enter thrust (0-10): "))

            if thrust < 0 or thrust > 10 or thrust > fuel:
                print("Invalid thrust. Try again.")
            else:
                break

        except ValueError:
            print("Please enter a number.")

    altitude, velocity, fuel = step(altitude, velocity, fuel, thrust)
    time = time + 1


# نتيجة الهبوط اليدوي
if velocity <= 3:
    print("Safe Landing!")
else:
    print("Crashed!")

print("Final speed:", round(velocity, 2))
print("Remaining fuel:", round(fuel, 2))
print("Flight time:", time, "seconds")


# -------------------------
# Autopilot
# -------------------------

def autopilot(altitude, velocity, fuel):

    # يحدد سرعة مناسبة حسب ارتفاع المركبة
    target_speed = (2 * 0.8 * altitude) ** 0.5

    if target_speed > 22:
        target_speed = 22

    thrust = 3.24 + 2 * (target_speed - velocity)

    if thrust < 0:
        thrust = 0

    if thrust > 10:
        thrust = 10

    return thrust


# بداية الطيار الآلي
altitude = 1000
velocity = 0
fuel = 200
time = 0

print("\nAutopilot Landing")

while altitude > 0:
    thrust = autopilot(altitude, velocity, fuel)

    if thrust > fuel:
        thrust = fuel

    altitude, velocity, fuel = step(altitude, velocity, fuel, thrust)
    time = time + 1


# نتيجة الطيار الآلي
if velocity <= 3:
    print("Safe Landing!")
else:
    print("Crashed!")

print("Final speed:", round(velocity, 2))
print("Remaining fuel:", round(fuel, 2))
print("Flight time:", time, "seconds")