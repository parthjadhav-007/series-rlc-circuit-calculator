import math
import matplotlib.pyplot as plt

names = ["",
         "R, L and C all in series",
         "R, L and C all in parallel",
         "L and C in parallel, with R in series",
         "C and R in parallel, with L in series",
         "L and R in parallel, with C in series"]

print("=== RLC Circuit Calculator (series, parallel and mixed) ===")
print("")

while True:
    print("How are R, L and C connected?")
    print("  1) all three in series")
    print("  2) all three in parallel")
    print("  3) two of them in parallel, and the third in series with that pair")
    while True:
        choice = input("Choose (1-3): ").strip()
        if choice == "1" or choice == "2" or choice == "3":
            break
        print("Please type 1, 2 or 3.")

    if choice == "1":
        case = 1
    elif choice == "2":
        case = 2
    else:
        print("")
        print("Which one is in series with the other two?")
        print("  1) R")
        print("  2) L")
        print("  3) C")
        while True:
            single = input("Choose (1-3): ").strip()
            if single == "1" or single == "2" or single == "3":
                break
            print("Please type 1, 2 or 3.")
        case = 2 + int(single)

    print("")
    print("Your circuit: " + names[case])
    print("")
    if case == 1:
        print("  --- R --- L --- C ---")
    elif case == 2:
        print("        +--- R ---+")
        print("  ------+--- L ---+------")
        print("        +--- C ---+")
    elif case == 3:
        print("            +--- L ---+")
        print("  --- R ---+          +---")
        print("            +--- C ---+")
    elif case == 4:
        print("            +--- C ---+")
        print("  --- L ---+          +---")
        print("            +--- R ---+")
    else:
        print("            +--- L ---+")
        print("  --- C ---+          +---")
        print("            +--- R ---+")
    print("")

    while True:
        answer = input("Is this your circuit? (y/n): ").strip().lower()
        if answer == "y" or answer == "n":
            break
        print("Please type y or n.")
    if answer == "y":
        break
    print("")

print("")

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

wc = 1 / math.sqrt(L * C)
fc = wc / (2 * math.pi)
Z0 = math.sqrt(L / C)

f_mark = 0

print("")
print("----- Results for: " + names[case] + " -----")
print("1 / sqrt(LC) frequency (wc)     =", wc, "rad/s")
print("1 / sqrt(LC) frequency (fc)     =", fc, "Hz")
print("sqrt(L / C)                     =", Z0, "ohm")
print("")

if case == 1:
    f0 = fc
    Q = Z0 / R
    bandwidth = f0 / Q
    f_low = f0 - bandwidth / 2
    f_high = f0 + bandwidth / 2
    f_mark = f0
    print("Series resonance")
    print("Resonant frequency (f0)         =", f0, "Hz")
    print("Impedance at resonance          =", R, "ohm (minimum)")
    print("Quality factor (Q = Z0 / R)     =", Q)
    print("Bandwidth (f0 / Q)              =", bandwidth, "Hz")
    print("Lower cutoff frequency          =", f_low, "Hz")
    print("Upper cutoff frequency          =", f_high, "Hz")
    print("Note: cutoff = f0 -/+ bandwidth/2 is an approximation.")
    print("It is accurate for high Q and weaker for low Q.")
    if f_low <= 0:
        print("Warning: Q is very low, so the lower cutoff is not meaningful.")

elif case == 2:
    f0 = fc
    Q = R / Z0
    bandwidth = f0 / Q
    f_low = f0 - bandwidth / 2
    f_high = f0 + bandwidth / 2
    f_mark = f0
    print("Parallel resonance")
    print("Resonant frequency (f0)         =", f0, "Hz")
    print("Impedance at resonance          =", R, "ohm (maximum)")
    print("Quality factor (Q = R / Z0)     =", Q)
    print("Bandwidth (f0 / Q)              =", bandwidth, "Hz")
    print("Lower cutoff frequency          =", f_low, "Hz")
    print("Upper cutoff frequency          =", f_high, "Hz")
    print("Note: cutoff = f0 -/+ bandwidth/2 is an approximation.")
    print("It is accurate for high Q and weaker for low Q.")
    if f_low <= 0:
        print("Warning: Q is very low, so the lower cutoff is not meaningful.")

