import os, concurrent.futures, requests

repos_to_clone = [
    {
        'team_name': 'Team-1',
        'git_repo_link': 'https://github.com/Alien501/gpaFinal',
        'key': 'sqp_54d814e4792b60bee6ca93c51c7c33004f35eccf'
    },
    {
        'team_name': 'Team-2',
        'git_repo_link': 'https://github.com/Alien501/thirukural',
        'key': 'sqp_0557404b10562ab2b8f221a2a14cbe183303a004'
    },
    {
        'team_name': 'Team-3',
        'git_repo_link': 'https://github.com/Alien501/LRC-Get',
        'key': 'sqp_91fb2656ebbc783eb1f05796f27f7ec8cfdd8586'
    },
    {
        'team_name': 'Team-4',
        'git_repo_link': 'https://github.com/Alien501/rec_comapnion',
        'key': 'sqp_d09c088ba41fdc4fb2d40db450a149b949e9cebf'
    },
    {
        'team_name': 'Team-5',
        'git_repo_link': 'https://github.com/BlackEmpir7199/FORUS',
        'key': 'sqp_dea18a3c4a539c263efce0d7bc59152aa2e871b1'
    },
    {
        'team_name': 'Team-6',
        'git_repo_link': 'https://github.com/aijurist/PDRS---Precautionary-Disaster-Response-System',
        'key': 'sqp_fd9b15819b77895beb1415d1d26a08d72840a7b9'
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
    os.chdir(f'./{team_name}')
    # content = f'sonar-scanner.bat -D"sonar.projectKey={}" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9001" -D"sonar.login=sqp_ccbbd55eed981b8746e17d1ac9f17ab4abdf55ce"'
    content = f'sonar-scanner.bat -D"sonar.projectKey={team_name}" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9001" -D"sonar.login={team_key}"'
    with open(f'{team_name}.bat', 'w') as sh:
        sh.write(content)
    os.chdir('../')

def clone_repo(team_data):
    try:
        link = team_data['git_repo_link']
        team_name = team_data['team_name']
        os.system(f'git clone {link}.git {team_name}')
        is_fork = is_forked(link.split('https://github.com/')[-1])
        write_sh_file(team_data)
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