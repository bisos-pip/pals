# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Unit= The .here names of PALS: the host's list (/bisos/var/palsHere/uri.list) and its /etc/hosts block
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
** This File: /bisos/git/bxRepos/bisos-pip/pals/py3/bisos/pals/palsHere_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos-pip/bisos.cs/_nodeBase_/fullUsagePanel-en.org][BISOS CmndSvcs Panel]]   [[elisp:(org-cycle)][| ]]
The commands over palsHere.py, as banna_csu's are over tcpPorts.py: palsForEtcHosts is the source of
the palsHere dblock of /etc/hosts, as bannaForEtcHosts is of banna's.
** Status: In use with BISOS
#+end_org """

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import typing
####+END:

from bisos.pals import palsHere

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-ParSpc   [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    pass

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
** [[elisp:(org-cycle)][| *DocStr* |]] Examples of the palsHere commands.
    #+end_org """

    cmnd = cs.examples.cmndEnter
    literal = cs.examples.execInsert

    if sectionTitle == 'default':
        cs.examples.menuChapter(f'*PALS .here Names --- {palsHere.listFile}*')

    cs.examples.menuSection('/The List/')
    cmnd('palsHereList', comment="# every name: ip, name, its PALS directory, date added")
    cmnd('palsHereIpOf', args='libre-halaal.org.here', comment="# the address of a name")
    cmnd('palsHereAdd', args='.', comment="# add the PALS of this directory (its uri/here/value)")
    literal(f"cat {palsHere.listFile}")

    cs.examples.menuSection('/The palsHere Block of /etc/hosts/')
    cmnd('palsForEtcHosts', comment=f"# the body of the dblock whose command is: {palsHere.palsHostsDblockCommand}")
    literal("grep -A20 palsForEtcHosts /etc/hosts")


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsForEtcHosts" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsForEtcHosts>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsForEtcHosts(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  The /etc/hosts lines of the live PALS .here names, one per name:
=ip  name  # pals=<directory> added=<date>=. Run as root by py-dblock.cs (dnsCap_update): it only reads.
        #+end_org """): return(cmndOutcome)

        # Each address is stored with its name in the list, never derived from its position:
        # adding or retiring a PALS must never move another one's address.
        # Only the lines: this output is the dblock's body, so no opResults (the framework would print them).
        for line in palsHere.forEtcHosts():
            print(line)

        return cmndOutcome.set(opError=b.OpError.Success,)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsHereList" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsHereList>>  =verify= ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsHereList(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Every entry of the list, retired ones (commented out) included, in file order.
        #+end_org """): return(cmndOutcome)

        entries = palsHere.entriesAll()
        if not entries:
            print(f"# {palsHere.listFile}: no PALS .here names yet")
        for each in entries:
            print(("# retired: " if each.retired else "") + each.hostsLine())

        return cmndOutcome.set(opError=b.OpError.Success,)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsHereIpOf" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsHereIpOf>>  =verify= argsMin=1 argsMax=9999 ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsHereIpOf(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Map each .here name to its 127.0.55.x address. Fails on an unknown name.
        #+end_org """): return(cmndOutcome)

        result: list[str] = []
        for name in self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList):
            ip = palsHere.palsHereIpOf(name)
            if ip is None:
                b_io.ann.note(f"palsHereIpOf: {name} is not in {palsHere.listFile}")
                return failed(cmndOutcome)
            result.append(ip)

        return cmndOutcome.set(opResults=result[0] if len(result) == 1 else result,)

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
            argName="names",
            argDefault='',
            argChoices=[],
            argDescription=".here names, e.g. libre-halaal.org.here"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "palsHereAdd" :comment "" :extent "verify" :ro "noCli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<palsHereAdd>>  =verify= argsMax=9999 ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class palsHereAdd(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Add the .here name of each PALS directory (its uri/here/value; default:
the current directory) to the list, with the next free address. Idempotent. Does not touch /etc/hosts:
a PALS's cbm/pals-here-dns.spcs -i dnsCap_update does both.
        #+end_org """): return(cmndOutcome)

        palsDirs = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList) or ["."]
        result: list[str] = []
        for palsDir in palsDirs:
            try:
                entry, added = palsHere.add(palsHere.uriHereOf(palsDir), palsDir)
            except (OSError, ValueError) as err:
                b_io.ann.note(f"palsHereAdd: {palsDir}: {err}")
                return failed(cmndOutcome)
            print(f"{entry.hostsLine()}  {'(added)' if added else '(already listed)'}")
            result.append(entry.ip)

        return cmndOutcome.set(opError=b.OpError.Success, opResults=result,)

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
            argName="palsDirs",
            argDefault='',
            argChoices=[],
            argDescription="PALS directories, each with uri/here/value (default: .)"
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* *[[elisp:(org-cycle)][| ~End-Of-Editable-Text~ |]]* :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
