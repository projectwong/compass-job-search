# Prompt 01 Establish the privacy boundary

```text
Read README.md, CLAUDE.md, docs/build-log.md, and the completed rubric artifacts in $COMPASS_DATA_DIR. Build only the privacy and configuration boundary for Compass.

First state your assumptions and a short implementation plan. Then add the minimum code needed to:
- require COMPASS_DATA_DIR;
- resolve it to an absolute path;
- refuse a path inside this Git repository;
- create private subdirectories only inside that path;
- keep secrets out of source, logs, exceptions, and test snapshots;
- run all tests against synthetic temporary data.

Add tests that prove missing, relative, and in-repository paths fail safely. Add a repository audit that fails on private file types and common credential patterns. Do not read or copy any real private record while implementing this phase.

Run the tests, show the changed files and results, and stop. Do not build the data model yet.
```
