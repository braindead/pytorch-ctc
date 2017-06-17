#!/usr/bin/env python

import os
import sys

from distutils.core import setup
from torch.utils.ffi import create_extension

sources = ['src/cpu_binding.cpp', 'src/util/status.cpp']
headers = ['src/cpu_binding.h']

ffi = create_extension(
    name='ctc_decode',
    language='c++',
    headers=headers,
    sources=sources,
    with_cuda=False,
    extra_compile_args=['-std=c++11', '-fPIC', '-w']
)
ffi = ffi.distutils_extension()
ffi.name = 'pytorch_ctc._ctc_decode'

setup(
    name="pytorch_ctc",
    version="0.1",
    description="CTC Decoder for PyTorch based on TensorFlow's implementation",
    url="https://github.com/ryanleary/pytorch-ctc-decode",
    author="Ryan Leary",
    author_email="ryanleary@gmail.com",
    # Require cffi.
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    # Exclude the build files.
    packages=["pytorch_ctc"],
    # Extensions to compile.
    ext_modules=[ffi]
)