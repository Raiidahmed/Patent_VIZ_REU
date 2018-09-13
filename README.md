#Patent Visualization Project

###[Applied Research Laboratory](https://www.arl.psu.edu/) and [THRED](http://thred.group/)

By Dr. Robert Fraleigh

**Research Question:** The basic goal of **Patent Visualization Project** is to explore information search strategies
impact characteristics of concepts when users are offered an interactive way to navigate 
the functional basis of a collection of US Patents.

## Installation

Clone the Repository: [Additional Help From Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone)

```console
git clone https://USERNAME@bitbucket.org/arldatasci/patent-visualization.git <DIRECTORY>
```

Install Requirements: [Additional Help from PIP](https://pip.pypa.io/en/stable/user_guide/)

```console
pip install -r requirements.txt
```

## Navigation
This repository has three parts:

* *data* => Store relevant data here. There are two subfolders for raw and cleaned data.

* *dashboard* => Contains the prototype visualization that the participants will use.

* *scripts* => Contains the python scripts that will be used in scraping / cleaning / processing patent data.

## Git Branches
[Read This Overview](https://hackernoon.com/understanding-git-fcffd87c15a3) if you are not familiar with git.

When you clone the repository, you often default to a master branch.  Think of the *Master* branch as we
migrate into production. It is gold.  And we do not want to inadvertantly mess it up.

So, once you clone the repository, checkout the develop branch. It is here where we will develop our code.  You can
even checkout a copy of the develop branch and rename it to **dev_USERNAME** to have a branch all to yourself.

Commit frequently.  This will save you time if you make a mistake and want to back to a previous version.

Push to the Develop Branch when you complete a task.

Pull occasionally from the Develop Branch so that you stay up to date with the evolution of the code.