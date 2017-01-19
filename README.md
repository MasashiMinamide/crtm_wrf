This is the set of codes to run CRTM for WRF output.
   written by Masashi Minamide, based on the sample test codes of released CRTM.

### How to use ###
0. download and install the released CRTM.
1. copy this ("crtm_wrf") directory in your CRTM directory.
2. set CRTM_DIR to your CRTM directory such as typing "export CRTM_DIR=/your_path_to_CRTM"
3. modify main_crtm.f90 code. 
   Most parameters can be set in the top of main_crtm.f90 such as grid size, input files and simulation time.
4. In $CRTM_DIR/crtm_wrf directory, type "./compile". It compiles the fortran codes and makes crtm.exe.
5. link coefficient files from $CRTM_DIR/fix/SpcCoeff/Big_Endian and $CRTM_DIR/fix/TauCoeff/Big_Endian to $CRTM_DIR/crtm_wrf/coefficients directory.
6. run crtm.exe

tips
- use Convert_wrf_crtm_nocloud.inc instead of Convert_wrf_crtm.inc if you want to exclude cloud-emission and cloud-scatterting calculation. 
