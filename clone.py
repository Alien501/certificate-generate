import os, concurrent.futures

repos_to_clone = []

if not os.path.exists('./clone'):
    os.mkdir('./clone')
    
os.chdir('./clone')

def clone_repo(repo_link):
    try:
        os.system(f'git clone {repo_link}.git')
    except:
        print(f'Failed to clone {repos_to_clone}.git')

with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
    futures = {
        executor.submit(clone_repo, repo): repo for repo in repos_to_clone
    }
    
    for future in concurrent.futures.as_completed(futures):
        repo = futures[future]
        try:
            future.result()
        except Exception as e:
            print(f'Repo couldn\'t be clone {repo}')