import numpy as np 
import matplotlib.pyplot as plt

fs=100; dt=1/fs; N=300 #샘플링주파수=100Hz, 0.01초 간격으로 300개 샘플 
t=np.arange(0,N)*dt #시간축은 0.01초*300샘플=3초 
x1t=1.0*np.sin(2*np.pi*1*t) #크기 1, 주파수 1Hz 정현파신호 
x2t=1/3*np.sin(2*np.pi*3*t) #크기 1/3, 주파수 3Hz 정현파신호 
x3t=1/5*np.sin(2*np.pi*5*t) #크기 1/5, 주파수 5Hz 정현파신호 
xt=x1t+x2t+x3t #서 신호의 합성

df=fs/N #주파수간격 
f=np.arange(0,N)*df #주파수축 0~50 Hz(0~fs/2) 
Xf=np.fft.fft(xt) #주파수별 크기 계산 (FFT) 

plt.subplot(5,1,1); plt.plot(t,xt, "b"); plt.ylim(-1,1); plt.grid() 
plt.ylabel("x(t)") 
plt.title("A periodic rectangular signal x(t)=x1(t)+x2(t)+x3(t)") 
plt.subplot(5,1,2); plt.plot(t,x1t, "b"); plt.ylim(-1,1); plt.grid() 
plt.ylabel("x1(t)") 
plt.subplot(5,1,3); plt.plot(t,x2t, "b"); plt.ylim(-1,1); plt.grid() 
plt.ylabel("x2(t)") 
plt.subplot(5,1,4); plt.plot(t,x3t, "b"); plt.ylim(-1,1); plt.grid() 
plt.ylabel("x3(t)") 
plt.subplot(5,1,5); plt.plot(f[0:int(N/2+1)],np.abs(Xf[0:int(N/2+1)]),"b"); 
plt.xlabel("frequency(Hz)"); plt.ylabel("Spectrum x(f)"); plt.grid()

plt.show()