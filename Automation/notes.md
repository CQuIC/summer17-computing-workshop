Introduction
============

Welcome to the lesson on using `make` for automation. In this lesson we
will cover some basic aspects of using the utility `make` for automating
the process of running several programs with a complicated dependency
structure.

As a running example, we will consider a simulation of a spin 1/2
particle in a magnetic field and see the spin precession. We will work
in Schrodinger's picture and evolve the state of the particle. For
simplicity, we consider a pure state. The programs doing the
computations are already written. The computations involve a pipeline of
several steps and in this lesson we will focus on how to automate
running these steps.

The lesson has three parts: part 0, part 1 and part 2. In part 0, we
will do everything manually, running all the computations in the
appropriate order. This will help us understand the dependencies in
different aspects of the computations better. In part 1, we will use
make to automate the computations in the appropriate order. We will see
how all the book keeping is done by make. Finally in part 2, we will
write an article in LaTeX using the results of our computations. For
this, we will invoke make recursively. Most of the article is already
written. You just have to write your name and claim it!

Part 0: Manually running the programs
=====================================
The computations for the precession of a spin 1/2 in a magnetic field is 
divided into three phases.

The first phase involves computing the time evolution of a state vector 
in the Schrodinger's picture. This is done in the program 
`simulation.py`. `simulation.py` computes the state and stores it in a 
file called `psi_t.pkl` using the pickle protocol. For our lesson, we 
do not worry about the details of storing and retrieving data using the 
pickle protocol.

Go through `simulation.py` and see how the state vector is computed at
different times. Note the initial state and the Hamiltonian.

Now run `simulation.py` using the following command. Note that we are 
using python3.

```
python3 simulation.py
```

A directory called `output` is created. There will be a directory inside
it called `simulation` which has `psi_t.pkl`.

After computing, the state as a function of time, we want to look at 
some measurement statistics that we expect. For simplicity, we consider 
expectation values of the Pauli operators. This is done in the program 
`statistics.py`. `statistics.py` reads the state as function of time 
from `psi_t.pkl` and computes the expectation value of the Pauli 
operators as a function of time. Thereafter it stores it in files 
called `exp_sigma_x.pkl`, `exp_sigma_y.pkl` and `exp_sigma_z.pkl`, using
the pickle protocol.

Go through `statistics.py` and see how the expectation values of the 
Pauli operators are computed as functions of time.

Now run `simulation.py` using the following command.

```
python3 statistics.py
```

A directory called `statistics` is create inside `output`, which has
`exp_sigma_x.pkl`, `exp_sigma_y.pkl` and `exp_sigma_z.pkl`, which have
the expectation values of the respective Pauli operators as functions
of time.

We usually want to look at things visually, preferring graphics over 
arrays of numbers. To that end we make some graphics to show the 
evolution of the expectation values of Pauli operators and the Bloch 
vector. This is done in the program `graphics.py`. `graphics.py` reads 
the state as function of time from `psi_t.pkl` and the expectation 
values from `exp_sigma_x.pkl`, `exp_sigma_y.pkl` and `exp_sigma_z.pkl`.
The graphics are produced in `pdf` format in `bloch.pdf` and
`exp_sigma.pdf`

Go through `exp_sigma.pdf` and explore the plotting of the expectation 
values and the Bloch vector. The former done use `matplotlib` and the 
latter is done using the `qutip` library.

Now run `graphics.py` using the following command
```
python3 graphics.py
```

A directory called `graphics` is created inside `output` which has 
`bloch.pdf` and `exp_sigma.pdf`.

As an exercise, change the Hamiltonian to something else. Thereafter run 
all the programs in the appropriate order. You will get plots 
corresponding to a different time evolution.

Part 1: Introduction to make
============================

If running the programs in the appropriate order every time you change 
something seems too tedious, then you are at the right place.  Here we 
will automate the process of manually running each program using a 
program called `make`. To use `make` we specify dependencies in a file 
which is typically called `Makefile`. To orchestrate running all the 
programs in the appropriate order we invoke the program `make` in the 
directory containing the `Makefile`. All the book keeping of 
dependencies and doing things in the correct order is done by `make` 
and we do not have to manually run each program in the correct order
ourselves.

Before we starting writing the `Makefile`, we should understand the 
dependencies in our computation. Each step of the computation depends 
one or more other steps. Let us try to understand the dependencies of 
each step of computation on others.

We need to run the simulation, before we perform the statistics. We 
need to perform statistics, before we can prepare graphics. Before 
writing the Makefile, let us draw a dependency flow chart showing the 
different steps in the computation and their dependencies.

Each step is called a "target", and everything it depends on it called 
a "dependency". Note that for most of our targets, there is 
dependencies include a program (the program to be run) and some data 
which a previous program would have generated. The steps to produce a 
target using dependencies are called "rules".

Here for simplicity, we do not create directories for the output of 
each program.

To know the syntax, we consider an example. The target `exp_sigma.pkl` 
is produced by the program `statistics.py`. Therefore `statistics.py` 
is a dependency of `exp_sigma.pkl`. Moreover, the program 
`statistics.py` needs the data file `psi_t.pkl`. Therefore the target 
`exp_sigma.pkl` has two dependencies `statistics.py` and 
`exp_sigma.pkl`.

To produce `exp_sigma.pkl`, we use the `python3` interpreter as 
earlier. This is the "rule" to produce `psi_t.pkl`. This is written as 
follows. Note that each line in the 'rule' starts with a `Tab`
```
exp_sigma.pkl: statistics.py psi_t.pkl
    python3 statistics.py
```

