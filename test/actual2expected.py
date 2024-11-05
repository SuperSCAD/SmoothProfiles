import os
import shutil
from pathlib import Path

if __name__ == '__main__':
    for path in Path('test').rglob('*.actual.scad'):
        basename = Path(Path(os.path.basename(path)).stem).stem
        dirname = os.path.dirname(path)

        path_actual = Path(dirname, basename + '.actual.scad')
        path_expected = Path(dirname, basename + '.expected.scad')
        actual = path_actual.read_text()

        copy = True
        if os.path.exists(path_expected):
            expected = path_expected.read_text()
            copy = actual != expected

        if copy:
            print('Copying {}'.format(path, path_actual))
            shutil.copy(path_actual, path_expected)
