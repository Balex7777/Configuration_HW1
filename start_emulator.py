import json
import tarfile
import os
import platform
import time


def load_config(config_file):
    with open(config_file) as f:
        config = json.load(f)
    return config["hostname"], config["filesystem_path"], config["startup_script"]


def extract_filesystem(tar_path, extract_to="/tmp/virtual_fs"):
    with tarfile.open(tar_path, 'r') as tar:
        tar.extractall(extract_to)
    return extract_to


class ShellEmulator:
    def __init__(self, hostname, root_dir):
        self.hostname = hostname
        self.current_dir = root_dir
        self.start_time = time.time()

    def ls(self):
        return os.listdir(self.current_dir)

    def cd(self, path):
        if path == "..":
            new_dir = os.path.dirname(self.current_dir)
        else:
            new_dir = os.path.join(self.current_dir, path)

        if os.path.isdir(new_dir):
            self.current_dir = new_dir
        else:
            print(f"Нет такого каталога: {path}")

    def uptime(self):
        return time.time() - self.start_time

    def uname(self):
        return platform.system()

    def prompt(self):
        return f"{self.hostname}:{self.current_dir}$ "

    def exit(self):
        print("Выход...")
        exit(0)


def run_shell(config_file):
    hostname, fs_path, startup_script = load_config(config_file)
    root_dir = extract_filesystem(fs_path)

    shell = ShellEmulator(hostname, root_dir)

    # Выполняем стартовый скрипт (если есть)
    if os.path.exists(startup_script):
        with open(startup_script) as f:
            for line in f:
                run_command(shell, line.strip())

    # Основной цикл командной строки
    while True:
        command = input(shell.prompt())
        run_command(shell, command)


def run_command(shell, command):
    if command == "ls":
        print("\n".join(shell.ls()))
    elif command.startswith("cd"):
        _, path = command.split(maxsplit=1)
        shell.cd(path)
    elif command == "uptime":
        print(f"Uptime: {shell.uptime():.2f} секунд")
    elif command == "uname":
        print(shell.uname())
    elif command == "exit":
        shell.exit()
    else:
        print(f"Команда не найдена: {command}")


if __name__ == "__main__":
    run_shell("config.json")

