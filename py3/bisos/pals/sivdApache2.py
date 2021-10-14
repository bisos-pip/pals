#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: An =ICM=: a beginning template for development of new ICMs.
"""

import typing

icmInfo: typing.Dict[str, typing.Any] = { 'moduleDescription': ["""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
*** concept             -- Desctiption of concept
**      [End-Of-Description]
"""], }

icmInfo['moduleUsage'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""


icmInfo['moduleStatus'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "aaSiGeneweb"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202109230835"
####+END:

####+BEGIN: bx:icm:py:status :status "Production"
icmInfo['status']  = "Production"
####+END:

icmInfo['credits'] = ""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/icmInfo-mbNedaGplByStar.py"
icmInfo['authors'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['copyright'] = "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]"
icmInfo['licenses'] = "[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"
icmInfo['maintainers'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['contacts'] = "[[http://mohsen.1.banan.byname.net/contact]]"
icmInfo['partOf'] = "[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]"
####+END:

icmInfo['panel'] = "{}-Panel.org".format(icmInfo['moduleName'])
icmInfo['groupingType'] = "IcmGroupingType-pkged"
icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"


####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/bisos/git/auth/bxRepos/bisos-pip/pals/py3/bin/aaSiGeneweb.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:


####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=  :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import collections
import os
import shutil
import invoke
import tempfile

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

from bisos.bpo import bpo
from bisos.pals import palsBpo
from bisos.pals import palsSis

g_importedCmndsModules = [       # Enumerate modules from which CMNDs become invokable
    'blee.icmPlayer.bleep',
]


####+BEGIN: bx:icm:python:section :title "= =Framework::= Options, Arguments and Examples Specifications ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= Options, Arguments and Examples Specifications =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "g_paramsExtraSpecify" :comment "FWrk: ArgsSpec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-FrameWrk :: /g_paramsExtraSpecify/ =FWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_paramsExtraSpecify(
    parser,
):
####+END:
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    icmParams.parDictAdd(
        parName='moduleVersion',
        parDescription="Module Version",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,  # type: ignore
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )

    bleep.commonParamsSpecify(icmParams)

    bpo.commonParamsSpecify(icmParams)
    palsSis.commonParamsSpecify(icmParams)

    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)

    return


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "examples" :cmndType "Cmnd-FWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cmnd-FWrk  :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:

        def cpsInit(): return collections.OrderedDict()
        #def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        oneBpo = "pmi_ByD-100001"

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())

        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()

        icm.cmndExampleMenuChapter('*Service Examples*')

        def oneSvcExample(svcName):
            si = os.path.join("apache2", svcName)
            def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
            cmndName = "svcExamples" ; cmndArgs = "create" ;
            cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = si
            menuItem(verbosity='none')

        def listOfSvcs():
            virDomSvcs = listOfA2VirDomTypes()
            for each in virDomSvcs:
                oneSvcExample(each)

        listOfSvcs()

        return(cmndOutcome)


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "svcExamples" :cmndType "Cmnd-FWrk"  :comment "FrameWrk: ICM Examples" :parsMand "bpoId si" :parsOpt "" :argsMin "0" :argsMax "999" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cmnd-FWrk  :: /svcExamples/ =FrameWrk: ICM Examples= parsMand=bpoId si parsOpt= argsMin=0 argsMax=999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class svcExamples(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        def cpsInit(): return collections.OrderedDict()
        def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        oneBpo = bpoId
        oneSiRelPath = si


        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())

        icm.G_commonBriefExamples()

        bleep.examples_icmBasic()

        icm.cmndExampleMenuChapter('*Full Actions*')

        cmndName = "fullUpdate" ; cmndArgs = "" ;
        cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
        menuItem(verbosity='none')

        cmndName = "fullDelete" ; cmndArgs = "" ;
        cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
        menuItem(verbosity='none')

        cmndName = "serviceDelete" ; cmndArgs = "" ;
        cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
        menuItem(verbosity='none')

        icm.cmndExampleMenuChapter('*siBaseStart -- Initialize siBaseDir*')

        cmndName = "siBaseStart" ; cmndArgs = "" ;
        cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
        menuItem(verbosity='none')

        cmndName = "siBaseUpdate" ; cmndArgs = "" ;
        cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
        menuItem(verbosity='none')

        icm.cmndExampleMenuChapter('*dbaseInitialContent for Bystar Account*')

        cmndName = "palsBpoInfo" ; cmndArgs = "notyet" ;
        cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
        menuItem(verbosity='none')
        menuItem(verbosity='full')

        # ${G_myName} ${extraInfo} -p bxoId="${oneBystarAcct}" -p ss=${oneSr} -p dbase=banan -i imagesList | bueGimpManage.sh -h -v -n showRun -i scaleReplaceHeightTo 200
        # $( examplesSeperatorChapter "Access, Verification And Test" )
        # ${G_myName} ${extraInfo} -i  visitUrl

        return(cmndOutcome)


####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&999",
            argName="actionPars",
            argChoices='any',
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict



####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "fullUpdate" :comment "" :parsMand "bpoId si" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /fullUpdate/ parsMand=bpoId si parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class fullUpdate(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

####+END:

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Creates bases.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "siBaseStart" :comment "" :parsMand "bpoId si" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /siBaseStart/ parsMand=bpoId si parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class siBaseStart(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

####+END:

        primInstanceBaseDir = palsBpo.si_primInstanceBaseDir(bpoId, si)
        if not os.path.exists(primInstanceBaseDir):
            icm.EH_critical_usageError(f"primInstanceBaseDir={primInstanceBaseDir} should have existed.")
            return cmndOutcome.set(
                opError=icm.OpError.Failure,  # type: ignore
                opResults=None,
            )

        svcInstanceBaseDir = palsBpo.si_instanceBaseDir(bpoId, si)
        if not os.path.exists(svcInstanceBaseDir):
            os.makedirs(svcInstanceBaseDir)

        print(f"svcInstanceBaseDir={svcInstanceBaseDir}")

        bsiAgentFile = os.path.join(svcInstanceBaseDir, "bsiAgent.sh")

        shutil.copyfile("/bisos/apps/defaults/pals/si/common/bsiAgent.sh", bsiAgentFile)

        siInfoBase = os.path.join(svcInstanceBaseDir, "siInfo")

        if not os.path.exists(siInfoBase): os.makedirs(siInfoBase)

        icm.FILE_ParamWriteTo(siInfoBase, 'svcCapability', __file__) # NOTYET, last part

        c = invoke.context.Context(config=None)

        with c.cd(svcInstanceBaseDir):
            c.run("bxtStartCommon.sh  -v -n showRun -i startObjectGen auxLeaf")


        c.run(f"ls -ld {primInstanceBaseDir}")

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Creates bases.
"""

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "siBaseUpdate" :comment "" :parsMand "bpoId si" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /siBaseUpdate/ parsMand=bpoId si parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class siBaseUpdate(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

####+END:

        siLogBase = "NOTYET"

        c = invoke.context.Context(config=None)

        c.sudo(f"echo mkdir -p {siLogBase}")
        c.sudo(f"echo chown -R bisos:bisos {siLogBase}")
        c.sudo(f"echo chmod -R  g+w {siLogBase}")

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Creates bases.
"""



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "palsBpoInfo" :comment "" :parsMand "bpoId si" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /palsBpoInfo/ parsMand=bpoId si parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class palsBpoInfo(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        infoType = effectiveArgsList[0]

        thisBpo = palsBpo.obtainBpo(bpoId,)

        print("AAA")

        print(thisBpo.__dict__)

        thisBpo.activate("apache2/plone3/main")

        print(thisBpo.basesObj.varBase_obtain())
        print(thisBpo.basesObj.tmpBase_obtain())
        print(thisBpo.basesObj.logBase_obtain())

        thisBpo.repo_rbxe.info()
        thisBpo.repo_bxeTree.info()

        thisBpo.repo_live.info()

        # a2VirDomProvider = palsBpo.obtainSiObj(thisBpo, "apache2")

        #print(palsBpo.svcProv_virDom_list())
        #print(palsBpo.svcProv_prim_list())

        thisBpo.sisDigest()

        siPath = palsSis.siIdToSiPath(bpoId, si)

        thisSi = palsSis.EffectiveSis.givenSiPathFindSiObj(bpoId, siPath,)
        print(thisSi.setMyVar)

        print(thisBpo.effectiveSisList)

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName='dbaseName',
            argChoices='any',
            argDescription="Name of the geneweb database",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Description
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "dbaseCreate" :comment "" :parsMand "" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /dbaseCreate/ parsMand= parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class dbaseCreate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        dbaseName = effectiveArgsList[0]
        dbaseFullPath = os.path.join('/var/lib/geneweb', dbaseName)

        context = invoke.context.Context(config=None)
        context.sudo(f"gwc -o {dbaseFullPath}")
        context.sudo(f"chmod g+w {dbaseFullPath}.gwb")

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName='dbaseName',
            argChoices='any',
            argDescription="Name of the geneweb database",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Description
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "dbaseInitialContentUpdate" :comment "" :parsMand "bpoId si" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /dbaseInitialContentUpdate/ parsMand=bpoId si parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class dbaseInitialContentUpdate(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        dbaseName = effectiveArgsList[0]
        dbaseFullPath = os.path.join('/var/lib/geneweb', dbaseName)
        context = invoke.context.Context(config=None)

        outcome = dbaseInitialContentStdout().cmnd(
            interactive=False, bpoId=bpoId, si=si, argsList=[dbaseName],
        )
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))
        dbaseAsStr = str(outcome.results)

        fd, tmpPath = tempfile.mkstemp()
        try:
            with os.fdopen(fd, 'w') as tmp:
                tmp.write(dbaseAsStr)
            context.sudo(f"ged2gwb -o {dbaseFullPath} {tmpPath}")
        finally:
            os.remove(tmpPath)

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName='dbaseName',
            argChoices='any',
            argDescription="Name of the geneweb database",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Description
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "dbaseInitialContentStdout" :comment "" :parsMand "bpoId si" :parsOpt "" :argsMin "1" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /dbaseInitialContentStdout/ parsMand=bpoId si parsOpt= argsMin=1 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class dbaseInitialContentStdout(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bpoId': bpoId, 'si': si, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bpoId = callParamsDict['bpoId']
        si = callParamsDict['si']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        dbaseName = effectiveArgsList[0]
        #dbaseFullPath = os.path.join('/var/lib/geneweb', dbaseName)

        # NOTYET, obtain firstName, lastName, etc from

        resStr = dbaseInitialContentTemplate().format(
            dbaseName=dbaseName,
            cp_FirstName="firstName",
            cp_LastName="lastName",
        )

        if interactive:
            print(resStr)

        return cmndOutcome.set(
            opError=icm.OpError.Success,  # type: ignore
            opResults=resStr,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName='dbaseName',
            argChoices='any',
            argDescription="Name of the geneweb database",
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Description
"""


####+BEGIN: bx:dblock:python:section :title "Class Definitions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Class Definitions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:python:class :className "A2SivdRepo" :superClass "bpo.BpoRepo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /A2SivdRepo/ bpo.BpoRepo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class A2SivdRepo(bpo.BpoRepo):
####+END:
    """
** Refers to the entirety of bpo/apache2 repo.
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not bpo.EffectiveBpos.givenBpoIdGetBpo(bpoId):
            icm.EH_critical_usageError(f"Missing BPO for {bpoId}")
            return

    def repoBase(self,):
        return os.path.join(self.bpo.baseDir, "apache2") # type: ignore


####+BEGIN: bx:dblock:python:class :className "obsoletedA2SivdBase_Plone3" :superClass "object" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /obsoletedA2SivdBase_Plone3/ object =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class obsoletedA2SivdBase_Plone3(object):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
    ):
        # super().__init__(bpoId)
        if not bpo.EffectiveBpos.givenBpoIdGetBpo(bpoId):
            icm.EH_critical_usageError(f"Missing BPO for {bpoId}")
            return


####+BEGIN: bx:dblock:python:class :className "AaSivdRepo_Apache2" :superClass "palsBpo.SiRepo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /AaSivdRepo_Apache2/ palsBpo.SiRepo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class AaSivdRepo_Apache2(palsSis.SiRepo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
            siPath,
    ):
        # print("eee  AaSivdRepo_Apache2")
        if palsSis.EffectiveSis.givenSiPathGetSiObjOrNone(bpoId, siPath,):
            icm.EH_critical_usageError(f"Duplicate Attempt At Singleton Creation bpoId={bpoId}, siPath={siPath}")
        else:
            super().__init__(bpoId, siPath,) # includes: EffectiveSis.addSi(bpoId, siPath, self,)


    def obtainFromFPs(self,):
        pass


####+BEGIN: bx:dblock:python:class :className "A2_Svc_Type" :superClass "palsBpo.SiVirDomSvcType" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /A2_Svc_Type/ palsBpo.SiVirDomSvcType =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class A2_Svc_Type(palsSis.SiVirDomSvcType):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
            siPath,
    ):
        # print("fff  A2_Svc_Type")
        if palsSis.EffectiveSis.givenSiPathGetSiObjOrNone(bpoId, siPath,):
            icm.EH_critical_usageError(f"Duplicate Attempt At Singleton Creation bpoId={bpoId}, siPath={siPath}")
        else:
            super().__init__(bpoId, siPath,) # includes: EffectiveSis.addSi(bpoId, siPath, self,)


####+BEGIN: bx:dblock:python:class :className "A2_Svc_Inst" :superClass "palsBpo.SiSvcInst" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /A2_Svc_Inst/ palsBpo.SiSvcInst =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class A2_Svc_Inst(palsSis.SiSvcInst):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
            siPath,
    ):
        # print("ggg  A2_Svc_Inst")
        if palsSis.EffectiveSis.givenSiPathGetSiObjOrNone(bpoId, siPath,):
            icm.EH_critical_usageError(f"Duplicate Attempt At Singleton Creation bpoId={bpoId}, siPath={siPath}")
        else:
            super().__init__(bpoId, siPath,) # includes: EffectiveSis.addSi(bpoId, siPath, self,)

    def obtainFromFPs(self,):
        pass


####+BEGIN: bx:dblock:python:class :className "A2_Plone3_Type" :superClass "A2_Svc_Type" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /A2_Plone3_Type/ A2_Svc_Type =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class A2_Plone3_Type(A2_Svc_Type):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

    def __init__(
        self,
            bpoId,
            siPath,
    ):
        # print("hhh  A2_Plone3_Type")
        if palsSis.EffectiveSis. givenSiPathGetSiObjOrNone(bpoId, siPath,):
            icm.EH_critical_usageError(f"Duplicate Attempt At Singleton Creation bpoId={bpoId}, siPath={siPath}")
        else:
            super().__init__(bpoId, siPath,) # includes: EffectiveSis.addSi(bpoId, siPath, self,)


    def obtainFromFPs(self,):
        pass

    def domainShow(self,):
        pass

    def stdout(self,):
        pass


####+BEGIN: bx:dblock:python:class :className "A2_Plone3_Inst" :superClass "A2_Svc_Inst" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /A2_Plone3_Inst/ A2_Svc_Inst =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class A2_Plone3_Inst(A2_Svc_Inst):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
        self,
            bpoId,
            siPath,
    ):
        # print("iii  A2_Plone3_Inst")
        if palsSis.EffectiveSis. givenSiPathGetSiObjOrNone(bpoId, siPath,):
            icm.EH_critical_usageError(f"Duplicate Attempt At Singleton Creation bpoId={bpoId}, siPath={siPath}")
        else:
            super().__init__(bpoId, siPath,) # includes: EffectiveSis.addSi(bpoId, siPath, self,)

    def obtainFromFPs(self,):
        pass

    def setVar(self, value,):
        self.setMyVar = value

    def domainShow(self,):
        pass

    def stdout(self,):
        pass




####+BEGIN: bx:dblock:python:class :className "A2_Geneweb_VirDom" :superClass "A2_Svc_Type" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /A2_Geneweb_VirDom/ A2_Svc_Type =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class A2_Geneweb_VirDom(A2_Svc_Type):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

    def __init__(
        self,
    ):
        pass

    def obtainFromFPs(self,):
        pass

    def domainShow(self,):
        pass

    def stdout(self,):
        pass



####+BEGIN: bx:dblock:python:section :title "Function Definitions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Function Definitions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:


####+BEGINNOT: bx:icm:python:func :funcName "listOfA2VirDomTypes" :funcType "anyOrNone" :retType "List" :deco "" :argsList ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /listOfA2VirDomSvcs/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def listOfA2VirDomTypes() -> typing.List:
####+END:
    return (
        [
            'plone3',
            'geneweb',
            'squirrelmail',
            'django',
            'gitweb',
            'gitolite',
            'gallery',
            'www',
        ]
    )


####+BEGIN: bx:icm:python:func :funcName "digestAtVirDomSvcProv" :funcType "anyOrNone" :retType "" :deco "" :argsList "bpoId siRepoBase"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /digestAtVirDomSvcProv/ retType= argsList=(bpoId siRepoBase)  [[elisp:(org-cycle)][| ]]
"""
def digestAtVirDomSvcProv(
    bpoId,
    siRepoBase,
):
####+END:
    icm.TM_here("Incomplete")
    palsSis.createSiObj(bpoId, siRepoBase, AaSivdRepo_Apache2)

    thisBpo = palsBpo.obtainBpo(bpoId,)

    for each in listOfA2VirDomTypes():
            siRepoPath = os.path.join(siRepoBase, each)
            if os.path.isdir(siRepoPath):
                if each == "plone3":
                    plone3SvcTypeObj = palsSis.createSiObj(bpoId, siRepoPath, A2_Plone3_Type)
                    digestAtVirDomSvcType(bpoId, siRepoPath, plone3SvcTypeObj)
                    thisBpo.sis.svcType_virDom_enabled.append(siRepoPath)

                icm.TM_here(f"is {siRepoPath}")
            else:
                icm.TM_here(f"is NOT {siRepoPath} -- skipped")


####+BEGIN: bx:icm:python:func :funcName "digestAtVirDomSvcType" :funcType "anyOrNone" :retType "" :deco "" :argsList "bpoId siRepoBase svcType"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /digestAtVirDomSvcType/ retType= argsList=(bpoId siRepoBase svcType)  [[elisp:(org-cycle)][| ]]
"""
def digestAtVirDomSvcType(
    bpoId,
    siRepoBase,
    svcTypeObj,
):
####+END:
    icm.TM_here("Incomplete")

    #palsBpo.createSiObj(bpoId, siRepoBase, AaSivdRepo_Apache2) # BAD USAGE

    thisBpo = palsBpo.obtainBpo(bpoId,)

    for (_, dirNames, _,) in os.walk(siRepoBase):
        for each in dirNames:
            if each == "siInfo":
                continue
            # verify that it is a svcInstance
            siRepoPath = os.path.join(siRepoBase, each)
            digestVirDomSvcInstance(bpoId, siRepoPath, svcTypeObj, each)
            thisBpo.sis.svcInst_virDom_enabled.append(siRepoPath)
        break


####+BEGIN: bx:icm:python:func :funcName "digestVirDomSvcInstance" :funcType "anyOrNone" :retType "" :deco "" :argsList "bpoId siRepoBase svcTypeObj instanceName"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /digestVirDomSvcInstance/ retType= argsList=(bpoId siRepoBase svcTypeObj instanceName)  [[elisp:(org-cycle)][| ]]
"""
def digestVirDomSvcInstance(
    bpoId,
    siRepoBase,
    svcTypeObj,
    instanceName,
):
####+END:
    icm.TM_here("Incomplete")

    thisSi = palsSis.createSiObj(bpoId, siRepoBase, A2_Plone3_Inst)

    thisSi.setVar(22)

    icm.TM_here(f"bpoId={bpoId}, siRepoBase={siRepoBase}, svcTypeObj={svcTypeObj} instanceName={instanceName}")


####+BEGIN: bx:icm:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:python:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""


####+BEGIN: bx:icm:python:section :title "= =Framework::=   __main__ g_icmMain ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::=   __main__ g_icmMain =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

if __name__ == "__main__":
    icm.g_icmMain(
        icmInfo=icmInfo,
        noCmndEntry=examples, # noCmndEntry=mainEntry,
        extraParamsHook=g_paramsExtraSpecify,
        importedCmndsModules=g_importedCmndsModules,
    )

####+BEGIN: bx:icm:python:section :title "Unused Facilities -- Temporary Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
