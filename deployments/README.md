# Configure the Infrastructure

A set of scripst, templates and Ansible playbooks to configure a new OpenShift cluster (>= 4.2.x) and other infrastructure.

Basic configuration for all scripts is in file `config`. Review and change accordingly, **DO NOT** store API keys etc. there !

## OpenShift

NOTE: Make sure to login into the cluster with `oc login ...` first and select a user that has the **cluster admin role**.

### Add users

Add a number of default users and with a default password.

```shell

cd 01_identity_provider
./create_identity_provider.sh

```

### Create default namespaces/projects

Create a default project for each user and set policies, resource limmits etc.

```shell

cd 02_projects
./create_projects.sh

```

To clean-up everything, run:
```shell

./delete_projects.sh

```

### Red Hat CodeReady Workspaces

To install RHCRW, create a shared infrastructure project first:

```shell

oc new-project shared-infra

```

Then, from the Web UI, navigate to project `shared-infra`, install the CodeReady operator and follow the instructions there.

