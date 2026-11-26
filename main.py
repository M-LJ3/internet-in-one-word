import os

def main():
    word = "Doomscrolling"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)

if __name__ == "__main__":
    main()
