import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# OBJECTIVE
# To determine the curie temperature for the given
# material.

# OPERATION

# 1st cell:
# Size affects the size of the electron array
# Runs affects the amount of times the electron array
# is flipped
# Trials affects the amount of trials ran per temperature
# The values in Temp can be adjusted to see the effect of
# various temperatures on the convergence of the array

# 2nd cell:
# Nothing can be changed here

# 3rd/4th/5th cell:
# steps affects the sequencing of array snapshots
# that are taken

# Amount of row/cols in square array
size = 50
# Number of iterations
runs = 600000
# Number of trials per temperature
trials = 5
# Array of temperatures to calculate the moment at
Temp = [0.01, 0.1, 1, 2, 3, 4, 5, 10, 100]


def gen_arr(size):
    """
    Returns an array of 1's and -1's representing
    the spin state of a grid of electrons
    """
    return np.where(np.random.rand(size, size) < 0.5, -1, 1)


def spinChange(elecArr, runs, t):
    """
    Calculates the change in energy from flipping
    the spin of a single electron, and either
    accepts the change if the energy is lower,
    or if the probability function is met

    elecArr is the array of electrons
    runs is the amount of iterations to calculate through
    t is the temperature from the temperature array
    """
    # store the size of the array
    xDim = np.shape(elecArr)[0]
    yDim = np.shape(elecArr)[1]

    for i in range(runs):
        # generate a random point in the array
        a = np.random.randint(0, xDim)
        b = np.random.randint(0, yDim)

        # Calculates the energy of the random point
        init = (-elecArr[a, b]) * (elecArr[(a + 1) % xDim, b] +
                                   elecArr[a - 1, b] +
                                   elecArr[a, (b + 1) % yDim] +
                                   elecArr[a, b - 1])
        # Calculates the change in energy of the new configuration
        # for the random point
        change = -2 * init

        # If the energy of the new config is lower, accept it
        if(change <= 0):
            elecArr[a, b] *= -1
        else:
            # calculate the probability of accepting the higher
            # energy configuration
            prob = np.exp(-change / t)
            chance = np.random.rand()
            if(chance < prob):
                elecArr[a, b] *= -1
    return elecArr


def moment(elecArr):
    """
    Returns the magnetic moment of the electron grid

    elecArr is the electron spin array
    """
    return np.sum(elecArr) / np.size(elecArr)


def maxMoments(Temp, trials, size, runs):
    """
    Returns a list of the maximum magnetic moments
    for each temperature in the array

    Temp is the temperature array
    trials is the amount of trials to run per temperature
    size is the size of the electron array
    runs is the amount of iterations to calculate the spins
    """
    # Stores the maximum magnetic moments of each temperature
    maximum = []
    for i in range(len(Temp)):
        trialMag = []
        for j in range(trials):
            elecArr = gen_arr(size)
            spinChange(elecArr, runs, Temp[i])
            magnet = moment(elecArr)
            trialMag.append(magnet)
        # Stores the largest of the magnetic moments for each trial
        maximum.append(max(abs(np.array(trialMag)))
    return maximum


# Creates an initial configuration
elecArr = gen_arr(size)

# Stores the list of maximum magnetic moments
max_Moments = maxMoments(Temp, trials, size, runs)

# Calculate M vs T and plot it here
plt.style.use("dark_background")
plt.title("Magnetic Moment vs"
          "Log10 of Temperature")
plt.xlabel("Magnetic Moment")
plt.ylabel("Log10 of Temperature")
plt.plot(np.log10(Temp), max_Moments)
print("The Curie Temperature is about 2.5")

# Generate 1st animation here
# YOUR CODE HERE

fig = plt.figure()
# list of images
ims = []
# The amount of frames to render the video
numFrames = 120

elecArr = gen_arr(size)

# Store the initial configuration
ims.append((plt.pcolormesh(elecArr), ))

# Stores as many frames as previously determined
for i in range(numFrames):
    elecArr = spinChange(elecArr, 2000, Temp[1])
    ims.append((plt.pcolormesh(elecArr.copy()), ))

# Generate the video
imani = animation.ArtistAnimation(fig, ims, interval=50, repeat=False)

# Save the video
imani.save('50x50low.webm', extra_args=['-vcodec', 'libvpx'])
plt.close()

# Clear up the memory for newly generated videos
del ims
del imani

# Create an interactable video UI
HTML('<video controls autoplay>' +
     '<source src="50x50low.webm" type="video/webm"></video>')

# Generate 2nd animation here
# YOUR CODE HERE

fig = plt.figure()
# list of images
ims = []
# The amount of frames to render the video
numFrames = 120

elecArr = gen_arr(size)

# Store the initial configuration
ims.append((plt.pcolormesh(elecArr), ))

# Stores as many frames as previously determined
for i in range(numFrames):
    elecArr = spinChange(elecArr, 2000, 2.5)
    ims.append((plt.pcolormesh(elecArr.copy()), ))

# Generate the video
imani = animation.ArtistAnimation(fig, ims, interval=50, repeat=False)

# Save the video
imani.save('50x50med.webm', extra_args=['-vcodec', 'libvpx'])
plt.close()

# Clear up the memory for newly generated videos
del ims
del imani

# Create an interactable video UI
HTML('<video controls autoplay>' +
     '<source src="50x50med.webm" type="video/webm"></video>')

# Generate 3rd animation here
# YOUR CODE HERE

fig = plt.figure()
# list of images
ims = []
# The amount of frames to render the video
numFrames = 120

elecArr = gen_arr(size)

# Store the initial configuration
ims.append((plt.pcolormesh(elecArr), ))

# Stores as many frames as previously determined
for i in range(numFrames):
    elecArr = spinChange(elecArr, 2000, Temp[-1])
    ims.append((plt.pcolormesh(elecArr.copy()), ))

# Generate the video
imani = animation.ArtistAnimation(fig, ims, interval=50, repeat=False)

# Save the video
imani.save('50x50high.webm', extra_args=['-vcodec', 'libvpx'])
plt.close()

# Clear up the memory for newly generated videos
del ims
del imani

HTML('<video controls autoplay>' '<source src="50x50high.webm" + type="video/webm"></video>')