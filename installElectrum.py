import os
import sys
import shutil
import platform
import subprocess
try:
    import libsecp256k1_0
except ImportError:
    print("Please install the libraries listed in requirements.txt.")
    sys.exit(1)

try:
    subprocess.run(["git", "--version"], check=True,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    print("Git is not installed.")
    sys.exit(1)

VERSION = "4.4.4"

os.system(
    f"git clone -b {VERSION} --depth 1 https://github.com/spesmilo/electrum")

if sys.platform in ('windows', 'win32') and platform.architecture()[0] == '32bit':
    library_paths = (libsecp256k1_0.Libsecp256k1.win32bit(),
                     'libsecp256k1-0.dll')
elif sys.platform in ('windows', 'win32') and platform.architecture()[0] == '64bit':
    library_paths = (libsecp256k1_0.Libsecp256k1.win64bit(),
                     'libsecp256k1-0.dll')
elif sys.platform in ('darwin'):
    library_paths = (libsecp256k1_0.Libsecp256k1.darwin(),
                     'libsecp256k1.0.dylib')
else:
    library_paths = (libsecp256k1_0.Libsecp256k1.unix(), 'libsecp256k1.so.0')

shutil.copy(library_paths[0], f"./electrum/electrum/{library_paths[1]}")

lines_to_remove = [
    "exclude electrum/*.so\n",
    "exclude electrum/*.so.0\n",
    "exclude electrum/*.dll\n",
    "exclude electrum/*.dylib\n"
]


with open("electrum/MANIFEST.in", "r+") as file:
    lines = file.readlines()
    file.seek(0)
    file.writelines(line for line in lines if line not in lines_to_remove)
    file.truncate()


os.system('pip install "./electrum[crypto]"')


def remove_directory(path):
    def onerror(func, path, exc_info):
        os.chmod(path, 0o755)
        func(path)

    try:
        shutil.rmtree(path, onerror=onerror)
        print(f"{path} and all its files have been removed successfully.")
    except FileNotFoundError:
        print(f"{path} does not exist.")
    except Exception as e:
        print(f"An error occurred while removing {path}: {e}")


# Call the function to remove the electrum folder
remove_directory('./electrum')
