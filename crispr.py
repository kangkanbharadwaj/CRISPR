import subprocess as sp
import os


class runCRTTool(object):

    def __init__(self, minNR=3, minRL=19, maxRL=38, minSL=19, maxSL=48, screen=0, searchWL=8):

        self.minNR = minNR
        self.minRL = minRL
        self.maxRL = maxRL
        self.minSL = minSL
        self.maxSL = maxSL
        self.screen = screen
        self.searchWL = searchWL

    def runCRT(self, name='', dest_path=''):
		
		cmd = "java -cp /scratch/0/bharadwk/CRISPR/bin/CRT1.2-CLI.jar crt -minNR %d -minRL %d -maxRL %d -minSL %d -maxSL %d -screen %d -searchWL %d %s %s" %(self.minNR, self.minRL, self.maxRL, self.minSL, self.maxSL, self.screen, self.searchWL, name, dest_path)
		sp.check_output(cmd, shell=True)
		#os.popen(cmd)
				

		
