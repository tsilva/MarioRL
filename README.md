## INSTALL

* Install Visual Studio Build Tools
* Install Python 64 bits
* Set environment var: VCTargetsPath  = C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\MSBuild\Microsoft\VC\v160\
* Install MinGW
* [Optional?] - Create C:\Users\Tiago Silva\AppData\Local\Programs\Python\Python38\Lib\distutils\distutils.cfg with following contents:

[build]
compiler = mingw32

[build_ext]
compiler = mingw32

* [Optional?] - pip install cmake
* [Optional?] - pip install dlib
* Install nvidia cuda 10.1
* pip install gym-retro
* pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
* python -m retro.examples.brute --game Airstriker-Genesis
* pip install tensorflow-gpu (remove distutils.cfg to do this??)
* git clone https://github.com/openai/baselines.git
* python setup.py install
* python -m retro.examples.ppo --game Airstriker-Genesis
* Go to roms location and run: python -m retro.import .
* Install ffpmeg and add to windows path
* Playback movie: python -m retro.scripts.playback_movie "C:\best.bk2"