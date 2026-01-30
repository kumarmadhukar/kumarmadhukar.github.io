
DirNT is a hybrid non-termination checker that (1) uses bounded symbolic
reasoning to generate concrete values for nondeterministic assignments to
variables that can steer program execution towards states that recur, (2)
substitutes these values into the program, and (3) executes the program to
check for recurrence. What makes DirNT unique as well as efficient is its
systematic search for recurrence seeking tests that guide the symbolic
reasoning engine.

