import matplotlib.pyplot as plt
import numpy
import modStore
from scipy.io import wavfile

[sampFreq, snd] = wavfile.read('440_sine.wav')
snd = snd/(2**15)
s1 = snd[:,0]
s12 = s1[:100]
FT_s12 = modStore.discrete_FT(s12, len(s12))
print(FT_s12)

timeArray = numpy.arange(0, 5292, 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds


plt.plot(timeArray, s1)
plt.suptitle('test title')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.show()



