# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= The .internal names of PALS --- the host's list, their 127.0.55.x addresses, /etc/hosts lines
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos-pip/bisos.cs/_nodeBase_/fullUsagePanel-en.org][BISOS CmndSvcs Panel]]   [[elisp:(org-cycle)][| ]]

A PALS that has =./uri/here/value= (e.g. =libre-halaal.org.internal=) gets a loopback address in
/etc/hosts, as banna's services get theirs (127.0.22.x, bisos.banna tcpPorts). PALS are not known in
advance, so their names are kept in a host-local list, =/bisos/var/palsHere/uri.list=, one line each:

    127.0.55.1  libre-halaal.org.internal  # pals=<the PALS directory> added=2026-10-18

- An address is assigned when its name is added (the next above every address in the file) and stored
  in its line: it is never renumbered, and never reused --- a retired name's line is commented out, not
  deleted, and still counts. So adding or retiring a name moves no other name (banna's rule).
- Names are added by each PALS's =cbm/pals-here-dns.spcs= (=dnsCapSetup()=), when its CBS's assemble
  runs =-i dnsCap_update=, or by hand with =palsHereInfo.cs -i palsHereAdd <palsDir>=.
- =palsHereInfo.cs -i palsForEtcHosts= prints the list as /etc/hosts lines: the source of the
  =palsHere= dblock of /etc/hosts, which bisos.dnsCap creates (=hostsDblockCommands=) and updates.
- =palsHereIpOf(name)= gives a vhost its address without /etc/hosts having to be current.

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
** This File: /bisos/git/bxRepos/bisos-pip/pals/py3/bisos/pals/palsHere.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

import dataclasses
import datetime
import fcntl
import os
import pathlib
import re

from bisos.banna import tcpPorts

listFile = pathlib.Path("/bisos/var/palsHere/uri.list")

ipPrefix = "127.0.55."
ipFirst = 1
ipLast = 254

palsHostsDblockCommand = "palsHereInfo.cs -i palsForEtcHosts"

_listHeader = """\
# palsHere --- the .internal names of this host's PALS, one per line (bisos.pals palsHere.py).
# An address is assigned once, when its name is added, and is never renumbered or reused:
# to retire a name, comment its line out --- do not delete it.
"""

# The suffix is banna's (tcpPorts.hereDomain), as for its own here names.
_nameRe = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9.-]*[A-Za-z0-9])?\." + re.escape(tcpPorts.hereDomain) + "$")
_lineRe = re.compile(
    r"^\s*(?P<retired>#\s*)?(?P<ip>127\.0\.55\.\d{1,3})\s+(?P<name>\S+)"
    r"(?:\s*#\s*pals=(?P<pals>\S+)\s+added=(?P<added>\S+))?\s*$"
)


@dataclasses.dataclass(frozen=True)
class PalsHereEntry:
    """One line of the list: ip, name and its provenance. retired: the line is commented out."""
    ip: str
    name: str
    palsDir: str | None
    added: str | None
    retired: bool = False

    def hostsLine(self) -> str:
        return f"{self.ip}  {self.name}  # pals={self.palsDir} added={self.added}"


def _ipHost(ip: str) -> int:
    return int(ip.rsplit(".", 1)[1])


def entriesAll(listPath: pathlib.Path = listFile) -> list[PalsHereEntry]:
    """Every entry of the list, retired ones included, in file order. Empty if there is no list."""
    if not listPath.is_file():
        return []
    entries = []
    for line in listPath.read_text().splitlines():
        match = _lineRe.match(line)
        if match is None:
            continue
        entries.append(PalsHereEntry(
            ip=match["ip"], name=match["name"], palsDir=match["pals"], added=match["added"],
            retired=match["retired"] is not None,
        ))
    _entriesValidate(entries, listPath)
    return entries


def entries(listPath: pathlib.Path = listFile) -> list[PalsHereEntry]:
    """The live entries (not retired), sorted by name."""
    return sorted((each for each in entriesAll(listPath) if not each.retired), key=lambda each: each.name)


def _entriesValidate(entries: list[PalsHereEntry], listPath: pathlib.Path) -> None:
    """Two live names on one address would silently route to the wrong vhost: refuse."""
    seenIps: dict[str, str] = {}
    seenNames: set[str] = set()
    for each in entries:
        if not ipFirst <= _ipHost(each.ip) <= ipLast:
            raise ValueError(f"{listPath}: {each.name} ip={each.ip} is outside {ipPrefix}{ipFirst}-{ipLast}")
        if each.retired:
            continue
        if each.ip in seenIps:
            raise ValueError(f"{listPath}: {each.ip} is both {seenIps[each.ip]} and {each.name}")
        if each.name in seenNames:
            raise ValueError(f"{listPath}: {each.name} is listed twice")
        seenIps[each.ip] = each.name
        seenNames.add(each.name)


