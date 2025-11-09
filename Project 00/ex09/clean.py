import os


def uninstall():
    os.system("pip3 uninstall ft_package")
    os.system("rm -rf build")
    os.system("rm -rf dist")
    os.system("rm -rf ft_package.egg-info")
    os.system("rm -rf ft_package/__pycache__")


if __name__ == "__main__":
    uninstall()
