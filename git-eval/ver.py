import os
import concurrent.futures
import subprocess, requests

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

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def is_forked(repo_name):
    url = f'https://api.github.com/repos/{repo_name}'
    try:
        res = requests.get(url)
        res.raise_for_status()
        repo_details = res.json()
        if repo_details.get('fork'):
            return {
                'status': True,
                'Original': repo_details['parent']['full_name']
            }
    except requests.RequestException as e:
        print(f"Error checking if repo is forked: {e}")
    return {
        'status': False,
        'Original': ''
    }

def write_sh_file(team_data):
    team_name = team_data['team_name']
    team_key = team_data['key']
    content = f'sonar-scanner.bat -D"sonar.projectKey={team_name}" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9001" -D"sonar.login={team_key}"'
    with open(f'{team_name}.bat', 'w') as sh:
        sh.write(content)

def clone_repo(team_data):
    try:
        link = team_data['git_repo_link']
        team_name = team_data['team_name']
        clone_path = os.path.join('./clone', team_name)
        create_directory(clone_path)

        clone_command = ['git', 'clone', '--progress', link, clone_path]
        process = subprocess.Popen(clone_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in process.stdout:
            if "Receiving objects" in line:
                percent_complete = line.split()[-1].strip('%')
                print(f"{team_name}: {percent_complete}% cloned", end='\r')
        
        process.wait()
        if process.returncode == 0:
            print(f"{team_name} cloned successfully")

            is_fork = is_forked(link.split('https://github.com/')[-1])
            os.chdir(clone_path)
            write_sh_file(team_data)
            os.chdir('../../')

            if is_fork['status']:
                print(f"Forked Repository: {is_fork['Original']}")
        else:
            print(f"Failed to clone {team_name}")
    except Exception as e:
        print(f'Failed to clone {link}: {e}')

if __name__ == "__main__":
    create_directory('./clone')
    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
        futures = {
            executor.submit(clone_repo, repo): repo for repo in repos_to_clone
        }
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error processing repo: {e}")

    print("\nSummary of Cloning:")
    for repo in repos_to_clone:
        team_name = repo['team_name']
        if os.path.exists(os.path.join('./clone', team_name)):
            print(f"{team_name}: Cloned successfully")
        else:
            print(f"{team_name}: Cloning failed")
