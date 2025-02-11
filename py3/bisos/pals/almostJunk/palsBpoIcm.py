#!/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: A /library/ Beginning point for development of new ICM oriented libraries.
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
** TODO [[elisp:(org-cycle)][| ]]  Current     :: For now it is an ICM. Turn it into ICM-Lib. [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "palsBpoIcm"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202112254431"
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
*  This file:/bisos/git/auth/bxRepos/bisos-pip/pals/py3/bisos/pals/almostJunk/palsBpoIcm.py :: [[elisp:(org-cycle)][| ]]
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


import os
# import pwd
# import grp
import collections
# import enum
#

#import traceback


####+OTHERBEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmG.py"

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from bisos.csPlayer import bleep
####+END:

from bisos.platform import bxPlatformConfig
# from bisos.platform import bxPlatformThis

from bisos.bpo import bpo

g_importedCmndsModules = [       # Enumerate modules from which CMNDs become invokable
    'bisos.csPlayer.bleep',
    'bisos.bpo.bpo',
]


####+BEGIN: bx:icm:python:section :title "= =Framework::= Options, Arguments and Examples Specifications ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= Options, Arguments and Examples Specifications =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "g_paramsExtraSpecify" :comment "FrameWrk: ArgsSpec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-FrameWrk :: /g_paramsExtraSpecify/ =FrameWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
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

    commonParamsSpecify(icmParams)

    bpo.commonParamsSpecify(icmParams)
    commonParamsSpecify(icmParams)

    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)

    return


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "examples" :cmndType "ICM-Cmnd-FWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd-FWrk :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {}
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome

####+END:
        def cpsInit(): return collections.OrderedDict()
        def menuItem(): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())

        icm.G_commonBriefExamples()

        bleep.examples_csBasic()

        oneBpo = "pmi_ByD-100001"

        icm.cmndExampleMenuChapter('*General Dev and Testing CMNDs*')

        cmndName = "argsAndParamsProc"

        cmndArgs = "list argOne twoArg arg3" ;  cps = cpsInit();
        menuItem()
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')

        icm.cmndExampleMenuChapter('*BPO Access And Management*')

        bpo.examples_bpo_basicAccess(oneBpo)

        icm.cmndExampleMenuChapter('*BPO-AAIS Access And Management*')

        examples_aaBpo_basicAccess()

        # icm.cmndExampleMenuChapter('*Other Than ICM Execution Line Examples*')

        # execLineEx("""ls -l""")

        return(cmndOutcome)


####+BEGIN: bx:dblock:global:file-insert :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/G_examples.bottom.py"
    # Intentionally Left Blank -- previously: lhip.G_devExamples(G_myName)

####+END:


####+BEGIN: bx:dblock:python:section :title "Start Your Sections Here"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Start Your Sections Here*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "si_svcName" :funcType "Obtain" :retType "str" :deco "" :argsList "si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_svcName/ retType=str argsList=(si)  [[elisp:(org-cycle)][| ]]
"""
def si_svcName(
    si,
):
####+END:
    """
**
"""
    siList = si.split('/')
    return siList[0]

####+BEGIN: bx:dblock:python:func :funcName "si_instanceName" :funcType "Obtain" :retType "str" :deco "" :argsList "si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_instanceName/ retType=str argsList=(si)  [[elisp:(org-cycle)][| ]]
"""
def si_instanceName(
    si,
):
####+END:
    """
**
"""
    siList = si.split('/')
    return siList[-1]

####+BEGIN: bx:dblock:python:func :funcName "si_virDomSvcName" :funcType "Obtain" :retType "str" :deco "" :argsList "si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_virDomSvcName/ retType=str argsList=(si)  [[elisp:(org-cycle)][| ]]
"""
def si_virDomSvcName(
    si,
):
####+END:
    """
