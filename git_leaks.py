#! user/bin/python3

from git import Repo
import re  # signal
import time


REPO_DIR = './skale/skale-manager'
KEY_WORDS = ['credentials', 'password', 'key',
             'new password', ]  # ,'password','username','key'


def extract(repo_dir):
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits

def transform(commits: list, found: list=[]) -> list:
    
    for commit in commits:
        s = re.findall(KEY_WORDS, commit.message, re.I)

        found.append([commit,s]) if s != [] else None 

    return found
    ...
 def load(found: list):
  file = open('secrets.txt','w')
  for secret in found: file.write(f'>> {secret[0].message}')
  file.close(
  time.sleep(1)


if __name__ == '__main__':
    commits = extract(REPO_DIR)
    for commit in commits:
        for word in KEY_WORDS:
            if re.search(word, commit.message, re.IGNORECASE):
                print('Commit: {} - {}'.format(commit.hexsha, commit.message))
