from git import Repo
import re  # signal
import time
import json


REPO_DIR = './skale/skale-manager'
KEY_WORDS = ['credentials', 'password', 'key',
             'new password', 'username']


def extract(repo_dir):
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits

# create a load function to save the data


def load():

    time.sleep(1)


if __name__ == '__main__':
    diccionario = {}
    commits = extract(REPO_DIR)
    for commit in commits:
        for word in KEY_WORDS:
            if re.search(word, commit.message, re.IGNORECASE):
                diccionario[commit.message] = commit.hexsha
                #print('Commit: {} - {}'.format(commit.hexsha, commit.message))
    json_object = json.dumps(diccionario, indent=4)
    print(json_object)

    with open("sample.json", "w") as outfile:
        json.dump(diccionario, outfile)
