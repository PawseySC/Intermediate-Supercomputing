# Makefile to compile Darts C OpenMP code

# Compiler definition
# If running on Cray use compiler wrapper cc instead of directly using Intel/GNU/PGI compiler. Consider swapping to an appropriate PrgEnv- module.
# On other systems use: gcc (for GNU), icc (for Intel), pgcc (PGI)

# Optimisation level set to -O2
# Debugging enabled if using -g
# Notice that OpenMP flag differs for different compiler families
# Use: -fopenmp (for GNU), -qopenmp (for Intel), -mp (for PGI)
# OpenMP is enabled by default for Cray compiler.
CFLAGS = -O2 -g
CC_NAME=$(shell $(CC) 2>&1 | head -n 1 | grep -m 1 -oE "(gcc|g++|icc|icpc|pgi)" | head -n 1)

ifeq ($(CC_NAME), icc)
CFLAGS += -qopenmp
endif

ifeq ($(CC_NAME), icpc)
CFLAGS += -qopenmp
endif

ifeq ($(CC_NAME), pgi)   
CFLAGS += -mp
endif 

ifeq ($(CC_NAME), gcc)   
CFLAGS += -fopenmp
endif 

ifeq ($(CC_NAME), g++)   
CFLAGS += -fopenmp
endif 
#
# Default target  

all: darts-omp

darts-omp: darts-omp.o 
	${CC} ${CFLAGS} -o darts-omp darts-omp.o

%.o: %.c lcgenerator.h
	${CC} ${CFLAGS} -c $< -o $@

clean:
	rm -rf *.o darts-omp
