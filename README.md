# Fortran code package for CRTM and WRF
This is a code package to calculate simulated radiances of the Advanced Weather Research and Forecasting model (WRF-ARW) output by the Community Radiative Transfer Model (CRTM).

### How to use
0. Download and install the released CRTM.
1. Copy this ("crtm_wrf") directory in your CRTM directory.
2. Set CRTM_DIR to your CRTM directory such as typing "export CRTM_DIR=/your_path_to_CRTM"
3. Modify main_crtm.f90 code. 
   Most parameters can be set in the top of main_crtm.f90 such as grid size, input files and simulation time.
4. In $CRTM_DIR/crtm_wrf directory, type "./compile". It compiles the fortran codes and makes crtm.exe.
5. Link coefficient files from $CRTM_DIR/fix/SpcCoeff/Big_Endian and $CRTM_DIR/fix/TauCoeff/Big_Endian to $CRTM_DIR/crtm_wrf/coefficients directory.
6. Run crtm.exe

### tips
- Use Convert_wrf_crtm_nocloud.inc instead of Convert_wrf_crtm.inc if you want to exclude cloud-emission and cloud-scatterting calculation. 
