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
    def test_readme_has_accessible_card_text(self):
        from build_readme import main
        main()
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('assets/hero.png', readme)
        self.assertIn('RNA–Ligand Pose Quality Prediction', readme)
        self.assertIn('ADMET Prediction', readme)
        self.assertIn('The Build Lab', readme)
        self.assertIn('Engineering', readme)
        self.assertNotIn('assets/generated/', readme)
        self.assertNotIn('Docker', readme)

    def test_compact_layout(self):
        from build_readme import main
        main()
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('## Research', readme)
        self.assertIn('## The Build Lab', readme)
        self.assertIn('## Tools & Technologies', readme)
        self.assertIn('## Recent Activity', readme)
        self.assertIn('## GitHub Stats', readme)
        self.assertNotIn('<table', readme)
        self.assertIn('width="100%"', readme)
        self.assertIn('01 / FEATURED PROJECT', readme)
        self.assertIn('02 / DEVELOPER UTILITY', readme)
        self.assertIn('Explore All Projects →', readme)
        self.assertIn('assets/github-stats.svg', readme)
        self.assertNotIn('Data Science', readme)
        self.assertIn('## Recent Activity', readme)
        self.assertNotIn('Public account data and available contribution activity', readme)
        self.assertIn('PyTorch', readme)
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


class RoundedCardTests(unittest.TestCase):
    def test_generated_cards_preserve_content_and_links(self):
        import re
        import xml.etree.ElementTree as ET
        from build_readme import main
        main()
        readme = (ROOT / 'README.md').read_text()
        paths = re.findall(r'src="(assets/cards/[^"]+)"', readme)
        self.assertGreaterEqual(len(paths), 8)
        ns = {'svg': 'http://www.w3.org/2000/svg'}
        for path in paths:
            root = ET.parse(ROOT / path).getroot()
            self.assertGreater(float(root.find('svg:rect', ns).get('rx')), 0)
            self.assertTrue(root.find('svg:desc', ns).text)
            height = float(root.get('height'))
            for node in root.findall('.//svg:text', ns):
                self.assertLess(float(node.get('y')), height - 10)
        self.assertIn('View repository', readme)
        self.assertIn('width="50%"', readme)

    def test_long_card_content_expands_without_overlapping_footer(self):
        from render_cards import layout
        short = layout({'title': 'Short', 'body': 'Small', 'footer': 'View commit'})
        long = layout({'title': 'Title ' * 20, 'body': 'Description ' * 100, 'footer': 'View commit'})
        self.assertGreater(long[-1], short[-1])
