# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Unit= The PALS-BXOs of a platform, the CBMs each declares, and their platform CBM leaves
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/pals/py3/bisos/pals/palsOfSys_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos-pip/bisos.cs/_nodeBase_/fullUsagePanel-en.org][BISOS CmndSvcs Panel]]   [[elisp:(org-cycle)][| ]]
The commands over palsOfSys.py: list and add PALS-BXOs (/bisos/platform/sys/pals/), list and declare
their CBMs (<palsBxo>/sys/cbm/), and plant the platform's CBM leaves (/bisos/platform/sys/cbm/pals/).
** Status: In use with BISOS
#+end_org """

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import typing
####+END:

from bisos.pals import palsOfSys

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-ParSpc   [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    csParams.parDictAdd(
        parName='origin',
        parDescription="Where to clone the PALS-BXO from (default: its checkout's git origin).",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        argparseShortOpt=None,
        argparseLongOpt='--origin',
    )
    csParams.parDictAdd(
        parName='capabilityType',
        parDescription="The CBM's capability type: " + ", ".join(palsOfSys.capabilityTypes),
        parDataType=None,
        parDefault='hereWeb',
        parChoices=list(palsOfSys.capabilityTypes),
        argparseShortOpt=None,
        argparseLongOpt='--capabilityType',
    )

####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :comment "~CSU Specification~" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-eType    [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  ~CSU Specification~ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
        sectionTitle: typing.AnyStr = '',
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr* |]] Examples of the palsOfSys commands.
    #+end_org """

    cmnd = cs.examples.cmndEnter
    literal = cs.examples.execInsert

    if sectionTitle == 'default':
        cs.examples.menuChapter('*PALS-BXOs of This Platform and Their CBMs*')

    cs.examples.menuSection(f'/PALS-BXOs --- {palsOfSys.platformPalsBase}/')
    cmnd('palsList', comment="# each PALS-BXO, activated or not, with its CBMs")
    cmnd('palsAdd', args='<bxoPath>', comment="# list a PALS-BXO here (path; origin from its git remote)")
    cmnd('palsAdd', pars={'origin': '<url>'}, args='<bxoPath>', comment="# with an explicit origin")

    cs.examples.menuSection('/CBMs a PALS-BXO Declares --- <palsBxo>/sys/cbm/<name>/')
    cmnd('palsCbmsList', args='[<palsBxo> ...]', comment="# default: every activated PALS-BXO")
    cmnd('palsCbmAdd', pars={'capabilityType': 'hereWeb'}, args='<palsBxo> <name> <cbsRelPath>',
         comment="# declare a CBM")

    cs.examples.menuSection(f'/Platform CBM Leaves --- {palsOfSys.platformCbmPalsBase}/')
    cmnd('palsLeavesPlant', comment="# plant or refresh the leaves; gates and status logs are kept")
    literal(f"cd {palsOfSys.platformCbmPalsBase} && ./ftoBranchProc.spcs -i fto_forwardToLeaves --cmndName=cbm_status")


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsList" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsList>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Each PALS-BXO the platform lists: its checkout (or "not activated"), its
origin, and the CBMs it declares, each with whether its platform leaf is planted and its gate.
        #+end_org """): return(cmndOutcome)

        entries = palsOfSys.palsList()
        if not entries:
            print(f"# {palsOfSys.platformPalsBase}: no PALS-BXOs listed")
        for pals in entries:
            state = pals.path if pals.activated else f"not activated (path: {pals.path})"
            print(f"{pals.name}  {state}")
            print(f"    origin: {pals.origin}")
            for cbm in palsOfSys.palsCbmsList(pals):
                control = cbm.leafDir / "cbmProc.control"
                leaf = f"gate={control.read_text().strip()}" if control.is_file() else "leaf not planted"
                print(f"    cbm {cbm.name}  {cbm.capabilityType}  {cbm.cbsSpec}  ({leaf})")

        return cmndOutcome.set(opError=b.OpError.Success,)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsAdd" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "origin" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsAdd>>  =verify= parsOpt=origin argsMin=1 argsMax=1 ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsAdd(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'origin', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             origin: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'origin': origin, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        origin = csParam.mappedValue('origin', origin)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  List a PALS-BXO on this platform: <name>/path/value (its checkout, as
