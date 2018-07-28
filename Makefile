export PYROP:="$(CURDIR)/pyrop"

all: otherapp.bin ropdb/DB.py code/build game/build

otherapp.bin:
	@cp $(OTHERAPP) otherapp.bin

ropdb/DB.py:
	@cp ropdb/$(REGION).py ropdb/DB.py

code/build:
	@cd code && make

game/build: rop/build
	@cd game && make

rop/build:
	@cd rop && make

clean:
	@cd game && make clean
	@cd rop && make clean
	@cd code && make clean
	@rm ropdb/DB.py
	@rm otherapp.bin
