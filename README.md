# Audio Compression

**Project Completed on 31 March 2019**

**Coding the Filter**

The running mean is a case of the mathematical operation of convolution. For the running mean, you slide a window along the input and compute the mean of the window's contents. For discrete 1D signals, convolution is the same thing, except instead of the mean you compute an arbitrary linear combination, i.e. multiply each element by a corresponding coefficient and add up the results. Those coefficients, one for each position in the window, are sometimes called the convolution kernel. Now, the arithmetic mean of N values is (x_1 + x_2 + ... + x_N) / N, so the corresponding kernel is (1/N, 1/N, ..., 1/N), and that's exactly what we get by using np.ones((N,))/N.

In this particular version of the program, we have coded a low pass filter with a set cutoff frequency by using the aforementioned concept of a running mean without actually using the scipy.signals module which contains a function called lfilter which is used to implement a digital low pass filter. 


# Authors

**N Krishna**    (https://github.com/NanaKrish)

**Hariharan S V**  (https://github.com/Hariharan20)

# Contributors

**Krishnan S G**  (https://github.com/KrishnanSG)

**K R Charan**     (https://github.com/KRC-Swaag)
