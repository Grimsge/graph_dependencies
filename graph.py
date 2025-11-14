import os 
import xml.etree.ElementTree as ET

def read_xml():
    try:
        if not os.path.exists("config.xml"):
            print("файл config.xml не найден")
            return None
    
        tree = ET.parse("config.xml")
        root = tree.getroot()
        config = {}
        
        package_name_elem = root.find("package_name")
        if package_name_elem is None:
            print("Ошибка: тег package_name отсутствует")
        else:
            config["package_name"] = package_name_elem.text
            
        repository_url_elem = root.find("repository_url")
        if repository_url_elem is None:
            print("Ошибка: тег repository_url отсутствует")
        else:
            config["repository_url"] = repository_url_elem.text
            
        test_repo_mode_elem = root.find("test_repo_mode")
        if test_repo_mode_elem is None:
            print("Ошибка: тег test_repo_mode отсутствует")
        else:
            config["test_repo_mode"] = test_repo_mode_elem.text
            
        package_version_elem = root.find("package_version")
        if package_version_elem is None:
            print("Ошибка: тег package_version отсутствует")
        else:
            config["package_version"] = package_version_elem.text
            
        output_filename_elem = root.find("output_filename")
        if output_filename_elem is None:
            print("Ошибка: тег output_filename отсутствует")
        else:
            config["output_filename"] = output_filename_elem.text
            
        return config
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def main():
    config = read_xml()
    if config:
        print("*Конфигурационный файл прочитан")
        for key, value in config.items():
            print(f"{key}: {value}")
    else:
        print("Ошибка чтения")

if __name__ == "__main__":
    main()