**
"""
    siList = si.split('/')
    virDomName = siList[1]
    if virDomName == si_instanceName(si):
        return ""
    else:
        return virDomName

####+BEGIN: bx:dblock:python:func :funcName "si_svcBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_svcBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_svcBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    bpoBaseDir = bpo.bpoBaseDir_obtain(bpoId)
    siServiceName = si_svcName(si)
    return (
        os.path.join(
            bpoBaseDir,
            format(f"si_{siServiceName}"),
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "si_virDomSvcBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_virDomSvcBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_virDomSvcBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    svcVirDomName = si_virDomSvcName(si)
    svcBaseDir = si_svcBaseDir(bpoId, si)
    return (
        os.path.join(
            svcBaseDir,
            svcVirDomName,
        )
    )



####+BEGIN: bx:dblock:python:func :funcName "si_instanceBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_instanceBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_instanceBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    svcInstance = si_instanceName(si)
    svcVirDomName = si_virDomSvcName(si)
    if svcInstance == svcVirDomName:
        # Not a virDom
        svcBaseDir = si_svcBaseDir(bpoId, si)
        return (
            os.path.join(
                svcBaseDir,
                svcInstance,
            )
        )
    else:
        virDomSvcBaseDir = si_virDomSvcBaseDir(bpoId, si)
        return (
            os.path.join(
                virDomSvcBaseDir,
                svcInstance,
            )
        )


####+BEGIN: bx:dblock:python:func :funcName "si_primSvcBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_primSvcBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_primSvcBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    bpoBaseDir = bpo.bpoBaseDir_obtain(bpoId)
    svcVirDomName = si_virDomSvcName(si)
    return (
        os.path.join(
            bpoBaseDir,
            format(f"si_{svcVirDomName}"),
        )
    )


####+BEGIN: bx:dblock:python:func :funcName "si_primInstanceBaseDir" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /si_primInstanceBaseDir/ retType=str argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def si_primInstanceBaseDir(
    bpoId,
    si,
):
####+END:
    """
**
"""
    svcInstance = si_instanceName(si)
    primSvcBaseDir = si_primSvcBaseDir(bpoId, si)

    return (
        os.path.join(
            primSvcBaseDir,
            svcInstance,
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "siRootDir_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoBaseDir"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /siRootDir_obtain/ retType=str argsList=(bpoBaseDir)  [[elisp:(org-cycle)][| ]]
"""
def siRootDir_obtain(
    bpoBaseDir,
):
####+END:
    """
**
"""
    return (
        os.path.join(
            bpoBaseDir,
            "so/r3/sr",
        )
    )


####+BEGIN: bx:dblock:python:func :funcName "siFullPathBaseDir_obtain" :funcType "Obtain" :retType "str" :deco "" :argsList "bpoId srRelPath"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-Obtain :: /siFullPathBaseDir_obtain/ retType=str argsList=(bpoId srRelPath)  [[elisp:(org-cycle)][| ]]
"""
def siFullPathBaseDir_obtain(
    bpoId,
    srRelPath,
):
####+END:
    """
** Join dirs as expected.
"""
    return (
        os.path.join(
            siRootDir_obtain(
                bpo.bpoBaseDir_obtain(
                    bpoId
                )
            ),
            siRelPath,
        )
    )


####+BEGIN: bx:dblock:python:subSection :title "Bpo+Si Roots and InfoBases (Control/Input)"

####+END:



####+BEGIN: bx:dblock:python:func :funcName "bpbBisos_baseObtain_control" :comment "BISOS DATA" :funcType "obtain" :retType "bool" :deco "" :argsList "baseDir"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpbBisos_baseObtain_control/ =BISOS DATA= retType=bool argsList=(baseDir)  [[elisp:(org-cycle)][| ]]
"""
def bpbBisos_baseObtain_control(
    baseDir,
):
####+END:
    # bxpRoot = "bxpRoot_baseObtain()"

    return( os.path.join(
        baseDir, "bisos", "input"
    ))


####+BEGIN: bx:dblock:python:subSection :title "Bpo+Sr RunTime  Bases"

####+END:

####+BEGIN: bx:dblock:python:func :funcName "bpoSi_runBaseObtain_root" :funcType "obtain" :retType "bool" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpoSi_runBaseObtain_root/ retType=bool argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def bpoSi_runBaseObtain_root(
    bpoId,
    si,
):
####+END:
    icm.unusedSuppress(si)
    return(
        os.path.join(
            str(bxPlatformConfig.rootDir_deRun_fpObtain(configBaseDir=None,)),
            "bisos/r3/bpo",
            str(bpoId),
        )
    )