given, not resolved) and <name>/origin/value. Idempotent; a legacy bare value file is migrated.
        #+end_org """): return(cmndOutcome)

        bxoPath = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        try:
            pals, action = palsOfSys.palsAdd(bxoPath, origin=origin)
        except ValueError as err:
            b_io.ann.note(f"palsAdd: {err}")
            return failed(cmndOutcome)
        print(f"{pals.name}  {action}: path={pals.path}  origin={pals.origin}")
        return cmndOutcome.set(opError=b.OpError.Success,)

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="bxoPath",
            argDefault='',
            argChoices=[],
            argDescription="the PALS-BXO's checkout, e.g. /bxRepos/bxObjects/bro_rawBisos/bro_rawBisosPals"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsCbmsList" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsCbmsList>>  =verify= argsMax=9999 ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsCbmsList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  The CBMs the named PALS-BXOs declare (default: every activated one), one
line each: palsBxo, name, capabilityType, cbsSpec (relative), the CBS's absolute path.
        #+end_org """): return(cmndOutcome)

        names = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)
        try:
            entries = [palsOfSys.palsOf(n) for n in names] if names else palsOfSys.palsList()
        except KeyError as err:
            b_io.ann.note(f"palsCbmsList: {err}")
            return failed(cmndOutcome)
        for pals in entries:
            for cbm in palsOfSys.palsCbmsList(pals):
                print(f"{pals.name}  {cbm.name}  {cbm.capabilityType}  {cbm.cbsSpec}  -> {cbm.cbsPath}")
        return cmndOutcome.set(opError=b.OpError.Success,)

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="palsBxos",
            argDefault='',
            argChoices=[],
            argDescription="PALS-BXO names, as listed in /bisos/platform/sys/pals (default: all)"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsCbmAdd" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "capabilityType" :argsMin 3 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsCbmAdd>>  =verify= parsOpt=capabilityType argsMin=3 argsMax=3 ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsCbmAdd(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'capabilityType', ]
    cmndArgsLen = {'Min': 3, 'Max': 3,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             capabilityType: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'capabilityType': capabilityType, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        capabilityType = csParam.mappedValue('capabilityType', capabilityType)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Declare a CBM in a PALS-BXO's sys/cbm/<name>/ (capabilityType/value,
cbsSpec/value). The CBS path is relative to the PALS-BXO and must exist. Then palsLeavesPlant.
        #+end_org """): return(cmndOutcome)

        # cmndArgsLen enforces exactly three.
        palsName, name, cbsRelPath = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)
        try:
            cbm, action = palsOfSys.palsCbmAdd(palsOfSys.palsOf(palsName), name, cbsRelPath,
                                               capabilityType or "hereWeb")
        except (KeyError, ValueError) as err:
            b_io.ann.note(f"palsCbmAdd: {err}")
            return failed(cmndOutcome)
        print(f"{palsName}  {cbm.name}  {action}: {cbm.capabilityType}  {cbm.cbsSpec}")
        return cmndOutcome.set(opError=b.OpError.Success,)

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="palsCbm",
            argDefault='',
            argChoices=[],
            argDescription="<palsBxo> <name> <cbsRelPath>"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsLeavesPlant" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsLeavesPlant>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsLeavesPlant(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        if self.cmndDocStr(""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Plant or refresh, from every activated PALS-BXO's declarations, the
platform's CBM leaves (/bisos/platform/sys/cbm/pals/<palsBxo>/<name>/) and the realm's
ftoBranchProc.spcs. Idempotent. A new leaf's gate is "available"; gates and status logs are never
overwritten; leaves without a declaration are reported, not removed.
        #+end_org """): return(cmndOutcome)

        for path, action in palsOfSys.leavesPlant():
            print(f"{action:12s}  {path}")
        return cmndOutcome.set(opError=b.OpError.Success,)


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* *[[elisp:(org-cycle)][| ~End-Of-Editable-Text~ |]]* :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
