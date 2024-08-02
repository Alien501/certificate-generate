import os, concurrent.futures, requests

repos_to_clone = [
    {
        'team_name': 'Team-1',
        'git_repo_link': 'https://github.com/Alien501/gpaFinal'
    },
    {
        'team_name': 'Team-2',
        'git_repo_link': 'https://github.com/Alien501/thirukural'
    },
    {
        'team_name': 'Team-3',
        'git_repo_link': 'https://github.com/Alien501/LRC-Get'
    },
    {
        'team_name': 'Team-4',
        'git_repo_link': 'https://github.com/Alien501/rec_comapnion'
    },
    {
        'team_name': 'Team-5',
        'git_repo_link': 'https://github.com/BlackEmpir7199/FORUS'
    },
    {
        'team_name': 'Team-6',
        'git_repo_link': 'https://github.com/aijurist/PDRS---Precautionary-Disaster-Response-System'
    }
]

if not os.path.exists('./clone'):
    os.mkdir('./clone')
    
os.chdir('./clone')

def is_forked(repo_name):
    url = f'https://api.github.com/repos/' + repo_name
    res = requests.get(url)
    repo_detials = res.json()
    
    if repo_detials.get('fork'):
        return {
            'status': True,
            'Original': repo_detials['parent']['full_name']
        }
    return {
        'status': False,
        'Original': ''
    }

def write_sh_file(team_data):
    team_name = team_data['team_name']
    team_key = team_data['key']
    # content = f'sonar-scanner.bat -D"sonar.projectKey={}" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9001" -D"sonar.login=sqp_ccbbd55eed981b8746e17d1ac9f17ab4abdf55ce"'
    content = f'sonar-scanner.bat -D"sonar.projectKey={team_name}" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9001" -D"sonar.login={team_key}"'
    with open(f'{team_name}.sh', 'w') as sh:
        sh.write()

def clone_repo(team_data):
    try:
        print(team_data['team_name'])
        print()
        link = team_data['git_repo_link']
        team_name = team_data['team_name']
        os.system(f'git clone {link}.git {team_name}')
        is_fork = is_forked(link.split('https://github.com/')[-1])
        if is_fork['status']:
            print('- * -' * 10)
            print('Forked Repository')
            print(is_fork['Original'])
            print('- * -' * 10)
    except Exception as e:
        # print(f'Failed to clone {repos_to_clone}.git')
        print()

with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
    futures = {
        executor.submit(clone_repo, repo): repo for repo in repos_to_clone
    }
    os.system('echo off')
    for future in concurrent.futures.as_completed(futures):
        repo = futures[future]
        try:
            future.result()
        except Exception as e:
            print(f'Repo couldn\'t be clone {repo}')