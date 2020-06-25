# MCT_n_and_k
Calculate the n and k values as a function of wavelength for MCT with a certain composition. 

## Basic Requirement: 

Python 3 (If not preinstalled, download it [here](https://www.python.org/downloads/) ); 

Python Numpy package;

Python Matplotlib package. 

If these two packages are missing, please run terminal/cmd and use pip to intall. For example, assuming Python 3 is already preinstalled in Windows, type the following command in cmd: 

`python -m pip install Numpy`

For a detailed instruction, please visit: [How to install Numpy](https://numpy.org/install/) and [How to install Matplotlib](https://matplotlib.org/users/installing.html#installing). 


## How to run: 
Changing parameters: Modify "n_and_k.py" line #127-131: 

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

Uncomment line #134 to print all result in terminal/cmd; 

Uncomment line #135 to plot n and k as a function of wavelength. 

Once everything is set up, run "n_and_k.py" in terminal/cmd.   

## Output: 
The output contains n, k1, k2 as a function of wavelength in micron. 

k1 is calculated using exponential absorption characteristic near the Urbach tail region; while k2 is calculated using power^1/2 absorption characteristic in the intrinsic region. So when the wavelength range under consideration is in the intrinsic region (can be checked by comparing the wavelength range with cutoff wavelength which is printed in terminal/cmd), k2 should always be used. 
