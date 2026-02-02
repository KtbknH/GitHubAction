# GitHubAction
Exercice du Cours - GitHub Actions Learning Project

## 📚 Description
This repository is a course exercise to learn and practice GitHub Actions. It contains example workflows that demonstrate various GitHub Actions concepts and features.

## 🚀 Workflows

### 1. Hello World Workflow (`.github/workflows/hello-world.yml`)
A simple workflow that introduces basic GitHub Actions concepts:
- **Triggers**: Runs on push to main, pull requests, and manual dispatch
- **Security**: Uses explicit permissions (contents: read) following the principle of least privilege
- **Features**:
  - Code checkout
  - Running shell commands
  - Using GitHub context variables
  - Displaying system information

### 2. Multi-Job Workflow (`.github/workflows/multi-job.yml`)
A more advanced workflow demonstrating multiple jobs and dependencies:
- **Security**: Uses explicit permissions (contents: read, actions: read)
- **Jobs**:
  - **Build**: Simulates a build process and creates artifacts
  - **Test**: Runs after build, downloads artifacts, and simulates testing
  - **Deploy**: Runs after build and test, only on push events
- **Features**:
  - Job dependencies with `needs`
  - Artifact upload and download
  - Conditional job execution with `if`

## 📖 Learning Objectives
- Understanding GitHub Actions syntax and structure
- Working with workflow triggers and events
- Using GitHub Actions marketplace actions
- Managing job dependencies and execution order
- Working with artifacts between jobs
- Using GitHub context variables and expressions
- Implementing security best practices (explicit permissions)

## 🔧 How to Use
1. Fork this repository
2. Make changes to trigger workflows
3. View workflow runs in the "Actions" tab
4. Experiment by modifying the workflows
5. Manually trigger workflows using workflow_dispatch

## 📝 Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
