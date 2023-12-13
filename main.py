patterns = {"div": 5, "tri": 20, "freezing": 30, "bi": 45, "above": 90}
bigl = max([len(e) for e,_ in patterns.items()])
patterns = {k + ":" + ((bigl - len(k)) * " "):v for k,v in patterns.items()}
patternsn = [v for k, v in patterns.items()]
patternsi = {v: k for k, v in patterns.items()}
# noby being wrong doesn't realise 180 is a special case, but we can't include it here
target = float(input("target theta (deg): "))
# sign = -1 if target < 0 else 0
# target = abs(target)
upper = 1601
for pattern in patternsn:
    if abs(target) > pattern:
        continue
    err = 10**-4
    for padding in range(1, upper):
        # spells = padding + 1
        # step = 2 * pattern / padding
        
		# theory:
		# theta = pattern - before / padding * 2 * pattern
		# we are trying to find before
		# theta = pattern * (1 - 2 * before / padding)
		# 1 - theta / pattern = 2 * before / padding
		# before = padding * (1 - theta / pattern) / 2 
		# force before E Z
        solution = round(padding * (1 - target / pattern) / 2)
        error = abs(pattern - solution / padding * 2 * pattern - target)
        if error < err:
            err = error
            print(f'{patternsi[pattern]} {(solution)}, {padding - solution} has {error:.5f}deg error\n{"." * (solution)}S{"."*(padding - solution)}')

# formation behind back is special so we have to do it here
pattern = 180
if abs(target) > pattern:
	exit()
err = 10**-4
for padding in range(1, upper):
	spells = padding + 1
	# step = 2 * pattern / spells # special rule: >= 179 does this
	
	# theory:
	# theta = pattern - before / padding * 2 * pattern
	# we are trying to find before
	# theta = pattern * (1 - 2 * before / padding)
	# 1 - theta / pattern = 2 * before / padding
	# before = padding * (1 - theta / pattern) / 2 
	# force before E Z
	solution = round(spells * (1 - target / pattern) / 2)
	error = abs(pattern - solution / spells * 2 * pattern - target)
	if error < err:
		err = error
		print(f'behind {(solution)}, {padding - solution} has {error:.5f}deg error\n{"." * (solution)}S{"."*(padding - solution)}')
