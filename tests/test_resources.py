#!/usr/bin/env python3
import base64
import html.parser
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
EXTENSION = ROOT / "_extensions" / "unilu-theme"


class Images(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))


with tempfile.TemporaryDirectory() as temp:
    project = Path(temp)
    extension = project / "_extensions" / "ginolhac" / "unilu-theme"
    shutil.copytree(EXTENSION, extension)
    (project / "_quarto.yml").write_text("project:\n  type: default\n")
    slides = project / "slides"
    slides.mkdir()
    shutil.copyfile(EXTENSION / "uni-logo.png", slides / "deck-logo.png")
    white_logo = (EXTENSION / "uni-logo-white.png").read_bytes()

    for embedded in (False, True):
        name = "embedded" if embedded else "regular"
        source = slides / f"{name}.qmd"
        math_option = "    html-math-method: mathml\n" if embedded else ""
        source.write_text(
            "---\n"
            "title: Resource test\n"
            "logo_url: https://example.com\n"
            "format:\n"
            "  unilu-theme-revealjs:\n"
            f"    embed-resources: {str(embedded).lower()}\n"
            f"{math_option}"
            "title-slide-attributes:\n"
            "  data-background-image: deck-logo.png\n"
            "---\n\n"
            "# Chapter {.chapter}\n\n## Slide\n\nMath: $x^2$.\n"
        )
        subprocess.run(["quarto", "render", str(source), "--quiet"], cwd=project, check=True)
        document = source.with_suffix(".html").read_text()
        images = Images()
        images.feed(document)
        chapter_logo = next(image for image in images.images if image.get("id") == "unilu-chapter-logo")
        src = chapter_logo["src"]
        assert "hidden" in chapter_logo
        if embedded:
            assert src.startswith("data:image/png;base64,")
            assert base64.b64decode(src.split(",", 1)[1]) == white_logo
            assert 'data-background-image="data:image/png;base64,' in document
            assert "<math" in document
            css = unquote(document)
        else:
            assert not src.startswith("/")
            assert (slides / unquote(src)).read_bytes() == white_logo
            css = "\n".join(path.read_text() for path in (slides / f"{name}_files").rglob("*.css"))
        assert "section.chapter.present) .slide-logo{content:var(--unilu-chapter-logo)" in css
        assert "logo.style.setProperty('--unilu-chapter-logo'" in document
        assert 'var url = "https://example.com"' in document
        assert "/_extensions/unilu-theme/uni-logo-white.png" not in css
        print(f"{name}: OK")

    (project / "_quarto.yml").write_text("project:\n  type: default\n  output-dir: _output\n")
    subprocess.run(["quarto", "render", "--quiet"], cwd=project, check=True)
    output = project / "_output" / "slides" / "regular.html"
    images = Images()
    images.feed(output.read_text())
    chapter_logo = next(image for image in images.images if image.get("id") == "unilu-chapter-logo")
    assert (output.parent / unquote(chapter_logo["src"])).read_bytes() == white_logo
    print("project output: OK")
