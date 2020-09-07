steps = "UDDDUDUU"
altitude = 0
valleys = 0

for n_step, direction in enumerate(steps):
    if direction == "U":
        altitude += 1
    elif direction == "D":
        if altitude == 0:
            valleys += 1
        altitude -= 1

print(valleys)
