import matplotlib.pyplot as plt
import control
import numpy as np
import seaborn as sns

# Set the style to a modern, clean theme
plt.style.use('seaborn-v0_8')
sns.set_style("whitegrid", {'grid.linestyle': ':'})
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['text.usetex'] = True  # Enable LaTeX rendering

# Define system parameters
NATURAL_FREQUENCY = 1.0  # Natural frequency (wn)
DAMPING_RATIO = 0.5      # Damping ratio (zeta)

# Create a second-order transfer function
numerator = [NATURAL_FREQUENCY**2]
denominator = [1, 2 * DAMPING_RATIO * NATURAL_FREQUENCY, NATURAL_FREQUENCY**2]
G = control.TransferFunction(numerator, denominator)

# Get step response
t, y = control.step_response(G)

# Get step response characteristics
info = control.step_info(G)

# Extract key values
rise_time = info['RiseTime']
peak_time = info['PeakTime']
peak_value = info['Peak']
settling_time = info['SettlingTime']
overshoot = info['Overshoot']

# Function to find the nearest index in the time array
def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx

# Create figure
plt.figure(figsize=(14, 8))
ax = plt.gca()

# Custom color palette
main_color = '#2E86AB'  # Blue
steady_state_color = '#D64933'  # Red
annotation_color = '#1B1B1E'  # Dark gray
grid_color = '#E5E5E5'  # Light gray
overshoot_color = '#FF6B6B'  # Coral for overshoot arrow
settling_color = '#6C757D'  # Gray for settling bounds

# Main plot
plt.plot(t, y, label='Step Response', linewidth=3, color=main_color)
plt.axhline(y=1, color=steady_state_color, linestyle='--', label='Steady-State Value', linewidth=2, alpha=0.8)
plt.axhline(y=1.02, color=settling_color, linestyle=':', label='±2% Bounds', linewidth=1.5, alpha=0.6)
plt.axhline(y=0.98, color=settling_color, linestyle=':', linewidth=1.5, alpha=0.6)

# Create shaded regions for better visualization
plt.fill_between(t, y, 1, where=(y > 1), color=main_color, alpha=0.15, interpolate=True, label='Error')
plt.fill_between(t, y, 1, where=(y < 1), color=main_color, alpha=0.1, interpolate=True)

# Plot vertical lines with gradient alpha and symbolic annotations
# Rise Time
plt.vlines(rise_time, 0, y[find_nearest(t, rise_time)], colors=annotation_color, linestyles=':', alpha=0.3)
# Add point at rise time on the actual response curve
rise_time_y = y[find_nearest(t, rise_time)]
plt.plot(rise_time, rise_time_y, 'o', color=annotation_color, markersize=6)

# Add rise time y-value annotation with arrow
plt.annotate(r'$0.632y_{ss}$', 
            xy=(rise_time, rise_time_y),  # Point to annotate
            xytext=(rise_time - 0.5, rise_time_y),  # Text position
            fontsize=12,
            color=annotation_color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.95, 
                     edgecolor=annotation_color, linewidth=1),
            ha='right',
            va='center',
            arrowprops=dict(arrowstyle='->', color=annotation_color, alpha=0.6))

# Add tr annotation without arrow
plt.annotate(r'$t_r$', 
            xy=(rise_time, 0.1),
            xytext=(rise_time, 0.1),
            fontsize=12,
            color=annotation_color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.95, 
                     edgecolor=annotation_color, linewidth=1),
            ha='center',
            va='center')

# Peak Time
plt.vlines(peak_time, 0, peak_value, colors=annotation_color, linestyles=':', alpha=0.3)
plt.annotate(r'$t_p$', 
            xy=(peak_time, peak_value - 0.5),
            xytext=(peak_time + 0.2, peak_value - 0.5),
            fontsize=12,
            color=annotation_color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.95, 
                     edgecolor=annotation_color, linewidth=1),
            ha='left',
            va='center',
            arrowprops=dict(arrowstyle='->', color=annotation_color, alpha=0.6))

# Add point at peak value
plt.plot(peak_time, peak_value, 'o', color=annotation_color, markersize=6)

# Add thick line at settling time between ±2% bounds
plt.vlines(settling_time, 0.98, 1.02, colors=settling_color, linewidth=3, alpha=0.8)

# Settling Time
plt.vlines(settling_time, 0, 1, colors=annotation_color, linestyles=':', alpha=0.3)
plt.annotate(r'$t_s$', 
            xy=(settling_time, 0.5),
            xytext=(settling_time + 0.2, 0.5),
            fontsize=12,
            color=annotation_color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.95, 
                     edgecolor=annotation_color, linewidth=1),
            ha='left',
            va='center',
            arrowprops=dict(arrowstyle='->', color=annotation_color, alpha=0.6))

# Add overshoot double-headed arrow with symbolic notation
plt.annotate('', xy=(peak_time, peak_value), 
            xytext=(peak_time, 1),
            arrowprops=dict(arrowstyle='<->', color=overshoot_color, 
                          linewidth=2, shrinkA=0, shrinkB=0))

# Add symbolic overshoot label
plt.annotate(r'$PO = \frac{y_{peak} - y_{ss}}{y_{ss}} \times 100\%$', 
            xy=(peak_time, (peak_value + 1)/2),
            xytext=(peak_time + 2.5, (peak_value + 1)/2),
            fontsize=11,
            color=annotation_color,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.95, 
                     edgecolor=annotation_color, linewidth=1),
            ha='left',
            va='center',
            arrowprops=dict(arrowstyle='->', color=annotation_color, alpha=0.6, linewidth=2))

# Add steady state annotation
plt.annotate(r'$y_{ss}$', 
            xy=(max(t)-0.5, 1),  # Point to the steady state line
            xytext=(max(t)-0.5, 0.8),  # Move text higher
            fontsize=12,
            color=steady_state_color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.95, 
                     edgecolor=steady_state_color, linewidth=1),
            ha='center',
            va='bottom',
            arrowprops=dict(arrowstyle='->', color=steady_state_color, 
                          alpha=0.8, linewidth=2))

# Add peak value annotation with adjusted position
plt.annotate(r'$y_{peak}$', 
            xy=(peak_time, peak_value),
            xytext=(peak_time - 0.3, peak_value + 0.05),
            fontsize=12,
            color=annotation_color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.95, 
                     edgecolor=annotation_color, linewidth=1),
            ha='right',
            va='bottom',
            arrowprops=dict(arrowstyle='->', color=annotation_color, alpha=0.6))

# Style the plot
plt.grid(True, which='major', color=grid_color, linewidth=1.2, alpha=0.8)
plt.grid(True, which='minor', color=grid_color, linewidth=0.8, alpha=0.5)
plt.xlim(-0.2, max(t) + 0.5)
plt.ylim(-0.1, max(y) + 0.3)
plt.title('Second-Order System Step Response', fontsize=16, pad=20, 
          color=annotation_color, fontweight='bold')
plt.xlabel('Time (s)', fontsize=12, labelpad=10, color=annotation_color)
plt.ylabel('Amplitude', fontsize=12, labelpad=10, color=annotation_color)
plt.legend(loc='upper right', fontsize=11, fancybox=True, framealpha=0.95, edgecolor=annotation_color)

# Adjust layout and save
plt.tight_layout()
plt.savefig('Second_Order_Response.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()