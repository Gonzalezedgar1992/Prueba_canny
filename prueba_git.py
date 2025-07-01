import matplotlib
matplotlib.use('Qt5Agg')  # Necesita PyQt o PySide
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import numpy as np


#plt.close('all')
# Datos simples (puedes reemplazar por tus vectores x, s_1, s_2, s_3)
x = np.array([0, 8, 16, 24, 32, 40])
s_1 = np.array([520, 528, 532, 537, 545, 548])
s_2 = np.array([523, 530, 533, 539, 546, 549])
s_3 = np.array([521, 529, 534, 538, 547, 550])

# Tamaño de la figura en cm -> pulgadas (1 pulgada = 2.54 cm)
fig_width_cm = 20
fig_height_cm = 15
figsize_inches = (fig_width_cm / 2.54, fig_height_cm / 2.54)

# Crear figura y ejes
fig, ax = plt.subplots(figsize=figsize_inches)

# Graficar curvas con distintos marcadores y estilos
ax.plot(x, s_1, '-or', label='CaCl$_2$–6H$_2$O', markersize=4, markerfacecolor='r', linewidth=2)
ax.plot(x, s_2, '-*k', label='RT-25', markersize=4, markerfacecolor='k', linewidth=2)
ax.plot(x, s_3, ':>b', label='RT-27', markersize=4, markerfacecolor='b', linewidth=2)

# Configurar leyenda
leg = ax.legend(loc='upper left', fontsize=8.5, frameon=False)
leg.set_title(None)

# Etiquetas de ejes con LaTeX
ax.set_xlabel('Thickness, mm', fontsize=10)
ax.set_ylabel('Energy, kWh', fontsize=10)

# Límites y ticks
ax.set_xlim(0, 40)
ax.set_xticks([0, 8, 16, 24, 32, 40])
ax.set_ylim(519, 550.5)

# Estilo de los ejes
ax.tick_params(direction='in', length=3, width=1, labelsize=15)
ax.set_facecolor('white')
ax.grid(False)
ax.set_title('', fontsize=15)

# Activar LaTeX en todo el plot (requiere tener LaTeX instalado)
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'

# Guardar como PDF con buena calidad
plt.tight_layout()
plt.savefig('FiguraD5_python.pdf', format='pdf', dpi=300)

print("Figura guardada como 'FiguraD5_python.pdf'")
plt.show()
#plt.pause(5)  # muestra la figura 2 segundos
