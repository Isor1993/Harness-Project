# Unit 1 - Block 1: variables, basic types, print, f-strings.
# Task: read and explain, then predict the exact output.

robot_name = "omega-3"
battery_level = 87
voltage = 11.63
is_charging = False

print("Robot:", robot_name)
print(f"Battery: {battery_level}%")

hours_left = battery_level / 20
print(f"Time left: {hours_left:.1f} hours")

if battery_level < 20 and not is_charging:
    print("WARNING: low battery!")
