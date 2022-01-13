import numpy as np
import matplotlib.pyplot as plt
import matplotlib

myself = ["timid", "cowardly", "insecure", "panicky", "insensitive",
          "passive", "dispassionate", "childish", "boastful", "smug"]
other = ["boastful", "smug", "cold", "humourless"]
all_adj = ["incompetent", "intolerant", "inflexible", "timid", "cowardly",
           "violent", "aloof", "glum", "stupid", "simple",
           "insecure", "irresponsible", "vulgar", "lethargic", "withdrawn",
           "hostile", "selfish", "unhappy", "unhelpful", "cynical",
           "needy", "unimaginative", "inane", "brash", "cruel",
           "ignorant", "irrational", "distant", "childish", "boastful",
           "blase", "imperceptive", "chaotic", "impatient", "weak",
           "embarrassed", "loud", "vacuous", "panicky", "unethical",
           "insensitive", "self-satisfied", "passive", "smug", "rash",
           "dispassionate", "overdramatic", "dull", "predictable", "callous",
           "inattentive", "unreliable", "cold", "foolish", "humourless"]

mat11 = list(set(myself) & set(other))
mat21 = list(set(myself) - set(mat11))
mat12 = list(set(other) - set(mat11))
mat22 = list(set(all_adj) - set(myself).union(other))

print("Known to others-Known to self (11)")
print(mat11)
print("\nKnown to others-Not known to self (12)")
print(mat12)
print("\nNot known to others-Known to self (21)")
print(mat21)
print("\nNot known to others-Not known to self (22)")
print(mat22)

mat = np.matrix([[len(mat11), len(mat12)], [len(mat21), len(mat22)]])
print("\nThe window:")
print(mat)

x = np.sqrt(55)
y = np.sqrt(55)

A11 = mat[0, 0]
A12 = mat[0, 1]
A21 = mat[1, 0]
A22 = mat[1, 1]
x1 = x * (A11 + A21) / 55
y1 = A21 / x1
y2 = A22 / (55 / y - x1)

fig = plt.figure()
plt.xlim(0, x)
plt.ylim(0, y)
plt.plot([x1, x1], [0, y], color="black", linewidth=1)
plt.plot([0, x1], [y1, y1], color="black", linewidth=1)
plt.plot([x1, x], [y2, y2], color="black", linewidth=1)
plt.axvspan(0, x1, ymin=y1/y, ymax=1, alpha=0.3, color='green')
plt.axvspan(x1, x, ymin=y2/y, ymax=1, alpha=0.3, color='red')
plt.axvspan(0, x1, ymin=0, ymax=y1/y, alpha=0.3, color='blue')
plt.axvspan(x1, x, ymin=0, ymax=y2/y, alpha=0.3, color='gray')
plt.text(0.5 * x1, 1.03 * y, "Known to me", fontsize=9, ha="center", wrap=True)
plt.text(0.5 * (x + x1), 1.03 * y, "Not known to me", fontsize=9, ha="center", wrap=True)
plt.text(-0.6, 0.5 * (y + y1), "Known to others", fontsize=9, ha="center", wrap=True)
plt.text(-0.6, 0.5 * y1, "Not known to others", fontsize=9, ha="center", wrap=True)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.savefig("JohariWindow.png", dpi=300)
plt.show()
