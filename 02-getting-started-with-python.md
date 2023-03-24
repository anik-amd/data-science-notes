### Getting Started With Python

### Anaconda

Anaconda is a platform for data science with Python. It includes all the essential libraries to perform various data science related tasks.

### Miniconda

Miniconda is a free minimal installer for conda. It is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others.

### Installing Miniconda

```
winget install miniconda3
```

Now use `conda install` to install additional packages from Anaconda repository.

### Virtual Environments

Data science projects requires various combinations of Python version and libraries. A single python installation can cause conflicts and other problems with those libraries. To solve this problem, _virtual environments_ are used.

To create virtual environment with `conda` use,

```
conda create -n Test python=3.6
```

### Conda Cheat sheet

1. Create an empty environment:

```
conda create --name {env_name}
```

2. Create an empty environment with specific python version:

```
conda create --name {env_name} python={version}
```

3. Activate the environment:

```
conda activate {env_name}
```

4. Deactivate the environment:

```
conda deactivate {env_name}
```

5. Install packages with `conda`:

```
conda install pkg_name1==1.x.y pkg_name2==1.x.y
```

6. Install packages with `pip`:

```
pip install pkg_name2==1.x.y pkg_name2==1.x.y
```

7. List of packages installed with `conda`:

```
conda list
```

8. List of packages in specific environment:

```
conda list -n {env_name}
```

9. list of environments:

```
conda env list
```

10. Remove an environment:

```
conda env remove -n {env_name}
```

_Make sure you are not in the environment._

11. Sharing environments across platfroms

```
conda env export --from-history > environment.yml
```

Adding --from-history flag will install only the packages you asked for using conda. It will NOT include the dependency packages or packages you installed using any other method.

Now, recreate the environment using

```
conda env create -f environment.yml
```

# References

- [Data Science from Scratch: First Principles with Python by Joel Grus](https://www.goodreads.com/en/book/show/25407018)

- [Conda create environment and everything you need to know to manage conda virtual environment](https://www.machinelearningplus.com/deployment/conda-create-environment-and-everything-you-need-to-know-to-manage-conda-virtual-environment/)
