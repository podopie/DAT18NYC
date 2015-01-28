# Git Workflow for Linux

[xkcd git commit fun](http://xkcd.com/1296/)

This workflow assumes you are starting in your **home directory in Linux** and that you will only use the command line for git interaction.

This means /home/*username*

	joe@ubuntu$ pwd
	/home/joe
	joe@ubuntu$

## Lectures Repository

You do not need to fork the [Lectures](https://github.com/podopie/DAT18NYC) repository because **you will never be pushing to the class repository**.

### Clone the class Repository

	git clone https://github.com/podopie/DAT18NYC.git

**Example:**

	joe@ubuntu:~$ git clone https://github.com/podopie/DAT18NYC.git
	Cloning into 'DAT18NYC'...
	remote: Counting objects: 824, done.
	remote: Compressing objects: 100% (432/432), done.
	remote: Total 824 (delta 360), reused 716 (delta 298)
	Receiving objects: 100% (824/824), 19.42 MiB | 659 KiB/s, done.
	Resolving deltas: 100% (360/360), done.
	Checking out files: 100% (72/72), done.
	joe@ubuntu:~$

### Update For Every Class

	cd DAT18NYC
	git pull origin master

**Example:**

	joe@ubuntu:~$ cd DAT18NYC/
	joe@ubuntu:~/DAT18NYC$ git pull origin master
	From https://github.com/datadave/DAT18NYC
	 * branch            master     -> FETCH_HEAD
	Already up-to-date.
	joe@ubuntu:~/DAT18NYC$
	
### Change Directory to the Current Lesson

	cd classes
	cd lesson0x_abc
	
**Example:**
	
	joe@ubuntu:~/DAT18NYC$ cd classes/
	joe@ubuntu:~/DAT18NYC/classes$ ls
	lesson01_intro_to_data_science           lesson03a_numpy   	lesson04_matplotlib_and_EDA
	lesson02_data_collection_and_extraction  lesson03b_pandas  README.md
	joe@ubuntu:~/DAT18NYC/classes$ cd lesson04_matplotlib_and_EDA/
	joe@ubuntu:~/DAT18NYC/classes/lesson04_matplotlib_and_EDA$ ls
	data  DataVizLecture_v2.pdf  readme.md  Visualization_Instructional_Set.ipynb
	joe@ubuntu:~/DAT18NYC/classes/lesson04_matplotlib_and_EDA$

### Do the Lesson

But don't push any changes.

	ipython notebook
	