####+BEGIN: bx:dblock:python:func :funcName "bpoSi_runBaseObtain_var" :funcType "obtain" :retType "bool" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpoSi_runBaseObtain_var/ retType=bool argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def bpoSi_runBaseObtain_var(
    bpoId,
    si,
):
####+END:
    return(
        os.path.join(
            bpoSi_runBaseObtain_root(
                bpoId,
                si,
            ),
            "var"
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bpoSi_runBaseObtain_tmp" :funcType "obtain" :retType "bool" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpoSi_runBaseObtain_tmp/ retType=bool argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def bpoSi_runBaseObtain_tmp(
    bpoId,
    si,
):
####+END:
    return(
        os.path.join(
            bpoSi_runBaseObtain_root(
                bpoId,
                si,
            ),
            "tmp"
        )
    )

####+BEGIN: bx:dblock:python:func :funcName "bpoSi_runBaseObtain_log" :funcType "obtain" :retType "bool" :deco "" :argsList "bpoId si"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-obtain :: /bpoSi_runBaseObtain_log/ retType=bool argsList=(bpoId si)  [[elisp:(org-cycle)][| ]]
"""
def bpoSi_runBaseObtain_log(
    bpoId,
    si,
):
####+END:
    return(
        os.path.join(
            bpoSi_runBaseObtain_root(
                bpoId,
                si,
            ),
            "log"
        )
    )

####+BEGIN: bx:dblock:python:section :title "Class Definitions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Class Definitions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "obtainBpo" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bpoId"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /obtainBpo/ retType=bool argsList=(bpoId)  [[elisp:(org-cycle)][| ]]
"""
def obtainBpo(
    bpoId,
):
####+END:
    return bpo.EffectiveBpos.givenBpoIdObtainBpo(bpoId, PalsBpo)


####+BEGIN: bx:dblock:python:class :className "PalsBpo" :superClass "bpo.Bpo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /PalsBpo/ bpo.Bpo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class PalsBpo(bpo.Bpo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""

    def __init__(
            self,
            bpoId,
    ):
        '''Constructor'''
        #print("ddd PalsBpo")
        if bpo.EffectiveBpos.givenBpoIdGetBpoOrNone(bpoId):
            icm.EH_critical_usageError(f"Duplicate Attempt At Singleton Creation bpoId={bpoId}")
        else:
            super().__init__(bpoId) # includes: bpo.EffectiveBpos.addBpo(bpoId, self)

        self.effectiveSisList = {}

        self.basesObj = PalsBases(bpoId)
        self.basesObj.pals_bases_update()

        self.repo_live = PalsRepo_Live(bpoId)

        # self.sivdApache2Repo = AaSivdRepo_Apache2(bpoId)

        self.siGeneweb = {}
        # self.bpoId = bpoId

    def activate(
            self,
            si,
    ):
        """When si is blank, activate the whole BPO. Otherwise just the specified bpo.

        """
        print(self.baseDir)
        print(si)

    def sisDigest(
            self,
    ):
        """Based on known si_s, locate and digest SIs."""
        siRepoPath = ""
        for each in svcProv_virDom_list():
            siRepoPath = os.path.join(self.baseDir, "si_{each}".format(each=each))
            if os.path.isdir(siRepoPath):
                sis_virDom_digest(self.bpoId, each, siRepoPath)
                icm.TM_here(f"is {siRepoPath}")
            else:
                icm.TM_here(f"is NOT {siRepoPath} -- skipped")

        for each in svcProv_prim_list():
            siRepoPath = os.path.join(self.baseDir, "si_{each}".format(each=each))
            if os.path.isdir(siRepoPath):
                sis_prim_digest(self.bpoId, each, siRepoPath)
                icm.TM_here(f"is {siRepoPath}")
            else:
                icm.TM_here(f"is NOT {siRepoPath} -- skipped")


####+BEGIN: bx:dblock:python:class :className "PalsBases" :superClass "bpo.BpoBases" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /PalsBases/ bpo.BpoBases =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class PalsBases(bpo.BpoBases):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not bpo.EffectiveBpos.givenBpoIdGetBpo(bpoId):
            icm.EH_critical_usageError(f"Missing BPO for {bpoId}")
            return

    def pals_bases_update(self,):
        """Extra pals bases."""
        self.bases_update()
        return

    def logBase_update(self,):
        return "NOTYET"

    def logBase_obtain(self,):
        return os.path.join(self.bpo.baseDir, "log") # type: ignore


####+BEGIN: bx:dblock:python:class :className "PalsRepo_Live" :superClass "bpo.BpoRepo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /PalsRepo_Live/ bpo.BpoRepo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class PalsRepo_Live(bpo.BpoRepo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
    ):
        super().__init__(bpoId)
        if not bpo.EffectiveBpos.givenBpoIdGetBpo(bpoId):
            icm.EH_critical_usageError(f"Missing BPO for {bpoId}")
            return

    def info(self,):
        print(f"PalsRepo_Live {self.bpo.bpoId}")


    def obtainFromFPs(self,):
        pass

    def update(
            self,
            containerBpoId,
            ipAddr
    ):
        self.containerBpoId = containerBpoId
        self.ipAddr = ipAddr


