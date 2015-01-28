# Git Workflow for Mac

[xkcd git commit fun](http://xkcd.com/1296/)

This workflow assumes you are starting in your **home directory on OS X** and that you will only use the command line (no GitHub GUI here!).

This means /Users/*username*
	
	mymac:~ joe$ pwd 
	/Users/joe
	mymac:~ joe$
	
## Lectures Repository

You do not need to fork the [Lectures](https://github.com/podopie/DAT18NYC) repository because **you will never be pushing to the Lectures repository**.

### Clone the Lectures Repository

	git clone https://github.com/podopie/DAT18NYC.git

**Example**:

	mymac:~ joe$ git clone https://github.com/podopie/DAT18NYC.git
	Cloning into 'DAT18NYC'...
	remote: Counting objects: 824, done.
	remote: Compressing objects: 100% (432/432), done.
	remote: Total 824 (delta 360), reused 716 (delta 298)
	Receiving objects: 100% (824/824), 19.42 MiB | 1.48 MiB/s, done.
	Resolving deltas: 100% (360/360), done.
	mymac:~ joe$
	
### Update For Every Class

	cd DAT18NYC
	git pull origin master

**Example:**

	mymac:~ joe$ cd DAT18NYC/
	mymac:DAT18NYC joe$ git pull origin master
	From https://github.com/podopie/DAT18NYC
	 * branch            master     -> FETCH_HEAD
	Already up-to-date.
	mymac:DAT18NYC joe$
	
### Change Directory to the Current Lesson

	cd lessons
	cd lesson0x_abc
	
**Example:**
	
	mymac:DAT18NYC joe$ cd classes/
	mymac:classes joe$ ls
	README.md                               lesson02_data_collection_and_extraction 	lesson03b_pandas
	lesson01_intro_to_data_science          lesson03a_numpy                         	lesson04_matplotlib_and_EDA
	mymac:classes joe$ cd lesson04_matplotlib_and_EDA/
	mymac:lesson04_matplotlib_and_EDA joe$ ls
	DataVizLecture_v2.pdf                 Visualization_Instructional_Set.ipynb 	data                                  readme.md
	mymac:lesson04_matplotlib_and_EDA joe$
	
### Do the Lesson

But don't push any changes.

	ipython notebook
	
