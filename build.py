import os

BANNED = [".circleci", ".git", "build.py", "README.md", "builds", ".gitignore"]

locs = os.listdir(".")
builds = []
for loc in locs:
    if loc not in BANNED:
        builds.append(loc)

num = len(builds) // 4

total = {"0": num, "1": num, "2": num, "3": num}
if len(builds) % 4 != 0:
    for i in range(1, (len(builds) % 4)+1):
        total[str(i)] += 1

count = 0
job = 0
job_code = "cd ..\n"
for build in builds:
    count += 1
    sh = (
        f"docker login -u $DOCKER_USER -p $DOCKER_PASS\n"
        f"cd {build}\n"
        f"docker pull sharp6292/{build}:latest || true\n"
        f"docker build --cache-from sharp6292/{build}:latest "
        f"-f Dockerfile -t sharp6292/{build}:latest .\n"
        f"docker push sharp6292/{build}:latest\n"
        "cd ..\n"
    )
    job_code += sh
    if count >= total[str(job)]:
        with open(f'./builds/build-{job}.sh', 'w') as file:
            file.write(job_code)
        job += 1
        job_code = "cd ..\n"
        count = 0
