# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= The PALS-BXOs of a platform, the CBMs each declares, and their platform CBM leaves
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos-pip/bisos.cs/_nodeBase_/fullUsagePanel-en.org][BISOS CmndSvcs Panel]]   [[elisp:(org-cycle)][| ]]

The model (bisos.pals README.org, "PALS on a Platform"; figure py3/images/palsModel.png):

- =/bisos/platform/sys/pals/<palsBxo>/= (host) lists the platform's PALS-BXOs, as FileParams:
  =path/value= (its checkout; absent: not activated) and =origin/value= (where to clone it from).
- =<palsBxo>/sys/cbm/<cbmName>/= (the PALS-BXO's repository) declares a CBM: =capabilityType/value=
  and =cbsSpec/value=, the CBS relative to the PALS-BXO.
- =/bisos/platform/sys/cbm/pals/<palsBxo>/<cbmName>/= (host) are the CBM leaves planted from the
  declarations: =cbmProc.spcs= (generated, rewritten each time), =cbmProc.control= (the gate; created
  =available=, never overwritten) and =cbmProc.status= (never overwritten). The walker finds them under
  =sys/cbm/pals/ftoBranchProc.spcs=, also planted here.

Host state (the list, the gates, the status logs) stays on the platform; a PALS-BXO only declares.
** Status: In use with BISOS
#+end_org """

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
** This File: /bisos/git/bxRepos/bisos-pip/pals/py3/bisos/pals/palsOfSys.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

import dataclasses
import os
import pathlib
import re
import subprocess

platformPalsBase = pathlib.Path("/bisos/platform/sys/pals")
platformCbmPalsBase = pathlib.Path("/bisos/platform/sys/cbm/pals")

capabilityTypes = ("hereWeb", "hereMail", "rpyc", "induct")
initialGate = "available"

_nameRe = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")


def _fpRead(base: pathlib.Path, name: str) -> str | None:
    """The FileParam <base>/<name>/value, stripped; None when absent."""
    valueFile = base / name / "value"
    return valueFile.read_text().strip() if valueFile.is_file() else None


def _fpWrite(base: pathlib.Path, name: str, value: str) -> None:
    (base / name).mkdir(parents=True, exist_ok=True)
    (base / name / "value").write_text(value + "\n")


def nameValidate(name: str, what: str) -> str:
    if not _nameRe.match(name):
        raise ValueError(f"not a valid {what} name: {name!r}")
    return name


@dataclasses.dataclass(frozen=True)
class PalsBxo:
    """A PALS-BXO known to the platform. path: its checkout (None: not activated)."""
    name: str
    path: str | None
    origin: str | None

    @property
    def activated(self) -> bool:
        return self.path is not None and os.path.isdir(self.path)


@dataclasses.dataclass(frozen=True)
class PalsCbm:
    """A CBM a PALS-BXO declares. cbsSpec is relative to the PALS-BXO."""
    pals: PalsBxo
    name: str
    capabilityType: str | None
    cbsSpec: str | None

    @property
    def cbsPath(self) -> str | None:
        if self.pals.path is None or self.cbsSpec is None:
            return None
        return os.path.join(self.pals.path, self.cbsSpec)

    @property
    def leafDir(self) -> pathlib.Path:
        return platformCbmPalsBase / self.pals.name / self.name


def palsOf(name: str, base: pathlib.Path = platformPalsBase) -> PalsBxo:
    """The platform's entry for a PALS-BXO. A legacy entry (a bare <name>/value holding the path) is
    read as its path. KeyError if the platform does not list it."""
    entryDir = base / name
    if not entryDir.is_dir():
        raise KeyError(f"{name}: not in {base}")
    path = _fpRead(entryDir, "path")
    if path is None and (entryDir / "value").is_file():
        path = (entryDir / "value").read_text().strip() or None
    return PalsBxo(name=name, path=path, origin=_fpRead(entryDir, "origin"))


def palsList(base: pathlib.Path = platformPalsBase) -> list[PalsBxo]:
    """Every PALS-BXO the platform lists, by name."""
    if not base.is_dir():
        return []
    return [palsOf(each.name, base) for each in sorted(base.iterdir()) if each.is_dir()]


def gitOrigin(path: str) -> str | None:
    """The origin remote of a checkout, or None."""
    result = subprocess.run(["git", "-C", path, "remote", "get-url", "origin"],
                            capture_output=True, text=True)
    return result.stdout.strip() or None if result.returncode == 0 else None


def palsAdd(
        bxoPath: str,
        origin: str | None = None,
        name: str | None = None,
        base: pathlib.Path = platformPalsBase,
) -> tuple[PalsBxo, str]:
    """List (or update) a PALS-BXO on the platform: path/value and origin/value (default: the checkout's
    git origin). The path is kept as given (absolute, not resolved): it is host state. A legacy bare
    value file is replaced by path/value. Returns (entry, 'added' | 'updated' | 'unchanged')."""
    path = os.path.abspath(bxoPath)
    if not os.path.isdir(path):
        raise ValueError(f"{bxoPath}: not a directory")
    name = nameValidate(name or os.path.basename(path.rstrip("/")), "PALS-BXO")
    origin = origin or gitOrigin(path)
    entryDir = base / name
    before = palsOf(name, base) if entryDir.is_dir() else None
    legacy = entryDir / "value"
    migrated = legacy.is_file()
    _fpWrite(entryDir, "path", path)
    if origin:
        _fpWrite(entryDir, "origin", origin)
    if migrated:
        legacy.unlink()
    after = palsOf(name, base)
    if before is None:
        return after, "added"
    return after, "updated" if migrated or before != after else "unchanged"


def palsCbmsList(pals: PalsBxo) -> list[PalsCbm]:
    """The CBMs a PALS-BXO declares in its sys/cbm/ (directories with cbsSpec/value), by name."""
    if not pals.activated:
        return []
    cbmBase = pathlib.Path(pals.path) / "sys" / "cbm"
    if not cbmBase.is_dir():
        return []
    return [
        PalsCbm(pals=pals, name=each.name, capabilityType=_fpRead(each, "capabilityType"),
                cbsSpec=_fpRead(each, "cbsSpec"))
        for each in sorted(cbmBase.iterdir())
        if each.is_dir() and (each / "cbsSpec" / "value").is_file()
    ]


def palsCbmAdd(
        pals: PalsBxo,
        name: str,
        cbsRelPath: str,
        capabilityType: str = "hereWeb",
) -> tuple[PalsCbm, str]:
    """Declare a CBM in a PALS-BXO's sys/cbm/<name>/. cbsRelPath is relative to the PALS-BXO and must
    exist there. Returns (cbm, 'added' | 'updated' | 'unchanged')."""
    if not pals.activated:
        raise ValueError(f"{pals.name}: not activated (no checkout at {pals.path})")
    name = nameValidate(name, "CBM")
    if capabilityType not in capabilityTypes:
        raise ValueError(f"capabilityType {capabilityType!r} is not one of {', '.join(capabilityTypes)}")
    if os.path.isabs(cbsRelPath) or ".." in pathlib.PurePath(cbsRelPath).parts:
        raise ValueError(f"{cbsRelPath}: must be relative to the PALS-BXO, without ..")
    if not os.path.isfile(os.path.join(pals.path, cbsRelPath)):
        raise ValueError(f"{cbsRelPath}: no such file in {pals.path}")
    cbmDir = pathlib.Path(pals.path) / "sys" / "cbm" / name
    before = (_fpRead(cbmDir, "capabilityType"), _fpRead(cbmDir, "cbsSpec")) if cbmDir.is_dir() else None
    _fpWrite(cbmDir, "capabilityType", capabilityType)
    _fpWrite(cbmDir, "cbsSpec", cbsRelPath)
    cbm = PalsCbm(pals=pals, name=name, capabilityType=capabilityType, cbsSpec=cbsRelPath)
    if before is None:
        return cbm, "added"
    return cbm, "unchanged" if before == (capabilityType, cbsRelPath) else "updated"


_branchSpcs = '''\
#!/usr/bin/env python

""" #+begin_org
* ftoBranchProc.spcs at sys/cbm/pals/ --- planted by bisos.pals (palsOfSys.cs -i palsLeavesPlant)
*
* Walker branch for the CBM pals realm: the leaves under it, pals/<palsBxo>/<cbmName>/, are planted
* from each PALS-BXO's sys/cbm/ declarations. Leaves are directories with cbmProc.spcs.
*
*   ./ftoBranchProc.spcs -i fto_treeList
*   ./ftoBranchProc.spcs -i fto_forwardToLeaves --cmndName=cbm_status
*   ./ftoBranchProc.spcs -i fto_forwardToLeaves --cmndName=cbm_materialize
#+end_org """

from bisos.fileObj import ftoBranch_seed         # noqa: F401  _atExit_
from bisos.fileObj import ftoBranch_seedInfo
from bisos.capability import cbmProc_seedInfo

ftoBranch_seedInfo.setup(
    leafProcessors=cbmProc_seedInfo.leafProcessorNames(),
    leafExamples=cbmProc_seedInfo.walkExamples(),
)
'''


def leafSpcs(cbm: PalsCbm) -> str:
    """The cbmProc.spcs of a planted leaf: a pointer to the CBS, as every CBM leaf is."""
    return f'''\
#!/usr/bin/env python

""" #+begin_org
* cbmProc.spcs --- {cbm.name} of the PALS-BXO {cbm.pals.name}, a {cbm.capabilityType} capability
*
* GENERATED by bisos.pals (palsOfSys.cs -i palsLeavesPlant) from
*   {cbm.pals.path}/sys/cbm/{cbm.name}/
* Do not edit: change the declaration and plant again. cbmProc.control (the gate) and cbmProc.status
* beside it are this host's, and are never overwritten.
*
* Realm:            pals
* PALS-BXO:         {cbm.pals.name}
* CapabilityType:   {cbm.capabilityType}
* CapabilityName:   {cbm.name}
#+end_org """

from bisos.capability import cbmProc_seed  # noqa: F401  _atExit_

from bisos.capability import cbmProc_seedInfo

cbmProc_seedInfo.setup(
    capabilityName="{cbm.name}",
    cbsSpec="{cbm.cbsPath}",
)
'''


def _writeIfChanged(path: pathlib.Path, content: str, mode: int | None = None) -> bool:
    if path.is_file() and path.read_text() == content:
        return False
    path.write_text(content)
    if mode is not None:
        path.chmod(mode)
    return True


def leavesPlant(
        palsBase: pathlib.Path = platformPalsBase,
        leavesBase: pathlib.Path = platformCbmPalsBase,
) -> list[tuple[str, str]]:
    """Plant or refresh the platform's CBM leaves from every activated PALS-BXO's declarations, and the
    realm's ftoBranchProc.spcs. Idempotent; a gate or a status log is never overwritten. Leaves whose
    declaration is gone are reported ('stale'), not removed. Returns (path, action) pairs."""
    report: list[tuple[str, str]] = []
    leavesBase.mkdir(parents=True, exist_ok=True)
    branch = leavesBase / "ftoBranchProc.spcs"
    report.append((str(branch), "planted" if _writeIfChanged(branch, _branchSpcs, 0o775) else "unchanged"))

    declared: set[pathlib.Path] = set()
    for pals in palsList(palsBase):
        if not pals.activated:
            report.append((str(palsBase / pals.name), "not activated: skipped"))
            continue
        for cbm in palsCbmsList(pals):
            if cbm.cbsPath is None or not os.path.isfile(cbm.cbsPath):
                report.append((str(cbm.leafDir), f"cbsSpec missing: {cbm.cbsPath}"))
                continue
            leafDir = leavesBase / pals.name / cbm.name
            declared.add(leafDir)
            existed = leafDir.is_dir()
            leafDir.mkdir(parents=True, exist_ok=True)
            changed = _writeIfChanged(leafDir / "cbmProc.spcs", leafSpcs(cbm), 0o775)
            control = leafDir / "cbmProc.control"
            if not control.exists():
                control.write_text(initialGate + "\n")
            status = leafDir / "cbmProc.status"
            if not status.exists():
                status.touch()
            report.append((str(leafDir), "planted" if not existed else "updated" if changed else "unchanged"))

    for palsDir in sorted(p for p in leavesBase.iterdir() if p.is_dir() and p.name != "__pycache__"):
        for leafDir in sorted(p for p in palsDir.iterdir() if (p / "cbmProc.spcs").is_file()):
            if leafDir not in declared:
                report.append((str(leafDir), "stale: no declaration (left in place)"))
    return report
