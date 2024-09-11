# pip3 install PyGitHub
#
#

from github import Github

# Replace with your GitHub personal access token
ACCESS_TOKEN = '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'

# Replace with your GitHub organization name
ORG_NAME = 'intralin'

# Authenticate with GitHub
g = Github(ACCESS_TOKEN)

# Get the organization
org = g.get_organization(ORG_NAME)

# Iterate over all repositories in the organization
for repo in org.get_repos():
    try:
        # Get the default branch of the repository
        default_branch = repo.default_branch

        # Create a new workflow file
        workflow_content = f"""
        name: Bulk Job

        on:
          push:
            branches: [ {default_branch} ]

        jobs:

          bulk-job:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v3
            - name: Run a script
              run: |
                echo "Running a script for {repo.full_name}"
                # Add your custom script or commands here
        """

        # Create or update the workflow file in the repository
        repo.create_file(
            path='.github/workflows/bulk-job.yml',
            message='Add bulk job workflow',
            content=workflow_content,
            branch=default_branch
        )
        print(f'Bulk job workflow created in {repo.full_name}')
    except Exception as e:
        print(f'Error creating bulk job workflow in {repo.full_name}: {e}')
