import matplotlib.pyplot as plt
import numpy as np

def plot_spiketrains(pop, simtime=None, fig=None, ax=None, 
                     color='r', markersize=4, verbose=False):
    """
    Plot all spike trains in a Segment in a raster plot.
    
    marker size is in points.
    
    """
    spiketrains = pop.get_data().segments[0].spiketrains
    
    if fig is None:
        fig, ax = plt.subplots(figsize = (12,8))
    if ax is None:
        ax = fig.subplot(1, 1)
    
    if simtime is None:
        from quantities import ms
        simtime = spiketrains[0].t_stop / ms

    if verbose: print('spiketrains[0].t_stop', spiketrains[0].t_stop)
    from sys import maxsize
    max_index = 0
    min_index = maxsize
    for spiketrain in spiketrains:
        ax.plot(spiketrain,
                 np.ones_like(spiketrain) * spiketrain.annotations['source_index'],
                 '|', c=color, markersize=markersize)
        max_index = max(max_index, spiketrain.annotations['source_index'])
        min_index = min(min_index, spiketrain.annotations['source_index'])
    ax.set_ylabel("Neuron index")
    ax.set_xlabel('Time(ms)')
    ax.set_xlim(0, simtime)
    ax.set_ylim(-0.5 + min_index, max_index + 0.5)
    return fig, ax

def spike_count_per_neuron(pop):
    sc = pop.get_spike_counts()
    return np.array([sc[i] for i in pop.all_cells])


def histogram(pop, do_fit=False, fig=None, ax=None, alpha=1., 
              color='g', lw=1, label='tc_cells', simtime=None):
    if fig is None:
        fig, ax = plt.subplots(figsize = (12,8))
    if ax is None:
        ax = fig.subplot(1, 1)
    
    if simtime is None:
        from quantities import ms
        spiketrains = pop.get_data().segments[0].spiketrains
        simtime = spiketrains[0].t_stop / ms
        
    ax.plot(spike_count_per_neuron(pop)/simtime*1000., color=color, lw=lw, alpha=alpha)
    
    if do_fit:
        from lmfit import Model, Parameters
        mod = Model(tuning_function)
        pars = Parameters()
        pars.add_many(('j', y.argmax(), True,  0.0, N), ('B', 15., True,  0.1, 360), 
                      ('fmax', y.max(), True,  0.0, 200.))

        #pars = mod.guess(y, x=x)
        #pars['center'] = lmfit.Parameter('center', seq_nbr*15)
        out = mod.fit(y, pars, x=x, nan_policy='omit')
        #print(out.fit_report(min_correl=0.25))

        #plot the fits
        out.plot_fit(ax = ax, datafmt = datacol, fitfmt = fitcol, data_kws = data_kws, show_init=False)
    
    return fig, ax