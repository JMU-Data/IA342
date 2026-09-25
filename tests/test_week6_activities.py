"""Validation test for IA342 Week 6 interactive activity iframe embeddings.

Asserts:
1. Exactly 13 Week 6 activity embeds exist in both Jekyll and standalone deck.
2. The slide-to-fragment mapping matches the intended assignment:
   - Slide 6  -> #bank
   - Slide 8  -> #oltp
   - Slide 9  -> #olap
   - Slide 10 -> #averages
   - Slide 13 -> #labels
   - Slide 15 -> #copypaste
   - Slide 18 -> #deletion
   - Slide 26 -> #roles
   - Slide 27 -> #roles-viz
   - Slide 28 -> #live-query
   - Slide 29 -> #extract-query
   - Slide 31 -> #reusable-flow
   - Slide 34 -> #join
3. Each fragment exists in docs/assets/week-6/activities.html.
4. Both docs/modules/module-6/index.md and docs/modules/module-6/preview.html
   use the correct mapping.
"""

import os
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

EXPECTED_MAPPING = {
    6: 'bank',
    8: 'oltp',
    9: 'olap',
    10: 'averages',
    13: 'labels',
    15: 'copypaste',
    18: 'deletion',
    26: 'roles',
    27: 'roles-viz',
    28: 'live-query',
    29: 'extract-query',
    31: 'reusable-flow',
    34: 'join',
}


class SlideIframeParser(HTMLParser):
    def __init__(self, is_index_md=False):
        super().__init__()
        self.is_index_md = is_index_md
        self.slide_tag = 'div' if is_index_md else 'section'
        self.current_slide = None
        self.slide_depth = 0
        self.mappings = {}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == self.slide_tag:
            if self.is_index_md and 'data-slide' in attrs_dict:
                self.current_slide = int(attrs_dict['data-slide'])
                self.slide_depth = 1
            elif not self.is_index_md:
                label = attrs_dict.get('aria-label', '')
                m = re.search(r'Slide (\d+):', label)
                if m:
                    self.current_slide = int(m.group(1))
                    self.slide_depth = 1
                elif self.current_slide is not None:
                    self.slide_depth += 1
            elif self.current_slide is not None:
                self.slide_depth += 1
        elif self.current_slide is not None and tag == self.slide_tag:
            self.slide_depth += 1

        if tag == 'iframe':
            classes = attrs_dict.get('class', '').split()
            if 'activity' in classes:
                src = attrs_dict.get('src', '')
                if self.current_slide is not None:
                    self.mappings[self.current_slide] = src

    def handle_endtag(self, tag):
        if tag == self.slide_tag and self.current_slide is not None:
            self.slide_depth -= 1
            if self.slide_depth <= 0:
                self.current_slide = None
                self.slide_depth = 0


class TestWeek6Activities(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.activities_path = REPO_ROOT / 'docs' / 'assets' / 'week-6' / 'activities.html'
        cls.index_md_path = REPO_ROOT / 'docs' / 'modules' / 'module-6' / 'index.md'
        cls.preview_html_path = REPO_ROOT / 'docs' / 'modules' / 'module-6' / 'preview.html'

    def test_fragments_exist_in_activities_html(self):
        """Assert each fragment exists as a registered route in activities.html."""
        self.assertTrue(self.activities_path.is_file(), f"Missing {self.activities_path}")
        content = self.activities_path.read_text(encoding='utf-8')

        # Find the pages map: const pages={...}
        m = re.search(r'const\s+pages\s*=\s*\{([^}]+)\}', content)
        self.assertIsNotNone(m, "Could not find 'pages' object in activities.html")
        pages_raw = m.group(1)

        # Parse keys from the object literal
        keys = set()
        for token in pages_raw.split(','):
            part = token.strip().split(':')[0].strip().strip("'\"")
            if part:
                keys.add(part)

        for slide, frag in EXPECTED_MAPPING.items():
            self.assertIn(
                frag,
                keys,
                f"Fragment #{frag} (required for Slide {slide}) is not registered in activities.html pages object",
            )

    def test_jekyll_module_6_activity_mapping(self):
        """Assert docs/modules/module-6/index.md has exactly 13 activity embeds with correct fragments."""
        self.assertTrue(self.index_md_path.is_file(), f"Missing {self.index_md_path}")
        parser = SlideIframeParser(is_index_md=True)
        parser.feed(self.index_md_path.read_text(encoding='utf-8'))

        # 1. Exactly 13 embeds
        self.assertEqual(
            len(parser.mappings),
            13,
            f"Expected exactly 13 activity embeds in index.md, found {len(parser.mappings)}",
        )

        # 2. Slide-to-fragment mapping matches EXPECTED_MAPPING
        for slide, expected_frag in EXPECTED_MAPPING.items():
            self.assertIn(slide, parser.mappings, f"Slide {slide} missing activity iframe in index.md")
            src = parser.mappings[slide]
            expected_src = f"../../assets/week-6/activities.html#{expected_frag}"
            self.assertEqual(
                src,
                expected_src,
                f"Slide {slide} in index.md has src '{src}', expected '{expected_src}'",
            )

    def test_standalone_preview_activity_mapping(self):
        """Assert docs/modules/module-6/preview.html has exactly 13 activity embeds with correct fragments."""
        self.assertTrue(self.preview_html_path.is_file(), f"Missing {self.preview_html_path}")
        parser = SlideIframeParser(is_index_md=False)
        parser.feed(self.preview_html_path.read_text(encoding='utf-8'))

        # 1. Exactly 13 embeds
        self.assertEqual(
            len(parser.mappings),
            13,
            f"Expected exactly 13 activity embeds in preview.html, found {len(parser.mappings)}",
        )

        # 2. Slide-to-fragment mapping matches EXPECTED_MAPPING
        for slide, expected_frag in EXPECTED_MAPPING.items():
            self.assertIn(slide, parser.mappings, f"Slide {slide} missing activity iframe in preview.html")
            src = parser.mappings[slide]
            expected_src = f"../../assets/week-6/activities.html#{expected_frag}"
            self.assertEqual(
                src,
                expected_src,
                f"Slide {slide} in preview.html has src '{src}', expected '{expected_src}'",
            )


if __name__ == '__main__':
    unittest.main()