####+BEGIN: bx:dblock:python:class :className "EffectiveSis" :superClass "object" :comment "" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /EffectiveSis/ object  [[elisp:(org-cycle)][| ]]
"""
class EffectiveSis(object):
####+END:
    """
** Only one instance is created for a given BpoId and an SiPath.
"""

    @staticmethod
    def addSi(
            bpoId,
            siPath,
            siObj
    ):
        icm.TM_here(f"Adding bpoId={bpoId} siPath={siPath} siObj={siObj}")
        thisBpo = obtainBpo(bpoId,)
        if not thisBpo:
            return None
        thisBpo.effectiveSisList.update({siPath: siObj})


    @staticmethod
    def withSiPathCreateSiObj(
            bpoId,
            siPath,
            SiClass,
    ):
        """Is invoked from Digest with appropriate Class. Returns and siObj."""
        thisBpo = obtainBpo(bpoId,)
        if not thisBpo:
            return None

        if siPath in thisBpo.effectiveSisList:
            icm.EH_problem_usageError(f"bpoId={bpoId} -- siPath={siPath} -- SiClass={SiClass}")
            icm.EH_problem_usageError(siPath)
            icm.EH_critical_oops("")
            return thisBpo.effectiveSisList[siPath]
        else:
            return SiClass(bpoId, siPath) # results in addSi()

    @staticmethod
    def givenSiPathFindSiObj(
            bpoId,
            siPath,
    ):
        """Should really not fail."""
        thisBpo = obtainBpo(bpoId,)
        if not thisBpo:
            return None

        if siPath in thisBpo.effectiveSisList:
            return thisBpo.effectiveSisList[siPath]
        else:
            icm.EH_problem_usageError("")
            return None

    @staticmethod
    def givenSiPathGetSiObjOrNone(
            bpoId,
            siPath,
    ):
        """Expected to perhaps fail."""
        thisBpo = obtainBpo(bpoId,)
        if not thisBpo:
            return None

        if siPath in thisBpo.effectiveSisList:
            return thisBpo.effectiveSisList[siPath]
        else:
            return None


####+BEGIN: bx:icm:python:func :funcName "createSiObj" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bpoId siPath SiClass"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /createSiObj/ retType=bool argsList=(bpoId siPath SiClass)  [[elisp:(org-cycle)][| ]]
"""
def createSiObj(
    bpoId,
    siPath,
    SiClass,
):
####+END:
    """Just an alias."""
    return EffectiveSis.withSiPathCreateSiObj(bpoId, siPath, SiClass)


####+BEGIN: bx:icm:python:func :funcName "siIdToSiPath" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bpoId siId"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /siIdToSiPath/ retType=bool argsList=(bpoId siId)  [[elisp:(org-cycle)][| ]]
"""
def siIdToSiPath(
    bpoId,
    siId,
):
####+END:
    """"Returns siPath"""
    thisBpo = obtainBpo(bpoId,)
    siPath = os.path.join(thisBpo.baseDir, "si_{siId}".format(siId=siId))
    return siPath


####+BEGIN: bx:icm:python:func :funcName "siPathToSiId" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bpoId siId"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /siPathToSiId/ retType=bool argsList=(bpoId siId)  [[elisp:(org-cycle)][| ]]
"""
def siPathToSiId(
    bpoId,
    siId,
):
####+END:
    """"Returns siPath"""
    result = ""
    thisBpo = obtainBpo(bpoId,)
    siPathPrefix = os.path.join(thisBpo.baseDir, "si_")
    if siPathPrefix in siPath:
        result = siPath.replace(siPathPrefix, '')
    else:
        icm.EH_critical_oops(f"bpoId={bpoId} -- siPath={siPath}")
    return result


####+BEGIN: bx:icm:python:func :funcName "sis_virDom_digest" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bpoId virDomSvcProv siRepoPath"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /sis_virDom_digest/ retType=bool argsList=(bpoId virDomSvcProv siRepoPath)  [[elisp:(org-cycle)][| ]]
"""
def sis_virDom_digest(
    bpoId,
    virDomSvcProv,
    siRepoPath,
):
####+END:
    """Using virDom Svc Provider."""
    if virDomSvcProv == "apache2":
        # We need to Create the virDomProvider object
        from bisos.pals import sivdApache2
        sivdApache2.digestAtVirDomSvcProv(bpoId, siRepoPath)


####+BEGIN: bx:icm:python:func :funcName "sis_prim_digest" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "bpoId primSvcProv siRepoPath"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-anyOrNone :: /sis_prim_digest/ retType=bool argsList=(bpoId primSvcProv siRepoPath)  [[elisp:(org-cycle)][| ]]
"""
def sis_prim_digest(
    bpoId,
    primSvcProv,
    siRepoPath,
):
####+END:
    """Using Primary Svc Provider."""
    if primSvcProv == "plone3":
        from bisos.pals import siPlone3
        siPlone3.digestAtSvcProv(bpoId, siRepoPath)


