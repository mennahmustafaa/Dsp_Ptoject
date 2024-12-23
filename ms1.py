import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Configuration
sampling_frequency = 1000  # Sampling frequency (Hz)
time_cont = np.linspace(0, 1, 1000)  # Time vector for continuous signal
time_disc = np.arange(0, 1, 1/sampling_frequency)  # Time vector for discrete signal

# Signal Parameters
frequency_signal = 5  # Frequency of the sinusoidal wave
signal_amplitude = 1

# 1. Generate and Plot Signals
## 1.1 Sinusoidal Wave
continuous_sine_wave = signal_amplitude * np.sin(2 * np.pi * frequency_signal * time_cont)
discrete_sine_wave = signal_amplitude * np.sin(2 * np.pi * frequency_signal * time_disc)

## 1.2 Square Wave
square_wave = np.sign(np.sin(2 * np.pi * frequency_signal * time_cont))

## Plotting the Signals
plt.figure(figsize=(12, 8))

# Sinusoidal Waves
plt.subplot(3, 2, 1)
plt.plot(time_cont, continuous_sine_wave, label="Continuous Sinusoidal Signal", color='b')
plt.title("Continuous Sinusoidal Signal")
plt.legend()

plt.subplot(3, 2, 2)
plt.stem(time_disc, discrete_sine_wave, label="Discrete Sinusoidal Signal", basefmt=" ", linefmt="b")
plt.title("Discrete Sinusoidal Signal")
plt.legend()

# Square Wave
plt.subplot(3, 2, 3)
plt.plot(time_cont, square_wave, label="Square Wave", color='r')
plt.title("Square Wave")
plt.legend()

plt.tight_layout()
plt.show()

# 1.3 Real-world Signals from Files
# Create a simple file with random data (simulating a real-world signal)
real_world_signal = np.sin(2 * np.pi * 2 * time_cont) + 0.5 * np.random.randn(len(time_cont))  # example noisy signal
np.savetxt("real_world_signal.txt", real_world_signal)

# Import and Plot Real-world Data from File
real_world_data = np.loadtxt("real_world_signal.txt")
plt.plot(time_cont, real_world_data, label="Real-world Signal", color='g')
plt.title("Real-world Signal from File")
plt.legend()
plt.show()

# 1.4 Custom Equation Signal
# Example: A combination of a sinusoidal and a square wave
custom_signal = 0.5 * np.sin(2 * np.pi * 5 * time_cont) + 0.5 * np.sign(np.sin(2 * np.pi * 10 * time_cont))

# Plot Custom Signal
plt.plot(time_cont, custom_signal, label="Custom Equation Signal", color='m')
plt.title("Custom Equation Signal")
plt.legend()
plt.show()

# 2. Sampling
sampling_rate = 50  # Sampling rate (Hz)
time_sampled = np.arange(0, 1, 1/sampling_rate)

# Sample the continuous sinusoidal signal
sampled_signal = signal_amplitude * np.sin(2 * np.pi * frequency_signal * time_sampled)

# Plot the original and sampled signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time_cont, continuous_sine_wave, label="Original Continuous Signal", color='purple')
plt.stem(time_sampled, sampled_signal, label="Sampled Signal", linefmt='r-', markerfmt='ro', basefmt=" ")
plt.title("Sampling of Continuous Signal")
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude")
plt.legend()

plt.tight_layout()
plt.show()

# 3. Quantization
quantization_levels = 8  # Number of quantization levels
quantized_signal = np.round(sampled_signal * (quantization_levels - 1)) / (quantization_levels - 1)

# Plot the quantized signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time_sampled, sampled_signal, label="Sampled Signal")
plt.stem(time_sampled, quantized_signal, 'g', label="Quantized Signal", basefmt=" ")
plt.title(f"Quantization with {quantization_levels} Levels")
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
