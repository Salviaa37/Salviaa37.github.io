Title: 一种更方便的Win Py ML开发环境配置
Date: 2025-09-09
Category: Review



OS：Windows 
Python发行版：Python （Microsoft Store）
虚拟环境管理：uv
IDE：Visual Studio Code 
GPU：Nvidia RTX 40xx

# 环境配置
## 安装Python
打开Microsoft Store搜索Python，可以看到Microsoft Store提供了不同版本的Python，选最新的下载。
一般来说，Python版本越新，性能越提升。

最新为3.13
3.13
https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=neutral&gl=US&ocid=pdpshare

3.9
https://apps.microsoft.com/detail/9P7QFQMJRFP7?hl=neutral&gl=US&ocid=pdpshare

## 检测安装情况
```powershell
PS C:\Users\xxx\Cpp_Projects> pip -V
pip 25.0.1 from C:\Users\xxx\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\pip (python 3.13)
```
如此则安装成功。





## 安装uv
使用uv作为虚拟环境管理器。
[uv 中文文档](https://uv.doczh.com/)
### **安装**
```shell
pip install uv
```

### **创建环境**
```
uv init
```


## 更换镜像服务器
使用国内（CERNET）的镜像服务器可以提高下载软件包速度。
参照下面的网页中指导操作。
[PyPI 软件仓库镜像使用帮助 - MirrorZ Help](https://help.mirrors.cernet.edu.cn/pypi/)

pip
```shell
python -m pip install --upgrade pip
pip config set global.index-url https://mirrors.cernet.edu.cn/pypi/web/simple
```

uv
uv不能直接通过命令行修改配置，需要在 `~/.config/uv/uv.toml` 或者 `/etc/uv/uv.toml` 填写下面的内容
```shell
[[index]]
url = "https://mirrors.cernet.edu.cn/pypi/web/simple"
default = true
```

## 安装Pytorch
这里我们安装cuda版本的Pytorch。

### 检查显卡CUDA版本
查看显卡驱动的cuda版本
```powershell
nvidia-smi    
```
命令行终端显示出的`CUDA version: 12.9`即为CUDA版本，安装的Pytorch包应当不高于这个版本。

Pytorch默认用pip安装，但是其安装索引不固定是Pypi，而是根据平台和加速类型（cpu、gpu）指定不同的安装索引。
如果直接使用`uv add`命令安装
```shell
uv add torch torchvision
```
只会默认安装Pypi索引版本的torch，这个版本不支持cuda。

### 集成Pytorch到uv
如果需要集成Pytorch索引到uv配置，需要向项目配置文件`pyproject.toml`（）中写入以下内容。
这里以 CUDA 12.9版本为例，并参考了官方文档。[Using uv with PyTorch | uv](https://docs.astral.sh/uv/guides/integration/pytorch/#installing-pytorch)

添加需要的包到依赖项
```toml
[project]
name = "uvproject"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "torch>=2.7.0", 
    "torchvision>=0.22.0", 
]
```

添加你需要的安装版本索引到
```toml
[[tool.uv.index]]
name = "pytorch-cu129"
url = "https://download.pytorch.org/whl/cu129"
explicit = true
```

指定包来源
```toml
[tool.uv.sources]
torch = [
  { index = "pytorch-cu129", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
]
torchvision = [
  { index = "pytorch-cu129", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
]
```

通过uv运行pip安装Pytorch
Pytorch具体命令详见官方网站[Pytorch Get Started](https://pytorch.org/get-started/locally/)
```shell
$ uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
```




等待Pytorch下载安装完成。

## 测试安装情况
Pytorch安装完成后，需要测试其是否与CUDA成功连接。
```python
import torch
print(torch.cuda.is_available())
print(torch.__version__)
```
第一行输出为`True`，第二行输出为`2.x.x+cu12x`，表明cuda可以连接上Pytorch，至此安装成功。


# Issue

不可以混用uv add和pip install语法。
比如下面的↓命令。
```powershell
PS C:\> uv add torch torchvision --index-url https://download.pytorch.org/whl/cu129        

```

会安装失败，可能因为uv没有pip编译wheel的能力。
```powershell
warning: Indexes specified via `--index-url` will not be persisted to the `pyproject.toml` file; use `--default-index` instead.
Resolved 30 packages in 3.12s
error: Distribution `markupsafe==3.0.2 @ registry+https://download.pytorch.org/whl/cu129` can't be installed because it doesn't have a source distribution or wheel for the current platform

hint: You're on Windows (`win_amd64`), but `markupsafe` (v3.0.2) only has wheels for the following platforms: `manylinux_2_17_x86_64`, `manylinux2014_x86_64`; consider adding your platform to `tool.uv.required-environments` to ensure uv resolves to a version with compatible wheels
```

解决办法是使用uv的pip接口，语法
```
uv pip install ....
```
如果原来的命令是pip3，也要替换成pip。




# 命令速查
### pip
```
# 安装&更新
pip install package_name
pip install --upgrade package_name
# 从指定文件安装包
pip install -r requirements.txt

# 卸载
pip uninstall package_name

# 列出
pip list

# 列出未更新
pip list --outdated

# 搜索
pip search package_name

# 清除缓存
pip cache purge

# 更新pip
python.exe -m pip install --upgrade pip

# 指定软件包服务器
pip install -i https://mirrors.cernet.edu.cn/pypi/web/simple some-package
```


### uv
```powershell
# 创建虚拟环境
uv init

# 同步配置文件，更新环境
uv sync

# 向当前虚拟环境添加包
uv add package_name

# 移除当前虚拟环境的包
uv remove package_name

# 展示当前环境的包依赖关系树
uv tree
```

文档
[uv](https://docs.astral.sh/uv/)
[uv 中文文档](https://uv.doczh.com/)

# 其他
## pip修改配置文件
### Linux / macOS
配置文件的位置在 `~/.pip/pip.conf`（如不存在，创建该目录和文件）：
打开配置文件 `~/.pip/pip.conf`，修改内容如下：
```
[global]index-url = https://pypi.tuna.tsinghua.edu.cn/simple[install]trusted-host = https://pypi.tuna.tsinghua.edu.cn
```
### Windows
在当前用户目录下（`C:/Users/xxx/`，xxx是你的用户名）创建一个 pip.ini文件，文件中输入上述内容。
查看镜像地址修改状态
```
$ pip3 config listglobal.index-url='https://pypi.tuna.tsinghua.edu.cn/simple'install.trusted-host='https://pypi.tuna.tsinghua.edu.cn'
```






---
（全文完）
