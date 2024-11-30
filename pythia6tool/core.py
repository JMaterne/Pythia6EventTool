# -*- coding: utf-8 -*-

import pythia6tool.particlecodes

class EventRecord:
    
    def __init__(self, **kwargs):
        
        self.I = kwargs.get('I', None)
        self.ievent = kwargs.get('ievent', None)
        self.genevent = kwargs.get('genevent', None)
        self.subprocess = kwargs.get('subprocess', None)
        self.nucleon = kwargs.get('nucleon', None)
        self.targetparton = kwargs.get('targetparton', None)
        self.xtargparton = kwargs.get('xtargparton', None)
        self.beamparton = kwargs.get('beamparton', None)
        self.xbeamparton = kwargs.get('xbeamparton', None)
        self.thetabeamprtn = kwargs.get('thetabeamprtn', None)
        self.truey = kwargs.get('truey', None)
        self.trueQ2 = kwargs.get('trueQ2', None)
        self.truex = kwargs.get('truex', None)
        self.trueW2 = kwargs.get('trueW2', None)
        self.trueNu = kwargs.get('trueNu', None)
        self.leptonphi = kwargs.get('leptonphi', None)
        self.s_hat = kwargs.get('s_hat', None)
        self.t_hat = kwargs.get('t_hat', None)
        self.u_hat = kwargs.get('u_hat', None)
        self.pt2_hat = kwargs.get('pt2_hat', None)
        self.Q2_hat = kwargs.get('Q2_hat', None)
        self.F2 = kwargs.get('F2', None)
        self.F1 = kwargs.get('F1', None)
        self.R = kwargs.get('R', None)
        self.sigma_rad = kwargs.get('sigma_rad', None)
        self.SigRadCor = kwargs.get('SigRadCor', None)
        self.EBrems = kwargs.get('EBrems', None)
        self.photonflux = kwargs.get('photonflux', None)
        self.t_diff = kwargs.get('t_diff', None)
        self.nrTracks = kwargs.get('nrTracks', None)
        
        #save line numbers where tracks start and end
        self.trackStart = kwargs.get('trackStart', None)
        self.trackEnd = kwargs.get('trackEnd', None)
        
        self.eventfile = kwargs.get('eventfile', None)
        
        self.trackrecords = []
    
    """
    User friendly printing
    """
    def __str__(self):
        return (
                    f"I: {self.I}\n"
                    f"ievent: {self.ievent}\n"
                    f"genevent: {self.genevent}\n"
                    f"subprocess: {self.subprocess}\n"
                    f"nucleon: {self.nucleon}\n"
                    f"targetparton: {self.targetparton}\n"
                    f"xtargparton: {self.xtargparton}\n"
                    f"beamparton: {self.beamparton}\n"
                    f"xbeamparton: {self.xbeamparton}\n"
                    f"thetabeamprtn: {self.thetabeamprtn}\n"
                    f"truey: {self.truey}\n"
                    f"trueQ2: {self.trueQ2}\n"
                    f"truex: {self.truex}\n"
                    f"trueW2: {self.trueW2}\n"
                    f"trueNu: {self.trueNu}\n"
                    f"leptonphi: {self.leptonphi}\n"
                    f"s_hat: {self.s_hat}\n"
                    f"t_hat: {self.t_hat}\n"
                    f"u_hat: {self.u_hat}\n"
                    f"pt2_hat: {self.pt2_hat}\n"
                    f"Q2_hat: {self.Q2_hat}\n"
                    f"F2: {self.F2}\n"
                    f"F1: {self.F1}\n"
                    f"R: {self.R}\n"
                    f"sigma_rad: {self.sigma_rad}\n"
                    f"SigRadCor: {self.SigRadCor}\n"
                    f"EBrems: {self.EBrems}\n"
                    f"photonflux: {self.photonflux}\n"
                    f"t_diff: {self.t_diff}\n"
                    f"nrTracks: {self.nrTracks}\n"
                )
    
    def getTrackRecords(self):
        if self.trackrecords == []:
            from pythia6tool.io_util import readTrackRecords
            return readTrackRecords(self.eventfile,[self])[self.ievent]
        else:
            return self.trackrecords
    
    
    def setTrackRecords(self,trackrecords):
        self.trackrecords = trackrecords
    
