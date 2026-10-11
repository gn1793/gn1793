import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_data import validate
from common import load_data


class ProfileTests(unittest.TestCase):
    def test_metadata(self):
        validate()

    def test_research_projects(self):
        projects = load_data('projects.yaml')['projects']
        self.assertEqual([p['id'] for p in projects],
                         ['rna-ligand-pose-quality', 'admet-prediction'])

    def test_engineering_exclusions(self):
        groups = load_data('tech_stack.yaml')['groups']
        engineering = next(g['technologies'] for g in groups if g['name'] == 'Engineering')
        self.assertEqual(engineering, ['GitHub', 'Linux', 'Swift'])

    def test_build_selection(self):
        builds = load_data('builds.yaml')['builds']
        self.assertEqual(sum(b['featured'] for b in builds), 1)


if __name__ == '__main__':
    unittest.main()
