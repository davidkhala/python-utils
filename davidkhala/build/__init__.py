import subprocess


class Installer:
    def __init__(self, out_dir, source_py: str):
        self.options = [
            '--distpath', out_dir, '--specpath', out_dir,
            "--onefile", source_py
        ]
        self.build = lambda: subprocess.run(["pyinstaller", *self.options])
        self.clean = lambda: subprocess.run(["pyinstaller", "--clean", *self.options])