####+BEGIN: bx:dblock:python:class :className "SiRepo" :superClass "bpo.BpoRepo" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /SiRepo/ bpo.BpoRepo =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class SiRepo(bpo.BpoRepo):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
            siPath,
    ):
        icm.TM_here("bpoId={bpoId}")
        if EffectiveSis. givenSiPathGetSiObjOrNone(bpoId, siPath,):
            icm.EH_critical_usageError(f"Duplicate Attempt At Singleton Creation bpoId={bpoId}, siPath={siPath}")
        else:
            EffectiveSis.addSi(bpoId, siPath, self,)


####+BEGIN: bx:dblock:python:class :className "SiVirDomSvcType" :superClass "object" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /SiVirDomSvcType/ object =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class SiVirDomSvcType(object):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
            siPath,
    ):
        EffectiveSis.addSi(bpoId, siPath, self,)


####+BEGIN: bx:dblock:python:class :className "SiSvcInst" :superClass "object" :comment "Expected to be subclassed" :classType "basic"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Class-basic :: /SiSvcInst/ object =Expected to be subclassed=  [[elisp:(org-cycle)][| ]]
"""
class SiSvcInst(object):
####+END:
    """
** Abstraction of the base ByStar Portable Object
"""
    def __init__(
            self,
            bpoId,
            siPath,
    ):
        EffectiveSis.addSi(bpoId, siPath, self,)



####+BEGIN: bx:dblock:python:section :title "Service Intsance Lists"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Service Intsance Lists*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:python:func :funcName "svcProv_virDom_list" :funcType "ParSpec" :retType "List" :deco "" :argsList ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-ParSpec :: /svcProv_virDom_list/ retType=List argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def svcProv_virDom_list():
####+END:
    """List of Virtual Domain Service Providers"""
    return (
        [
            'apache2',
            'qmail',
        ]
    )

####+BEGIN: bx:dblock:python:func :funcName "svcProv_prim_list" :funcType "ParSpec" :retType "List" :deco "" :argsList ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-ParSpec :: /svcProv_prim_list/ retType=List argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def svcProv_prim_list():
####+END:
    """List of Primary Service Providers"""
    return (
        [
            'plone3',
            'geneweb',
        ]
    )


####+BEGIN: bx:dblock:python:section :title "Common Parameters Specification"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Parameters Specification*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "commonParamsSpecify" :funcType "ParSpec" :retType "" :deco "" :argsList "icmParams"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-ParSpec :: /commonParamsSpecify/ retType= argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
"""
def commonParamsSpecify(
    icmParams,
):
####+END:
    icmParams.parDictAdd(
        parName='si',
        parDescription="Service Instances Relative Path (plone3/main)",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        # parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--si',
    )


####+BEGIN: bx:dblock:python:section :title "Common Examples Sections"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Examples Sections*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:dblock:python:func :funcName "examples_aaBpo_basicAccess" :comment "Show/Verify/Update For relevant PBDs" :funcType "examples" :retType "none" :deco "" :argsList ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-examples :: /examples_aaBpo_basicAccess/ =Show/Verify/Update For relevant PBDs= retType=none argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def examples_aaBpo_basicAccess():
####+END:
    """
** Common examples.
"""
    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    # def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    oneBpo = "pmi_ByD-100001"
    oneSiRelPath = "plone3/main"

    # def moduleOverviewMenuItem(overviewCmndName):
    #     icm.cmndExampleMenuChapter('* =Module=  Overview (desc, usage, status)')
    #     cmndName = "overview_bxpBaseDir" ; cmndArgs = "moduleDescription moduleUsage moduleStatus" ;
    #     cps = collections.OrderedDict()
    #     icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none') # 'little' or 'none'

    # moduleOverviewMenuItem(bpo_libOverview)

    icm.cmndExampleMenuChapter(' =Bpo+Sr Info Base Roots=  *bpoSi Control Roots*')

    cmndName = "bpoSiFullPathBaseDir" ; cmndArgs = "" ;
    cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
    menuItem(verbosity='little')


    icm.cmndExampleMenuChapter(' =Bpo+Sr Info Base Roots=  *bpoSi Control Roots*')

    cmndName = "bpoSiRunRootBaseDir" ; cmndArgs = "" ;
    cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
    menuItem(verbosity='little')

    cmndName = "bpoSiRunRootBaseDir" ; cmndArgs = "all" ;
    cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
    menuItem(verbosity='little')

    cmndName = "bpoSiRunRootBaseDir" ; cmndArgs = "var" ;
    cps=cpsInit() ; cps['bpoId'] = oneBpo ; cps['si'] = oneSiRelPath
    menuItem(verbosity='little')