elif case == 3:
    f_mark = fc
    print("The L and C pair is in parallel, so it blocks the current at fc.")
    print("Anti-resonance frequency        =", fc, "Hz")
    print("Impedance at that frequency     = very large (ideal L and C)")
    print("Impedance at very low frequency =", R, "ohm (L acts like a wire)")
    print("The circuit never becomes purely resistive at a normal frequency.")

elif case == 4:
    w0_square = 1 / (L * C) - 1 / (R * R * C * C)
    if w0_square > 0:
        w0 = math.sqrt(w0_square)
        f0 = w0 / (2 * math.pi)
        Zres = L / (R * C)
        f_mark = f0
        print("Resonance (impedance becomes purely resistive)")
        print("Resonant angular frequency (w0) =", w0, "rad/s")
        print("Resonant frequency (f0)         =", f0, "Hz")
        print("Impedance at resonance (L/RC)   =", Zres, "ohm")
    else:
        print("For these values the impedance never becomes purely resistive.")
        print("(Resonance needs R x R x C to be bigger than L.)")

else:
    den = L * (R * R * C - L)
    if den > 0:
        w0_square = R * R / den
        w0 = math.sqrt(w0_square)
        f0 = w0 / (2 * math.pi)
        Zres = w0_square * L * L * R / (R * R + w0_square * L * L)
        f_mark = f0
        print("Resonance (impedance becomes purely resistive)")
        print("Resonant angular frequency (w0) =", w0, "rad/s")
        print("Resonant frequency (f0)         =", f0, "Hz")
        print("Impedance at resonance          =", Zres, "ohm")
    else:
        print("For these values the impedance never becomes purely resistive.")
        print("(Resonance needs R x R x C to be bigger than L.)")

points = 400
frequencies = []
magnitudes = []
phases = []

for i in range(points):
    power = -1 + 2 * i / (points - 1)
    f = fc * (10 ** power)
    w = 2 * math.pi * f

    if case == 1:
        real = R
        imag = w * L - 1 / (w * C)
        magnitude = math.sqrt(real * real + imag * imag)
        phase = math.atan2(imag, real) * 180 / math.pi

    elif case == 2:
        G = 1 / R
        B = w * C - 1 / (w * L)
        magnitude = 1 / math.sqrt(G * G + B * B)
        phase = -math.atan2(B, G) * 180 / math.pi

    elif case == 3:
        den = 1 - w * w * L * C
        if abs(den) < 0.000000000001:
            den = 0.000000000001
        real = R
        imag = w * L / den
        magnitude = math.sqrt(real * real + imag * imag)
        phase = math.atan2(imag, real) * 180 / math.pi

    elif case == 4:
        den = 1 + w * w * R * R * C * C
        real = R / den
        imag = -w * R * R * C / den + w * L
        magnitude = math.sqrt(real * real + imag * imag)
        phase = math.atan2(imag, real) * 180 / math.pi

    else:
        den = R * R + w * w * L * L
        real = w * w * L * L * R / den
        imag = w * L * R * R / den - 1 / (w * C)
        magnitude = math.sqrt(real * real + imag * imag)
        phase = math.atan2(imag, real) * 180 / math.pi

    frequencies.append(f)
    magnitudes.append(magnitude)
    phases.append(phase)

smallest = magnitudes[0]
smallest_f = frequencies[0]
largest = magnitudes[0]
largest_f = frequencies[0]
for i in range(points):
    if magnitudes[i] < smallest:
        smallest = magnitudes[i]
        smallest_f = frequencies[i]
    if magnitudes[i] > largest:
        largest = magnitudes[i]
        largest_f = frequencies[i]

print("")
print("Between", 0.1 * fc, "Hz and", 10 * fc, "Hz:")
print("Smallest |Z| =", smallest, "ohm at", smallest_f, "Hz")
print("Largest |Z|  =", largest, "ohm at", largest_f, "Hz")

plt.figure(figsize=(8, 7))

plt.subplot(2, 1, 1)
plt.loglog(frequencies, magnitudes)
if f_mark > 0:
    plt.axvline(f_mark, linestyle="--")
plt.title("Impedance Magnitude: " + names[case])
plt.ylabel("|Z| (ohm)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phases)
if f_mark > 0:
    plt.axvline(f_mark, linestyle="--")
plt.title("Impedance Phase")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.grid(True)

plt.show()

