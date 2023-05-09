import subprocess

def update_package_list():
    print("Updating package list...")
    subprocess.run(["sudo", "apt-get", "update"], check=True)

def upgrade_packages():
    print("Upgrading packages...")
    subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)

def clean_up():
    print("Cleaning up...")
    subprocess.run(["sudo", "apt-get", "autoremove", "-y"], check=True)

def main():
    update_package_list()
    upgrade_packages()
    clean_up()
    print("Patches installed successfully.")

if __name__ == "__main__":
    main()
