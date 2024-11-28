from pythia6tool.particlecodes import getParticleName

def getTrackRecordsByParticle(eventrecord, particlecode):
    """
    

    Parameters
    ----------
    eventrecord : EventRecord

    Returns
    -------
    The TrackRecord objects of the requested particle type in the provided event.
    """
    
    trs = eventrecord.getTrackRecords()
    
    ret = []
    
    for tr in trs:
        if tr.K2 == particlecode:
            ret.append(tr)
            
            
    return ret



def getParticleStatistics(eventrecord):
    stat  = dict()
    
    for tr in eventrecord.getTrackRecords():
        if tr.K2 in stat.keys():
            stat[tr.K2] += 1
        else:
            stat[tr.K2] = 1
    
    return stat

def printParticleStatistics(eventrecord):
    
    stat = getParticleStatistics(eventrecord)
    
    for key in stat.keys():
        print(getParticleName(key) + " : " + str(stat[key]))
        
        
def getUndecayedParticles(eventrecord):
    
    ret = []
    
    for tr in eventrecord.getTrackRecords():
        if tr.K1 == 1 or tr.K1 == 4:
            ret.append(tr)
            
    return ret

def printUndecayedParticles(eventrecord):
    
    for tr in getUndecayedParticles(eventrecord):
        print(getParticleName(tr.K2) + " (status code: " + str(tr.K1) + " )")
            

def tracebackParticleHistory(eventrecord, trackrecord):
    """
    

    Parameters
    ----------
    eventrecord : EventRecord
        DESCRIPTION.
    trackrecord : TrackRecord
        TrackRecord of the particle to be traced back in the EventRecord.

    Returns
    -------
    List of TrackRecords which belong to the decay chain.

    """
    
    trs = eventrecord.getTrackRecords()
    
    decaychain = [trackrecord]
    
    parent = decaychain[len(decaychain)-1]
    
    while not parent.K3 == 0:
        parent = trs[parent.K3-1]
        decaychain.append(parent)
    
    return list(reversed(decaychain))
        

def printParticleHistory(eventrecord, trackrecord):
    """
    

    Parameters
    ----------
    eventrecord : EventRecord
        DESCRIPTION.
    trackrecord : TrackRecord
        TrackRecord of the particle to be traced back in the EventRecord.

    -------
    Prints all particles which belong to the decay chain.

    """
    decaychain = tracebackParticleHistory(eventrecord, trackrecord)
    
    for i in range(len(decaychain)):
        
        tr = decaychain[i]
        print(tr.getParticleName() , end=" ")
        if(i<len(decaychain)-1):
            print("-->", end=" ")
    