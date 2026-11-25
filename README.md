# File Organizer Preview

See how files in one directory could be grouped into Documents, Images, Archives and Media.

Run `python3 organizer.py /path/to/a/folder`. The program prints its proposals to the terminal. It works only on files directly inside the selected directory, skips hidden files and symbolic links, and leaves every file in place.

Run the focused check with `python3 -m unittest discover -s tests -p test_preview.py`.

[Current status](docs/HANDOFF.md)
