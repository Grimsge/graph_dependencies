import os #проверка существования config.xml
import xml.etree.ElementTree as ET #для чтения xml
import urllib.request
import urllib.error #для чтения ссылки

def read_xml(): #Этап1 -проверка существования файла config, чтение этого файла, заполнение словаря.
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
    
def extract_section_with_braces(content, start_pos): #Этап2 - извлечение секции зависимостей с учетом фигурных скобок
    result = []
    brace_count = 0
    in_section = False
    
    lines = content[start_pos:].split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        
        if not in_section and stripped_line == "[dependencies]":
            in_section = True
            result.append(line)
            continue
            
        if in_section:
            brace_count += line.count('{')
            brace_count -= line.count('}')
            
            if stripped_line.startswith('[') and brace_count == 0:
                break
                
            result.append(line)
    
    return '\n'.join(result)

def dependencies_find(cargo_content): #Этап2 - поиск и вывод секции зависимостей

    deps_start = cargo_content.find("[dependencies]")
    if deps_start != -1:
        #print("*Секция [dependencies] найдена!")
        deps_content = extract_section_with_braces(cargo_content, deps_start)
        print("---Прямые зависимости пакета:")
        print(deps_content)
    else:
        print("Секция [dependencies] не найдена")


      
def url_raw_maker(repo_url): #Этап2 - создание raw ссылки на toml файл
    possible_urls = [
        repo_url.replace("github.com", "raw.githubusercontent.com") + "/main/Cargo.toml",
        repo_url.replace("github.com", "raw.githubusercontent.com") + "/master/Cargo.toml",
    ]
    
    for test_url in possible_urls:
        try:
            with urllib.request.urlopen(test_url) as response:
                if response.getcode() == 200:
                    #print("Cargo.toml найден")
                    return test_url
        except:
            continue
    
    default_url = possible_urls[0]
    print(f"Используем: {default_url}")
    return default_url
def download_cargo_toml(raw_url): #Этап2 - чтение файла toml
    try:
        with urllib.request.urlopen(raw_url) as response:
            cargo_content = response.read().decode('utf-8')
            return cargo_content
    except urllib.error.URLError as e:
        print(f"Ошибка загрузки: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None
    
def analyser(config): #Этап2 -анализ репозитория
    repo_url = config["repository_url"]
    #print(f"Анализ репозитория: {repo_url}")
    
    raw_url = url_raw_maker(repo_url)
    print(f"Raw URL: {raw_url}") 
    
    cargo_content = download_cargo_toml(raw_url)
    if cargo_content is None:
        print("Файл Cargo.toml не был прочитан")
        return None
    else:
        #print("Cargo.toml успешно загружен")
        return cargo_content

def main(): #Основная функция программы
    config = read_xml()
    if config:
        print("*Конфигурационный файл прочитан")
        for key, value in config.items():
            print(f"{key}: {value}")
    else:
        print("Ошибка чтения конфигурации")
        return
        
    cargo_content = analyser(config)
    if cargo_content is None:
        return
    else:
        dependencies_find(cargo_content)
    
if __name__ == "__main__": #Точка входа в программу
    main()