import os


def black_all_py_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                full_file_path = os.path.join(root, file)
                os.system(f"black {full_file_path}")


if __name__ == "__main__":
    black_all_py_files()
