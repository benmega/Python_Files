import os
from tkinter.filedialog import askdirectory


def make_folder_skeleton_copy(source_dir: str, target_dir: str, skeleton_name: str) -> str:
    """
    Create a skeleton copy of the first-level subfolders from source_dir
    into target_dir/skeleton_name.

    Parameters
    ----------
    source_dir : str
        Path to the original directory.
    target_dir : str
        Path to the location where the skeleton copy will be created.
    skeleton_name : str
        Name of the new skeleton directory.

    Returns
    -------
    str
        Path to the created skeleton root directory.
    """
    skeleton_root = os.path.join(target_dir, skeleton_name)
    subfolders = next(os.walk(source_dir))[1]

    for sub in subfolders:
        os.makedirs(os.path.join(skeleton_root, sub), exist_ok=True)

    return skeleton_root


def run_skeleton_copy() -> None:
    """
    Prompt the user to select a source folder, a destination folder,
    and a name for the skeleton copy. Executes the copy and reports the result.
    """
    print("Select the folder you want to skeletonize:")
    source = askdirectory()
    if not source:
        print("Operation cancelled. No source folder selected.")
        return

    print("Select the destination where the skeleton copy will be saved:")
    destination = askdirectory()
    if not destination:
        print("Operation cancelled. No destination selected.")
        return

    skeleton_name = input("Enter a name for the skeleton copy: ").strip()
    if not skeleton_name:
        print("Operation cancelled. No valid name provided.")
        return

    try:
        result_path = make_folder_skeleton_copy(source, destination, skeleton_name)
        print(f"Success: Skeleton copy created at {result_path}")
    except Exception as e:
        print(f"Error: Failed to create skeleton copy. {e}")


if __name__ == "__main__":
    run_skeleton_copy()
