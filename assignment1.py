Last login: Sun Jan 18 17:38:31 on ttys000
kojofrimpong@Kojo--MacBook-Pro ~ % python3 --version
Python 3.14.2
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip --version
pip 25.3 from /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/pip (python 3.14)
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install --upgrade pip
Requirement already satisfied: pip in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (25.3)
kojofrimpong@Kojo--MacBook-Pro ~ % 
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install pandas
Collecting pandas
  Downloading pandas-2.3.3-cp314-cp314-macosx_11_0_arm64.whl.metadata (91 kB)
Collecting numpy>=1.26.0 (from pandas)
  Downloading numpy-2.4.1-cp314-cp314-macosx_14_0_arm64.whl.metadata (6.6 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
  Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading pandas-2.3.3-cp314-cp314-macosx_11_0_arm64.whl (10.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.8/10.8 MB 57.1 MB/s  0:00:00
Downloading numpy-2.4.1-cp314-cp314-macosx_14_0_arm64.whl (5.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 53.2 MB/s  0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
Successfully installed numpy-2.4.1 pandas-2.3.3 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.3
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
>>> exit()
kojofrimpong@Kojo--MacBook-Pro ~ % pip install polars
zsh: command not found: pip
kojofrimpong@Kojo--MacBook-Pro ~ % python -m install polars
zsh: command not found: python
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m install polars
/Library/Frameworks/Python.framework/Versions/3.14/bin/python3: No module named install
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m ensurepip --upgrade
Looking in links: /var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/tmpu0aab0w9
Requirement already satisfied: pip in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (25.3)
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install polars
Collecting polars
  Downloading polars-1.37.1-py3-none-any.whl.metadata (10 kB)
Collecting polars-runtime-32==1.37.1 (from polars)
  Downloading polars_runtime_32-1.37.1-cp310-abi3-macosx_11_0_arm64.whl.metadata (1.5 kB)
Downloading polars-1.37.1-py3-none-any.whl (805 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 805.7/805.7 kB 9.4 MB/s  0:00:00
Downloading polars_runtime_32-1.37.1-cp310-abi3-macosx_11_0_arm64.whl (39.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.7/39.7 MB 81.6 MB/s  0:00:00
Installing collected packages: polars-runtime-32, polars
Successfully installed polars-1.37.1 polars-runtime-32-1.37.1
kojofrimpong@Kojo--MacBook-Pro ~ % -m pip install modin [all]
zsh: no matches found: [all]
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install modin[all]
zsh: no matches found: modin[all]
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install "modin[all]" 
Collecting modin[all]
  Downloading modin-0.37.1-py3-none-any.whl.metadata (17 kB)
Requirement already satisfied: pandas<2.4,>=2.2 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (2.3.3)
Collecting packaging>=21.0 (from modin[all])
  Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: numpy>=1.22.4 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (2.4.1)
Collecting fsspec>=2022.11.0 (from modin[all])
  Downloading fsspec-2026.1.0-py3-none-any.whl.metadata (10 kB)
Collecting psutil>=5.8.0 (from modin[all])
  Downloading psutil-7.2.1-cp36-abi3-macosx_11_0_arm64.whl.metadata (22 kB)
Collecting typing-extensions (from modin[all])
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting dask>=2.22.0 (from modin[all])
  Downloading dask-2026.1.1-py3-none-any.whl.metadata (3.8 kB)
Collecting distributed>=2.22.0 (from modin[all])
  Downloading distributed-2026.1.1-py3-none-any.whl.metadata (3.4 kB)
INFO: pip is looking at multiple versions of modin[all] to determine which version is compatible with other requirements. This could take a while.
Collecting modin[all]
  Downloading modin-0.37.0-py3-none-any.whl.metadata (17 kB)
  Downloading modin-0.36.0-py3-none-any.whl.metadata (17 kB)
  Downloading modin-0.35.0-py3-none-any.whl.metadata (17 kB)
  Downloading modin-0.34.1-py3-none-any.whl.metadata (17 kB)
Collecting pandas<2.3,>=2.2 (from modin[all])
  Downloading pandas-2.2.3.tar.gz (4.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 34.3 MB/s  0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [17 lines of output]
      + meson setup /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-xfk14de2/pandas_7284bb683b6e4329a8cabd90f0233e03 /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-xfk14de2/pandas_7284bb683b6e4329a8cabd90f0233e03/.mesonpy-0hfm8zkj/build -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md --vsenv --native-file=/private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-xfk14de2/pandas_7284bb683b6e4329a8cabd90f0233e03/.mesonpy-0hfm8zkj/build/meson-python-native-file.ini
      The Meson build system
      Version: 1.2.1
      Source dir: /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-xfk14de2/pandas_7284bb683b6e4329a8cabd90f0233e03
      Build dir: /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-xfk14de2/pandas_7284bb683b6e4329a8cabd90f0233e03/.mesonpy-0hfm8zkj/build
      Build type: native build
      Project name: pandas
      Project version: 2.2.3
      
      ../../meson.build:2:0: ERROR: Unknown compiler(s): [['cc'], ['gcc'], ['clang'], ['nvc'], ['pgcc'], ['icc'], ['icx']]
      The following exception(s) were encountered:
      Running `nvc --version` gave "[Errno 2] No such file or directory: 'nvc'"
      Running `pgcc --version` gave "[Errno 2] No such file or directory: 'pgcc'"
      Running `icc --version` gave "[Errno 2] No such file or directory: 'icc'"
      Running `icx --version` gave "[Errno 2] No such file or directory: 'icx'"
      
      A full log can be found at /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-xfk14de2/pandas_7284bb683b6e4329a8cabd90f0233e03/.mesonpy-0hfm8zkj/build/meson-logs/meson-log.txt
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> pandas

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install "dask[complete]" 
Collecting dask[complete]
  Using cached dask-2026.1.1-py3-none-any.whl.metadata (3.8 kB)
Collecting click>=8.1 (from dask[complete])
  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting cloudpickle>=3.0.0 (from dask[complete])
  Downloading cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)
Collecting fsspec>=2021.09.0 (from dask[complete])
  Using cached fsspec-2026.1.0-py3-none-any.whl.metadata (10 kB)
Collecting packaging>=20.0 (from dask[complete])
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting partd>=1.4.0 (from dask[complete])
  Downloading partd-1.4.2-py3-none-any.whl.metadata (4.6 kB)
Collecting pyyaml>=5.3.1 (from dask[complete])
  Downloading pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.4 kB)
Collecting toolz>=0.12.0 (from dask[complete])
  Downloading toolz-1.1.0-py3-none-any.whl.metadata (5.1 kB)
Collecting pyarrow>=14.0.1 (from dask[complete])
  Downloading pyarrow-23.0.0-cp314-cp314-macosx_12_0_arm64.whl.metadata (3.0 kB)
Collecting lz4>=4.3.2 (from dask[complete])
  Downloading lz4-4.4.5-cp314-cp314-macosx_11_0_arm64.whl.metadata (3.8 kB)
Collecting locket (from partd>=1.4.0->dask[complete])
  Downloading locket-1.0.0-py2.py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: numpy>=1.24 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask[complete]) (2.4.1)
Requirement already satisfied: pandas>=2.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask[complete]) (2.3.3)
Collecting distributed<2026.1.2,>=2026.1.1 (from dask[complete])
  Using cached distributed-2026.1.1-py3-none-any.whl.metadata (3.4 kB)
Collecting bokeh>=3.1.0 (from dask[complete])
  Downloading bokeh-3.8.2-py3-none-any.whl.metadata (10 kB)
Collecting jinja2>=2.10.3 (from dask[complete])
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting msgpack>=1.0.2 (from distributed<2026.1.2,>=2026.1.1->dask[complete])
  Downloading msgpack-1.1.2-cp314-cp314-macosx_11_0_arm64.whl.metadata (8.1 kB)
Collecting psutil>=5.8.0 (from distributed<2026.1.2,>=2026.1.1->dask[complete])
  Using cached psutil-7.2.1-cp36-abi3-macosx_11_0_arm64.whl.metadata (22 kB)
Collecting sortedcontainers>=2.0.5 (from distributed<2026.1.2,>=2026.1.1->dask[complete])
  Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl.metadata (10 kB)
Collecting tblib!=3.2.0,!=3.2.1,>=1.6.0 (from distributed<2026.1.2,>=2026.1.1->dask[complete])
  Downloading tblib-3.2.2-py3-none-any.whl.metadata (27 kB)
Collecting tornado>=6.2.0 (from distributed<2026.1.2,>=2026.1.1->dask[complete])
  Downloading tornado-6.5.4-cp39-abi3-macosx_10_9_universal2.whl.metadata (2.8 kB)
Collecting urllib3>=1.26.5 (from distributed<2026.1.2,>=2026.1.1->dask[complete])
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting zict>=3.0.0 (from distributed<2026.1.2,>=2026.1.1->dask[complete])
  Downloading zict-3.0.0-py2.py3-none-any.whl.metadata (899 bytes)
Collecting contourpy>=1.2 (from bokeh>=3.1.0->dask[complete])
  Downloading contourpy-1.3.3-cp314-cp314-macosx_11_0_arm64.whl.metadata (5.5 kB)
Collecting narwhals>=1.13 (from bokeh>=3.1.0->dask[complete])
  Downloading narwhals-2.15.0-py3-none-any.whl.metadata (13 kB)
Collecting pillow>=7.1.0 (from bokeh>=3.1.0->dask[complete])
  Downloading pillow-12.1.0-cp314-cp314-macosx_11_0_arm64.whl.metadata (8.8 kB)
Collecting xyzservices>=2021.09.1 (from bokeh>=3.1.0->dask[complete])
  Downloading xyzservices-2025.11.0-py3-none-any.whl.metadata (4.3 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=2.10.3->dask[complete])
  Downloading markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl.metadata (2.7 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from pandas>=2.0->dask[complete]) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from pandas>=2.0->dask[complete]) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from pandas>=2.0->dask[complete]) (2025.3)
