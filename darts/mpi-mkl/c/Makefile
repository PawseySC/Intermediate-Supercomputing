# Makefile to compile Darts serial C code using the MKL library

# Compiler definition
# If running on Cray use compiler wrapper cc instead of directly using Intel/GNU/PGI compiler. Consider swapping to an appropriate PrgEnv- module.
# On other systems load appropriate MPI module and use: mpicc
MPICC = ${CC}

# Optimisation level set to -O2
# Debugging enabled if using -g
CFLAGS = -O2 -g

# Setup include directory and libraries for MKL. Use the Intel MKL Link Line Advisor
MKL_LIBS=-Wl,--start-group -L${MKLROOT}/lib/intel64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core  -Wl,--end-group -lpthread -lm
MKL_INCL=-DMKL_ILP64 -I$(MKLROOT)/include

# Default target  
all: darts-mpi-mkl

darts-mpi-mkl: darts-mpi-mkl.o 
	${MPICC} ${CFLAGS} ${MKL_LIBS} -o darts-mpi-mkl darts-mpi-mkl.o

%.o: %.c 
	${MPICC} ${CFLAGS} ${MKL_INCL} -c $< -o $@

clean:
	rm -rf *.o darts-mpi-mkl
