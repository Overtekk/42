import os

filename = "standard_archive.txt"
print(f"Creating {filename}")
with open(filename, "w", encoding="utf-8") as file:
        file.write("Knowledge preserved for humanity")

filename = "corrupted_archive.txt"
print(f"Creating {filename}")
with open(filename, "wb") as file:
        file.write(b"System Start... \xff ...CRITICAL FAILURE")

filename = "classified_vault.txt"
print(f"Creating {filename}...")
with open(filename, "w", encoding="utf-8") as file:
    file.write("[CLASSIFIED] Chocolate do not exist.")
os.chmod(filename, 0o000)

dirname = "folder"
empty_filename = os.path.join(dirname, "empty.txt")
print(f"Creating folder '{dirname}' with empty file...")
if not os.path.exists(dirname):
        os.mkdir(dirname)
with open(empty_filename, "w", encoding="utf-8") as file:
        pass

if os.path.exists("lost_archive.txt"):
    os.remove("lost_archive.txt")
    print("Removing 'lost_archive.txt' to simulate missing file...")

print("\nGeneration complete.")
