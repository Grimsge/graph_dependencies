# Инструмент визуализации графа зависимостей

## Этап 1: Минимальный прототип с конфигурацией
## Этап 2: Вывод прямых зависимостей пакета, используя ссылку на репозиторий

### Описание
CLI-приложение для чтения конфигурации из XML файла и вывода прямых зависимостей пакета.

### Использование
1. Создайте файл `config.xml` в той же папке
2. Заполните его по примеру ниже
3. Запустите: `python graph.py`

### Пример config.xml
```xml
<?xml version="1.0" ?>
<configuration>
    <package_name>name</package_name>
    <repository_url>https://url</repository_url>
    <test_repo_mode>false_or_true</test_repo_mode>
    <package_version>1.0</package_version>
    <output_filename>my_graph.png</output_filename>
</configuration>

работающие примеры:
<configuration>
    <package_name>clap</package_name>
    <repository_url>https://github.com/clap-rs/clap</repository_url>
    <test_repo_mode>false</test_repo_mode>
    <package_version>4.0.0</package_version>
    <output_filename>clap_deps.png</output_filename>
</configuration>

<configuration>
    <package_name>mypkg</package_name>
    <repository_url>https://github.com/rust-lang/rustfmt</repository_url>
    <test_repo_mode>false</test_repo_mode>
    <package_version>1.0.0</package_version>
    <output_filename>rustfmt_dependencies.png</output_filename>
</configuration>