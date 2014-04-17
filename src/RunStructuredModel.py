import sys

import GWFModel as gwf

def main():
    #get name of xml control file
    narg = len(sys.argv)
    iarg = 0
    if narg > 1:
        while iarg < narg-1:
            iarg += 1
            fxml = sys.argv[iarg]

    #--read xml file and return structured model instance
    model = gwf.GWFModel(fxml)

    number_periods = 2
    number_timesteps = 1

    for kper in xrange(number_periods):
        model.get_StressPeriodData(kper)
        for kstp in xrange(number_timesteps):
            converge = model.solve(kper, kstp)
            if converge:
                break
        print model.x[0:10]
        print model.x[90:]


if __name__ == '__main__':

    main()
