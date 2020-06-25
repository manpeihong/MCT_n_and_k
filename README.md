# MCT_n_and_k
Calculate the n and k values as a function of wavelength for MCT with a certain composition. 

## Basic Requirement: 

Python 3; 

If not preinstalled, download it [here](https://www.python.org/downloads/) 

Python Numpy package;

Python Matplotlib package. 

If these two packages are missing, please run terminal/cmd and use pip to intall. For example, assuming Python 3 is already preinstalled in Windows, type the following command in cmd: 

`python -m pip install Numpy`

For a detailed instruction, please visit: [Here](https://numpy.org/install/) and [Here](https://matplotlib.org/users/installing.html#installing)


## How to run: 
Changing parameters: Modify "n_and_k.py" line 127-131: 

What material are under consideration: 

`material = "MCT"`

Composition:

`x = 0.3     # Hg1-xCdxTe`

Temperature: 

`temp=300    # Kelvin`

Wavelength range under consideration: 

`lamdas = np.arange(1, 3, 0.02)  # Start, stop and increment`

Whether or not to save the result to a local file: 

`save_to_file = True     # If true, the result will be saved to the root folder as a csv file. `

Once everything is set up, run "n_and_k.py" in terminal/cmd.   
