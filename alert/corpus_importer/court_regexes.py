import re

fd_pairs = (
    (re.compile('D(\.|:|(istrict))?,? (court )?(of )?Colu(m|(in))bia', re.I), 'dcd'),
    (re.compile('M(\.|(iddle))? ?D(\.|:|(istrict)),? ?(of )?Alabama', re.I), 'almd'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?Alabama', re.I), 'alnd'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict)),? ?(of )?Alabama', re.I), 'alsd'),
    (re.compile('Alaska', re.I), 'akd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Arizona', re.I), 'azd'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Arkansas', re.I), 'ared'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Arkansas', re.I), 'arwd'),
    (re.compile('C(\.|(entral))? ?D(\.|:|(istrict)),? ?(of )?Cal(ifornia)?', re.I), 'cacd'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?Cal(ifornia)?', re.I), 'cand'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict)),? ?(of )?Cal(ifornia)?', re.I), 'casd'),
    # No longer exists. Existed 1866-07-27 to 1886-08-05
    (re.compile('D(\.|:|(istrict))? ?(of )?California', re.I), 'californiad'), # Must go last for Cal.
    (re.compile('D(\.|:|(istrict))? ?(of )?Colo(rado)?', re.I), 'cod'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Conn', re.I), 'ctd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Delaware', re.I), 'ded'),
    (re.compile('M(\.|(iddle))? ?D(\.|:|(istrict)),? ?(of )?Fl(orid)?a', re.I), 'flmd'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?Fl(orid)?a', re.I), 'flnd'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict)),? ?(of )?Fl(orid)?a', re.I), 'flsd'),
    (re.compile('M(\.|(iddle))? ?D(\.|:|(istrict)),? ?(of )?G(a|(eorgia))', re.I), 'gamd'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?G(a|(eorgia))', re.I), 'gand'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict)),? ?(of )?G(a|(eorgia))', re.I), 'gasd'),
    (re.compile('Hawai', re.I), 'hid'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Idaho', re.I), 'idd'),
    (re.compile('C(\.|(entral))? ?D(\.|:|(istrict))?,? ?(of )?Ill(inois)?', re.I), 'ilcd'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict))?,? ?(of )?Ill(inois)?', re.I), 'ilnd'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict)),? ?(of )?Illinois', re.I), 'ilsd'),
    # Abolished. 1905-03-03 to 1978-10-02
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Illinois', re.I), 'illinoised'),
    # Abolished. 1819-03-03 to 1855-02-13
    (re.compile('D(\.|:|(istrict))? ?(of )?Illinois', re.I), 'illinoisd'), # Must go last
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict))?,? ?(of )?Indiana', re.I), 'innd'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict))?,? ?(of )?Indiana', re.I), 'insd'),
    # Abolished. 1817-03-03 to 1928-04-21
    (re.compile('D(\.|:|(istrict))? ?(of )?Indiana', re.I), 'indianad'), # Must go last
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?Iowa', re.I), 'iand'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict))?,? ?(of )?Iowa', re.I), 'iasd'),
    (re.compile('Kansas', re.I), 'ksd'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Kentucky', re.I), 'kyed'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Kentucky', re.I), 'kywd'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Louisiana', re.I), 'laed'),
    (re.compile('Eastern District, Louisiana', re.I), 'laed'),
    (re.compile('M(\.|(iddle))? ?D(\.|:|(istrict)),? ?(of )?Louisiana', re.I), 'lamd'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Louisiana', re.I), 'lawd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Maine', re.I), 'med'),
    (re.compile('D(\.|(istrict))? ?(of )?Maryland', re.I), 'mdd'),
        (re.compile(', Maryland', re.I), 'mdd'),
        (re.compile('Maryland Admiralty', re.I), 'mdd'),
    (re.compile('D?\.? ?(of )?Mass(achusetts)?', re.I), 'mad'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict))?,? ?(of )?Michigan', re.I), 'mied'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict))?,? ?(of )?Michigan', re.I), 'miwd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Minnesota', re.I), 'mnd'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?Mississippi', re.I), 'msnd'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict)),? ?(of )?Mississippi', re.I), 'mssd'),
    (re.compile('C(\.|(entral))? ?D(\.|:|(istrict)),? ?(of )?Missouri', re.I), 'mocd'),
    (re.compile('E(\.|(astern))? ?D(\.|(istrict))?,? ?(of )?(the )?Missouri', re.I), 'moed'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Missouri', re.I), 'mowd'),
        (re.compile('Missouri, W\.D', re.I), 'mowd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Montana', re.I), 'mtd'),
    (re.compile('D(\.|(istrict))? ?(of )?Nebraska', re.I), 'ned'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Nevada', re.I), 'nvd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?New Hampshire', re.I), 'nhd'),
    (re.compile('New Jersey', re.I), 'njd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?New Mexico', re.I), 'nmd'),
    (re.compile('E(\.|(astern))? ?D(\.|(istrict)),? ?(of )?N(\.|(ew)) ?Y(ork)?', re.I), 'nyed'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict))?,? ?(of )?N(\.|(ew)) ?Y(ork)?', re.I), 'nynd'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict))?,? ?(of )?N(\.|(ew)) ?Y(ork)?', re.I), 'nysd'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict))?,? ?(of )?N(\.|(ew)) ?Y(ork)?', re.I), 'nywd'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?North Carolina', re.I), 'nced'),
    (re.compile('M(\.|(iddle))? ?D(\.|:|(istrict)),? ?(of )?North Carolina', re.I), 'ncmd'),
    (re.compile('Greensboro Division', re.I), 'ncmd'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?North Carolina', re.I), 'ncwd'),
    (re.compile('North Dakota', re.I), 'ndd'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?Ohio', re.I), 'ohnd'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict)),? ?(of )?Ohio', re.I), 'ohsd'),
    # Abolished. 1803-02-19 to 1855-02-10
    (re.compile('D(\.|:|(istrict))? ?(of )?Ohio', re.I), 'ohiod'), # Must be the last court!
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Oklahoma', re.I), 'oked'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?Oklahoma', re.I), 'oknd'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Oklahoma', re.I), 'okwd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?Oregon', re.I), 'ord'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?P(a|(ennsylvania))', re.I), 'paed'),
    (re.compile('M(\.|(iddle))? ?D(\.|(ist\.))?,? ?(of )?P(a|(ennsylvania))', re.I), 'pamd'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?P(a|(ennsylvania))', re.I), 'pawd'),
    # Abolished. 1789-09-24 to 1818-04-20
    (re.compile('D(\.|:|(istrict))? ?(of )?P(a|(ennsylvania))', re.I), 'pennsylvaniad'), # Must go last
    (re.compile('Rhode Island', re.I), 'rid'),
    # Abolished. 1823-02-21 to 1965-10-07
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?South Carolina', re.I), 'southcarolinaed'),
    # Abolished. 1823-02-21 to 1965-10-07
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?South Carolina', re.I), 'southcarolinawd'),
    (re.compile('D(\.|:|(istrict))? ?(of )?South Carolina', re.I), 'scd'), # Must go last!
    (re.compile('South Dakota', re.I), 'sdd'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Tennessee', re.I), 'tned'),
    (re.compile('M(\.|(iddle))? ?D(\.|(istrict))?,? ?(of )?Tennessee', re.I), 'tnmd'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Tennessee', re.I), 'tnwd'),
    # Abolished. 1797-01-31 to 1839-06-18
    (re.compile('D(\.|(istrict))? ?(of )?Tennessee', re.I), 'tennessed'), # Must be the last court!
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Texas', re.I), 'txed'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?Texas', re.I), 'txnd'),
    (re.compile('S(\.|(outhern))? ?D(\.|(istrict)),? ?(of )?Texas', re.I), 'txsd'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict))?,? ?(of )?Texas', re.I), 'txwd'),
        (re.compile('Midland/Odessa', re.I), 'txwd'),
    (re.compile('Utah', re.I), 'utd'),
    (re.compile('Vermont', re.I), 'vtd'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict))?,? ?(of )?Virginia', re.I), 'vaed'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Virginia', re.I), 'vawd'),
        (re.compile('Abingdon', re.I), 'vawd'),
        (re.compile('Big Stone Gap', re.I), 'vawd'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Wash(ington)?', re.I), 'waed'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Wash(ington)?', re.I), 'wawd'),
    (re.compile('N(\.|(orthern))? ?D(\.|:|(istrict)),? ?(of )?W(\.|(est)) V(a|(irginia))', re.I), 'wvnd'),
    (re.compile('S(\.|(outhern))? ?D(\.|:|(istrict)),? ?(of )?W(\.|(est)) V(a|(irginia))', re.I), 'wvsd'),
    (re.compile('West Virginia, at Charleston', re.I), 'wvsd'),
    (re.compile('E(\.|(astern))? ?D(\.|:|(istrict)),? ?(of )?Wisconsin', re.I), 'wied'),
        (re.compile('D\. Wisconsin, E\. D', re.I), 'wied'),
    (re.compile('W(\.|(estern))? ?D(\.|:|(istrict)),? ?(of )?Wisconsin', re.I), 'wiwd'),
    (re.compile('Wyoming', re.I), 'wyd'),
    # Abolished. 1937-07-26 to 1982-03-31
    (re.compile('Canal Zone', re.I), 'canalzoned'),
    (re.compile('Guam', re.I), 'gud'),
    (re.compile('Northern Mariana', re.I), 'nmid'),
    (re.compile('Puerto Rico', re.I), 'prd'),
    (re.compile('Virgin Islands', re.I), 'vid'),
)

