# -*- coding: utf-8 -*-

from pythia6tool.core import EventRecord
from pythia6tool.core import TrackRecord

def initialRead(evtfile_path, **kwargs):  
    """
    Parameters
    ----------
    evtfile_path : str
        The path for the pythia event file.
    **kwargs { highram : bool
              If highram is set to True (default), all the eventrecords will be loaded with their associated trackrecords.
              Otherwise the trackrecords will be loaded dynamically during runtime which can yield slower runtimes.
            }
            
    Returns list of EventRecord objects
    -------
    Initially all the events are read into EventRecord objects

    """
    highram = kwargs.get('highram', True)
    
    separator = "============================================"
        
    print("Reading " + evtfile_path + " ...")
    
    
    with open(evtfile_path) as infile:

        #TODO check what parameters are used in headers, e.g. V(I,4), V(I,5) currently not supported

        eventrecords = []
        evtinfo = ""

        trackStart = 0
        trackEnd = 0

        for i, line in enumerate(infile):


            if i < 6:
                # TODO: treat pythia headers
                pass

            elif separator in line:
                  trackStart = i+1
                  
                  
            elif trackStart == 0:
                evtinfo += line
            
            elif "Event finished" in line:
                trackEnd = i-1
                
                evt = evtinfo.split()
                              
                
                er = EventRecord(
                                    I=int(evt[0]),
                                    ievent=int(evt[1]),
                                    genevent=int(evt[2]),
                                    subprocess=int(evt[3]),
                                    nucleon=int(evt[4]),
                                    targetparton=int(evt[5]),
                                    xtargparton=float(evt[6]),
                                    beamparton=int(evt[7]),
                                    xbeamparton=float(evt[8]),
                                    thetabeamprtn=float(evt[9]),
                                    truey=float(evt[10]),
                                    trueQ2=float(evt[11]),
                                    truex=float(evt[12]),
                                    trueW2=float(evt[13]),
                                    trueNu=float(evt[14]),
                                    leptonphi=float(evt[15]),
                                    s_hat=float(evt[16]),
                                    t_hat=float(evt[17]),
                                    u_hat=float(evt[18]),
                                    pt2_hat=float(evt[19]),
                                    Q2_hat=float(evt[20]),
                                    F2=float(evt[21]),
                                    F1=float(evt[22]),
                                    R=float(evt[23]),
                                    sigma_rad=float(evt[24]),
                                    SigRadCor=float(evt[25]),
                                    EBrems=float(evt[26]),
                                    photonflux=float(evt[27]),
                                    t_diff=float(evt[28]),
                                    nrTracks=int(evt[29]),
                                    trackStart = trackStart,
                                    trackEnd = trackEnd,
                                    eventfile = evtfile_path
                                )
                    
                eventrecords.append(er)
                
                evtinfo = ""
                trackStart = 0
                trackEnd = 0
        
    if(highram):
                
        readTrackRecords(evtfile_path, eventrecords)
        
    print("Finished Reading.")
    
    return eventrecords

def readTrackRecords(evtfile_path,eventrecords):
    """
    

    Parameters
    ----------
    evtfile_path : str
        Path to eventfile.
    eventrecords : list[EventRecord]
        eventrecords to read
        
    Returns
    -------
    trackrecords : dict
        Returns a dictionary with the ievent index as key and a list of TrackRecord objects as values.

    """
    
    #necessary so we will only iterate over the file once
    trStartDict = dict()
    endDict = dict()
    
    for event in eventrecords:
        trStartDict[event.trackStart] = event
        endDict[event] = event.trackEnd
        
    
    startline = 10**10
    endline = 10**10
    
    with open(evtfile_path) as infile:
        
        
        for i, line in enumerate(infile):
            
            
            if i+1 in trStartDict.keys():
                startline = i+1
                endline = endDict[trStartDict[i+1]]
                
            elif i >= startline and i <= endline:
                
                track = line.split()

                tr = TrackRecord(
                    I=int(track[0]),
                    K1=int(track[1]),
                    K2=int(track[2]),
                    K3=int(track[3]),
                    K4=int(track[4]),
                    K5=int(track[5]),
                    P1=float(track[6]),
                    P2=float(track[7]),
                    P3=float(track[8]),
                    P4=float(track[9]),
                    P5=float(track[10]),
                    V1=float(track[11]),
                    V2=float(track[12]),
                    V3=float(track[13]),
                    V4=float(track[14]) if len(track) > 14 else None,
                    V5=float(track[15]) if len(track) > 15 else None
                )
                        
                trStartDict[startline].trackrecords.append(tr)
                
                if i == endline:
                    endDict.pop(trStartDict[startline])
                    trStartDict.pop(startline)
                    startline = 10**10
                    endline = 10**10
                
                



def writeEventFile(eventrecords, output_path, **kwargs):
    """
    Writes a list of eventrecords into a new Pythia6 event file.

    Parameters
    ----------
    eventrecords : List[EventRecord]
        The event records to write.
    output_path : str
        The output path for the resulting file. If you specify just the filename, then a file will be created in the current working directory.
    **kwargs: headerfile : str
        Path to a text file containing a Pythia6 header, e.g. another Pythia6 event file. If no argument is given, then it will create an empty header.
    Returns
    -------
    None.

    """
    
    
    with open(output_path, "w") as output_file:
        
        
        if kwargs.get('headerfile',None) == None:
            output_file.write('  EVENT FILE WITHOUT HEADER\n\n\n\n\n')
            output_file.write(' ============================================\n')
        else:
            return #TODO: Copy a header from an existing file
        

        
        er_attributes = [
                            "I", "ievent", "genevent", "subprocess", "nucleon", "targetparton", 
                            "xtargparton", "beamparton", "xbeamparton", "thetabeamprtn", "truey", 
                            "trueQ2", "truex", "trueW2", "trueNu", "leptonphi", "s_hat", "t_hat", 
                            "u_hat", "pt2_hat", "Q2_hat", "F2", "F1", "R", "sigma_rad", 
                            "SigRadCor", "EBrems", "photonflux", "t_diff", "nrTracks"
                        ]
        
        tr_attributes = [
                            "I", 
                            "K1", "K2", "K3", "K4", "K5", 
                            "P1", "P2", "P3", "P4", "P5", 
                            "V1", "V2", "V3"
                        ]
        
        def format_value(value):
            if isinstance(value, float):
                
                if( len('{0:6f}'.format(value)) > len(str(value)) ): 
                    return '{0:6f}'.format(value)
                else: 
                    return str(value)
                
            elif isinstance(value, int):
                return str(value)
            elif value is None:
                return "None"
            else:
                return str(value)
        
        
        for er in eventrecords:
            values = [format_value(getattr(er, attr, "None")) for attr in er_attributes]
            output_file.write("\t".join(values)+'\n')
            output_file.write(' ============================================\n')
            
            for tr in er.getTrackRecords():
                values = [format_value(getattr(tr, attr, "None")) for attr in tr_attributes]
                output_file.write("\t\t".join(values)+'\n')
            output_file.write(' =============== Event finished ===============\n')