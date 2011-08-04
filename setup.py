from distutils.core import setup
from distutils.extension import Extension
import numpy as np
import os

#gsl_include = os.popen('gsl-config --cflags').read()[2:-1]

#if gsl_include == '':
#    print "Couldn't find gsl-config. Make sure it's installed and in the path."
#    sys.exit(-1)

setup(
    name="HDDM",
    version="0.1.1",
    author="Thomas V. Wiecki, Imri Sofer, Michael J. Frank",
    author_email="thomas_wiecki@brown.edu",
    url="http://github.com/hddm-devs/hddm",
    packages=["hddm", "hddm.tests"],
    package_data={"hddm":["examples/*.csv", "examples/*.conf", "examples/plots/*.png"]},
    #package_dir={"hddm":"hddm/examples"},
    scripts=["scripts/hddm_fit.py", "scripts/hddm_demo.py"],
    description="HDDM is a python module that implements Hierarchical Bayesian estimation of Drift Diffusion Models.",
    install_requires=['NumPy >=1.3.0', 'kabuki', 'pymc'],
    setup_requires=['NumPy >=1.3.0', 'kabuki', 'pymc'],
    include_dirs = [np.get_include()],
    classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Environment :: Console',
                'Operating System :: OS Independent',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering',
                 ],
    ext_modules = [Extension("wfpt", ["src/wfpt.c"]),
                   Extension("wfpt_full", ["src/wfpt_full.c"])]
)