Requirement already satisfied: six>=1.5 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from python-dateutil>=2.8.2->pandas>=2.0->dask[complete]) (1.17.0)
Downloading dask-2026.1.1-py3-none-any.whl (1.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 14.7 MB/s  0:00:00
Downloading click-8.3.1-py3-none-any.whl (108 kB)
Downloading cloudpickle-3.1.2-py3-none-any.whl (22 kB)
Downloading fsspec-2026.1.0-py3-none-any.whl (201 kB)
Downloading lz4-4.4.5-cp314-cp314-macosx_11_0_arm64.whl (207 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Downloading partd-1.4.2-py3-none-any.whl (18 kB)
Downloading pyarrow-23.0.0-cp314-cp314-macosx_12_0_arm64.whl (34.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 34.2/34.2 MB 90.0 MB/s  0:00:00
Downloading pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl (173 kB)
Downloading toolz-1.1.0-py3-none-any.whl (58 kB)
Downloading distributed-2026.1.1-py3-none-any.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 56.4 MB/s  0:00:00
Downloading bokeh-3.8.2-py3-none-any.whl (7.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 82.6 MB/s  0:00:00
Downloading contourpy-1.3.3-cp314-cp314-macosx_11_0_arm64.whl (273 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading locket-1.0.0-py2.py3-none-any.whl (4.4 kB)
Downloading markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl (12 kB)
Downloading msgpack-1.1.2-cp314-cp314-macosx_11_0_arm64.whl (84 kB)
Downloading narwhals-2.15.0-py3-none-any.whl (432 kB)
Downloading pillow-12.1.0-cp314-cp314-macosx_11_0_arm64.whl (4.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 67.4 MB/s  0:00:00
Downloading psutil-7.2.1-cp36-abi3-macosx_11_0_arm64.whl (128 kB)
Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Downloading tblib-3.2.2-py3-none-any.whl (12 kB)
Downloading tornado-6.5.4-cp39-abi3-macosx_10_9_universal2.whl (443 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading xyzservices-2025.11.0-py3-none-any.whl (93 kB)
Downloading zict-3.0.0-py2.py3-none-any.whl (43 kB)
Installing collected packages: sortedcontainers, zict, xyzservices, urllib3, tornado, toolz, tblib, pyyaml, pyarrow, psutil, pillow, packaging, narwhals, msgpack, MarkupSafe, lz4, locket, fsspec, contourpy, cloudpickle, click, partd, jinja2, dask, bokeh, distributed
Successfully installed MarkupSafe-3.0.3 bokeh-3.8.2 click-8.3.1 cloudpickle-3.1.2 contourpy-1.3.3 dask-2026.1.1 distributed-2026.1.1 fsspec-2026.1.0 jinja2-3.1.6 locket-1.0.0 lz4-4.4.5 msgpack-1.1.2 narwhals-2.15.0 packaging-25.0 partd-1.4.2 pillow-12.1.0 psutil-7.2.1 pyarrow-23.0.0 pyyaml-6.0.3 sortedcontainers-2.4.0 tblib-3.2.2 toolz-1.1.0 tornado-6.5.4 urllib3-2.6.3 xyzservices-2025.11.0 zict-3.0.0
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install vaex
Collecting vaex
  Downloading vaex-4.17.0-py3-none-any.whl.metadata (6.0 kB)
Collecting vaex-core~=4.17.1 (from vaex)
  Downloading vaex-core-4.17.1.tar.gz (2.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 20.6 MB/s  0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  error: subprocess-exited-with-error
  
  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [23 lines of output]
      Traceback (most recent call last):
        File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
          main()
          ~~~~^^
        File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
                                   ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 143, in get_requires_for_build_wheel
          return hook(config_settings)
        File "/private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-build-env-cb8fwbis/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 331, in get_requires_for_build_wheel
          return self._get_build_requires(config_settings, requirements=[])
                 ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-build-env-cb8fwbis/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 301, in _get_build_requires
          self.run_setup()
          ~~~~~~~~~~~~~~^^
        File "/private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-build-env-cb8fwbis/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 512, in run_setup
          super().run_setup(setup_script=setup_script)
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-build-env-cb8fwbis/overlay/lib/python3.14/site-packages/setuptools/build_meta.py", line 317, in run_setup
          exec(code, locals())
          ~~~~^^^^^^^^^^^^^^^^
        File "<string>", line 4, in <module>
      ModuleNotFoundError: No module named 'imp'
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
ERROR: Failed to build 'vaex-core' when getting requirements to build wheel
kojofrimpong@Kojo--MacBook-Pro ~ % brew install pyenv        # install pyenv if you don’t have it
pyenv install 3.11.8      # install Python 3.11
pyenv global 3.11.8       # make 3.11 default
python -m pip install vaex

zsh: command not found: brew
zsh: command not found: pyenv
zsh: command not found: pyenv
zsh: command not found: python
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install tensorflow
ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
ERROR: No matching distribution found for tensorflow
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install "tensorflow"
ERROR: Could not find a version that satisfies the requirement tensorflow (from versions: none)
ERROR: No matching distribution found for tensorflow
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install duckdb
Collecting duckdb
  Downloading duckdb-1.4.3-cp314-cp314-macosx_11_0_arm64.whl.metadata (4.3 kB)
Downloading duckdb-1.4.3-cp314-cp314-macosx_11_0_arm64.whl (13.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.7/13.7 MB 57.9 MB/s  0:00:00
Installing collected packages: duckdb
Successfully installed duckdb-1.4.3
kojofrimpong@Kojo--MacBook-Pro ~ % import pandas as pd
import polars as pl
import dask.dataframe as dd
import modin.pandas as mpd
import duckdb

zsh: command not found: import
zsh: command not found: import
zsh: command not found: import
zsh: command not found: import
zsh: command not found: import
kojofrimpong@Kojo--MacBook-Pro ~ % import pandas as pd
zsh: command not found: import
kojofrimpong@Kojo--MacBook-Pro ~ % important pandas as pd
zsh: command not found: important
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd 
>>> import polars as pl
>>> import dask.dataframe as dd
>>> import modin.pandas as mpd
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    import modin.pandas as mpd
ModuleNotFoundError: No module named 'modin'
>>> 
>>> import pandas as pd
>>> import polars as pl
>>> import modin.pandas as mpd
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    import modin.pandas as mpd
ModuleNotFoundError: No module named 'modin'
>>> import duckdb
>>> python3 -m pip install "modin[all]"
  File "<python-input-9>", line 1
    python3 -m pip install "modin[all]"
               ^^^
SyntaxError: invalid syntax
>>> exit()
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install "modin[all]"
Collecting modin[all]
  Using cached modin-0.37.1-py3-none-any.whl.metadata (17 kB)
Requirement already satisfied: pandas<2.4,>=2.2 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (2.3.3)
Requirement already satisfied: packaging>=21.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (25.0)
Requirement already satisfied: numpy>=1.22.4 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (2.4.1)
Requirement already satisfied: fsspec>=2022.11.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (2026.1.0)
Requirement already satisfied: psutil>=5.8.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (7.2.1)
Collecting typing-extensions (from modin[all])
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: dask>=2.22.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (2026.1.1)
Requirement already satisfied: distributed>=2.22.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin[all]) (2026.1.1)
INFO: pip is looking at multiple versions of modin[all] to determine which version is compatible with other requirements. This could take a while.
Collecting modin[all]
  Using cached modin-0.37.0-py3-none-any.whl.metadata (17 kB)
  Using cached modin-0.36.0-py3-none-any.whl.metadata (17 kB)
  Using cached modin-0.35.0-py3-none-any.whl.metadata (17 kB)
  Using cached modin-0.34.1-py3-none-any.whl.metadata (17 kB)
Collecting pandas<2.3,>=2.2 (from modin[all])
  Using cached pandas-2.2.3.tar.gz (4.4 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [17 lines of output]
      + meson setup /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-64_pqrdb/pandas_ad9c5f0132054736a450e846cbf30fa7 /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-64_pqrdb/pandas_ad9c5f0132054736a450e846cbf30fa7/.mesonpy-qsv78j1l/build -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md --vsenv --native-file=/private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-64_pqrdb/pandas_ad9c5f0132054736a450e846cbf30fa7/.mesonpy-qsv78j1l/build/meson-python-native-file.ini
      The Meson build system
      Version: 1.2.1
      Source dir: /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-64_pqrdb/pandas_ad9c5f0132054736a450e846cbf30fa7
      Build dir: /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-64_pqrdb/pandas_ad9c5f0132054736a450e846cbf30fa7/.mesonpy-qsv78j1l/build
      Build type: native build
      Project name: pandas
      Project version: 2.2.3
      
      ../../meson.build:2:0: ERROR: Unknown compiler(s): [['cc'], ['gcc'], ['clang'], ['nvc'], ['pgcc'], ['icc'], ['icx']]
      The following exception(s) were encountered:
      Running `nvc --version` gave "[Errno 2] No such file or directory: 'nvc'"
      Running `pgcc --version` gave "[Errno 2] No such file or directory: 'pgcc'"
      Running `icc --version` gave "[Errno 2] No such file or directory: 'icc'"
      Running `icx --version` gave "[Errno 2] No such file or directory: 'icx'"
      
      A full log can be found at /private/var/folders/vf/qy2kp8457z31j2q7t74cddvc0000gn/T/pip-install-64_pqrdb/pandas_ad9c5f0132054736a450e846cbf30fa7/.mesonpy-qsv78j1l/build/meson-logs/meson-log.txt
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> pandas

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import modin.pandas as mpd
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    import modin.pandas as mpd
ModuleNotFoundError: No module named 'modin'
>>> brew install pyenv
  File "<python-input-1>", line 1
    brew install pyenv
         ^^^^^^^
SyntaxError: invalid syntax
>>> install pyenv
  File "<python-input-2>", line 1
    install pyenv
            ^^^^^
SyntaxError: invalid syntax
>>> exit ()
kojofrimpong@Kojo--MacBook-Pro ~ % brew install pyenv
zsh: command not found: brew
kojofrimpong@Kojo--MacBook-Pro ~ % exit ()
function> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
kojofrimpong@Kojo--MacBook-Pro ~ % echo 'eval "$(/opt/homebrew/bin/brew shellenv)"'>> ~/.zprofile
kojofrimpong@Kojo--MacBook-Pro ~ % eval "$(/opt/homebrew/bin/brew shellenv)"
zsh: no such file or directory: /opt/homebrew/bin/brew
kojofrimpong@Kojo--MacBook-Pro ~ % echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
zsh: no such file or directory: /opt/homebrew/bin/brew
kojofrimpong@Kojo--MacBook-Pro ~ % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
\Sorry, try again.
Password:
Sorry, try again.
Password:
3114sudo: 3 incorrect password attempts
Need sudo access on macOS (e.g. the user kojofrimpong needs to be an Administrator)!
kojofrimpong@Kojo--MacBook-Pro ~ % 3114
zsh: command not found: 3114
kojofrimpong@Kojo--MacBook-Pro ~ % 3114
zsh: command not found: 3114
kojofrimpong@Kojo--MacBook-Pro ~ % which brew
brew not found
kojofrimpong@Kojo--MacBook-Pro ~ % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
==> This script will install:
/opt/homebrew/bin/brew
/opt/homebrew/share/doc/homebrew
/opt/homebrew/share/man/man1/brew.1
/opt/homebrew/share/zsh/site-functions/_brew
/opt/homebrew/etc/bash_completion.d/brew
/opt/homebrew
/etc/paths.d/homebrew
==> The following new directories will be created:
/opt/homebrew/bin
/opt/homebrew/etc
/opt/homebrew/include
/opt/homebrew/lib
/opt/homebrew/sbin
/opt/homebrew/share
/opt/homebrew/var
/opt/homebrew/opt
/opt/homebrew/share/zsh
/opt/homebrew/share/zsh/site-functions
/opt/homebrew/var/homebrew
/opt/homebrew/var/homebrew/linked
/opt/homebrew/Cellar
/opt/homebrew/Caskroom
/opt/homebrew/Frameworks
==> The Xcode Command Line Tools will be installed.

Press RETURN/ENTER to continue or any other key to abort:
kojofrimpong@Kojo--MacBook-Pro ~ % which brew
brew not found
kojofrimpong@Kojo--MacBook-Pro ~ % which brew
brew not found
kojofrimpong@Kojo--MacBook-Pro ~ % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
==> This script will install:
/opt/homebrew/bin/brew
/opt/homebrew/share/doc/homebrew
/opt/homebrew/share/man/man1/brew.1
/opt/homebrew/share/zsh/site-functions/_brew
/opt/homebrew/etc/bash_completion.d/brew
/opt/homebrew
/etc/paths.d/homebrew
==> The following new directories will be created:
/opt/homebrew/bin
/opt/homebrew/etc
/opt/homebrew/include
/opt/homebrew/lib
/opt/homebrew/sbin
/opt/homebrew/share
/opt/homebrew/var
/opt/homebrew/opt
/opt/homebrew/share/zsh
/opt/homebrew/share/zsh/site-functions
/opt/homebrew/var/homebrew
/opt/homebrew/var/homebrew/linked
/opt/homebrew/Cellar
/opt/homebrew/Caskroom
/opt/homebrew/Frameworks
==> The Xcode Command Line Tools will be installed.

Press RETURN/ENTER to continue or any other key to abort:
kojofrimpong@Kojo--MacBook-Pro ~ % which brew
brew not found
kojofrimpong@Kojo--MacBook-Pro ~ % brew --version
zsh: command not found: brew
kojofrimpong@Kojo--MacBook-Pro ~ % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
Sorry, try again.
Password:
==> This script will install:
/opt/homebrew/bin/brew
/opt/homebrew/share/doc/homebrew
/opt/homebrew/share/man/man1/brew.1
/opt/homebrew/share/zsh/site-functions/_brew
/opt/homebrew/etc/bash_completion.d/brew
/opt/homebrew
/etc/paths.d/homebrew
==> The following new directories will be created:
/opt/homebrew/bin
/opt/homebrew/etc
/opt/homebrew/include
/opt/homebrew/lib
/opt/homebrew/sbin
/opt/homebrew/share
/opt/homebrew/var
/opt/homebrew/opt
/opt/homebrew/share/zsh
/opt/homebrew/share/zsh/site-functions
/opt/homebrew/var/homebrew
/opt/homebrew/var/homebrew/linked
/opt/homebrew/Cellar
/opt/homebrew/Caskroom
/opt/homebrew/Frameworks
==> The Xcode Command Line Tools will be installed.

Press RETURN/ENTER to continue or any other key to abort:
==> /usr/bin/sudo /usr/bin/install -d -o root -g wheel -m 0755 /opt/homebrew
==> /usr/bin/sudo /bin/mkdir -p /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /bin/chmod ug=rwx /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /bin/chmod go-w /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions
==> /usr/bin/sudo /usr/sbin/chown kojofrimpong /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /usr/bin/chgrp admin /opt/homebrew/bin /opt/homebrew/etc /opt/homebrew/include /opt/homebrew/lib /opt/homebrew/sbin /opt/homebrew/share /opt/homebrew/var /opt/homebrew/opt /opt/homebrew/share/zsh /opt/homebrew/share/zsh/site-functions /opt/homebrew/var/homebrew /opt/homebrew/var/homebrew/linked /opt/homebrew/Cellar /opt/homebrew/Caskroom /opt/homebrew/Frameworks
==> /usr/bin/sudo /usr/sbin/chown -R kojofrimpong:admin /opt/homebrew
==> Searching online for the Command Line Tools
==> /usr/bin/sudo /usr/bin/touch /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
==> Installing Command Line Tools for Xcode-16.2
==> /usr/bin/sudo /usr/sbin/softwareupdate -i Command\ Line\ Tools\ for\ Xcode-16.2
Software Update Tool

Finding available software
Not enough free disk space: a total of 10.57 GB is required.
==> /usr/bin/sudo /usr/bin/xcode-select --switch /Library/Developer/CommandLineTools
xcode-select: error: invalid developer directory '/Library/Developer/CommandLineTools'
Failed during: /usr/bin/sudo /usr/bin/xcode-select --switch /Library/Developer/CommandLineTools
kojofrimpong@Kojo--MacBook-Pro ~ % which brew
brew not found
kojofrimpong@Kojo--MacBook-Pro ~ % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
==> This script will install:
/opt/homebrew/bin/brew
/opt/homebrew/share/doc/homebrew
/opt/homebrew/share/man/man1/brew.1
/opt/homebrew/share/zsh/site-functions/_brew
/opt/homebrew/etc/bash_completion.d/brew
/opt/homebrew
/etc/paths.d/homebrew
==> The Xcode Command Line Tools will be installed.

Press RETURN/ENTER to continue or any other key to abort:
==> /usr/bin/sudo /usr/sbin/chown -R kojofrimpong:admin /opt/homebrew
==> Searching online for the Command Line Tools
==> /usr/bin/sudo /usr/bin/touch /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
==> Installing Command Line Tools for Xcode-16.2
==> /usr/bin/sudo /usr/sbin/softwareupdate -i Command\ Line\ Tools\ for\ Xcode-16.2
Software Update Tool

Finding available software

Downloading Command Line Tools for Xcode
Downloaded Command Line Tools for Xcode
Installing Command Line Tools for Xcode
Done with Command Line Tools for Xcode
Done.
==> /usr/bin/sudo /usr/bin/xcode-select --switch /Library/Developer/CommandLineTools
==> /usr/bin/sudo /bin/rm -f /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
==> Downloading and installing Homebrew...
remote: Enumerating objects: 319764, done.
remote: Counting objects: 100% (251/251), done.
remote: Compressing objects: 100% (140/140), done.
remote: Total 319764 (delta 165), reused 156 (delta 111), pack-reused 319513 (from 2)
remote: Enumerating objects: 55, done.
remote: Counting objects: 100% (34/34), done.
remote: Total 55 (delta 34), reused 34 (delta 34), pack-reused 21 (from 1)
==> /usr/bin/sudo /bin/mkdir -p /etc/paths.d
==> /usr/bin/sudo tee /etc/paths.d/homebrew
/opt/homebrew/bin
==> /usr/bin/sudo /usr/sbin/chown root:wheel /etc/paths.d/homebrew
==> /usr/bin/sudo /bin/chmod a+r /etc/paths.d/homebrew
==> Updating Homebrew...
==> Downloading https://ghcr.io/v2/homebrew/core/portable-ruby/blobs/sha256:1c98fa49eacc935640a6f8e10a2bf33f14cfc276804b71ddb658ea45ba99d167
######################################################################################################## 100.0%
==> Pouring portable-ruby-3.4.8.arm64_big_sur.bottle.tar.gz
==> Installation successful!

==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
  https://docs.brew.sh/Analytics
No analytics data has been sent yet (nor will any be during this install run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
  https://github.com/Homebrew/brew#donations

==> Next steps:
- Run this command in your terminal to add Homebrew to your PATH:
    eval "$(/opt/homebrew/bin/brew shellenv zsh)"
- Run brew help to get started
- Further documentation:
    https://docs.brew.sh

kojofrimpong@Kojo--MacBook-Pro ~ % which brew
brew not found
kojofrimpong@Kojo--MacBook-Pro ~ % brew --version
zsh: command not found: brew
kojofrimpong@Kojo--MacBook-Pro ~ % eval "$(/opt/homebrew/bin/brew shellenv)"
kojofrimpong@Kojo--MacBook-Pro ~ % which brew
/opt/homebrew/bin/brew
kojofrimpong@Kojo--MacBook-Pro ~ % brew --version
Homebrew 5.0.10
kojofrimpong@Kojo--MacBook-Pro ~ % echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
kojofrimpong@Kojo--MacBook-Pro ~ % brew install pyenv
pyenv install 3.11.8
pyenv global 3.11.8
python3 -m pip install --upgrade pip
python3 -m pip install pandas polars dask modin duckdb
✔︎ JSON API formula.jws.json                                                         Downloaded   32.0MB/ 32.0MB
✔︎ JSON API cask.jws.json                                                            Downloaded   15.3MB/ 15.3MB
==> Fetching downloads for: pyenv
✔︎ Bottle Manifest pyenv (2.6.20)                                                    Downloaded   15.9KB/ 15.9KB
✔︎ Bottle Manifest m4 (1.4.20)                                                       Downloaded   11.7KB/ 11.7KB
✔︎ Bottle Manifest autoconf (2.72)                                                   Downloaded   19.7KB/ 19.7KB
✔︎ Bottle Manifest ca-certificates (2025-12-02)                                      Downloaded    2.0KB/  2.0KB
✔︎ Bottle Manifest openssl@3 (3.6.0)                                                 Downloaded   11.8KB/ 11.8KB
✔︎ Bottle Manifest pkgconf (2.5.1)                                                   Downloaded   12.2KB/ 12.2KB
✔︎ Bottle Manifest readline (8.3.3)                                                  Downloaded   10.0KB/ 10.0KB
✔︎ Bottle m4 (1.4.20)                                                                Downloaded  279.3KB/279.3KB
✔︎ Bottle ca-certificates (2025-12-02)                                               Downloaded  131.8KB/131.8KB
✔︎ Bottle autoconf (2.72)                                                            Downloaded    1.1MB/  1.1MB
✔︎ Bottle pkgconf (2.5.1)                                                            Downloaded  121.9KB/121.9KB
✔︎ Bottle readline (8.3.3)                                                           Downloaded  758.1KB/758.1KB
✔︎ Bottle pyenv (2.6.20)                                                             Downloaded    1.4MB/  1.4MB
✔︎ Bottle openssl@3 (3.6.0)                                                          Downloaded   10.9MB/ 10.9MB
==> Installing dependencies for pyenv: m4, autoconf, ca-certificates, openssl@3, pkgconf and readline
==> Installing pyenv dependency: m4
==> Pouring m4--1.4.20.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/m4/1.4.20: 14 files, 802.7KB
==> Installing pyenv dependency: autoconf
==> Pouring autoconf--2.72.arm64_sequoia.bottle.1.tar.gz
🍺  /opt/homebrew/Cellar/autoconf/2.72: 72 files, 3.8MB
==> Installing pyenv dependency: ca-certificates
==> Pouring ca-certificates--2025-12-02.all.bottle.tar.gz
==> Regenerating CA certificate bundle from keychain, this may take a while...
🍺  /opt/homebrew/Cellar/ca-certificates/2025-12-02: 4 files, 236.4KB
==> Installing pyenv dependency: openssl@3
==> Pouring openssl@3--3.6.0.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/openssl@3/3.6.0: 7,609 files, 37.7MB
==> Installing pyenv dependency: pkgconf
==> Pouring pkgconf--2.5.1.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pkgconf/2.5.1: 28 files, 533.5KB
==> Installing pyenv dependency: readline
==> Pouring readline--8.3.3.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/readline/8.3.3: 56 files, 2.7MB
==> Installing pyenv
==> Pouring pyenv--2.6.20.arm64_sequoia.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pyenv/2.6.20: 1,458 files, 4.6MB
==> Running `brew cleanup pyenv`...
Disable this behaviour by setting `HOMEBREW_NO_INSTALL_CLEANUP=1`.
Hide these hints with `HOMEBREW_NO_ENV_HINTS=1` (see `man brew`).
python-build: use openssl@3 from homebrew
python-build: use readline from homebrew
Downloading Python-3.11.8.tar.xz...
-> https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tar.xz
Installing Python-3.11.8...
patching file setup.py
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/lzma.py", line 27, in <module>
    from _lzma import *
ModuleNotFoundError: No module named '_lzma'
WARNING: The Python lzma extension was not compiled. Missing the lzma lib?
Installed Python-3.11.8 to /Users/kojofrimpong/.pyenv/versions/3.11.8
Requirement already satisfied: pip in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (25.3)
Requirement already satisfied: pandas in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (2.3.3)
Requirement already satisfied: polars in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (1.37.1)
Requirement already satisfied: dask in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (2026.1.1)
Collecting modin
  Using cached modin-0.37.1-py3-none-any.whl.metadata (17 kB)
Requirement already satisfied: duckdb in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (1.4.3)
Requirement already satisfied: numpy>=1.26.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from pandas) (2.4.1)
Requirement already satisfied: python-dateutil>=2.8.2 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from pandas) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from pandas) (2025.3)
Requirement already satisfied: polars-runtime-32==1.37.1 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from polars) (1.37.1)
Requirement already satisfied: click>=8.1 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask) (8.3.1)
Requirement already satisfied: cloudpickle>=3.0.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask) (3.1.2)
Requirement already satisfied: fsspec>=2021.09.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask) (2026.1.0)
Requirement already satisfied: packaging>=20.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask) (25.0)
Requirement already satisfied: partd>=1.4.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask) (1.4.2)
Requirement already satisfied: pyyaml>=5.3.1 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask) (6.0.3)
Requirement already satisfied: toolz>=0.12.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from dask) (1.1.0)
Requirement already satisfied: psutil>=5.8.0 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from modin) (7.2.1)
Collecting typing-extensions (from modin)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: locket in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from partd>=1.4.0->dask) (1.0.0)
Requirement already satisfied: six>=1.5 in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
Downloading modin-0.37.1-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 13.1 MB/s  0:00:00
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Installing collected packages: typing-extensions, modin
Successfully installed modin-0.37.1 typing-extensions-4.15.0
kojofrimpong@Kojo--MacBook-Pro ~ % df = pd.read_csv("metadava.csv")
zsh: number expected
kojofrimpong@Kojo--MacBook-Pro ~ % data.csv
zsh: command not found: data.csv
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> DATA_PATH = "/Users/kojofrimpong/Downloads/data.csv"
>>> import pandas as pd
... 
... df_pd = pd.read_csv(DATA_PATH)
... 
>>> import polars as pl
... 
... df_pl = pl.read_csv(DATA_PATH)
... 
>>> import dask.dataframe as dd
... 
... df_dd = dd.read_csv(DATA_PATH)
... 
>>> import duckdb
... 
... df_duck = duckdb.query(
...     f"SELECT * FROM read_csv_auto('{DATA_PATH}')"
... ).to_df()
... 
>>> import modin.pandas as mpd
... 
... df_md = mpd.read_csv(DATA_PATH)
... 
>>> exit()
2026-01-18 20:54:44,303 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55383' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-5abf0793e5e236221e1b33c72c9e96d1', 'lambda-c70e0eab569ea1c204981cdea7083fe4'} (stimulus_id='handle-worker-cleanup-1768791284.302838')
2026-01-18 20:54:44,306 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55382' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-7c663e5c240404425276ca944978564e', 'lambda-7104154e0bb0b81473faccea6bcab05a'} (stimulus_id='handle-worker-cleanup-1768791284.306587')
2026-01-18 20:54:44,306 - distributed.scheduler - ERROR - Removing worker 'tcp://127.0.0.1:55382' caused the cluster to lose scattered data, which can't be recovered: {'function-d0575a438022879b53a43d7f3f81d481'} (stimulus_id='handle-worker-cleanup-1768791284.306587')
2026-01-18 20:54:44,308 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55390' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-b8f68136ff11439cef7d72d6a745aa73', 'lambda-3f9d62369acd96342273de71ee9c765c'} (stimulus_id='handle-worker-cleanup-1768791284.3087811')
2026-01-18 20:54:44,309 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55376' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-44d257c2df79c8fcbb69326690785a78', 'lambda-e07af25a7b9727ddd6a5ec9d86f82a60'} (stimulus_id='handle-worker-cleanup-1768791284.309052')
2026-01-18 20:54:44,310 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55399' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-7ff2a5699050ba8b2b6f8d6df84c81cd', 'lambda-f5d0da4c9f1bbf2a6344c6b5da9e1210'} (stimulus_id='handle-worker-cleanup-1768791284.3105059')
2026-01-18 20:54:44,310 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55375' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-abc6268bec0d0a7848d9b19d0238b5cc', 'lambda-8ce10fdb54faa91fe27c071eaabb1432'} (stimulus_id='handle-worker-cleanup-1768791284.310684')
2026-01-18 20:54:44,310 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55381' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-75b3a7d731fd2249779780c77d51ea6c', 'lambda-943da46b0128c712687aa97b00ab37bc'} (stimulus_id='handle-worker-cleanup-1768791284.310824')
2026-01-18 20:54:44,310 - distributed.scheduler - ERROR - Removing worker 'tcp://127.0.0.1:55381' caused the cluster to lose scattered data, which can't be recovered: {'function-364c0a682a7a955a871a7efde92671cd'} (stimulus_id='handle-worker-cleanup-1768791284.310824')
2026-01-18 20:54:44,316 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55402' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-162c3f39b23a372dfbf75f19446555a1', 'lambda-1b8139ad8aa1799ca84fcd08a857a59a'} (stimulus_id='handle-worker-cleanup-1768791284.316716')
2026-01-18 20:54:44,316 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55405' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-efa5355751cf3f873d358d735f44767f', 'lambda-7c7c266dd92a87fd68645a078cef8b5e'} (stimulus_id='handle-worker-cleanup-1768791284.31693')
2026-01-18 20:54:44,317 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55391' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-f80754fef5bcf50c68ff97925568354c', 'lambda-16273feb088d741e8a73044bab0fc55e'} (stimulus_id='handle-worker-cleanup-1768791284.317734')
2026-01-18 20:54:44,318 - distributed.scheduler - WARNING - Removing worker 'tcp://127.0.0.1:55396' caused the cluster to lose already computed task(s), which will be recomputed elsewhere: {'lambda-5896cb610e520f02dd7c942ac86d5102', 'lambda-9045e606a795cff83d5ccede70652264'} (stimulus_id='handle-worker-cleanup-1768791284.318625')
kojofrimpong@Kojo--MacBook-Pro ~ % echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zprofile
source ~/.zprofile
kojofrimpong@Kojo--MacBook-Pro ~ % pyenv --version
pyenv 2.6.20
kojofrimpong@Kojo--MacBook-Pro ~ % pyenv global 3.11.8
python --version
Python 3.11.8
kojofrimpong@Kojo--MacBook-Pro ~ % python -m pip install --upgrade pip
python -m pip install pandas polars dask modin duckdb
Requirement already satisfied: pip in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (24.0)
Collecting pip
  Downloading pip-25.3-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-25.3-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 11.1 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-25.3
