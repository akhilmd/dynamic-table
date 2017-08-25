SWIG = ./swig
GEN = ./gen
SRC = ./src
TESTS = ./tests
INCLUDE = ./include

MODULE = dynamic_table

CC = gcc
MK = @mkdir -p $(@D)
CFLAGS = -g -fpic -I/usr/include/python3.5m/

all:	$(GEN)/$(MODULE).py $(GEN)/_$(MODULE).so

tests:	$(TESTS)/$(MODULE).py $(TESTS)/_$(MODULE).so

$(TESTS)/$(MODULE).py:	$(GEN)/$(MODULE).py
	$(MK)
	cp $< $@

$(TESTS)/_$(MODULE).so:  $(GEN)/_$(MODULE).so
	$(MK)
	cp $< $@

$(GEN)/_$(MODULE).so:	$(GEN)/$(MODULE).o $(GEN)/$(MODULE)_wrap.o $(GEN)/timer.o
	$(MK)
	ld -shared $^ -o $@

$(GEN)/$(MODULE).o:	$(SRC)/$(MODULE).c $(INCLUDE)/$(MODULE).h
	$(MK)
	$(CC) $(CFLAGS) -c $< -o $@

$(GEN)/$(MODULE)_wrap.o:	$(GEN)/$(MODULE)_wrap.c $(GEN)/$(MODULE).py
	$(MK)
	$(CC) $(CFLAGS) -c $< -o $@

$(GEN)/%.py $(GEN)/%_wrap.c:	$(SWIG)/%.i $(INCLUDE)/%.h
	$(MK)
	swig -outdir $(GEN)/ -python $<
	mv $(SWIG)/$(MODULE)_wrap.c $(GEN)/$(MODULE)_wrap.c

$(GEN)/timer.o:	$(SRC)/timer.c $(INCLUDE)/timer.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(GEN)/
	rm -f $(TESTS)/$(MODULE).py
	rm -rf $(TESTS)/_*

