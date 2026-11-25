import os

LINE = "My agent burned 40,000 tokens and three subagents to confidently report 'done' on a file it never opened, then apologized to itself for the delay."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
