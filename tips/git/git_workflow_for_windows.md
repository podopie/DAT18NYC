# Git Workflow for Windows

[xkcd git commit fun](http://xkcd.com/1296/)

This workflow assumes you are starting in your your **personal Documents folder on Windows** (this makes finding things in Windows Explorer super easy) and that you will only use the command line (```Start > run > cmd.exe```) for git interaction.

This means C:\\Users\\*username*\\Documents
```posh
C:\Users\Joe\Documents>cd
C:\Users\Joe\Documents

C:\Users\Joe\Documents>
```
## Lectures Repository

You do not need to fork the [Lectures](https://github.com/podopie/DAT18NYC) repository because **you will never be pushing to the Lectures repository**.

### Clone the Lectures Repository
```posh
git clone https://github.com/podopie/DAT18NYC.git
```
**Example**:

```posh
C:\Users\Joe\Documents>git clone git clone https://github.com/podopie/DAT18NYC.git

Cloning into 'DAT18NYC'...
remote: Counting objects: 824, done.
remote: Compressing objects: 100% (432/432), done.
Remote: Total 824 (delta 360), reused 716 (delta 298)eceiving objects:  93% (76
Receiving objects: 100% (824/824), 19.42 MiB | 882.00 KiB/s, done.

Resolving deltas: 100% (360/360), done.
Checking connectivity... done.

C:\Users\Joe\Documents>
```
### Update For Every classes
```posh
cd DAT18NYC
git pull origin master
```
**Example:**
```posh
C:\Users\Joe\Documents>cd DAT18NYC

C:\Users\Joe\Documents\DAT18NYC>git pull origin master
From https://github.com/podopie/DAT18NYC
 * branch            master     -> FETCH_HEAD
Already up-to-date.

C:\Users\Joe\Documents\DAT18NYC>
```
### Change Directory to the Current Lesson
```posh
cd classes
cd lesson0x_abc
```
**Example:**
```posh
C:\Users\Joe\Documents\DAT18NYC>cd classes

C:\Users\Joe\Documents\DAT18NYC\classes>dir
 Volume in drive C has no label.
 Volume Serial Number is 6C01-BBC7

 Directory of C:\Users\Joe\Documents\DAT18NYC\classes

04/18/2014  09:11 PM    <DIR>          .
04/18/2014  09:11 PM    <DIR>          ..
04/18/2014  09:11 PM    <DIR>          lesson01_intro_to_data_science
04/18/2014  09:11 PM    <DIR>          lesson02_data_collection_and_extraction
04/18/2014  09:11 PM    <DIR>          lesson03a_numpy
04/18/2014  09:11 PM    <DIR>          lesson03b_pandas
04/18/2014  09:11 PM    <DIR>          lesson04_matplotlib_and_EDA
04/18/2014  09:11 PM                43 README.md
	           1 File(s)             43 bytes
    	       7 Dir(s)  37,088,002,048 bytes free

C:\Users\Joe\Documents\DAT18NYC\classes>cd lesson04_matplolib_and_EDA

C:\Users\Joe\Documents\DAT18NYC\classes\lesson04_matplotlib_and_EDA>dir
 Volume in drive C has no label.
 Volume Serial Number is 6C01-BBC7

 Directory of C:\Users\Joe\Documents\DAT18NYC\classes\lesson04_matplotlib_and_EDA

04/18/2014  09:11 PM    <DIR>          .
04/18/2014  09:11 PM    <DIR>          ..
04/18/2014  09:11 PM    <DIR>          .ipynb_checkpoints
04/18/2014  09:11 PM    <DIR>          data
04/18/2014  09:11 PM         1,429,481 DataVizLecture_v2.pdf
04/18/2014  09:11 PM               988 readme.md
04/18/2014  09:11 PM            95,844 Visualization_Instructional_Set.ipynb
	           3 File(s)      1,526,313 bytes
    	       4 Dir(s)  37,088,002,048 bytes free

C:\Users\Joe\Documents\DAT18NYC\classes\lesson04_matplotlib_and_EDA>
```
### Do the Lesson

But don't push any changes.
```posh
ipython notebook
```
