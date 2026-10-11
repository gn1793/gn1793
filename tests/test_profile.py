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


class TextRenderTests(unittest.TestCase):
    def test_readme_is_text_first(self):
        from build_readme import main
        main()
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('assets/hero.png', readme)
        self.assertIn('RNA–Ligand Pose Quality Prediction', readme)
        self.assertIn('ADMET Prediction', readme)
        self.assertIn('The Build Lab', readme)
        self.assertIn('| **Engineering** |', readme)
        self.assertNotIn('assets/generated/', readme)
        self.assertNotIn('Docker', readme)

    def test_v4_compact_layout(self):
        from build_readme import main
        main()
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('## Featured Research', readme)
        self.assertIn('## The Build Lab', readme)
        self.assertIn('## Tools & Technologies', readme)
        self.assertIn('## Recent Activity', readme)
        self.assertIn('## GitHub Stats', readme)
        self.assertIn('PREVIOUS BUILD', readme)
        self.assertIn('<table width="100%">', readme)
        self.assertIn('<strong>01 / LATEST BUILD</strong>', readme)
        self.assertIn('<strong>02 / PREVIOUS BUILD</strong>', readme)
        self.assertIn('Build Collection ↗', readme)
        self.assertIn('assets/github-stats.svg', readme)
        self.assertNotIn('Data Science', readme)
        self.assertIn('Build Collection', readme)
        self.assertIn('## Recent Activity', readme)
        self.assertNotIn('Public account data and available contribution activity', readme)
        self.assertIn('img.shields.io/badge/', readme)
        self.assertNotIn('## Research Interests', readme)
        self.assertNotIn('## Publications', readme)  # Hide empty section
        self.assertNotIn('assets/generated/', readme)
        self.assertNotIn('Docker', readme)
        self.assertNotIn('**Git**', readme)

    def test_markdown_links(self):
        from build_readme import main
        main()
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('https://github.com/gn1793/AI-Usage-System-Monitor', readme)
        self.assertIn('https://github.com/gn1793/CodeMonitor', readme)


if __name__ == '__main__':
    unittest.main()


class StatsRenderTests(unittest.TestCase):
    def test_stats_svg_is_generated_and_well_formed(self):
        import xml.etree.ElementTree as ET
        from render_stats import main
        main()
        root = ET.parse(ROOT / 'assets' / 'github-stats.svg').getroot()
        self.assertTrue(root.tag.endswith('svg'))
        svg = (ROOT / 'assets' / 'github-stats.svg').read_text(encoding='utf-8')
        self.assertIn('Contributions', svg)
        self.assertNotIn('(12m)', svg)
        self.assertNotIn('Public GitHub data ·', svg)
        self.assertIn('100-contribution reference', svg)

    def test_stack_removes_data_science(self):
        names = [g['name'] for g in load_data('tech_stack.yaml')['groups']]
        self.assertNotIn('Data Science', names)
