from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from organizer import plan


class PreviewTests(unittest.TestCase):
    def test_plan_stays_within_the_selected_folder(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "Images").mkdir()
            (root / "Images" / "existing.png").touch()
            (root / "existing.png").touch()
            (root / "picture.PNG").touch()
            (root / ".private.pdf").touch()
            (root / "linked.pdf").symlink_to(root / "picture.PNG")
            (root / "inside").mkdir()
            (root / "inside" / "nested.pdf").touch()
            self.assertEqual(plan(root), [{"source": "picture.PNG", "destination": "Images/picture.PNG"}])
            self.assertTrue((root / "picture.PNG").is_file())
            self.assertFalse((root / "Images" / "picture.PNG").exists())