If there is more than one dependency, we list them after the colon, 
separated by spaces. 

Now complete `Makefile` using the dependency flow chart you created 
earlier. You can list the targets along with their respective 
dependencies and rules in any order. However the target listed first is 
the default target, which is "made" if `make` is run without a 
specification of a target.

Run `make` with the target corresponding to preparing the plots. For 
example that target is called `graphics`, run the following command.
```
make graphics
```

If you want this to be your default target, that is the target which is 
made if simply `make` is run without a name of a target, list this
target along with its dependencies and rules at the beginning of your 
`Makefile`.

If your `Makefile` is correct, everything that you did in part 0 would 
be done automatically with a single command. Is that not wonderful?

Finally, there is one target that cleans up everything. It is called 
`clean`. For the `clean` target in the rule we just delete all the 
outputs of all programs. This is already done. Note that `clean` has no 
dependency.

Run `make clean` and see how the output of all programs is cleaned up.

Now run `make` to run all the programs again. Then go and experiment 
with the python programs. For example change the Hamiltonian. Then run 
`make` and see everything done automatically. Tweak around with the 
simulation parameters and run `make` as many times as you like.

Part 2: Recursive make
======================

Finally, we want to write an article with the graphics we have produced 
earlier. We write an article in LaTeX describing our simulation, which 
will include figures we produce using our programs. We will do this 
using a `Makefile` to prepare the article by invoking the program 
`pdflatex`. This `Makefile` will also recursively invoke `make` using 
the `Makefile` we wrote for our programs in part 1.

To prepare a `pdf` from a `tex` file, we use `pdflatex`. We run 
`pdflatex` twice ensure all references and citations are handled. For 
this we have a `Makefile` target in `TeX/Makefile` called 
`spinprecession.pdf`, which has the following rules.

```
spinprecession.pdf: spinprecession.tex bloch.pdf exp_sigma.pdf
	pdflatex spinprecession.tex
	pdflatex spinprecession.tex
```

Now the article uses figures which the programs produce. We want 
everything to be automated with minimum manual intervention. Therefore 
we will use the `Makefile` from part 1 to run the programs which 
produce the figures. Before starting, do not forget to copy your 
solution for part 1 to the `Python` directory.

```
cp part1_make_intro/Makefile part2_make_recursive/Python/
```

In the `Makefile` inside the `TeX` directory, we have a target 
`bloch.pdf` which depends on `../Python/bloch.pdf`. The rule simply 
copies the file from the `Python` directory to the `TeX` directory. 
Similarly, we have a target `exp_sigma.pdf` which depends on 
`../Python/exp_sigma.pdf`. Again, the rule simply copies the file from 
the `Python` directory to the `TeX` directory.

In order to create `../Python/bloch.pdf` and `../Python/exp_sigma.pdf`, 
we need to run the programs. For this we have already written a 
`Makefile` in part 1. All we have to do it use it. In the rules for 
`../Python/bloch.pdf` and `../Python/exp_sigma.pdf`, invoke `make` 
using the `Makefile` in the `Python` directory. This is the `Makefile`
you copied earlier from your solution to part 1.

If we run `make` inside the `TeX` directory it uses the `Makefile` in 
the `TeX` directory. In order to run the `Makefile` in the `Python` 
directory we need to ask make to change directory. This done with the 
command line argument `-C ../Python` while invoking `make`. This is 
done using the following command.

```
make -C ../Python
```

This will run `make` using the `Makefile` in the `Python` directory and 
produce the figures. By doing this inside our `Makefile` in the `TeX` 
directory, we are recursively using `make`.

By recursively invoking `make`, in the `Makefile` in the `TeX` 
directory, complete the rules for the targets `../Python/bloch.pdf` and 
`../Python/exp_sigma.pdf`.

Finally we have the `clean` target. Note that we have to recursively 
clean. Therefore, we need to invoke the other `Makefile` here. Note 
that the target for the recursively invoked `make` is not the default 
target but the `clean` target of the other `Makefile`. Complete the 
`clean` target by invoking `make clean` for the other `Makefile` using 
the change directory command line argument for `make` as we did 
earlier.

For simplicity, we have defined a target `cleanlatex`, which removes 
all files created by the LaTeX program. We could have put all these 
commands under the target `clean`. Of course `cleanlatex` is a 
dependency of the target `clean`.

Before running `make`, edit `TeX/spinprecession.tex`, adding your name 
and the date. Now run `make` in the `TeX` directory. If you `Makefile`s 
are correct, then you will have a `pdf` containing your article with 
the figures.

Run `make clean` and see how the outputs of both the python programs 
and LaTeX are cleaned up.

Now run `make` to run all the programs again. Then go and experiment 
with the python programs. For example change the Hamiltonian. Do not 
forget to update `TeX/spinprecession.tex` with the new Hamiltonian that 
you chose. Then run `make` and see everything done automatically. 
Tweak around with the simulation parameters and run `make` as many 
times as you like.

Where to go from here?
======================

`make` is a very powerful tool, which can be used for many purposes. We 
have covered only the basics of writing `Makefile`s. There are many 
more features provided by `make` like defining and using variables, 
functions, pattern matching, which we did not cover in this lesson.

Hopefully, after this lesson, we are motivated enough to use `make` or 
a similar to automate our computational work and learn more about the 
appropriate tool as we do so. Most of these tools have extensive 
documentation on their respective websites and we will be able to
follow them.