Collecting pandas
  Downloading pandas-2.3.3-cp311-cp311-macosx_11_0_arm64.whl.metadata (91 kB)
Collecting polars
  Using cached polars-1.37.1-py3-none-any.whl.metadata (10 kB)
Collecting dask
  Using cached dask-2026.1.1-py3-none-any.whl.metadata (3.8 kB)
Collecting modin
  Using cached modin-0.37.1-py3-none-any.whl.metadata (17 kB)
Collecting duckdb
  Downloading duckdb-1.4.3-cp311-cp311-macosx_11_0_arm64.whl.metadata (4.3 kB)
Collecting numpy>=1.23.2 (from pandas)
  Downloading numpy-2.4.1-cp311-cp311-macosx_14_0_arm64.whl.metadata (6.6 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
  Using cached tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting polars-runtime-32==1.37.1 (from polars)
  Using cached polars_runtime_32-1.37.1-cp310-abi3-macosx_11_0_arm64.whl.metadata (1.5 kB)
Collecting click>=8.1 (from dask)
  Using cached click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting cloudpickle>=3.0.0 (from dask)
  Using cached cloudpickle-3.1.2-py3-none-any.whl.metadata (7.1 kB)
Collecting fsspec>=2021.09.0 (from dask)
  Using cached fsspec-2026.1.0-py3-none-any.whl.metadata (10 kB)
Collecting packaging>=20.0 (from dask)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting partd>=1.4.0 (from dask)
  Using cached partd-1.4.2-py3-none-any.whl.metadata (4.6 kB)
Collecting pyyaml>=5.3.1 (from dask)
  Downloading pyyaml-6.0.3-cp311-cp311-macosx_11_0_arm64.whl.metadata (2.4 kB)
Collecting toolz>=0.12.0 (from dask)
  Using cached toolz-1.1.0-py3-none-any.whl.metadata (5.1 kB)
Collecting importlib_metadata>=4.13.0 (from dask)
  Downloading importlib_metadata-8.7.1-py3-none-any.whl.metadata (4.7 kB)
Collecting psutil>=5.8.0 (from modin)
  Using cached psutil-7.2.1-cp36-abi3-macosx_11_0_arm64.whl.metadata (22 kB)
Collecting typing-extensions (from modin)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting zipp>=3.20 (from importlib_metadata>=4.13.0->dask)
  Downloading zipp-3.23.0-py3-none-any.whl.metadata (3.6 kB)
Collecting locket (from partd>=1.4.0->dask)
  Using cached locket-1.0.0-py2.py3-none-any.whl.metadata (2.8 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading pandas-2.3.3-cp311-cp311-macosx_11_0_arm64.whl (10.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.8/10.8 MB 33.2 MB/s  0:00:00
Using cached polars-1.37.1-py3-none-any.whl (805 kB)
Using cached polars_runtime_32-1.37.1-cp310-abi3-macosx_11_0_arm64.whl (39.7 MB)
Using cached dask-2026.1.1-py3-none-any.whl (1.5 MB)
Using cached modin-0.37.1-py3-none-any.whl (1.2 MB)
Downloading duckdb-1.4.3-cp311-cp311-macosx_11_0_arm64.whl (13.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.7/13.7 MB 67.3 MB/s  0:00:00
Using cached click-8.3.1-py3-none-any.whl (108 kB)
Using cached cloudpickle-3.1.2-py3-none-any.whl (22 kB)
Using cached fsspec-2026.1.0-py3-none-any.whl (201 kB)
Downloading importlib_metadata-8.7.1-py3-none-any.whl (27 kB)
Downloading numpy-2.4.1-cp311-cp311-macosx_14_0_arm64.whl (5.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 78.1 MB/s  0:00:00
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached partd-1.4.2-py3-none-any.whl (18 kB)
Using cached psutil-7.2.1-cp36-abi3-macosx_11_0_arm64.whl (128 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Downloading pyyaml-6.0.3-cp311-cp311-macosx_11_0_arm64.whl (175 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached toolz-1.1.0-py3-none-any.whl (58 kB)
Using cached tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
Using cached locket-1.0.0-py2.py3-none-any.whl (4.4 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Installing collected packages: pytz, zipp, tzdata, typing-extensions, toolz, six, pyyaml, psutil, polars-runtime-32, packaging, numpy, locket, fsspec, duckdb, cloudpickle, click, python-dateutil, polars, partd, importlib_metadata, pandas, dask, modin
Successfully installed click-8.3.1 cloudpickle-3.1.2 dask-2026.1.1 duckdb-1.4.3 fsspec-2026.1.0 importlib_metadata-8.7.1 locket-1.0.0 modin-0.37.1 numpy-2.4.1 packaging-25.0 pandas-2.3.3 partd-1.4.2 polars-1.37.1 polars-runtime-32-1.37.1 psutil-7.2.1 python-dateutil-2.9.0.post0 pytz-2025.2 pyyaml-6.0.3 six-1.17.0 toolz-1.1.0 typing-extensions-4.15.0 tzdata-2025.3 zipp-3.23.0
kojofrimpong@Kojo--MacBook-Pro ~ % python
Python 3.11.8 (main, Jan 18 2026, 19:11:58) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
import polars as pl
import dask.dataframe as dd
import modin.pandas as mpd
import duckdb

print("All good!")
>>> import polars as pl
import dask.dataframe as dd
import modin.pandas as mpd
import duckdb

print("All good!")
>>> import dask.dataframe as dd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/__init__.py", line 25, in <module>
    from dask.dataframe.dask_expr import (
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/__init__.py", line 3, in <module>
    from dask.dataframe.dask_expr import datasets
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/datasets.py", line 10, in <module>
    from dask.dataframe.dask_expr._collection import new_collection
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/_collection.py", line 14, in <module>
    import pyarrow as pa
ModuleNotFoundError: No module named 'pyarrow'
>>> import modin.pandas as mpd
>>> import duckdb
>>> 
>>> print("All good!")
All good!
>>> DATA_PATH = "/Users/kojofrimpong/Downloads/data.csv"
>>> 
>>> import pandas as pd
>>> df_pd = pd.read_csv(DATA_PATH)
>>> df_pd.head()
      image_id  split  ...             png_image_path                    png_label_path
0  10078660_15  train  ...  png/train/10078660_15.png  png/train_labels/10078660_15.png
1  10078675_15  train  ...  png/train/10078675_15.png  png/train_labels/10078675_15.png
2  10078690_15  train  ...  png/train/10078690_15.png  png/train_labels/10078690_15.png
3  10078705_15  train  ...  png/train/10078705_15.png  png/train_labels/10078705_15.png
4  10078720_15  train  ...  png/train/10078720_15.png  png/train_labels/10078720_15.png

[5 rows x 8 columns]
>>> import polars as pl
>>> df_pl = pl.read_csv(DATA_PATH)
>>> df_pl.head()
shape: (5, 8)
┌─────────────┬───────┬──────────────┬──────────────┬──────────────┬──────────────┬─────────────┬─────────────┐
│ image_id    ┆ split ┆ image_souce_ ┆ label_source ┆ tiff_image_p ┆ tif_label_pa ┆ png_image_p ┆ png_label_p │
│ ---         ┆ ---   ┆ url          ┆ _url         ┆ ath          ┆ th           ┆ ath         ┆ ath         │
│ str         ┆ str   ┆ ---          ┆ ---          ┆ ---          ┆ ---          ┆ ---         ┆ ---         │
│             ┆       ┆ str          ┆ str          ┆ str          ┆ str          ┆ str         ┆ str         │
╞═════════════╪═══════╪══════════════╪══════════════╪══════════════╪══════════════╪═════════════╪═════════════╡
│ 10078660_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078660_15.t ┆ abels/100786 ┆ 0078660_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 60_15.…      ┆ png         ┆ 660_15.p…   │
│ 10078675_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078675_15.t ┆ abels/100786 ┆ 0078675_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 75_15.…      ┆ png         ┆ 675_15.p…   │
│ 10078690_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078690_15.t ┆ abels/100786 ┆ 0078690_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 90_15.…      ┆ png         ┆ 690_15.p…   │
│ 10078705_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078705_15.t ┆ abels/100787 ┆ 0078705_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 05_15.…      ┆ png         ┆ 705_15.p…   │
│ 10078720_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078720_15.t ┆ abels/100787 ┆ 0078720_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 20_15.…      ┆ png         ┆ 720_15.p…   │
└─────────────┴───────┴──────────────┴──────────────┴──────────────┴──────────────┴─────────────┴─────────────┘
>>> 
>>> import dask.dataframe as dd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/__init__.py", line 25, in <module>
    from dask.dataframe.dask_expr import (
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/__init__.py", line 3, in <module>
    from dask.dataframe.dask_expr import datasets
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/datasets.py", line 10, in <module>
    from dask.dataframe.dask_expr._collection import new_collection
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/_collection.py", line 14, in <module>
    import pyarrow as pa
ModuleNotFoundError: No module named 'pyarrow'
>>> df_dd = dd.read_csv(DATA_PATH)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dd' is not defined. Did you mean: 'pd'?
>>> df_dd.head()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_dd' is not defined. Did you mean: 'df_pd'?
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> exit()
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.11.8 (main, Jan 18 2026, 19:11:58) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> DATA_PATH = "/Users/kojofrimpong/Downloads/data.csv"
>>> 
>>> DATA_PATH = "/Users/kojofrimpong/Downloads/data.csv"
>>> DATA_PATH = "/Users/kojofrimpong/Downloads/data.csv"
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> exit()
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.11.8 (main, Jan 18 2026, 19:11:58) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
>>> exit()
kojofrimpong@Kojo--MacBook-Pro ~ % exit()
function> exit()
function function> exit()
function function function> python3
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.11.8 (main, Jan 18 2026, 19:11:58) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> python3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> exit()
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.11.8 (main, Jan 18 2026, 19:11:58) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> print(pd.__version__)
2.3.3
>>> DATA_PATH = "/Users/kojofrimpong/Downloads/data.csv"
>>> import pandas as pd
>>> df_pd = pd.read_csv(DATA_PATH)
>>> df_pd.head()
      image_id  split  ...             png_image_path                    png_label_path
0  10078660_15  train  ...  png/train/10078660_15.png  png/train_labels/10078660_15.png
1  10078675_15  train  ...  png/train/10078675_15.png  png/train_labels/10078675_15.png
2  10078690_15  train  ...  png/train/10078690_15.png  png/train_labels/10078690_15.png
3  10078705_15  train  ...  png/train/10078705_15.png  png/train_labels/10078705_15.png
4  10078720_15  train  ...  png/train/10078720_15.png  png/train_labels/10078720_15.png

[5 rows x 8 columns]
>>> import polars as pl
>>> df_pl = pl.read_csv(DATA_PATH)
>>> df_pl.head()
shape: (5, 8)
┌─────────────┬───────┬──────────────┬──────────────┬──────────────┬──────────────┬─────────────┬─────────────┐
│ image_id    ┆ split ┆ image_souce_ ┆ label_source ┆ tiff_image_p ┆ tif_label_pa ┆ png_image_p ┆ png_label_p │
│ ---         ┆ ---   ┆ url          ┆ _url         ┆ ath          ┆ th           ┆ ath         ┆ ath         │
│ str         ┆ str   ┆ ---          ┆ ---          ┆ ---          ┆ ---          ┆ ---         ┆ ---         │
│             ┆       ┆ str          ┆ str          ┆ str          ┆ str          ┆ str         ┆ str         │
╞═════════════╪═══════╪══════════════╪══════════════╪══════════════╪══════════════╪═════════════╪═════════════╡
│ 10078660_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078660_15.t ┆ abels/100786 ┆ 0078660_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 60_15.…      ┆ png         ┆ 660_15.p…   │
│ 10078675_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078675_15.t ┆ abels/100786 ┆ 0078675_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 75_15.…      ┆ png         ┆ 675_15.p…   │
│ 10078690_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078690_15.t ┆ abels/100786 ┆ 0078690_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 90_15.…      ┆ png         ┆ 690_15.p…   │
│ 10078705_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078705_15.t ┆ abels/100787 ┆ 0078705_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 05_15.…      ┆ png         ┆ 705_15.p…   │
│ 10078720_15 ┆ train ┆ http://www.c ┆ http://www.c ┆ tiff/train/1 ┆ tiff/train_l ┆ png/train/1 ┆ png/train_l │
│             ┆       ┆ s.toronto.ed ┆ s.toronto.ed ┆ 0078720_15.t ┆ abels/100787 ┆ 0078720_15. ┆ abels/10078 │
│             ┆       ┆ u/~vmn…      ┆ u/~vmn…      ┆ iff          ┆ 20_15.…      ┆ png         ┆ 720_15.p…   │
└─────────────┴───────┴──────────────┴──────────────┴──────────────┴──────────────┴─────────────┴─────────────┘
>>> import dask.dataframe as dd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/__init__.py", line 25, in <module>
    from dask.dataframe.dask_expr import (
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/__init__.py", line 3, in <module>
    from dask.dataframe.dask_expr import datasets
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/datasets.py", line 10, in <module>
    from dask.dataframe.dask_expr._collection import new_collection
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/dask/dataframe/dask_expr/_collection.py", line 14, in <module>
    import pyarrow as pa
ModuleNotFoundError: No module named 'pyarrow'
>>> df_dd = dd.read_csv(DATA_PATH)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dd' is not defined. Did you mean: 'pd'?
>>> df_dd.head()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_dd' is not defined. Did you mean: 'df_pd'?
>>> import duckdb
>>> df_duck = duckdb.query(
...     f"SELECT * FROM read_csv_auto('{DATA_PATH}')"
... ).to_df()
>>> df_duck.head()
      image_id  split  ...             png_image_path                    png_label_path
0  10078660_15  train  ...  png/train/10078660_15.png  png/train_labels/10078660_15.png
1  10078675_15  train  ...  png/train/10078675_15.png  png/train_labels/10078675_15.png
2  10078690_15  train  ...  png/train/10078690_15.png  png/train_labels/10078690_15.png
3  10078705_15  train  ...  png/train/10078705_15.png  png/train_labels/10078705_15.png
4  10078720_15  train  ...  png/train/10078720_15.png  png/train_labels/10078720_15.png

[5 rows x 8 columns]
>>> # Pandas
>>> len(df_pd)
1171
>>> 
>>> # Polars
>>> df_pl.height
1171
>>> 
>>> # Dask
>>> df_dd.shape[0].compute()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_dd' is not defined. Did you mean: 'df_pd'?
>>> 
>>> # DuckDB
>>> duckdb.query(
...     f"SELECT COUNT(*) FROM read_csv_auto('{DATA_PATH}')"
... ).fetchone()
(1171,)
>>> # Pandas
>>> df_pd.describe()
           image_id  split  ...             png_image_path                    png_label_path
count          1171   1171  ...                       1171                              1171
unique         1171      3  ...                       1171                              1171
top     10078660_15  train  ...  png/train/10078660_15.png  png/train_labels/10078660_15.png
freq              1   1108  ...                          1                                 1

[4 rows x 8 columns]
>>> 
>>> # Polars
>>> df_pl.describe()
shape: (9, 9)
┌────────────┬─────────────┬───────┬──────────────┬───┬─────────────┬─────────────┬─────────────┬─────────────┐
│ statistic  ┆ image_id    ┆ split ┆ image_souce_ ┆ … ┆ tiff_image_ ┆ tif_label_p ┆ png_image_p ┆ png_label_p │
│ ---        ┆ ---         ┆ ---   ┆ url          ┆   ┆ path        ┆ ath         ┆ ath         ┆ ath         │
│ str        ┆ str         ┆ str   ┆ ---          ┆   ┆ ---         ┆ ---         ┆ ---         ┆ ---         │
│            ┆             ┆       ┆ str          ┆   ┆ str         ┆ str         ┆ str         ┆ str         │
╞════════════╪═════════════╪═══════╪══════════════╪═══╪═════════════╪═════════════╪═════════════╪═════════════╡
│ count      ┆ 1171        ┆ 1171  ┆ 1171         ┆ … ┆ 1171        ┆ 1171        ┆ 1171        ┆ 1171        │
│ null_count ┆ 0           ┆ 0     ┆ 0            ┆ … ┆ 0           ┆ 0           ┆ 0           ┆ 0           │
│ mean       ┆ null        ┆ null  ┆ null         ┆ … ┆ null        ┆ null        ┆ null        ┆ null        │
│ std        ┆ null        ┆ null  ┆ null         ┆ … ┆ null        ┆ null        ┆ null        ┆ null        │
│ min        ┆ 10078660_15 ┆ test  ┆ http://www.c ┆ … ┆ tiff/test/1 ┆ tiff/test_l ┆ png/test/10 ┆ png/test_la │
│            ┆             ┆       ┆ s.toronto.ed ┆   ┆ 0378780_15. ┆ abels/10378 ┆ 378780_15.p ┆ bels/103787 │
│            ┆             ┆       ┆ u/~vmn…      ┆   ┆ tiff        ┆ 780_15.t…   ┆ ng          ┆ 80_15.pn…   │
│ 25%        ┆ null        ┆ null  ┆ null         ┆ … ┆ null        ┆ null        ┆ null        ┆ null        │
│ 50%        ┆ null        ┆ null  ┆ null         ┆ … ┆ null        ┆ null        ┆ null        ┆ null        │
│ 75%        ┆ null        ┆ null  ┆ null         ┆ … ┆ null        ┆ null        ┆ null        ┆ null        │
│ max        ┆ 99238675_15 ┆ val   ┆ http://www.c ┆ … ┆ tiff/val/25 ┆ tiff/val_la ┆ png/val/252 ┆ png/val_lab │
│            ┆             ┆       ┆ s.toronto.ed ┆   ┆ 229245_15.t ┆ bels/252292 ┆ 29245_15.pn ┆ els/2522924 │
│            ┆             ┆       ┆ u/~vmn…      ┆   ┆ iff         ┆ 45_15.ti…   ┆ g           ┆ 5_15.png    │
└────────────┴─────────────┴───────┴──────────────┴───┴─────────────┴─────────────┴─────────────┴─────────────┘
>>> 
>>> # Dask
>>> df_dd.describe().compute()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_dd' is not defined. Did you mean: 'df_pd'?
>>> 
>>> # DuckDB
>>> duckdb.query(
...     f"""
...     SELECT 
...         COUNT(*) AS rows
...     FROM read_csv_auto('{DATA_PATH}')
...     """
... ).to_df()
   rows
0  1171
>>> # Pandas
>>> df_pd[df_pd["value"] > 50]
Traceback (most recent call last):
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc
    return self._engine.get_loc(casted_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pandas/_libs/index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7096, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'value'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/pandas/core/frame.py", line 4113, in __getitem__
    indexer = self.columns.get_loc(key)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/pandas/core/indexes/base.py", line 3819, in get_loc
    raise KeyError(key) from err
KeyError: 'value'
>>> 
>>> # Polars
>>> df_pl.filter(pl.col("value") > 50)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/polars/dataframe/frame.py", line 5345, in filter
    .collect(optimizations=QueryOptFlags._eager())
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/polars/_utils/deprecation.py", line 97, in wrapper
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/polars/lazyframe/opt_flags.py", line 324, in wrapper
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kojofrimpong/.pyenv/versions/3.11.8/lib/python3.11/site-packages/polars/lazyframe/frame.py", line 2429, in collect
    return wrap_df(ldf.collect(engine, callback))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
polars.exceptions.ColumnNotFoundError: unable to find column "value"; valid columns: ["image_id", "split", "image_souce_url", "label_source_url", "tiff_image_path", "tif_label_path", "png_image_path", "png_label_path"]
>>> 
>>> # Dask
>>> df_dd[df_dd["value"] > 50].compute()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_dd' is not defined. Did you mean: 'df_pd'?
>>> 
>>> # DuckDB
>>> duckdb.query(
...     f"""
...     SELECT *
...     FROM read_csv_auto('{DATA_PATH}')
...     WHERE value > 50
...     """
... ).to_df()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
_duckdb.BinderException: Binder Error: Referenced column "value" not found in FROM clause!
Candidate bindings: "image_id", "label_source_url", "png_image_path", "tiff_image_path"
>>> import time
>>> 
>>> start = time.time()
>>> pd.read_csv(DATA_PATH)
         image_id  split  ...             png_image_path                    png_label_path
0     10078660_15  train  ...  png/train/10078660_15.png  png/train_labels/10078660_15.png
1     10078675_15  train  ...  png/train/10078675_15.png  png/train_labels/10078675_15.png
2     10078690_15  train  ...  png/train/10078690_15.png  png/train_labels/10078690_15.png
3     10078705_15  train  ...  png/train/10078705_15.png  png/train_labels/10078705_15.png
4     10078720_15  train  ...  png/train/10078720_15.png  png/train_labels/10078720_15.png
...           ...    ...  ...                        ...                               ...
1166  25079170_15   test  ...   png/test/25079170_15.png   png/test_labels/25079170_15.png
1167  26278720_15   test  ...   png/test/26278720_15.png   png/test_labels/26278720_15.png
1168  26428735_15   test  ...   png/test/26428735_15.png   png/test_labels/26428735_15.png
1169  26578720_15   test  ...   png/test/26578720_15.png   png/test_labels/26578720_15.png
1170  26878690_15   test  ...   png/test/26878690_15.png   png/test_labels/26878690_15.png

[1171 rows x 8 columns]
>>> print("Pandas load time:", time.time() - start)
Pandas load time: 1.3031642436981201
>>> python3 -m pip install pyarrow
  File "<stdin>", line 1
    python3 -m pip install pyarrow
               ^^^
SyntaxError: invalid syntax
>>> python3 -m pip install pyarrow
  File "<stdin>", line 1
    python3 -m pip install pyarrow
               ^^^
SyntaxError: invalid syntax
>>> exit()
kojofrimpong@Kojo--MacBook-Pro ~ % python -m pip install pyarrow
Collecting pyarrow
  Downloading pyarrow-23.0.0-cp311-cp311-macosx_12_0_arm64.whl.metadata (3.0 kB)
Downloading pyarrow-23.0.0-cp311-cp311-macosx_12_0_arm64.whl (34.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 34.3/34.3 MB 75.1 MB/s  0:00:00
Installing collected packages: pyarrow
Successfully installed pyarrow-23.0.0
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.11.8 (main, Jan 18 2026, 19:11:58) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import dask.dataframe as dd
df_dd = dd.read_csv(DATA_PATH)
df_dd.head()

>>> df_dd = dd.read_csv(DATA_PATH)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'DATA_PATH' is not defined
>>> df_dd.head()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_dd' is not defined
>>> 
>>> DATA_PATH = "/Users/kojofrimpong/Downloads/data.csv"
>>> import dask.dataframe as dd
>>> df_dd = dd.read_csv(DATA_PATH)
>>> df_dd.head()
      image_id  split  ...             png_image_path                    png_label_path
0  10078660_15  train  ...  png/train/10078660_15.png  png/train_labels/10078660_15.png
1  10078675_15  train  ...  png/train/10078675_15.png  png/train_labels/10078675_15.png
2  10078690_15  train  ...  png/train/10078690_15.png  png/train_labels/10078690_15.png
3  10078705_15  train  ...  png/train/10078705_15.png  png/train_labels/10078705_15.png
4  10078720_15  train  ...  png/train/10078720_15.png  png/train_labels/10078720_15.png

[5 rows x 8 columns]
>>> import time
>>> start = time.time()
>>> df_pd = pd.read_csv(DATA_PATH)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pd' is not defined. Did you mean: 'dd'?
>>> df_pd.head()   # forces full read
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_pd' is not defined. Did you mean: 'df_dd'?
>>> pandas_time = time.time() - start
>>> 
>>> print("Pandas load time:", pandas_time)
Pandas load time: 0.0018088817596435547
>>> start = time.time()
>>> df_pl = pl.read_csv(DATA_PATH)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pl' is not defined
>>> df_pl.head()   # forces execution
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_pl' is not defined. Did you mean: 'df_dd'?
>>> polars_time = time.time() - start
>>> 
>>> print("Polars load time:", polars_time)
Polars load time: 0.0017271041870117188
>>> start = time.time()
>>> df_dd = dd.read_csv(DATA_PATH)
>>> df_dd.head()   # THIS triggers execution
      image_id  split  ...             png_image_path                    png_label_path
0  10078660_15  train  ...  png/train/10078660_15.png  png/train_labels/10078660_15.png
1  10078675_15  train  ...  png/train/10078675_15.png  png/train_labels/10078675_15.png
2  10078690_15  train  ...  png/train/10078690_15.png  png/train_labels/10078690_15.png
3  10078705_15  train  ...  png/train/10078705_15.png  png/train_labels/10078705_15.png
4  10078720_15  train  ...  png/train/10078720_15.png  png/train_labels/10078720_15.png

[5 rows x 8 columns]
>>> dask_time = time.time() - start
>>> 
>>> print("Dask load time:", dask_time)
Dask load time: 0.03870582580566406
>>> start = time.time()
>>> df_duck = duckdb.query(
...     f"SELECT * FROM read_csv_auto('{DATA_PATH}')"
... ).to_df()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'duckdb' is not defined
>>> duckdb_time = time.time() - start
>>> 
>>> print("DuckDB load time:", duckdb_time)
DuckDB load time: 0.0010571479797363281
>>> import pandas as pd
>>> 
>>> results = pd.DataFrame({
...     "Library": ["Pandas", "Polars", "Dask", "DuckDB"],
...     "Load Time (seconds)": [
...         pandas_time,
...         polars_time,
...         dask_time,
...         duckdb_time
...     ]
... })
>>> 
>>> results
  Library  Load Time (seconds)
0  Pandas             0.001809
1  Polars             0.001727
2    Dask             0.038706
3  DuckDB             0.001057
>>> exit()
kojofrimpong@Kojo--MacBook-Pro ~ % python3 -m pip install "modin[ray]"
Requirement already satisfied: modin[ray] in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (0.37.1)
Requirement already satisfied: pandas<2.4,>=2.2 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from modin[ray]) (2.3.3)
Requirement already satisfied: packaging>=21.0 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from modin[ray]) (25.0)
Requirement already satisfied: numpy>=1.22.4 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from modin[ray]) (2.4.1)
Requirement already satisfied: fsspec>=2022.11.0 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from modin[ray]) (2026.1.0)
Requirement already satisfied: psutil>=5.8.0 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from modin[ray]) (7.2.1)
Requirement already satisfied: typing-extensions in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from modin[ray]) (4.15.0)
Collecting ray<3,>=2.10.0 (from modin[ray])
  Downloading ray-2.53.0-cp311-cp311-macosx_12_0_arm64.whl.metadata (22 kB)
Requirement already satisfied: pyarrow>=10.0.1 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from modin[ray]) (23.0.0)
Requirement already satisfied: python-dateutil>=2.8.2 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from pandas<2.4,>=2.2->modin[ray]) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from pandas<2.4,>=2.2->modin[ray]) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from pandas<2.4,>=2.2->modin[ray]) (2025.3)
Requirement already satisfied: click>=7.0 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from ray<3,>=2.10.0->modin[ray]) (8.3.1)
Collecting filelock (from ray<3,>=2.10.0->modin[ray])
  Downloading filelock-3.20.3-py3-none-any.whl.metadata (2.1 kB)
Collecting jsonschema (from ray<3,>=2.10.0->modin[ray])
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting msgpack<2.0.0,>=1.0.0 (from ray<3,>=2.10.0->modin[ray])
  Downloading msgpack-1.1.2-cp311-cp311-macosx_11_0_arm64.whl.metadata (8.1 kB)
Collecting protobuf>=3.20.3 (from ray<3,>=2.10.0->modin[ray])
  Downloading protobuf-6.33.4-cp39-abi3-macosx_10_9_universal2.whl.metadata (593 bytes)
Requirement already satisfied: pyyaml in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from ray<3,>=2.10.0->modin[ray]) (6.0.3)
Collecting requests (from ray<3,>=2.10.0->modin[ray])
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Requirement already satisfied: six>=1.5 in ./.pyenv/versions/3.11.8/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas<2.4,>=2.2->modin[ray]) (1.17.0)
Collecting attrs>=22.2.0 (from jsonschema->ray<3,>=2.10.0->modin[ray])
  Downloading attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema->ray<3,>=2.10.0->modin[ray])
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema->ray<3,>=2.10.0->modin[ray])
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema->ray<3,>=2.10.0->modin[ray])
  Downloading rpds_py-0.30.0-cp311-cp311-macosx_11_0_arm64.whl.metadata (4.1 kB)
