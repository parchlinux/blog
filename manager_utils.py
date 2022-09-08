import os
import shutil
from pathlib import Path

import markdown


def get_posts():
    """Get blog and faq post"""

    for path in ("content/blog", "content/blog/faq"):
        if not Path(path).exists():
            Path(path).mkdir(parents=True)
    blogs_dir = os.listdir("content/blog")
    faqs = os.listdir("content/blog/faq")

    blogs = []
    for category in blogs_dir:
        bposts = os.listdir(os.path.join("content", "blog", category))
        for post in bposts:
            blogs.append([post, category])

    data = {"blogs": blogs, "faqs": faqs}

    return data


def delete_post(filePath, docs_dir):
    """Delete post .md file and rendered files in docs"""
    # First, delete main .md file (in data folder)
    os.remove(filePath)

    # Second, delete folder from docs folder
    shutil.rmtree(os.path.join("docs", docs_dir, ntpath.basename(filePath)[:-3]))


def format_authors_tags(items):
    """Format authors and tags to be compatible with Markdown metadata"""
    s = ""
    count = 0
    for item in items:
        count += 1
        if count > 1:
            # More than one author
            s += f"{item}"
            if item != items[-1]:
                s += ","
        else:
            s += f"{item}"

    return s.strip()


def get_comma_separated(string):
    """Get items in comma separated string and clean whitespaces"""
    result = [x.strip() for x in string.split(",")]
    return result


def get_md_template(post_type):
    """Return given template content"""
    with open(f"manager_app/templates/post.{post_type}.md") as f:
        content = f.read()
        return content


def get_file_body(file_lines):
    """Get body of file content without metadata"""
    indicestoremove = []
    for n, line in enumerate(file_lines):
        indicestoremove.append(n)
        if "slug:" in line:
            break

    for index in sorted(indicestoremove, reverse=True):
        file_lines.pop(index)

    body = "".join(file_lines)
    return body


def parse_file(file_path):
    """Open, get and return conntent of given file"""
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
    with open(file_path, encoding="utf-8") as f2:
        lines = f2.readlines()

    md = markdown.Markdown(extensions=["extra", "smarty", "meta"])
    md.convert(text)
    metadata = md.Meta

    body = get_file_body(lines)

    return [body, metadata]


def save_md_file(post_type, data):
    """Save post to respective category (blog, faq)"""
    template = get_md_template(post_type)
    slug = data["slug"]

    if post_type == "blog":
        category = data["category"]
        post = template.format(
            data["title"],
            data["summary"],
            format_authors_tags(data["authors"]),
            data["date"],
            format_authors_tags(data["tags"]),
            slug,
            data["post_content"],
        )
        path = Path(f"content/blog/{category}/{slug}.md")
        with open(path.as_posix(), "w") as f:
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
            f.write(post)
    else:
        post = template.format(
            data["title"], format_authors_tags(data["tags"]), slug, data["post_content"]
        )

        path = Path(f"content/blog/faq/{slug}.md")
        with open(path.as_posix(), "w") as f:
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
            f.write(post)
