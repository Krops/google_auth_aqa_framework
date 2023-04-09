## 1. Install python3.10
## 2. Create virtual env
  ```shell
  python3.10 -m venv venv
  source venv/bin/activate
  ```

## 3. Install [requirements.txt](requirements.txt)
  ```shell
  pip install -r requirements.txt
  ```

## 4. Set env variables
    GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxx
## 4. RUN tests
  ```shell
  pytest /test
  ```