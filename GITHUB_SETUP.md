# Getting Started: Pull Git Repository to Cursor (macOS)

This tutorial will walk you through downloading code from GitHub and opening it in Cursor, step by step. No technical experience required!

## What You'll Need

- A Mac computer
- A GitHub account (which you already have!)
- Cursor code editor installed on your Mac
- The repository URL: `https://github.com/cowjuh/fs-utilities.git`

## Step 1: Install Cursor (if you haven't already)

1. Go to [cursor.sh](https://cursor.sh)
2. Download Cursor for macOS
3. Open the downloaded file and drag Cursor to your Applications folder
4. Open Cursor from your Applications folder

## Step 2: Open Terminal

Don't worry - we'll only use a few simple commands!

1. Press `Cmd + Space` to open Spotlight search
2. Type "Terminal" and press Enter
3. A black window will open - this is your Terminal

## Step 3: Choose Where to Save the Code

First, let's navigate to a good place to store your code projects.

In Terminal, type these commands one at a time (press Enter after each):

```bash
cd Desktop
mkdir my-projects
cd my-projects
```

This creates a folder called "my-projects" on your Desktop and moves into it.

## Step 4: Download the Repository

Now we'll "clone" (download) the code from GitHub:

```bash
git clone https://github.com/cowjuh/fs-utilities.git
```

You should see some text showing the download progress. When it's done, you'll see your command prompt again.

## Step 5: Open the Code in Cursor

Now let's open the downloaded code in Cursor:

```bash
cd fs-utilities
cursor .
```

The first command moves you into the downloaded folder, and the second opens it in Cursor.

## Step 6: Explore Your Code!

Cursor should now open with the fs-utilities project loaded. You'll see:

- A file explorer on the left showing all the project files
- The main editing area where you can view and edit code
- Various files like README.md, package.json, etc.

## What Just Happened?

Congratulations! You just:

1. **Cloned a repository** - Downloaded a copy of someone's code project from GitHub to your computer
2. **Opened it in Cursor** - Made the code ready to view, edit, and work with

## Next Steps

- Click on different files in the left sidebar to explore the code
- Read the project's README.md file to understand what it does
- Try making small changes to see how the code editor works

## Troubleshooting

**"git: command not found"**
- You need to install Git first. Go to [git-scm.com](https://git-scm.com) and download Git for macOS

**"cursor: command not found"**
- Cursor might not be in your system PATH. Instead of `cursor .`, try:
  1. Open Cursor manually from Applications
  2. Go to File → Open Folder
  3. Navigate to Desktop → my-projects → fs-utilities

**Permission denied errors**
- Try adding `sudo` before the command, like `sudo git clone ...`
- You might need to enter your Mac password

## Useful Commands to Remember

- `pwd` - Shows where you currently are
- `ls` - Lists files and folders in current location
- `cd foldername` - Moves into a folder
- `cd ..` - Moves up one folder level
- `cd ~` - Goes to your home directory

## Getting Updates

If the original repository gets updated and you want the latest changes:

```bash
cd ~/Desktop/my-projects/fs-utilities
git pull
```

This downloads any new changes from the original repository.

---

**You did it!** You're now ready to explore and work with code from GitHub in Cursor. This same process works for any public GitHub repository - just replace the URL with the one you want to download.