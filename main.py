from sys import stdin

patterns = {
	"Divide by X": 5,
	"Formation - Trifurcated": 20,
	"Freezing Gaze": 30,
	"Formation - Bifurcated": 45,
	"Formation - Above and Below": 90,
	"Formation - Circle": 180,
}
bigl = max([len(e) for e, _ in patterns.items()])
patterns = {k + ":" + ((bigl - len(k)) * " "): v for k, v in patterns.items()}
patternsn = [v for k, v in patterns.items()]
patternsi = {v: k for k, v in patterns.items()}
target = float(input("target theta (deg): "))
# sign = -1 if target < 0 else 0
# target = abs(target)
error_degrees = input("maximum error (deg) (no input is find best solutions):")
error_cond = error_degrees == ""
upper = input("maximum number of projectiles in a solution (no input is 200):")
output = ""
if upper == "":
	upper = "200"
upper = int(upper)
for pattern in patternsn:
	if abs(target) > pattern:
		continue
	output = output + patternsi[pattern] + "\n"
	cur_table = []
	err = 360 if error_cond else float(error_degrees)
	for padding in range(upper):
		# theory:
		# theta = pattern - before / padding * 2 * pattern
		# we are trying to find before
		# theta = pattern * (1 - 2 * before / padding)
		# 1 - theta / pattern = 2 * before / padding
		# before = padding * (1 - theta / pattern) / 2
		# force before E Z
		if padding == 0:
			solution = 0
			error = target
		else:
			if pattern >= 179:	# off by 1 present in vanilla
				spells = padding + 1
				solution = round(spells * (1 - target / pattern) / 2)
				error = abs(pattern - solution / spells * 2 * pattern - target)
			else:
				solution = round(padding * (1 - target / pattern) / 2)
				error = abs(pattern - solution / padding * 2 * pattern - target)
		if error < err:
			if error_cond:
				err = error
			cur_table.append((solution, (padding - solution), error))
	cur_table = [[f"{float(y):.5} ".replace(".0 ", "") for y in x] for x in cur_table]
	cur_table = [("Left ", "Right ", "Error (deg) ")] + cur_table
	parts = [max([len(x[i]) for x in cur_table]) for i in range(3)]
	output = (
		output
		+ "┌"
		+ "─" * (1 + parts[0])
		+ "┬"
		+ "─" * (1 + parts[1])
		+ "┬"
		+ "─" * (1 + parts[2])
		+ "┐\n│ "
	)
	output += "│\n│ ".join(
		[
			str(x[0])
			+ " " * (parts[0] - len(str(x[0])))
			+ "│ "
			+ str(x[1])
			+ " " * (parts[1] - len(str(x[1])))
			+ "│ "
			+ str(x[2])
			+ " " * (parts[2] - len(str(x[2])))
			for x in cur_table
		]
	)
	output += (
		"│\n└"
		+ "─" * (1 + parts[0])
		+ "┴"
		+ "─" * (1 + parts[1])
		+ "┴"
		+ "─" * (1 + parts[2])
		+ "┘\n"
	)

print(output)
copy = input("Copy results? (y/d(iscord)/N): ")
if copy.lower() == "y" or copy.lower() == "d":
	if copy.lower() == "d":
		output = f"```\n{output}```"
	import subprocess

	pipe = subprocess.Popen(["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE)
	pipe.communicate(input=output.encode())
