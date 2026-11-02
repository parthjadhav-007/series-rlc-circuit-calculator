
import math
import matplotlib.pyplot as plt

print("=== RLC Circuit Calculator ===")


while True:
    text = input("Enter resistance value: ")
    try:
        R = float(text)
    except ValueError:
        print("That is not a number. Please try again.")
        continue
    if R <= 0:
        print("The value must be greater than zero. Please try again.")
        continue
    break

print("Unit:  1) ohm   2) kilo-ohm")
while True:
    unit = input("Choose unit (1-2): ")
    if unit == "1" or unit == "2":
        break
    print("Please type 1 or 2.")

if unit == "2":
    R = R * 1000


while True:
    text = input("Enter inductance value: ")
    try:
        L = float(text)
    except ValueError:
        print("That is not a number. Please try again.")
        continue
    if L <= 0:
        print("The value must be greater than zero. Please try again.")
        continue
    break

print("Unit:  1) henry   2) millihenry   3) microhenry")
while True:
    unit = input("Choose unit (1-3): ")
    if unit == "1" or unit == "2" or unit == "3":
        break
    print("Please type 1, 2 or 3.")

if unit == "2":
    L = L / 1000
elif unit == "3":
    L = L / 1000000


while True:
    text = input("Enter capacitance value: ")
    try:
        C = float(text)
    except ValueError:
        print("That is not a number. Please try again.")
        continue
    if C <= 0:
        print("The value must be greater than zero. Please try again.")
        continue
    break

print("Unit:  1) farad   2) microfarad   3) nanofarad   4) picofarad")
while True:
    unit = input("Choose unit (1-4): ")
    if unit == "1" or unit == "2" or unit == "3" or unit == "4":
        break
    print("Please type 1, 2, 3 or 4.")

if unit == "2":
    C = C / 1000000
elif unit == "3":
    C = C / 1000000000
elif unit == "4":
    C = C / 1000000000000


w0 = 1 / math.sqrt(L * C)
f0 = w0 / (2 * math.pi)
Z0 = math.sqrt(L / C)
Q = Z0 / R
bandwidth = f0 / Q
f_low = f0 - bandwidth / 2
f_high = f0 + bandwidth / 2

print("")
print("----- Results -----")
print("Resonant angular frequency (w0) =", w0, "rad/s")
print("Resonant frequency (f0)         =", f0, "Hz")
print("Characteristic impedance (Z0)   =", Z0, "ohm")
print("Quality factor (Q)              =", Q)
print("Bandwidth (f0 / Q)              =", bandwidth, "Hz")
print("Lower cutoff frequency          =", f_low, "Hz")
print("Upper cutoff frequency          =", f_high, "Hz")
print("")
print("Note: cutoff = f0 -/+ bandwidth/2 is an approximation.")
print("It is accurate for high Q and weaker for low Q.")
if f_low <= 0:
    print("Warning: Q is very low, so the lower cutoff is not meaningful.")


points = 200
frequencies = []
magnitudes = []
phases = []

for i in range(points):
    power = -1 + 2 * i / (points - 1)
    f = f0 * (10 ** power)
    w = 2 * math.pi * f
    X = w * L - 1 / (w * C)
    magnitude = math.sqrt(R * R + X * X)
    phase = math.atan2(X, R) * 180 / math.pi

    frequencies.append(f)
    magnitudes.append(magnitude)
    phases.append(phase)


plt.figure(figsize=(8, 7))

plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitudes)
plt.title("Impedance Magnitude")
plt.ylabel("|Z| (ohm)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phases)
plt.title("Impedance Phase")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.grid(True)

plt.show()

