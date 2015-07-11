from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

casetitle = 'hsimt'


datafile = 'ocean_his.nc'
figtitle = 'River plume by: '+casetitle.upper()
ncfile = Dataset(datafile,'r') 
xi_rho = ncfile.dimensions['xi_rho']
eta_rho = ncfile.dimensions['eta_rho']
s_rho = ncfile.dimensions['s_rho']
s_w = ncfile.dimensions['s_w']
x_rho=ncfile.variables['x_rho'][:]
y_rho=ncfile.variables['y_rho'][:]
mask_rho=ncfile.variables['mask_rho'][:]
salt = ncfile.variables['salt'][:]
u = ncfile.variables['u'][:]
v = ncfile.variables['v'][:]
ocean_time = ncfile.variables['ocean_time'][:]
ntime,nz,ny,nx = salt.shape

x_rho = x_rho/1000.
y_rho = y_rho/1000.


u_rho = np.zeros((ntime,nz,ny,nx))
v_rho = np.zeros((ntime,nz,ny,nx))

u_rho[:,:,1:ny-1,1:nx-1] = 0.5*(u[:,:,1:ny-1,:nx-2]+u[:,:,1:ny-1,1:])
v_rho[:,:,1:ny-1,1:nx-1] = 0.5*(v[:,:,:ny-2,1:nx-1]+v[:,:,1:,1:nx-1])

u_rho[np.abs(u_rho)>10.]=0.
v_rho[np.abs(v_rho)>10.]=0.

intervalx = 2
intervaly = 1
minspeed = 0.03
x = x_rho[::intervaly,::intervalx]
y = y_rho[::intervaly,::intervalx]
maskrho = mask_rho[::intervaly,::intervalx]
maskrho = 1. - maskrho
for i in np.arange(0,ntime):
    fig = plt.figure()
    
# Plot surface salinity    
    cmap=plt.cm.RdYlBu
    cmap.set_bad(color = [0.75,0.75,0.75], alpha = 1.)
    plt.pcolormesh(x_rho,y_rho,salt[i,nz-1,:,:],cmap=cmap,edgecolors = 'None',vmin=22,vmax=32)
    cb = plt.colorbar(label='Salinity')
    cb.ax.tick_params(labelsize=10)
    
# Plot surface currents
    maskuv=maskrho.copy()
    uu0=u_rho[i,nz-1,::intervaly,::intervalx]
    vv0=v_rho[i,nz-1,::intervaly,::intervalx]
    maskuv[np.sqrt(uu0**2+vv0**2)<minspeed] = 1.
    
    uu= np.ma.masked_array(uu0,mask=maskuv)
    vv= np.ma.masked_array(vv0,mask=maskuv)
    
    
    Q = plt.quiver(x,y,uu,vv,angles='xy',scale=3,color='w',width=0.005)
#    plt.quiver(40,170,0.2,0,angles='xy',scale=3,color='w')
    qk = plt.quiverkey(Q, 0.7, 0.92, 0.2, '20 cm/s',labelcolor='w',labelpos='W',fontproperties={'size': 10})
    
    plt.xlim([0,50.])
    plt.ylim([60.,180.])
    ax = fig.gca()
    ax.set_aspect('equal')
    hour=int(ocean_time[i]//3600.)
    figtitle1 = figtitle+'\n No.' +str(hour).zfill(3)+' hr'
    plt.title(figtitle1,fontsize=10)
    plt.xlabel('Distance(km)',fontsize=12)
    plt.ylabel('Distance(km)',fontsize=12)
    figname='pyplume_'+str(i).zfill(3)+'.png'
    plt.savefig(figname,dpi=600,bbox_inches='tight')
    plt.close(fig)
#plt.show()
