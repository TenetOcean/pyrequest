# pyrequest Web 接口 自动化项目

### 框架和库
Requests + Pytest + Pytest_html + SqlSever


### 特点

* 测试数据参数化。

### 安装

```shell
$ pip install -r requirements.txt
```

注：安装```requirements.txt```指定依赖库的版本，这是经过测试的，有时候新的版本可会有错。

### 配置

在 `config.py` 文件配置

```python
class RunConfig:
   
    # 运行测试用例的目录或文件
    cases_path = "./test_interface/"
```

### 框架解析
test_interface文件夹存放测试用例
test_report文件夹存放测试报告
db_fixture文件夹存放初始化数据库数据