state_pairs = (
    (re.compile('Supreme Court of Alabama', re.I), 'ala'),
    (re.compile('Court of Criminal Appeals of Alabama', re.I), 'alacrimapp'),
    (re.compile('Court of Civil Appeals of Alabama', re.I), 'alacivapp'),
    (re.compile('Supreme Court of Alaska', re.I), 'alaska'),
    (re.compile('Court of Appeals of Alaska', re.I), 'alaskactapp'),
    (re.compile('Supreme Court of Arizona', re.I), 'ariz'),
    (re.compile('Court of Appeals,? of Arizona', re.I), 'arizctapp'),
    (re.compile('Supreme Court of Arkansas', re.I), 'ark'),
    (re.compile('Court of Appeals of Arkansas', re.I), 'arkctapp'),
    (re.compile('Supreme Court of California', re.I), 'cal'),
    (re.compile('California Court of Appeals', re.I), 'calctapp'),
        (re.compile('Court of Appeals? of California', re.I), 'calctapp'),
    (re.compile('Supreme Court of Colorado', re.I), 'colo'),
    (re.compile('Colorado Court of Appeals', re.I), 'coloctapp'),
        (re.compile('Court of Appeals of Colorado', re.I), 'coloctapp'),
    (re.compile('Supreme Court of Connecticut', re.I), 'conn'),
    (re.compile('Appellate Court of Connecticut', re.I), 'connappct'),
    (re.compile('Supreme Court of Delaware', re.I), 'del'),
    (re.compile('Court of Chancery of Delaware', re.I), 'delch'),
    (re.compile('Superior Court of Delaware', re.I), 'delsuperct'),
    (re.compile('Supreme Court of Florida', re.I), 'fla'),
    (re.compile('District Court of Appeal of Florida', re.I), 'fladistctapp'),
    (re.compile('Supreme Court of Georgia', re.I), 'ga'),
    (re.compile('Court of Appeals of Georgia', re.I), 'gactapp'),
    (re.compile('Supreme Court of Illinois', re.I), 'ill'),
    (re.compile('Supreme Court of Hawai', re.I), 'haw'),
    (re.compile('Intermediate Court of Appeals .*Hawai', re.I), 'hawapp'),
        (re.compile('Court of Appeals of Hawai', re.I), 'hawapp'),
    (re.compile('Supreme Court of (the state of )?Idaho', re.I), 'idaho'),
    (re.compile('Court of Appeals of Idaho', re.I), 'idahoctapp'),
        (re.compile('Idaho Court of Appeals', re.I), 'idahoctapp'),
    (re.compile('Supreme Court of Illinois', re.I), 'ill'),
    (re.compile('Appellate Court of Illinois', re.I), 'illappct'),
        (re.compile('Illinois Appellate Court', re.I), 'illappct'),
    (re.compile('Supreme Court of Indiana', re.I), 'ind'),
    (re.compile('Court of Appeals ((of)|(in)) Indiana', re.I), 'indctapp'),
        (re.compile('Appe((llate)|(als)) Court of Indiana', re.I), 'indctapp'),
        (re.compile('Indiana Court of Appeals', re.I), 'indctapp'),
    (re.compile('Supreme Court of Iowa', re.I), 'iowa'),
    (re.compile('Court of Appeals of Iowa', re.I), 'iowactapp'),
        (re.compile('Iowa Court of Appeals', re.I), 'iowactapp'),
    (re.compile('Supreme Court of Kansas', re.I), 'kan'),
    (re.compile('Court of Appeals of Kansas', re.I), 'kanctapp'),
    (re.compile('Court of Appeals of Kentucky', re.I), 'kyctapp'),
    (re.compile('Supreme Court of Louisiana', re.I), 'la'),
    (re.compile('Supreme Judicial Court of Maine', re.I), 'me'),
    (re.compile('Court of Appeals of Maryland', re.I), 'md'),
    (re.compile('Court of Special Appeals of Maryland', re.I), 'mdctspecapp'),
    (re.compile('Supreme (Judicial )?Court of Massachusetts', re.I), 'mass'),
    (re.compile('Appeals Court of Massachusetts', re.I), 'massappct'),
    (re.compile('Supreme Court of Michigan', re.I), 'mich'),
    (re.compile('Michigan Court of Appeals', re.I), 'michctapp'),
        (re.compile('Court of Appeals of Michigan', re.I), 'michctapp'),
    (re.compile('Supreme Court of Minnesota', re.I), 'minn'),
    (re.compile('Court of Appeals of Minnesota', re.I), 'minnctapp'),
    (re.compile('Supreme Court of Mississippi', re.I), 'miss'),
    (re.compile('Court of Appeals of Mississippi', re.I), 'missctapp'),
    (re.compile('Supreme Court of Missouri', re.I), 'mo'),
    (re.compile('Missouri Court of Appeals', re.I), 'moctapp'),
        (re.compile('St. Louis Court of Appeals', re.I), 'moctapp'),
    (re.compile('Supreme Court of Montana', re.I), 'mont'),
    (re.compile('Supreme Court of Nebraska', re.I), 'neb'),
    (re.compile('Supreme Court of Nevada', re.I), 'nev'),
    (re.compile('Supreme Court of New Hampshire', re.I), 'nh'),
    (re.compile('Supreme Court of New Jersey', re.I), 'nj'),
    (re.compile('Superior Court of New Jersey', re.I), 'njsuperctappdiv'),
    (re.compile('Supreme Court of New Mexico', re.I), 'nm'),
    (re.compile('Court of Appeals of New Mexico', re.I), 'nmctapp'),
        (re.compile('New Mexico Court of Appeals', re.I), 'nmctapp'),
    (re.compile('Court of Appeals of (the State of )?New York', re.I), 'ny'),
    (re.compile('Supreme Court of North Carolina', re.I), 'nc'),
    (re.compile('Court of Appeals of North Carolina', re.I), 'ncctapp'),
    (re.compile('Supreme Court of North Dakota', re.I), 'nd'),
    (re.compile('Supreme Court of Ohio', re.I), 'ohio'),
    (re.compile('Supreme Court (of )?Oklahoma', re.I), 'okla'),
    (re.compile('Court of Criminal Appeals (of )?Oklahoma', re.I), 'oklacrimapp'),
        (re.compile('Criminal Courts of Appeals of Oklahoma', re.I), 'oklacrimapp'),
    (re.compile('Court of Civils? Appeals of Oklahoma', re.I), 'oklacivapp'),
        # When they refer to simply the "Court of Appeals" they mean the the civil court
        (re.compile('Court of Appeals?,? (civil )?(of )?(State )?(of )?Oklahoma', re.I), 'oklacivapp'),
    (re.compile('Supreme Court (((for)|(of)) the State )?of (the )?Oregon', re.I), 'or'),
        (re.compile('Oregon Supreme Court', re.I), 'or'),
    (re.compile('Court of Appeals of (the )?(state of )?Oregon', re.I), 'orctapp'),
        (re.compile('oregon court of appeals', re.I), 'orctapp'),
    (re.compile('Supreme Court of Pennsylvania', re.I), 'pa'),
    (re.compile('Superior Court of Pennsylvania', re.I), 'pasuperct'),
    (re.compile('Commonwealth Court of Pennsylvania', re.I), 'pacommwct'),
    (re.compile('Supreme Court of Rhode Island', re.I), 'ri'),
    (re.compile('Supreme Court of South Carolina', re.I), 'sc'),
    (re.compile('Court of Appeals of South Carolina', re.I), 'scctapp'),
    (re.compile('Supreme Court of South Dakota', re.I), 'sd'),
    (re.compile('Supreme Court of Tennessee', re.I), 'tenn'),
    (re.compile('Court of Appeals of Tennessee', re.I), 'tennctapp'),
    (re.compile('Court of Criminal Appeals of Tennessee', re.I), 'tenncrimapp'),
    (re.compile('Supreme Court of Texas', re.I), 'tex'),
    (re.compile('Court of Appeals of Texas', re.I), 'texapp'),
        # The Civil Appeals courts were renamed in 1985 to be the "Court of Appeals"
        (re.compile('Court of Civil Appeals of Texas', re.I), 'texapp'),
    (re.compile('Court of Criminal Appeals of Texas', re.I), 'texcrimapp'),
    (re.compile('Supreme Court of (the )?(state of )?Utah', re.I), 'utah'),
    (re.compile('Court of Appeals (of )?Utah', re.I), 'utahctapp'),
    (re.compile('Utah Court of Appeals', re.I), 'utahctapp'),
    (re.compile('Supreme Court of Vermont', re.I), 'vt'),
    (re.compile('Supreme Court of Virginia', re.I), 'va'),
    (re.compile('Court of Appeals of Virginia', re.I), 'vactapp'),
    (re.compile('Supreme Court of Washington', re.I), 'wash'),
    (re.compile('Court of Appeals of Washington', re.I), 'washctapp'),
    (re.compile('Supreme Court of Appeals of West Virginia', re.I), 'wva'),
    (re.compile('Supreme Court of Wisconsin', re.I), 'wis'),
    (re.compile('Court of Appeals of Wisconsin', re.I), 'wisctapp'),
        (re.compile('Wisconsin Court of Appeals', re.I), 'wisctapp'),
    (re.compile('Supreme Court (of )?Wyoming', re.I), 'wyo'),

    # State Special
    (re.compile('Tax Court of Arizona', re.I), 'ariztaxct'),
    (re.compile('Tax Court of Indiana', re.I), 'indtc'),
        (re.compile('Indiana Tax Court', re.I), 'indtc'),
    (re.compile('Oklahoma Judicial Ethics Advisory Panel', re.I), 'oklajeap'),
    (re.compile('Court on the Judiciary of Oklahoma', re.I), 'oklacoj'),
)
