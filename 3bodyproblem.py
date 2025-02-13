import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import time

#massas dos três corpos

m1 = 1.0
m2 = 1.0
m3 = 1.0

#posições e velocidades iniciais dos três corpos

posicao_inicial_1 = [0.5, 0.0, 0.0]
posicao_inicial_2 = [-0.5, 0.0, 0.0]
posicao_inicial_3 = [0.0, 0.0, 1.0]

velocidade_inicial_1 = [0.0, -0.347111, 0.0]
velocidade_inicial_2 = [0.0,0.347111, 0.0]
velocidade_inicial_3 = [0.0, 0.0, -0.1]

condicoes_iniciais = np.array([
    posicao_inicial_1, posicao_inicial_2, posicao_inicial_3,
    velocidade_inicial_1, velocidade_inicial_2, velocidade_inicial_3 
]).ravel()


#definindo sistema de EDO's de **primeira ordem**
def sistema_edos(t, S, m1, m2, m3):
    print(S)
    x1, x2, x3 = S[0:3], S[3:6], S[6:9]
    dx1_dt, dx2_dt, dx3_dt = S[9:12], S[12:15], S[15:18]

    f1, f2, f3 = dx1_dt, dx2_dt, dx3_dt

    df1_dt = m3*(x3-x1)/np.linalg.norm(x3-x1)**3 + m2*(x2-x1)/np.linalg.norm(x2-x1)**3
    df2_dt = m3*(x3-x2)/np.linalg.norm(x3-x2)**3 + m1*(x1-x2)/np.linalg.norm(x1-x2)**3
    df3_dt = m1*(x1-x3)/np.linalg.norm(x1-x3)**3 + m2*(x2-x3)/np.linalg.norm(x2-x3)**3

    return np.array([f1,f2,f3,df1_dt,df2_dt,df3_dt]).ravel()

#resolvendo o problema numericamente
tempo_i, tempo_f = 0, 25
t_pontos = np.linspace(tempo_i, tempo_f, 1501)

solucao = solve_ivp(
    fun = sistema_edos,
    args = (m1, m2, m3),
    t_span=(tempo_i, tempo_f),
    y0 = condicoes_iniciais,
    t_eval=t_pontos,)

t_sol = solucao.t
p1x_sol = solucao.y[0]
p1y_sol = solucao.y[1]
p1z_sol = solucao.y[2]

p2x_sol = solucao.y[3]
p2y_sol = solucao.y[4]
p2z_sol = solucao.y[5]

p3x_sol = solucao.y[6] 
p3y_sol = solucao.y[7]
p3z_sol = solucao.y[8]

#plotando as soluções

fig, ax = plt.subplots(subplot_kw={"projection":"3d"}, figsize=(10,10))

planeta1_plt, = ax.plot(p1x_sol, p1y_sol, p1z_sol, 'black', label ='Planeta 1', linewidth = 1)
planeta2_plt, = ax.plot(p2x_sol, p2y_sol, p2z_sol, 'red', label = 'Planeta 2', linewidth = 1)
planeta3_plt, = ax.plot(p3x_sol, p3y_sol, p3z_sol, 'orange', label ='Planeta 3', linewidth = 1)

planeta1_dot, = ax.plot([p1x_sol[-1]], [p1y_sol[-1]], [p1z_sol[-1]], 'o', color = 'black', markersize = 5 )
planeta2_dot, = ax.plot([p2x_sol[-1]], [p2y_sol[-1]], [p2z_sol[-1]], 'o', color = 'red', markersize = 5)
planeta3_dot, = ax.plot([p3x_sol[-1]], [p3y_sol[-1]], [p3z_sol[-1]], 'o', color = 'orange', markersize = 5)

ax.set_title("Problema dos 3 corpos")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.grid()
plt.legend()


#animando os resultados com matplotlib

from matplotlib.animation import FuncAnimation

def update(frame):
    x_atual_1 = p1x_sol[0:frame+1]
    y_atual_1 = p1y_sol[0:frame+1]
    z_atual_1 = p1z_sol[0:frame+1]

    x_atual_2 = p2x_sol[0:frame+1]
    y_atual_2 = p2y_sol[0:frame+1]
    z_atual_2 = p2z_sol[0:frame+1]

    x_atual_3 = p3x_sol[0:frame+1]
    y_atual_3 = p3y_sol[0:frame+1]
    z_atual_3 = p3z_sol[0:frame+1]

    planeta1_plt.set_data(x_atual_1, y_atual_1)
    planeta1_plt.set_3d_properties(z_atual_1)

    planeta1_dot.set_data([x_atual_1[-1]], [y_atual_1[-1]])
    planeta1_dot.set_3d_properties([z_atual_1[-1]])

    planeta2_plt.set_data(x_atual_2, y_atual_2)
    planeta2_plt.set_3d_properties(z_atual_2)

    planeta2_dot.set_data([x_atual_2[-1]], [y_atual_2[-1]])
    planeta2_dot.set_3d_properties([z_atual_2[-1]])

    planeta3_plt.set_data(x_atual_3, y_atual_3)
    planeta3_plt.set_3d_properties(z_atual_3)

    planeta3_dot.set_data([x_atual_3[-1]], [y_atual_3[-1]])
    planeta3_dot.set_3d_properties([z_atual_3[-1]])

    return planeta1_plt, planeta1_dot, planeta2_plt, planeta2_dot, planeta3_plt, planeta3_dot

animation = FuncAnimation(fig, update, frames=range(0,len(t_pontos), 2), interval = 20, blit = True)

from matplotlib.animation import FFMpegWriter

# Configuração do FFMpegWriter com parâmetros ajustados
mp4_writer = FFMpegWriter(fps=60, bitrate=5000)  # FPS alto e bitrate para alta qualidade

# Salvar a animação como um vídeo MP4 em alta resolução
animation.save("problema_tres_corpos_alta_qualidade.mp4", writer=mp4_writer, dpi=300)  # Alta resolução com dpi=300


plt.show()