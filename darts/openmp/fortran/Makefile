# Makefile to compile Darts Fortran OpenMP code

# Compiler definition
# If running on Cray use compiler wrapper ftn instead of directly using Intel/GNU/PGI compiler. Consider swapping to an appropriate PrgEnv- module.
# On other systems use: gfortran (for GNU), ifort (for Intel), pgf90 (PGI)
F90?=${FC}

# Optimisation level set to -O2
# Debugging enabled if using -g
# Notice that OpenMP flag differs for different compiler families
# Use: -fopenmp (for GNU), -qopenmp (for Intel), -mp (for PGI)
# OpenMP is enabled by default for Cray compiler.

FFLAGS = -O2 -g
F90_NAME=$(shell $(F90) 2>&1 | head -n 1 | grep -m 1 -oE "(gfortran|ifort|pgf)" | head -n 1)

ifeq ($(F90_NAME), ifort)
FFLAGS += -qopenmp
endif

ifeq ($(F90_NAME), pgf)   
FFLAGS += -mp
endif 

ifeq ($(F90_NAME), gfortran)   
FFLAGS += -fopenmp
endif 


darts-omp: darts-omp.o
	${F90} ${FFLAGS} -o darts-omp darts-omp.o

%.o: %.f
	${F90} ${FFLAGS} -c $< -o $@

clean:
	rm -rf *.o *.mod darts-omp
