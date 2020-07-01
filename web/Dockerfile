version: '3'

services:
  vue:
    image: node:12
    container_name: <app_name>_vue
    volumes:
      - ./:/code
    working_dir: /code
    env_file:
      - .env
    command: bash -c "npm i && npm run build"
