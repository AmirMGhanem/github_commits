from datetime import datetime
import yaml
from git import Repo
from tqdm import tqdm
FILE_TO_COMMIT_NAME: str = 'update_me.yaml'


def update_yaml_file():
    with open(FILE_TO_COMMIT_NAME, 'r') as file:
        YAML_FILE = {
            'UPDATE_TIMES':int(yaml.safe_load(file)['UPDATE_TIMES']) + 1,
            'LAST_UPDATE':datetime.now().strftime("%A %B %d %Y at %X%p")
            }
        
    with open(FILE_TO_COMMIT_NAME, 'w') as file: yaml.dump(YAML_FILE, file, default_flow_style=False, sort_keys=True)
    return YAML_FILE
    
def push_commit(YAML_FILE):
    print('Commiting to repository...')
    for i in tqdm(range(int(9e6))):
        pass
    repo = Repo('.')  # if repo is CWD just do '.'
    repo.index.add([FILE_TO_COMMIT_NAME])
    repo.index.commit(f'Amir Updated {YAML_FILE["UPDATE_TIMES"]} times. Last update was on {YAML_FILE["LAST_UPDATE"]}.')
    origin = repo.remote('origin')
    origin.push()


if __name__ == '__main__':
    push_commit(update_yaml_file())