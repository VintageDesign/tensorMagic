def itfft(t):
    s = t.shape()
    s = len(s)
    for i in range(0, s):
        t = np.fft.ifft(t, axis=i)
        # I think this works...
    return t

