stages_of_legislation = [
    ("Bill Introduction", "A bill is introduced in either the House of Representatives or the Senate by a member of Congress."),
    ("Committee Action", "The bill is referred to the relevant committee(s), where it is studied, and hearings may be held. The committee may amend, pass, or reject the bill."),
    ("Floor Action", "The bill is debated and voted on by the full chamber (House or Senate). Amendments may be proposed and voted on."),
    ("Conference Committee", "If the House and Senate pass different versions of the bill, a conference committee is formed to reconcile the differences."),
    ("Final Approval", "The reconciled bill is sent back to both chambers for final approval. It must pass both chambers in identical form."),
    ("Presidential Action", "The bill is sent to the President, who can sign it into law, veto it, or take no action (leading to a 'pocket veto' if Congress adjourns)."),
    ("Law Implementation", "Once signed into law, the relevant government agencies implement the new law, and it is enforced accordingly."),
]

types_of_legislation = {
    "Bill": "A proposal for a new law, or a proposal to amend or repeal an existing law, presented for debate and approval by a legislative body.",
    "Joint Resolution": "A legislative measure that requires approval by both the House and Senate and is submitted to the president for approval or disapproval. Joint resolutions generally deal with limited matters or temporary issues.",
    "Concurrent Resolution": "A legislative measure adopted by both houses that does not have the force of law and does not require the president's signature. It is often used to make or amend rules that apply to both houses or to express the sentiment of Congress.",
    "Simple Resolution": "A legislative measure passed by either the House or Senate that addresses matters entirely within the prerogative of the house concerned. It does not have the force of law and does not require the president's signature.",
    "Appropriation Bill": "A bill that provides the legal authority to spend or obligate the government's money for a particular purpose.",
    "Authorization Bill": "A bill that establishes, continues, or modifies a federal program or agency. It may set specific policies or limits on the programs and authorize appropriations for carrying out the policies.",
    "Omnibus Bill": "A bill that combines multiple areas of legislation into one document that is voted on as a single item. It can cover a wide range of topics and is often used to pass multiple provisions in a single vote."
}

glossary_terms = {
    "Amendment": "A change or addition proposed during the debate on a bill in either the House or Senate.",
    "Filibuster": "A tactic used in the Senate to prevent a bill from coming to a vote by speaking at length on the floor, thereby delaying or blocking legislative action.",
    "Cloture": "A procedure used in the Senate to bring a debate to a quick end, thereby overcoming a filibuster. It requires a three-fifths majority vote.",
    "Quorum": "The minimum number of members needed to be present in either the House or Senate for the body to conduct official business.",
    "Veto": "The power of the president to reject a bill passed by Congress. A veto can be overridden by a two-thirds majority vote in both the House and Senate.",
    "Pocket Veto": "An indirect veto of a bill by the president by retaining the bill unsigned until it is too late for it to be dealt with during the legislative session.",
    "Rider": "An additional provision added to a bill that is not related to the bill's main topic. Riders are often used to pass controversial provisions that would not pass on their own.",
    "Conference Committee": "A temporary committee formed to reconcile differences between the House and Senate versions of a bill."
}


# List of events for the timeline in the history tab
events = [
    {"year": "1791", "event": "1st Amendment: Freedom of Speech, Press, Religion and Petition"},
    {"year": "1791", "event": "2nd Amendment: Right to keep and bear arms"},
    {"year": "1791", "event": "3rd Amendment: Conditions for quarters of soldiers"},
    {"year": "1791", "event": "4th Amendment: Right of search and seizure regulated"},
    {"year": "1791", "event": "5th Amendment: Provisions concerning prosecution"},
    {"year": "1791", "event": "6th Amendment: Right to a speedy trial, witnesses, etc."},
    {"year": "1791", "event": "7th Amendment: Right to a trial by jury"},
    {"year": "1791", "event": "8th Amendment: Excessive bail, cruel punishment"},
    {"year": "1791", "event": "9th Amendment: Rule of construction of Constitution"},
    {"year": "1791", "event": "10th Amendment: Rights of the States under Constitution"},
    {"year": "1795", "event": "11th Amendment: Judicial limits"},
    {"year": "1804", "event": "12th Amendment: Choosing the President, Vice-President"},
    {"year": "1865", "event": "13th Amendment: Slavery abolished"},
    {"year": "1868", "event": "14th Amendment: Citizenship rights"},
    {"year": "1870", "event": "15th Amendment: Race no bar to vote"},
    {"year": "1913", "event": "16th Amendment: Status of income tax clarified"},
    {"year": "1913", "event": "17th Amendment: Senators elected by popular vote"},
    {"year": "1919", "event": "18th Amendment: Liquor abolished"},
    {"year": "1920", "event": "19th Amendment: Women's suffrage"},
    {"year": "1933", "event": "20th Amendment: Presidential, Congressional terms"},
    {"year": "1933", "event": "21st Amendment: 18th Amendment repealed"},
    {"year": "1951", "event": "22nd Amendment: Presidential term limits"},
    {"year": "1961", "event": "23rd Amendment: Presidential vote for D.C."},
    {"year": "1964", "event": "24th Amendment: Poll tax barred"},
    {"year": "1967", "event": "25th Amendment: Presidential disability and succession"},
    {"year": "1971", "event": "26th Amendment: Voting age set to 18 years"},
    {"year": "1992", "event": "27th Amendment: Limiting changes to Congressional pay"}
]