class TrackRecord:
    
    def __init__(self, **kwargs):

        self.I = kwargs.get('I', None)

        self.K1 = kwargs.get('K1', None)
        self.K2 = kwargs.get('K2', None)
        self.K3 = kwargs.get('K3', None)
        self.K4 = kwargs.get('K4', None)
        self.K5 = kwargs.get('K5', None)

        self.P1 = kwargs.get('P1', None)
        self.P2 = kwargs.get('P2', None)
        self.P3 = kwargs.get('P3', None)
        self.P4 = kwargs.get('P4', None)
        self.P5 = kwargs.get('P5', None)

        self.V1 = kwargs.get('V1', None)
        self.V2 = kwargs.get('V2', None)
        self.V3 = kwargs.get('V3', None)
        self.V4 = kwargs.get('V4', None)
        self.V5 = kwargs.get('V5', None)
    
    
    """
    User friendly printing
    """
    def __str__(self):
        
        if self.K1 == 0:
            K1meaning = "empty line"
        elif self.K1 == 1:
            K1meaning = "an undecayed particle or unfragmented parton"
        elif self.K1 == 2:
            K1meaning = "an unfragmented parton, which is followed by more partons in the same colour-singlet parton system."
        elif self.K1 == 3:
            K1meaning = "an unfragmented parton with special colour flow information stored in K(I,4) and K(I,5) - see Pythia6 Manual"
        elif self.K1 == 4:
            K1meaning = "a particle which could have decayed, but did not within the allowed volume around the original vertex."
        elif self.K1 == 5:
            K1meaning = "a particle which is to be forced to decay in the next PYEXEC call - see Pythia6 Manual"
        elif self.K1 == 11:
            K1meaning = "a decayed particle or a fragmented parton, the latter being either a single parton or the last one of a parton system"
        elif self.K1 == 12:
            K1meaning = "a fragmented parton, which is followed by more partons in the same colour-singlet parton system. Or B Bbar meson decaying into each other - see Pythia6 Manual"
        elif self.K1 == 13:
            K1meaning = "a parton which has been removed when special colour flow information has been used to rearrange a parton system - see Pythia6 Manual"
        elif self.K1 == 14:
            K1meaning = "a parton which has branched into further partons, with special colour-flow information provided"
        elif self.K1 == 15:
            K1meaning = "a particle which has been forced to decay (by user intervention)"
        elif self.K1 == 21:
            K1meaning = "documentation lines used to give a compressed story of the event at the beginning of the event record"
        else:
            K1meaning = "Please consult Pythia6 Manual"
        
        K2particlecode = pythia6tool.particlecodes.getParticleName(self.K2)
        
        return (
                    f"K(I,1): {self.K1} (status code: {K1meaning})\n\n"
                    f"K(I,2): {self.K2} (particle code: {K2particlecode})\n\n"
                    f"K(I,3): {self.K3} (line number of parent particle where known, otherwise 0)\n\n"
                    f"K(I,4): {self.K4} (normally the line number of the first daughter or 0 for undecayed/unfragmented - see Pythia6 Manual for other cases)\n\n"
                    f"K(I,5): {self.K5} (normally the line number of the last daughter or 0 for undecayed/unfragmented - see Pythia6 Manual for other cases)\n\n"
                    f"P(I,1): {self.P1} (p_x momentum in x direction in GeV/c)\n\n"
                    f"P(I,2): {self.P2} (p_y momentum in y direction in GeV/c)\n\n"
                    f"P(I,3): {self.P3} (p_z momentum in z direction in GeV/c)\n\n"
                    f"P(I,4): {self.P4} (energy in GeV)\n\n"
                    f"P(I,5): {self.P5} (mass in GeV/c^2; for space-like virtualities it is P(I,5)=-Q)\n\n"
                    f"V(I,1): {self.V1} (x position of production vertex in mm)\n\n"
                    f"V(I,2): {self.V2} (y position of production vertex in mm)\n\n"
                    f"V(I,3): {self.V3} (z position of production vertex in mm)\n\n"
                    f"V(I,4): {self.V4} (time of production in mm/c)\n\n"
                    f"V(I,5): {self.V5} (proper lifetime of particle in mm/c - see Pythia6 Manual)"
                )
    def getParticleName(self):
        return pythia6tool.particlecodes.getParticleName(self.K2)