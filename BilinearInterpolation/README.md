Bilinear Interpolation
======================

This is a proof-of-concept implementation of bilinear interpolation and should 
time various implementation in Cython (both native and wrapping external C 
code).


* Installation: python setup.py build_ext
* Run comparison (boxplots and timing): python tests/generate_test_data.py
* Explore timing for vectorized function: python tests/generate_test_data_2.py
