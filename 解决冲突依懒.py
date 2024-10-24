import yaml
from collections import defaultdict
from packaging.version import parse

# 读取依赖文件
with open('所需依赖.txt', 'r', encoding='utf-8') as file:
    dependencies = yaml.safe_load(file)

# 用于存储依赖和版本
dependency_map = defaultdict(set)

# 遍历依赖，收集版本信息
for package, versions in dependencies.items():
    for version in versions:
        dependency_map[package].add(version)

# 生成兼容的依赖列表
compatible_dependencies = {}
for package, versions in dependency_map.items():
    # 选择最新的版本
    latest_version = max(versions, key=parse)
    compatible_dependencies[package] = latest_version

# 输出兼容的依赖列表为 requirements.txt 格式
with open('兼容依赖列表.txt', 'w', encoding='utf-8') as file:
    for package, version in compatible_dependencies.items():
        file.write(f"{package}{version}\n")  # 格式化为 requirements.txt 格式

print("兼容依赖列表已生成：兼容依赖列表.txt")