# Amendments for the flashcards or other purposes
amendments = [
            {"front": "1st Amendment", "back": "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances."},
            {"front": "2nd Amendment", "back": "A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed."},
            {"front": "3rd Amendment", "back": "No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in time of war, but in a manner to be prescribed by law."},
            {"front": "4th Amendment", "back": "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."},
            {"front": "5th Amendment", "back": "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation."},
            {"front": "6th Amendment", "back": "In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed, which district shall have been previously ascertained by law, and to be informed of the nature and cause of the accusation; to be confronted with the witnesses against him; to have compulsory process for obtaining witnesses in his favor, and to have the Assistance of Counsel for his defence."},
            {"front": "7th Amendment", "back": "In Suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by jury shall be preserved, and no fact tried by a jury, shall be otherwise re-examined in any Court of the United States, than according to the rules of the common law."},
            {"front": "8th Amendment", "back": "Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted."},
            {"front": "9th Amendment", "back": "The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people."},
            {"front": "10th Amendment", "back": "The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people."},
            {"front": "11th Amendment", "back": "The Judicial power of the United States shall not be construed to extend to any suit in law or equity, commenced or prosecuted against one of the United States by Citizens of another State, or by Citizens or Subjects of any Foreign State."},
            {"front": "12th Amendment", "back": "The Electors shall meet in their respective states and vote by ballot for President and Vice-President..."},
            {"front": "13th Amendment", "back": "Neither slavery nor involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, shall exist within the United States, or any place subject to their jurisdiction."},
            {"front": "14th Amendment", "back": "All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside..."},
            {"front": "15th Amendment", "back": "The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of race, color, or previous condition of servitude."},
            {"front": "16th Amendment", "back": "The Congress shall have power to lay and collect taxes on incomes, from whatever source derived, without apportionment among the several States, and without regard to any census or enumeration."},
            {"front": "17th Amendment", "back": "The Senate of the United States shall be composed of two Senators from each State, elected by the people thereof, for six years; and each Senator shall have one vote."},
            {"front": "18th Amendment", "back": "After one year from the ratification of this article the manufacture, sale, or transportation of intoxicating liquors within, the importation thereof into, or the exportation thereof from the United States and all territory subject to the jurisdiction thereof for beverage purposes is hereby prohibited."},
            {"front": "19th Amendment", "back": "The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of sex."},
            {"front": "20th Amendment", "back": "The terms of the President and the Vice President shall end at noon on the 20th day of January, and the terms of Senators and Representatives at noon on the 3d day of January, of the years in which such terms would have ended if this article had not been ratified; and the terms of their successors shall then begin."},
            {"front": "21st Amendment", "back": "The eighteenth article of amendment to the Constitution of the United States is hereby repealed."},
            {"front": "22nd Amendment", "back": "No person shall be elected to the office of the President more than twice, and no person who has held the office of President, or acted as President, for more than two years of a term to which some other person was elected President shall be elected to the office of the President more than once."},
            {"front": "23rd Amendment", "back": "The District constituting the seat of Government of the United States shall appoint in such manner as the Congress may direct: A number of electors of President and Vice President equal to the whole number of Senators and Representatives in Congress to which the District would be entitled if it were a State..."},
            {"front": "24th Amendment", "back": "The right of citizens of the United States to vote in any primary or other election for President or Vice President, for electors for President or Vice President, or for Senator or Representative in Congress, shall not be denied or abridged by the United States or any State by reason of failure to pay any poll tax or other tax."},
            {"front": "25th Amendment", "back": "In case of the removal of the President from office or of his death or resignation, the Vice President shall become President."},
            {"front": "26th Amendment", "back": "The right of citizens of the United States, who are eighteen years of age or older, to vote shall not be denied or abridged by the United States or by any State on account of age."},
            {"front": "27th Amendment", "back": "No law, varying the compensation for the services of the Senators and Representatives, shall take effect, until an election of Representatives shall have intervened."}
        ]