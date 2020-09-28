## INSTALL

* Install Visual Studio Build Tools
* Install Python 64 bits
* Set environment var: VCTargetsPath=C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\MSBuild\Microsoft\VC\v160\
* Create C:\Users\Tiago Silva\AppData\Local\Programs\Python\Python38\Lib\distutils\distutils.cfg with following contents:

[build]
compiler=msvc

[build_ext]
compiler=msvc

* Install nvidia cuda 10.1
* pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
* pip install tensorflow-gpu nes_py gym_super_mario_bros
* pip install gym-retro 
* python -m retro.examples.ppo --game Airstriker-Genesis
* Go to roms location and run: python -m retro.import .
* Install ffpmeg and add to windows path
* python -m retro.examples.brute --game Airstriker-Genesis
* Playback movie: python -m retro.scripts.playback_movie "C:\best.bk2"

## TODO 

* Convert to use gym-retro instead of nes_py