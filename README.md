# api-test

### Go to project root directory
`cd <project-dir>`

### Build image
`docker buildx build -t zfastapi .`

### Run app in container
`docker run --rm  -p 8000:8000 -v $(pwd)/src/app:/app --name devcontainer zfastapi:latest`