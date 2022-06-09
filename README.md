## Usage

Check the google doc: <https://docs.google.com/document/d/1-pr4S8KrndepW5iWYabOQbB9T0UMvLiDnmiu0JSkvTI/>.

### Docker usage

```shell
docker buildx build --tag aoe-stats:latest .
docker run --volume "$PWD/replays:/replays" aoe-stats:latest
```

Replace `$PWD/replays` to a path on your machine containing age2de recorded files.