Collecting charset_normalizer<4,>=2 (from requests->ray<3,>=2.10.0->modin[ray])
  Downloading charset_normalizer-3.4.4-cp311-cp311-macosx_10_9_universal2.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests->ray<3,>=2.10.0->modin[ray])
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests->ray<3,>=2.10.0->modin[ray])
  Using cached urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2017.4.17 (from requests->ray<3,>=2.10.0->modin[ray])
  Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
Downloading ray-2.53.0-cp311-cp311-macosx_12_0_arm64.whl (69.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 69.5/69.5 MB 68.4 MB/s  0:00:01
Downloading msgpack-1.1.2-cp311-cp311-macosx_11_0_arm64.whl (84 kB)
Downloading protobuf-6.33.4-cp39-abi3-macosx_10_9_universal2.whl (427 kB)
Downloading filelock-3.20.3-py3-none-any.whl (16 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading attrs-25.4.0-py3-none-any.whl (67 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading rpds_py-0.30.0-cp311-cp311-macosx_11_0_arm64.whl (359 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.4-cp311-cp311-macosx_10_9_universal2.whl (206 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
Installing collected packages: urllib3, rpds-py, protobuf, msgpack, idna, filelock, charset_normalizer, certifi, attrs, requests, referencing, jsonschema-specifications, jsonschema, ray
Successfully installed attrs-25.4.0 certifi-2026.1.4 charset_normalizer-3.4.4 filelock-3.20.3 idna-3.11 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 msgpack-1.1.2 protobuf-6.33.4 ray-2.53.0 referencing-0.37.0 requests-2.32.5 rpds-py-0.30.0 urllib3-2.6.3
kojofrimpong@Kojo--MacBook-Pro ~ % exit()
function> python3
kojofrimpong@Kojo--MacBook-Pro ~ % python3
Python 3.11.8 (main, Jan 18 2026, 19:11:58) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import time
>>> import modin.pandas as mpd
>>> start = time.time()
>>> df_modin = mpd.read_csv(DATA_PATH)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'DATA_PATH' is not defined
>>> df_modin.head()   # forces execution
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df_modin' is not defined
>>> modin_time = time.time() - start
>>> 
>>> print("Modin load time:", modin_time)
Modin load time: 0.0021250247955322266

