# Makefile to compile Darts serial C code
CC?=mpicc
# Optimisation level set to -O2
# Debugging enabled if using -g
CFLAGS = -O2 -g

# Default target  
all: darts

darts: darts.o 
	${CC} ${CFLAGS} -o darts darts.o

%.o: %.c lcgenerator.h
	${CC} ${CFLAGS} -c $< -o $@

clean:
	rm -rf *.o darts