def palsHereIpOf(name: str, listPath: pathlib.Path = listFile) -> str | None:
    """The 127.0.55.x address of name (e.g. libre-halaal.org.internal) --- without /etc/hosts being current."""
    for each in entries(listPath):
        if each.name == name:
            return each.ip
    return None


def forEtcHosts(listPath: pathlib.Path = listFile) -> list[str]:
    """The /etc/hosts lines of the live entries: the body of the palsHere dblock."""
    return [each.hostsLine() for each in entries(listPath)]


def nameValidate(name: str) -> str:
    """name, stripped, if it is a host name ending in .internal; ValueError otherwise."""
    name = name.strip()
    if not _nameRe.match(name):
        raise ValueError(f"not a .{tcpPorts.hereDomain} host name: {name!r}")
    return name


def add(
        name: str,
        palsDir: str | pathlib.Path,
        listPath: pathlib.Path = listFile,
) -> tuple[PalsHereEntry, bool]:
    """Add name to the list, with the next free address. Idempotent: an existing live name is returned
    as it is (its address and provenance unchanged). Returns (entry, added). The list is locked while
    it is read and appended, so two PALS adding at once cannot get one address.
    """
    name = nameValidate(name)
    palsDir = os.path.realpath(palsDir)
    listPath.parent.mkdir(parents=True, exist_ok=True)
    with listPath.open("a+") as listFd:
        fcntl.flock(listFd, fcntl.LOCK_EX)
        try:
            existing = entriesAll(listPath)
            for each in existing:
                if each.name == name and not each.retired:
                    return each, False
            used = [_ipHost(each.ip) for each in existing]
            nextHost = max(used) + 1 if used else ipFirst
            if nextHost > ipLast:
                raise ValueError(f"{listPath}: no address left in {ipPrefix}{ipFirst}-{ipLast} for {name}")
            entry = PalsHereEntry(
                ip=f"{ipPrefix}{nextHost}", name=name, palsDir=palsDir,
                added=datetime.date.today().isoformat(),
            )
            listFd.seek(0, os.SEEK_END)
            if listFd.tell() == 0:
                listFd.write(_listHeader)
            listFd.write(entry.hostsLine() + "\n")
            listFd.flush()
            return entry, True
        finally:
            fcntl.flock(listFd, fcntl.LOCK_UN)


def uriHereOf(palsDir: str | pathlib.Path) -> str:
    """The .internal name of a PALS: the content of its uri/here/value."""
    valueFile = pathlib.Path(palsDir) / "uri" / "here" / "value"
    if not valueFile.is_file():
        raise ValueError(f"{palsDir}: no uri/here/value")
    return nameValidate(valueFile.read_text())


def palsDirOfPlant(plant: str | pathlib.Path) -> pathlib.Path:
    """The PALS directory of a planted file: the nearest directory, from the plant's own upward, that
    has uri/here/value. The plant's path is not resolved, so a planted file that is a symlink (to a
    generic one in bisos.pals) still finds the PALS it is planted in. ValueError if there is none.
    """
    plantDir = pathlib.Path(os.path.abspath(plant)).parent
    for each in (plantDir, *plantDir.parents):
        if (each / "uri" / "here" / "value").is_file():
            return each
    raise ValueError(f"{plant}: no uri/here/value in its directory or above --- not planted in a PALS")


def plantOf() -> str:
    """The path a planted file was invoked by, not resolved (a symlink stays the symlink): the seed's
    record of it once the seed runs, else sys.argv[0] --- the same path, on the plant's first pass."""
    import sys
    from bisos.csSeed import seedsLib
    return seedsLib.seededCsxuInfo.plantOfThisSeed or sys.argv[0]


def dnsCapSetup() -> str | None:
    """For a PALS's cbm/pals-here-dns.spcs (planted on bisos.dnsCap's seed): name the palsHere dblock
    besides banna's, take the fqdn from the PALS's uri/here, and have dnsCap_update first add it to
    the list. Returns the fqdn; None on the plant's first pass, before its seed runs.
    """
    from bisos.csSeed import seedsLib
    from bisos.dnsCap import dnsCap_seedInfo

    ci = dnsCap_seedInfo.cmndsControlInfo
    ci.dnsSpecMethod = dnsCap_seedInfo.DnsSpecMethod.etcHosts
    ci.hostsDblockCommands = [dnsCap_seedInfo.bannaHostsDblockCommand, palsHostsDblockCommand]

    plant = seedsLib.seededCsxuInfo.plantOfThisSeed
    if plant is None:
        return None
    palsDir = palsDirOfPlant(plant)
    fqdn = uriHereOf(palsDir)
    ci.fqdn = fqdn

    def palsHereAdd() -> bool:
        try:
            entry, added = add(fqdn, palsDir)
        except (OSError, ValueError) as err:
            print(f"palsHere: {fqdn}: {err}")
            return False
        print(f"palsHere: {entry.ip}  {entry.name}  {'added to' if added else 'already in'} {listFile}")
        return True

    ci.preUpdateFuncs = [palsHereAdd]
    return fqdn
