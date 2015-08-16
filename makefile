# Makefile for Foreign Function Interfaces for Web Developers
# Make manual: http://www.gnu.org/software/make/manual/make.html

# Make sure to use <tab> instead of space.
PYTHON ?= python

# n.b. this makefile is for OS X.
# for linux:
#   CPP may need to get set to something else
#   objdump needs to replace otool usage
#   be wary of the switches sent to commands

# this is great for getting includes and library locations
PYTHON_INCLUDES ?= `python3.4-config --includes`
#BOOST_LIBS ?= 'boost_python-mt'
BOOST_LIBS ?= '/usr/local/lib/libboost_python-mt.dylib'
CC = gcc
CPP = g++

# -g debugging info; -Wall turns on most compiler warnings
CFLAGS = -g -Wall

MODULE_DIR=jumper/blueprints/backends/modules/

SRC_DIR = src/
SRC_CYTHON = $(SRC_DIR)cython/
SRC_CTYPES = $(SRC_DIR)ctypes/
SRC_CPP = $(SRC_DIR)cpp/

DST_CYTHON=$(MODULE_DIR)cython/
DST_CTYPES=$(MODULE_DIR)ctypes/
DST_FFI = $(MODULE_DIR)ffi/
DST_BOOST = $(MODULE_DIR)ffi_boost/

# 'all' as the default by putting it first
all: python cython ctypes cpp
	@echo "You should be able to start the server now (probably ./manage.py runserver)..."

install: all
	@echo "Installing..."

python:
	@echo "Installing Python requirements..."
	pip install -r requirements.txt

cython:
	@echo "Making Cython required files..."
	cd $(SRC_CYTHON); OPT="-O3 -ffast-math" $(PYTHON) setup.py build_ext --inplace;
	cp $(SRC_CYTHON)*.so $(DST_CYTHON).

ctypes:
	@echo "Making CTypes required files..."
	clang -shared -undefined dynamic_lookup -o $(DST_CTYPES)libffi_ctypes.so $(SRC_CTYPES)ffi_ctypes.cpp

cpp:
	@echo "Making C++ FFI required files..."
	#clang++ $(PYTHON_INCLUDES) -shared -undefined dynamic_lookup -o $(SRC_CPP)fficpp.so $(SRC_CPP)fficpp.cpp -framework Python
	cd $(SRC_CPP); $(PYTHON) setup.py build_ext --inplace;
	cp $(SRC_CPP)*.so $(DST_FFI)

clean:
	@echo "Cleaning..."
	@#clean up other files generated. start over from scratch
	find ./jumper -name \*.pyc | xargs $(RM)
	find ./jumper -type d -name __pycache__ | xargs $(RM) -rf
	-rm $(SRC_CYTHON)*.c
	-rm -rf $(SRC_CYTHON)build
	-rm $(SRC_CYTHON)*.html
	-rm $(SRC_CYTHON)*.so
	-rm -rf $(SRC_CPP)build/
