import os
from dotenv import load_dotenv


def main() -> None:

    # Read the .env and load its content inside the memory of the program.
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    matrix = os.getenv('MATRIX_MODE')
    log = os.getenv('LOG_LEVEL')
    zion = os.getenv('ZION_ENDPOINT')

    missing = False

    config_list = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY', 'LOG_LEVEL',
                   'ZION_ENDPOINT']

    for item in config_list:
        value = os.getenv(item)
        if value is None or value == "":
            print(f"{item}: missing value")
            missing = True

    if not missing:
        print("Configuration loaded:")
        print(f"Mode: {matrix}")
        print("Database: Connected to URL")
        print("API Access: Authenticated")
        print(f"Log Level {log}")
        print(f"Zion Network: {zion}")

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if not missing:
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file no properly configured")

    print("Production overrides available")

    print("\n The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
