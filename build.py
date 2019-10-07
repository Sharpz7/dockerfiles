import os

BANNED = [
    ".circleci", ".git", "build.py", "README.md",
    "builds", ".gitignore", ".github"
    ]
EXECUTOR_COUNT = 4


def split_builds(builds, n):
    return [builds[i::n] for i in range(n)]


class Build:
    def __init__(self, location):
        self.location = location

        if "$" in self.location:
            self.name, self.version = self.location.split("$")
        else:
            self.name = self.location
            self.version = "latest"

    def __repr__(self):
        return f"{self.name}, {self.version}"


locs = os.listdir(".")
builds = []
for loc in locs:
    if loc not in BANNED:
        builds.append(Build(loc))

split = split_builds(builds, EXECUTOR_COUNT)

for num, executor in enumerate(split):
    job_code = ""
    for build in executor:
        sh = (
            "set -e\n"
            f"docker login -u $DOCKER_USER -p $DOCKER_PASS\n"
            f"cd {build.location}\n"
            f"docker pull sharp6292/{build.name}:{build.version} || true\n"
            f"docker build --cache-from sharp6292/{build.name}:{build.version}"
            f" -f Dockerfile -t sharp6292/{build.name}:{build.version} .\n"
            f"docker push sharp6292/{build.name}:{build.version}\n"
            "cd ..\n"
        )
        job_code += sh
    with open(f'./builds/build-{num}.sh', 'w') as file:
        file.write(job_code)