####+BEGIN: bx:dblock:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bpoSiFullPathBaseDir" :parsMand "bpoId si" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /bpoSiFullPathBaseDir/ parsMand=bpoId si parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bpoSiFullPathBaseDir(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome

            callParamsDict = {'bpoId': bpoId, 'si': si, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            bpoId = callParamsDict['bpoId']
            si = callParamsDict['si']

####+END:
        retVal = siFullPathBaseDir_obtain(
            bpoId=bpoId,
            siRelPath=si,
        )

        if interactive:
            icm.ANN_write("{}".format(retVal))

        return cmndOutcome.set(
            opError=icm.notAsFailure(retVal),
            opResults=retVal,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns the full path of the Sr baseDir.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "bpoSiRunRootBaseDir" :parsMand "bpoId si" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /bpoSiRunRootBaseDir/ parsMand=bpoId si parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class bpoSiRunRootBaseDir(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'si', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        si=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
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

        cmndArgs = list(self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)) # type: ignore

        if len(cmndArgs):
            if cmndArgs[0] == "all":
                cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
                argChoices = cmndArgsSpec.argChoicesGet()
                argChoices.pop(0)
                cmndArgs= argChoices

        retVal = bpoSi_runBaseObtain_root(
            bpoId=bpoId,
            si=si,
        )

        if interactive:
            icm.ANN_write("{}".format(retVal))
            for each in cmndArgs:
                if each == "var":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_var(bpoId, si)))
                elif each == "tmp":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_tmp(bpoId, si)))
                elif each == "log":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_log(bpoId, si)))
                else:
                    icm.EH_problem_usageError("")

        return cmndOutcome.set(
            opError=icm.notAsFailure(retVal),
            opResults=retVal,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="cmndArgs",
            argDefault=None,
            argChoices=['all', 'var', 'tmp', 'log',],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict

    
####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns the full path of the Sr baseDir.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "parLive_setup" :parsMand "bpoId repo" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  ICM-Cmnd   :: /parLive_setup/ parsMand=bpoId repo parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class parLive_setup(icm.Cmnd):
    cmndParamsMandatory = [ 'bpoId', 'repo', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bpoId=None,         # or Cmnd-Input
        repo=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if not self.obtainDocStr:
            if interactive:
                if not self.cmndLineValidate(outcome=cmndOutcome):
                    return cmndOutcome
                effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
            else:
                effectiveArgsList = argsList

            callParamsDict = {'bpoId': bpoId, 'repo': repo, }
            if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
                return cmndOutcome
            bpoId = callParamsDict['bpoId']
            repo = callParamsDict['repo']

            cmndArgsSpecDict = self.cmndArgsSpec()
            if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
                return cmndOutcome
####+END:

        cmndArgs = list(self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)) # type: ignore

        if len(cmndArgs):
            if cmndArgs[0] == "all":
                cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
                argChoices = cmndArgsSpec.argChoicesGet()
                argChoices.pop(0)
                cmndArgs= argChoices

        retVal = bpoSi_runBaseObtain_root(
            bpoId=bpoId,
            si=si,
        )

        if interactive:
            icm.ANN_write("{}".format(retVal))
            for each in cmndArgs:
                if each == "var":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_var(bpoId, si)))
                elif each == "tmp":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_tmp(bpoId, si)))
                elif each == "log":
                    icm.ANN_write("{each}".format(each=bpoSi_runBaseObtain_log(bpoId, si)))
                else:
                    icm.EH_problem_usageError("")

        return cmndOutcome.set(
            opError=icm.notAsFailure(retVal),
            opResults=retVal,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="cmndArgs",
            argDefault=None,
            argChoices=['all', 'var', 'tmp', 'log',],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict


####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:
        return """
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns the full path of the Sr baseDir.
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

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
