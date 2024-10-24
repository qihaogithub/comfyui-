import os
from collections import defaultdict

def get_requirements(plugin_directory):
    """
    获取插件目录下的requirements.txt文件中的依赖名称
    
    :param plugin_directory: 插件目录的完整路径
    :return: 依赖名称列表
    """
    requirements_file = os.path.join(plugin_directory, 'requirements.txt')
    if os.path.exists(requirements_file):
        with open(requirements_file, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    return []

def get_installed_plugins(directory):
    """
    获取指定目录下所有文件夹的名称（即插件名称）
    
    :param directory: 插件目录的完整路径
    :return: 插件名称及其依赖名称的字典
    """
    plugins = {}
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            requirements = get_requirements(item_path)
            plugins[item] = requirements
    return plugins

def main():
    plugin_directory = r"E:\ComfyUI-aki\ComfyUI-aki-v1.3\custom_nodes"
    
    if os.path.exists(plugin_directory):
        plugins = get_installed_plugins(plugin_directory)
        print("已安装的插件及其依赖列表：")
        
        # 反向收集依赖与插件的关系
        dependency_map = defaultdict(list)
        for plugin, requirements in plugins.items():
            for req in requirements:
                dependency_map[req].append(plugin)

        # 保存依赖列表到文件
        with open("所需依赖.txt", 'w', encoding='utf-8') as req_file:
            for req, plugin_list in dependency_map.items():
                req_file.write(f"{req}:\n")
                for plugin in plugin_list:
                    req_file.write(f"  - {plugin}\n")
                req_file.write("\n")  # 添加空行以分隔不同依赖

        print(f"\n共找到 {len(plugins)} 个插件，依赖列表已保存到 '所需依赖.txt'。")
    else:
        print("指定的插件目录不存在，请检查路径是否正确。")

if __name__ == "__main__":
    main()
