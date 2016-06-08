# Plotting
import matplotlib as mpl
import numpy as np
from .velocities import *
from .particles import *
# Select the graphics back end
# Apparently this has to happen 
# before importing pyplot.
mpl.use('TkAgg');

# Import pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')


# This function plots the vector field of velocities
# Todo: Convert list to array
# Get Correct velocity
def VectorField(ax, ParticleField = None):
    if ParticleField is not None:
	
        # Get all velocities
        x, y, z, u, v, w = ParticleField.GetVelocity()
       
		
        x_new = np.asarray(x)
        y_new = np.asarray(y)
        z_new = np.zeros(x_new.shape[0])
		
        u_new = np.asarray(u)
        v_new = np.asarray(v)
        w_new = np.zeros(u_new.shape[0])
        print(x_new.shape[0])
        print(y_new.shape[0])
        #print(z)
        print(u_new.shape[0])
        print(v_new.shape[0])
        #print(w)
        # Meshgrid the vectors
        x_rec, y_rec, z_rec, u_rec, v_rec, w_rec = np.meshgrid(x_new, y_new,z_new, u_new, v_new, w_new)
		
        print(x_rec.shape[0])
        print(y_rec.shape[0])
		
        print(u_rec.shape[0])
        print(v_rec.shape[0])
		
        # Plot Vector field of velocity
        ax.quiver(x_rec, y_rec, z_rec, u_rec, v_rec, w_rec, length = 0.01)

        plt.show()


# This function plots streaklines.
def StreakPlot(ax, ParticleField = None):
    if ParticleField is not None:
        
        # Get all the streakline
        x_streak, y_streak, z_streak, d_streak = ParticleField.GetStreaklines();
     
        # Number of streaklines
        n_streaks = len(x_streak);
        
        # Clear the axes
        for n in range(n_streaks):

            # Number of points in this streakline
            npoints = len(x_streak[n]);

            # Plot this streak line
            #ax.plot(x_streak[n], y_streak[n], '.');
            ax.plot(x_streak[n], y_streak[n], z_streak[n], '.');
            #ax.scatter( x_streak, y_streak, z_streak, c = 'r', marker = 'o')
            #plt.show()
            
            
def PathlinePlot(ax, ParticleField = None):
    if ParticleField is not None:
        
        # Loop over all the particles.
        for k in range(ParticleField.Count):
            
            # Extract the positions
            x = ParticleField.Particles[k].Position.History.X;
            y = ParticleField.Particles[k].Position.History.Y;
            
            # Make the plot
            ax.plot(x, y, '-');
            
def TimelinePlot(ax, ParticleField = None):
    if ParticleField is not None:
        
        # Initialize the position vectors
        x = [];
        y = [];
        
        # Loop over all the particles
        for k in range(ParticleField.Count):
        
            # Extract the positions
            x.append(ParticleField.Particles[k].Position.Current.X);
            y.append(ParticleField.Particles[k].Position.Current.Y);
        
        # Make the plot
        ax.plot(x, y, '.-k');
