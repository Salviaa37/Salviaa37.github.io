Date: 2025-03-04 
Title: WSL的备份和迁移



## 解决的问题

1.需要把WSL迁移到其他电脑上工作。 
2.默认情况下WSL安装位置在系统盘，系统盘容量不足。 
3.像使用虚拟机软件一样备份你正在使用的WSL系统。

## 步骤

下面的命令都在Powershell里面执行。 开始之前你需要先记下**需要迁移的WSL系统的用户名**。

### 查看需要迁移的WSL是否在运行

```
wsl -l -v
#   NAME      STATE           VERSION
# * Debian    Running         2
```

### 终止WSL运行

两条命令都可以，任选其一。

```
wsl --shutdown 
# 立即终止所有正在运行的分发和 WSL 2 轻型虚拟机。

wsl -t <DistributionName>
# 终止指定分发。
```

### 导出

将WSL系统导出到指定目录，得到一个tar格式的归档。
注意：指定目录，也就是<FileName>字段，需要给出导出的归档文件名称，只给出目录位置会报错。

```python
wsl 
```

```
wsl --export <Distro> <FileName> [Options]
# 将指定的 tar 导入为新分发。
# 对于标准输入，文件名可以是“-”。

#example 
wsl --export Debian D:\export_Debian.tar
```

### 注销原系统

根据你的需要自行选择是否注销原来的WSL。

```
wsl --unregister <Distro>
# 注销分发并删除根文件系统。

#example
wsl --unregister Debian
```

### 导入

将导出的WSL系统导入到指定位置，需要等待一段时间。

```
wsl --import <Distro> <InstallLocation> <FileName> [Options]
# 将指定的 tar 导入为新分发。
# 对于标准输入，文件名可以是“-”。

#example
wsl --import Debian_2 D:\wsl\Debian\ D:\export_Debian.tar
```

在安装目录看到了一个vhdx文件，导入成功。 
![image.jpg](https://cdn.nlark.com/yuque/0/2024/jpeg/27527519/1724067201109-d2e3839d-48e9-4392-b975-3b5f7a5f3dbc.jpeg#clientId=ufefb1a36-1659-4&from=paste&height=236&id=u69f4b817&originHeight=236&originWidth=777&originalType=url&ratio=1&rotation=0&showTitle=false&size=17812&status=done&style=none&taskId=u72f21c67-e075-4861-b154-ca1bbd1ad21&title=&width=777)

### 设置登录用户

新还原的WSL系统的默认用户会变成root，不能使用原来安装的软件，必须修改默认用户。

```
Debian.exe config --default-user <username>
```

把Debian.exe 替换为你使用WSL分发版执行文件名称，如ubuntu2204.exe等等。 username是原来WSL系统的用户名。 重新启动新的WSL系统，你就可以继续使用了。

## 其他

### 设置默认发行版

要设置与 wsl 命令一起使用的默认 Linux 发行版，请输入 

```
wsl -s <Distro>
# 将 <Distro> 替换为要使用的分发名称。
```

例如，从 PowerShell/CMD 输入 `wsl -s` Debian，将默认发行版设置为 Debian。 现在从 Powershell 运行 `wsl npm init` 将在 Debian 中运行 npm init 命令。 要在 PowerShell 或 Windows 命令提示符下运行特定的 WSL 发行版而不更改默认发行版，请使用命令 `wsl -d` ，将 替换为要使用的发行版的名称。

### 删除导出的归档文件

### Ref

## 解决的问题

1.需要把WSL迁移到其他电脑上工作。 
2.默认情况下WSL安装位置在系统盘，系统盘容量不足。 
3.像使用虚拟机软件一样备份你正在使用的WSL系统。

## 步骤

下面的命令都在Powershell里面执行。 开始之前你需要先记下**需要迁移的WSL系统的用户名**。

### 查看需要迁移的WSL是否在运行

```
wsl -l -v
#   NAME      STATE           VERSION
# * Debian    Running         2
```

### 终止WSL运行

两条命令都可以，任选其一。

```
wsl --shutdown 
# 立即终止所有正在运行的分发和 WSL 2 轻型虚拟机。

wsl -t <DistributionName>
# 终止指定分发。
```

### 导出

将WSL系统导出到指定目录，得到一个tar格式的归档。
注意：指定目录，也就是<FileName>字段，需要给出导出的归档文件名称，只给出目录位置会报错。

```
wsl --export <Distro> <FileName> [Options]
# 将指定的 tar 导入为新分发。
# 对于标准输入，文件名可以是“-”。

#example 
wsl --export Debian D:\export_Debian.tar
```

### 注销原系统

根据你的需要自行选择是否注销原来的WSL。

```
wsl --unregister <Distro>
# 注销分发并删除根文件系统。

#example
wsl --unregister Debian
```

### 导入

将导出的WSL系统导入到指定位置，需要等待一段时间。

```
wsl --import <Distro> <InstallLocation> <FileName> [Options]
# 将指定的 tar 导入为新分发。
# 对于标准输入，文件名可以是“-”。

#example
wsl --import Debian_2 D:\wsl\Debian\ D:\export_Debian.tar
```

在安装目录看到了一个vhdx文件，导入成功。 
![image.jpg](https://cdn.nlark.com/yuque/0/2024/jpeg/27527519/1724067293526-27bfeea3-ba0b-4804-8ad5-c7064fb43d88.jpeg#clientId=ufefb1a36-1659-4&from=paste&height=236&id=u4982a36a&originHeight=236&originWidth=777&originalType=url&ratio=1&rotation=0&showTitle=false&size=17812&status=done&style=none&taskId=uf3dafa13-cd99-4e89-8840-e0f7364d6c5&title=&width=777)

### 设置登录用户

新还原的WSL系统的默认用户会变成root，不能使用原来安装的软件，必须修改默认用户。

```
Debian.exe config --default-user <username>
```

把Debian.exe 替换为你使用WSL分发版执行文件名称，如ubuntu2204.exe等等。 username是原来WSL系统的用户名。 重新启动新的WSL系统，你就可以继续使用了。

## 其他

### 设置默认发行版

要设置与 wsl 命令一起使用的默认 Linux 发行版，请输入 

```
wsl -s <Distro>
# 将 <Distro> 替换为要使用的分发名称。
```

例如，从 PowerShell/CMD 输入 `wsl -s` Debian，将默认发行版设置为 Debian。 现在从 Powershell 运行 `wsl npm init` 将在 Debian 中运行 npm init 命令。 要在 PowerShell 或 Windows 命令提示符下运行特定的 WSL 发行版而不更改默认发行版，请使用命令 `wsl -d` ，将 替换为要使用的发行版的名称。

### 删除导出的归档文件

### Ref

> 来自: [WSL的备份和迁移 - 知乎](https://zhuanlan.zhihu.com/p/622706723)
