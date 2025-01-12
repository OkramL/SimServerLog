import time
import random
from datetime import datetime
from faker import Faker
import os
import shutil

# Logifaili ja kausta nimi
LOG_DIR = "C:\\Temp"
LOG_FILE = os.path.join(LOG_DIR, "application.log")
# Maksimaalne failisuurus baitides
FILE_SIZE = 10 * 1024  # 10 KB

# Näidistegevused logimiseks
ACTIONS = [
    "User logged in",
    "User logged out",
    "File uploaded",
    "File downloaded",
    "Email sent",
    "Email received",
    "Error: Invalid password",
    "Error: File not found",
    "Session expired",
    "Database connection established",
    "Database connection lost",
    "New user registered",
    "System update initiated",
    "System rebooted",
    "User password changed",
    "User profile updated",
    "Admin privileges granted",
    "Login attempt failed",
    "New device connected",
    "Service started",
    "Service stopped",
    "Backup created",
    "Backup restored",
    "Configuration file updated",
    "Notification sent",
    "Notification received",
]

# Levinud teenuste ja seadmete nimed
SERVICES = [
    "apache", "mysql", "ssh", "nginx", "web", "ftp", "redis",
    "lighttpd", "tomcat", "mariadb", "postgresql", "mongodb",
    "cassandra", "bind9", "dhcpd", "openvpn", "ipsec",
    "postfix", "sendmail", "exim", "dovecot", "spamassassin",
    "cron", "rsyslog", "journalctl", "auditd", "docker",
    "kubelet", "libvirtd", "qemu-kvm", "cups", "bluetoothd",
    "network-manager", "firewalld", "ntpd"
]
DEVICES = ["USB drive", "SD card", "SSD drive", "External HDD", "Bluetooth device", "WiFi adapter"]

# Faker objekt andmete genereerimiseks
faker = Faker()


def setup_log_directory():
    """Loo logikaust ja eemalda vanad logid."""
    if os.path.exists(LOG_DIR):
        shutil.rmtree(LOG_DIR)  # Kustuta vana kaust ja failid
    os.makedirs(LOG_DIR)  # Loo uus kaust


def generate_log_entry():
    """Genereerib ühe logikirje kuupäeva, kellaaja ja juhusliku tegevusega."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    action = random.choice(ACTIONS)

    # Lisa konteksti tegevuse kohta
    if "user" in action.lower():
        detail = faker.user_name()
    elif "file" in action.lower():
        detail = faker.file_name()
    elif "email" in action.lower():
        detail = faker.email()
    elif "database" in action.lower():
        detail = faker.first_name()
    elif "system" in action.lower():
        detail = faker.hostname()
    elif "service" in action.lower():
        detail = random.choice(SERVICES)
    elif "device" in action.lower():
        detail = random.choice(DEVICES)
    elif "notification" in action.lower():
        detail = faker.sentence(nb_words=3)
    elif "backup" in action.lower():
        detail = faker.file_path(depth=2)
    elif "configuration" in action.lower():
        detail = faker.file_name(extension="cfg")
    elif "admin privileges granted" in action.lower():
        detail = faker.user_name()
    elif "invalid password" in action.lower():
        detail = faker.user_name()
    else:
        detail = "N/A"

    return f"[{timestamp}] {action} - {detail}"


def rotate_logs():
    """Nimetab logifaili ümber vastavalt rotatsiooniskeemile (1-9)."""
    for i in range(9, 0, -1):
        old_file = os.path.join(LOG_DIR, f"application.log.{i}")
        new_file = os.path.join(LOG_DIR, f"application.log.{i + 1}")
        if os.path.exists(new_file):
            os.remove(new_file)  # Eemalda olemasolev fail enne ümbernimetamist
        if os.path.exists(old_file):
            os.rename(old_file, new_file)

    # Nimeta praegune logifail ümber application.log.1
    if os.path.exists(LOG_FILE):
        first_log = os.path.join(LOG_DIR, "application.log.1")
        if os.path.exists(first_log):
            os.remove(first_log)  # Eemalda olemasolev application.log.1
        os.rename(LOG_FILE, first_log)


def write_log_to_file(entry):
    """Kirjutab logikirje faili."""
    # Kontrolli faili suurust
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > FILE_SIZE:
        rotate_logs()

    # Kirjuta uus logikirje faili
    with open(LOG_FILE, "a") as log_file:
        log_file.write(entry + "\n")


def main():
    """Käivitab logide genereerimise tsüklis juhuslike pausidega."""
    setup_log_directory()
    print(f"Logimine algas. Kirjutatakse faili: {LOG_FILE}")
    while True:
        # Genereeri ja kirjuta logikirje
        log_entry = generate_log_entry()
        print(log_entry)
        write_log_to_file(log_entry)

        # Tee juhuslik paus (1 kuni 5 sekundit)
        time.sleep(random.randint(1, 5))


if __name__ == "__main__":
    main()
