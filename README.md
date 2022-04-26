# blog

To update blog:
1. Write blog post
2. Update `_toc.yml`
3. Push changes to git
4. cd to repo root
5. Run `jupyter-book build .` 
6. Run `ghp-import -n -p -f _build/html`
